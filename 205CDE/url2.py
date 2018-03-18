#!/205CDE/bin/python3
from flask import Flask, request, render_template, flash, session, logging, redirect, url_for, send_from_directory
from flask_mysqldb import MySQL
from wtforms import Form, StringField, SelectField, TextAreaField, FileField, PasswordField, validators
from wtforms.fields.html5 import DateField
from passlib.hash import sha256_crypt
from functools import wraps
from werkzeug import secure_filename, SharedDataMiddleware, FileStorage
from werkzeug.datastructures import FileStorage
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class, UploadNotAllowed
from flask_wtf.file import FileField, FileAllowed, FileRequired
from base64 import b64decode
import datetime
import os


app = Flask(__name__)

UPLOAD_FOLDER = '/home/pokemonmax00/205CDE/static/img'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Evigate'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOADED_PHOTOS_DEST'] = '/home/pokemonmax00/205CDE/static/img'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

mysql = MySQL(app)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS 

@app.route('/') 
def origin(): 
    cursor = mysql.connection.cursor()
    
    result = cursor.execute("SELECT * FROM news ORDER BY newsID DESC")
    
    news = cursor.fetchall()
    
    if result > 0:
        
        return render_template('home.html', news = news)
    
    cursor.close()
          
    return render_template("home.html")

