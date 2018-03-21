-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- 主機: localhost
-- 產生時間： 2018 年 03 月 19 日 23:10
-- 伺服器版本: 5.7.21-0ubuntu0.16.04.1
-- PHP 版本： 7.0.25-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `Evigate`
--

-- --------------------------------------------------------

--
-- 資料表結構 `message`
--

CREATE TABLE `message` (
  `messageID` int(10) NOT NULL,
  `productID` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `topic` varchar(100) NOT NULL,
  `date` varchar(50) NOT NULL,
  `content` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `message`
--

INSERT INTO `message` (`messageID`, `productID`, `username`, `topic`, `date`, `content`) VALUES
(1, 9, 'huston', 'I want to buy', '2018-03-16 08:27:34', 'Tel: 55418729'),
(4, 11, 'huston', 'I want to buy', '2018-03-16 08:57:09', '$1000\r\ncall me if you sell it to me, my phone no. is 23382338.'),
(6, 9, 'fisherman lok', 'I want to buy', '2018-03-16 09:16:25', 'tel:12345678'),
(8, 13, 'fisherman lok', 'Plz buy it', '2018-03-17 02:04:00', 'Thx');

-- --------------------------------------------------------

--
-- 資料表結構 `news`
--

CREATE TABLE `news` (
  `newsID` int(10) NOT NULL,
  `newsDate` varchar(20) NOT NULL,
  `newsType` varchar(20) NOT NULL,
  `newsTitle` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `news`
--

INSERT INTO `news` (`newsID`, `newsDate`, `newsType`, `newsTitle`) VALUES
(1, '2018-3-16', 'Announcement', 'Flask is dangerous.'),
(2, '2018-3-16', 'News', 'I can handle it.'),
(3, '2018-3-16', 'News', 'Nothing is impossible.'),
(4, '2018-3-16', 'Homework', 'I will not do it.'),
(5, '2018-3-16', 'Art', 'CSS is enough.'),
(6, '2018-3-16', 'Deadline', 'None of my bussinss.'),
(7, '2018-3-16', 'Prize', 'I am done.');

-- --------------------------------------------------------

--
-- 資料表結構 `product`
--

CREATE TABLE `product` (
  `productID` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `productPhotoName` varchar(500) NOT NULL,
  `productPhoto` mediumblob NOT NULL,
  `productName` varchar(50) NOT NULL,
  `productPrice` varchar(10) NOT NULL,
  `productStatus` varchar(20) NOT NULL,
  `productCategory` varchar(20) NOT NULL,
  `productDescription` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `product`
--

INSERT INTO `product` (`productID`, `username`, `productPhotoName`, `productPhoto`, `productName`, `productPrice`, `productStatus`, `productCategory`, `productDescription`) VALUES
(9, 'huston', 'T9hIOi4.jpg', 0x543968494f69345f312e6a7067, 'Dell 7577', '6000', 'Second hand', 'Laptop', 'Good'),
(11, 'huston', '466265-amazon-fire-hd-10.jpg', 0x3436363236352d616d617a6f6e2d666972652d68642d31305f322e6a7067, 'Mainland Tablet', '1000', 'Second hand', 'Tablet', 'Tel:23382338'),
(12, 'fisherman lok', 'cs1601g0012_xps_13_9365_2in1_pdp_module2.jpg', 0x63733136303167303031325f7870735f31335f393336355f32696e315f7064705f6d6f64756c65325f312e6a7067, 'rubbish', '2000', 'Second hand', '2-in-1', '12345'),
(13, 'fisherman lok', '71FUKZe4cfL._SL1500_.jpg', 0x373146554b5a653463664c2e5f534c313530305f5f322e6a7067, 'Headphone', '1000', 'Brand new', 'Accessories', 'Tel: 2180000');

-- --------------------------------------------------------

--
-- 資料表結構 `registeredUser`
--

CREATE TABLE `registeredUser` (
  `userID` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dateOfBirth` date NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `registeredUser`
--

INSERT INTO `registeredUser` (`userID`, `username`, `gender`, `dateOfBirth`, `email`, `password`) VALUES
(3, 'james', 'm', '1997-12-14', 'yipsheungman00@gmail.com', '$5$rounds=535000$RnNlgZxy9zxe5JmG$mXPnu202/FploIPp5PCdzqsvezzr1VTS1.DK.VHL2V3'),
(5, 'lucas', 'm', '1997-12-18', 'yipsheungman01@gmail.com', '$5$rounds=535000$Sb.C67Ms0s7N8t9i$b3wzb.FvyzH6SuZVPK1HV1Q9AnaeG0lVbQen8l0LQg8'),
(6, 'yip1', 'm', '1997-12-17', 'yipsheungman02@gmail.com', '$5$rounds=535000$8AL5p3PD2DJSNDch$Zv.IZSsB9RvesAEFPOSFJoya7BIeQBzWdCTHwPIIz./'),
(8, 'huston', 'm', '1997-12-14', 'yipsheungman03@gmail.com', '$5$rounds=535000$BF/0Mt7Lct/RFD0Y$guVb2mbg1fhTe/jO6HcFbpeRCAezVchuQB6awvWuSoC'),
(9, 'fisherman lok', 'm', '1999-12-14', 'fish01@gmail.com', '$5$rounds=535000$iJvjufY3bqrhDM8T$9f6TwSjlSoTGNQtiaVh2MFO1NrPBQL7V7llA1g57qq7');

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`messageID`);

--
-- 資料表索引 `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`newsID`);

--
-- 資料表索引 `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`productID`);

--
-- 資料表索引 `registeredUser`
--
ALTER TABLE `registeredUser`
  ADD PRIMARY KEY (`userID`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `message`
--
ALTER TABLE `message`
  MODIFY `messageID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- 使用資料表 AUTO_INCREMENT `news`
--
ALTER TABLE `news`
  MODIFY `newsID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- 使用資料表 AUTO_INCREMENT `product`
--
ALTER TABLE `product`
  MODIFY `productID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- 使用資料表 AUTO_INCREMENT `registeredUser`
--
ALTER TABLE `registeredUser`
  MODIFY `userID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
