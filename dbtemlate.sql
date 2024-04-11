-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 11, 2024 at 11:04 AM
-- Server version: 10.1.43-MariaDB
-- PHP Version: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbname`
--

-- --------------------------------------------------------

--
-- Table structure for table `addressees`
--

CREATE TABLE `addressees` (
  `runind` int(11) NOT NULL,
  `addressee` text COLLATE hebrew_bin NOT NULL,
  `email` text COLLATE hebrew_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=hebrew COLLATE=hebrew_bin;

--
-- Dumping data for table `addressees`
--

INSERT INTO `addressees` (`runind`, `addressee`, `email`) VALUES
(1, 'שכר_קבוע', 'email1@domain'),
(2, 'משאבי אנוש', 'email2@domain'),
(3, 'שכר_אחר', 'email3@domain');

-- --------------------------------------------------------

--
-- Table structure for table `ordertab`
--

CREATE TABLE `ordertab` (
  `runind` int(11) NOT NULL,
  `empid` int(9) NOT NULL,
  `addressee` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `ordercapt` text COLLATE hebrew_bin NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL DEFAULT '2099-12-31',
  `ordertext` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `reference` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `username` text COLLATE hebrew_bin NOT NULL,
  `orderfile` longblob,
  `filename` text COLLATE hebrew_bin,
  `listfile` longblob,
  `listfilename` text COLLATE hebrew_bin,
  `listnum` int(11) DEFAULT '0',
  `state` int(1) NOT NULL DEFAULT '0' COMMENT '0-temporary, -1-declined, 1 -authorized',
  `ordertime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=hebrew COLLATE=hebrew_bin;

--
-- Dumping data for table `ordertab`
--
-- --------------------------------------------------------

--
-- Table structure for table `ordertype`
--

CREATE TABLE `ordertype` (
  `runind` int(11) NOT NULL,
  `ordercapt` text COLLATE hebrew_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=hebrew COLLATE=hebrew_bin;

--
-- Dumping data for table `ordertype`
--

INSERT INTO `ordertype` (`runind`, `ordercapt`) VALUES
(1, 'הפסקה או חידוש שכר'),
(2, 'שינוי זכאות לתוספת'),
(3, 'סעיף תקציב'),
(4, 'דירוג-דרגה'),
(5, 'עדכון ותק'),
(6, 'עדכון מעמד'),
(7, 'עדכון שיעור משרה'),
(8, 'עדכון זכאות לרכב'),
(9, 'שינוי תפקיד'),
(10, 'עדכון הסכם נוכחות'),
(11, 'עדכון נתוני גמלה'),
(12, 'עדכון תכנית עבודה'),
(13, 'שעות');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ind` int(11) NOT NULL,
  `username` text COLLATE hebrew_bin NOT NULL,
  `name` text COLLATE hebrew_bin NOT NULL,
  `orderertype` text COLLATE hebrew_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=hebrew COLLATE=hebrew_bin;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ind`, `username`, `name`, `orderertype`) VALUES
(1, 'username', 'name for email', 'manager'),
(2, 'username', 'name for email', 'orderer'),
(3, 'username', 'name for email', 'searcher');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addressees`
--
ALTER TABLE `addressees`
  ADD PRIMARY KEY (`runind`);

--
-- Indexes for table `ordertab`
--
ALTER TABLE `ordertab`
  ADD PRIMARY KEY (`runind`);

--
-- Indexes for table `ordertype`
--
ALTER TABLE `ordertype`
  ADD PRIMARY KEY (`runind`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ind`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addressees`
--
ALTER TABLE `addressees`
  MODIFY `runind` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `ordertab`
--
ALTER TABLE `ordertab`
  MODIFY `runind` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12043;

--
-- AUTO_INCREMENT for table `ordertype`
--
ALTER TABLE `ordertype`
  MODIFY `runind` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ind` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