@app.route('/home') 
def home(): 
    cursor = mysql.connection.cursor()
    
    result = cursor.execute("SELECT * FROM news ORDER BY newsID DESC")
    
    news = cursor.fetchall()
    
    if result > 0:
        
        return render_template('home.html', news = news)
    
    cursor.close()
        
    return render_template("home.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()

        result = cursor.execute("SELECT * FROM registeredUser WHERE email = %s", [email])

        if result > 0:
            getrow = cursor.fetchone()
            getusernameinrow = getrow['username']
            getemailinrow = getrow['email']
            getpasswordinrow = getrow['password']

            if sha256_crypt.verify(password, getpasswordinrow):
                session['loginuser'] = True
                session['username'] = getusernameinrow
                session['email'] = getemailinrow

                flash('Login success', 'success')
                return redirect(url_for('newhome'))
            else:
                error = 'Login fail'
                return render_template('loginform2.html', error=error)

            cursor.close()
        else:
            error = 'Unknown username'
            return render_template('loginform2.html', error=error)

    return render_template('loginform2.html')
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'loginuser' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout')
def logout():
    session.clear()
    flash('Logout', 'success')
    return redirect(url_for('home'))


class RegisterForm(Form):
    username = StringField('Username', [validators.DataRequired(),validators.Length(min=4, max=50)])
    gender = SelectField('Gender', choices = [('m', 'Male'), ('f', 'Female')])
    dateofbirth = DateField('Date-of-birth', format='%Y-%m-%d')
    email = StringField('Email', [validators.DataRequired(),validators.Length(min=6, max=50)])
    password = StringField('Password', [
        validators.DataRequired(), 
        validators.EqualTo('retypepassword', message='Passwords do not match')])
    retypepassword = PasswordField('Retype Password')
    
@app.route("/register", methods = ['POST', 'GET']) 
def register(): 
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate(): 
        username = form.username.data
        gender = form.gender.data
        dateofbirth = form.dateofbirth.data
        email = form.email.data 
        password = sha256_crypt.encrypt(str(form.password.data))
        retypepassword = form.retypepassword.data
		
        cursor = mysql.connection.cursor()  
        
        result = cursor.execute("SELECT * FROM registeredUser WHERE username = %s OR email = %s", (username, email))
        
        if result == 0:
            
            cursor.execute("INSERT INTO registeredUser (username, gender, dateOfBirth, email, password) VALUES(%s, %s, %s, %s, %s)", (username, gender, dateofbirth, email, password))
        
            mysql.connection.commit()
        
            cursor.close()
        
            flash('Success to register your account!', 'success')  
            
            return redirect(url_for('login'))
        
        else:
            
            flash('Username or email has been used', 'danger')  
            
    return render_template('bregisterform.html', form=form)

@app.route('/newhome')
@is_logged_in
def newhome():
    cursor = mysql.connection.cursor()
    
    result = cursor.execute("SELECT * FROM news ORDER BY newsID DESC")
    
    news = cursor.fetchall()
    
    if result > 0:
        
        return render_template('newhome.html', news = news)
    
    cursor.close()
    
    return render_template('newhome.html')

@app.route('/profile')
@is_logged_in
def profile():
    username = session['username']
    
    cursor = mysql.connection.cursor()
    
    result = cursor.execute("SELECT * FROM registeredUser WHERE username = %s", (username,))
    
    profile = cursor.fetchone()
    
    result2 = cursor.execute("SELECT * FROM product WHERE username = %s ORDER BY productID DESC", (username,))
    
    cardinfos = cursor.fetchall()    
    
    if result > 0:
        
        return render_template('profile.html', profile = profile, cardinfos = cardinfos)   
    
    if result2 > 0:
        
        return render_template('profile.html', profile = profile, cardinfos = cardinfos)    
    
    cursor.close()    
    
    return render_template('profile.html', profile = profile, cardinfos = cardinfos)

@app.route('/item')
@is_logged_in
def item():
    return render_template('item.html')

@app.route('/laptopcategory')
@is_logged_in
def laptopcategory():
    cursor = mysql.connection.cursor()
    
    result = cursor.execute("SELECT * FROM product WHERE productCategory = 'Laptop' ORDER BY productID DESC")
    
    cardinfos = cursor.fetchall()
    
    if result > 0:
        
        return render_template('laptopcategory.html', cardinfos = cardinfos)
    
    cursor.close()
    
    return render_template('laptopcategory.html')

@app.route('/tabletcategory')
@is_logged_in
def tabletcategory():
    cursor = mysql.connection.cursor()
    
    result = cursor.execute("SELECT * FROM product WHERE productCategory = 'Tablet' ORDER BY productID DESC")
    
    cardinfos = cursor.fetchall()
    
    if result > 0:
        
        return render_template('tabletcategory.html', cardinfos = cardinfos)
    
    cursor.close()
    
    return render_template('tabletcategory.html')

@app.route('/2-in-1category')
@is_logged_in
def twoinonecategory():
    cursor = mysql.connection.cursor()
    
    result = cursor.execute("SELECT * FROM product WHERE productCategory = '2-in-1' ORDER BY productID DESC")
    
    cardinfos = cursor.fetchall()
    
    if result > 0:
        
        return render_template('2in1category.html', cardinfos = cardinfos)
    
    cursor.close()
    
    return render_template('2in1category.html')

@app.route('/accessoriescategory')
@is_logged_in
def accessoriescategory():
    cursor = mysql.connection.cursor()
    
    result = cursor.execute("SELECT * FROM product WHERE productCategory = 'Accessories' ORDER BY productID DESC")
    
    cardinfos = cursor.fetchall()
    
    if result > 0:
        
        return render_template('accessoriescategory.html', cardinfos = cardinfos)
    
    cursor.close()
    
    return render_template('accessoriescategory.html')

@app.route('/product/<productid>/', methods=['GET', 'POST'])
@is_logged_in
def productinfo(productid):
    cursor = mysql.connection.cursor()
    
    result1 = cursor.execute("SELECT * FROM product WHERE productID = %s",(productid,))   
    
    productinfos = cursor.fetchone()
    
    result2 = cursor.execute("SELECT * FROM message WHERE productID = %s ORDER BY messageID DESC", [productid])
        
    discuss = cursor.fetchall()    
    
    if request.method == 'POST':
            username = session['username']
            messagetopic = request.form['message-topic']
            messagecontent = request.form['message-content']
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
            cursor.execute("INSERT INTO message (productID, username, topic, date, content) VALUES(%s, %s, %s, %s, %s)", ([productid], username, messagetopic, date, messagecontent))
        
            mysql.connection.commit()
        
            flash('Message sent', 'success')
        
            return render_template('productinfo.html', productid = productid, productinfos = productinfos, discuss = discuss)
    
    if result1 > 0:
    
        return render_template('productinfo.html', productid = productid, productinfos = productinfos, discuss = discuss)    
    
    elif result1 > 0 and result2 > 0:
    
        return render_template('productinfo.html', productid = productid, productinfos = productinfos, discuss = discuss)    
    
    cursor.close()
    
    return render_template('productinfo.html', productid = productid, productinfos = productinfos, discuss = discuss)

@app.route('/uploadfile/<filename>')
@is_logged_in
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/setting')
@is_logged_in
def setting():
    return render_template('setting.html')
    
@app.route('/sell', methods=['GET', 'POST'])
@is_logged_in
def sell():
    if request.method == 'POST':
        file = request.files['product-photo']
        uploaduser = session['username']
        productphotoname = secure_filename(file.filename)
        productname = request.form['product-name']
        productprice = request.form['product-price']
        productstatus = request.form.get('product-status')
        productcategory = request.form.get('product-category') 
        productdescription = request.form['product-description']
        
        
        if file and allowed_file(file.filename):
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], productphotoname)
            filename = photos.save(request.files['product-photo'])
            file_url = photos.url(filename)
           
            
            cursor = mysql.connection.cursor()  
        
            cursor.execute("INSERT INTO product (username, productPhotoName, productPhoto, productName, productPrice, productStatus, productCategory, productDescription) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (uploaduser, productphotoname, filename, productname, productprice, productstatus, productcategory, productdescription))
        
            mysql.connection.commit()  
        
            cursor.close()  
        
            flash('Upload success', 'success')
            return redirect(url_for('newhome'))
        
    return render_template('uploadform2.html')

@app.route('/editproduct/<productid>/', methods=['GET', 'POST'])
@is_logged_in
def editproduct(productid):
    if request.method == 'POST':
        file = request.files['product-photo']
        uploaduser = session['username']
        productphotoname = secure_filename(file.filename)
        productname = request.form['product-name']
        productprice = request.form['product-price']
        productstatus = request.form.get('product-status')
        productcategory = request.form.get('product-category') 
        productdescription = request.form['product-description']
        
        if file and allowed_file(file.filename):
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], productphotoname)
            filename = photos.save(request.files['product-photo'])
            file_url = photos.url(filename)
           
            
            cursor = mysql.connection.cursor()  
        
            cursor.execute("UPDATE product SET username = %s, productPhotoName = %s, productPhoto = %s, productName = %s, productPrice = %s, productStatus = %s, productCategory = %s, productDescription = %s WHERE productID = %s", (uploaduser, productphotoname, filename, productname, productprice, productstatus, productcategory, productdescription, productid))
        
            mysql.connection.commit()  
        
            cursor.close()  
        
            flash('Edit success', 'success')
            return redirect(url_for('profile'))        
    
    return render_template('editproduct.html')

@app.route('/deleteproduct/<productid>/', methods=['GET', 'POST'])
@is_logged_in
def deleteproduct(productid):
    cursor = mysql.connection.cursor()  

    cursor.execute("DELETE FROM product WHERE productID = %s", (productid,))

    mysql.connection.commit()  

    cursor.close()      
    
    return redirect(url_for('profile')) 

if __name__ == '__main__': 
    app.secret_key= 'mysecret'
    app.run(debug = True)
    app.run(host='0.0.0.0', port=5000)