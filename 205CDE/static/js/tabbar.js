$(document).ready(function() {
	var scrolldown = 0;
    $(window).scroll(function(event){
        var scrollup = $(this).scrollTop();
        if (scrollup > scrolldown){
            $("#nav-tab").hide();
        } else {
            $("#nav-tab").show();
        }
        scrolldown = scrollup;
    });
});