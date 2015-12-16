-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2015 at 06:09 PM
-- Server version: 5.6.20
-- PHP Version: 5.5.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `measurementApp`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE IF NOT EXISTS `customer` (
`cid` int(10) NOT NULL,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `age` varchar(15) NOT NULL,
  `contactnumber` int(10) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

CREATE TABLE IF NOT EXISTS `invoice` (
`iid` int(10) NOT NULL,
  `iv_cid` int(10) DEFAULT NULL,
  `submitdata` date DEFAULT NULL,
  `requiredate` date DEFAULT NULL,
  `quantity` int(5) DEFAULT NULL,
  `price` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `measurement`
--

CREATE TABLE IF NOT EXISTS `measurement` (
`mid` int(10) NOT NULL,
  `me_iid` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `measurementdetails`
--

CREATE TABLE IF NOT EXISTS `measurementdetails` (
`mdid` int(10) NOT NULL,
  `md_mid` int(10) DEFAULT NULL,
  `measurementname` varchar(20) DEFAULT NULL,
  `distance` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
 ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
 ADD PRIMARY KEY (`iid`), ADD KEY `iv_cid` (`iv_cid`);

--
-- Indexes for table `measurement`
--
ALTER TABLE `measurement`
 ADD PRIMARY KEY (`mid`), ADD KEY `me_iid` (`me_iid`);

--
-- Indexes for table `measurementdetails`
--
ALTER TABLE `measurementdetails`
 ADD PRIMARY KEY (`mdid`), ADD KEY `md_mid` (`md_mid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
MODIFY `cid` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `invoice`
--
ALTER TABLE `invoice`
MODIFY `iid` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `measurement`
--
ALTER TABLE `measurement`
MODIFY `mid` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `measurementdetails`
--
ALTER TABLE `measurementdetails`
MODIFY `mdid` int(10) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `invoice`
--
ALTER TABLE `invoice`
ADD CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`iv_cid`) REFERENCES `customer` (`cid`);

--
-- Constraints for table `measurement`
--
ALTER TABLE `measurement`
ADD CONSTRAINT `measurement_ibfk_1` FOREIGN KEY (`me_iid`) REFERENCES `invoice` (`iid`);

--
-- Constraints for table `measurementdetails`
--
ALTER TABLE `measurementdetails`
ADD CONSTRAINT `measurementdetails_ibfk_1` FOREIGN KEY (`md_mid`) REFERENCES `measurement` (`mid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
