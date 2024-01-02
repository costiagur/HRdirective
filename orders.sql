-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 12, 2022 at 08:41 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `orders`
--

-- --------------------------------------------------------

--
-- Table structure for table `addressee`
--

CREATE TABLE `addressee` (
  `rowind` int(11) NOT NULL,
  `saldep` text COLLATE utf8_bin NOT NULL,
  `salemail` text COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `addressee`
--

INSERT INTO `addressee` (`rowind`, `saldep`, `salemail`) VALUES
(1, 'salworker1', 'salworker1@org'),
(2, 'salworker2', 'salworker2@org'),
(3, 'salworker3', 'salworker3@org');

-- --------------------------------------------------------

--
-- Table structure for table `emps`
--

CREATE TABLE `emps` (
  `rowind` int(11) NOT NULL,
  `empid` int(9) NOT NULL,
  `empname` text COLLATE utf8_bin NOT NULL,
  `empdep` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `emps`
--

INSERT INTO `emps` (`rowind`, `empid`, `empname`, `empdep`) VALUES
(1, 11111111, 'aaaaaaaaa', 1234567890),
(2, 222222222, 'bbbbbbbbb', 1234567890),
(3, 3333333, 'ccccccccc', 1234567890),
(4, 444444444, 'ddddddddd', 1234567891),
(5, 555555555, 'eeeee', 1234567891);

-- --------------------------------------------------------

--
-- Table structure for table `ordertab`
--

CREATE TABLE `ordertab` (
  `rowind` int(11) NOT NULL,
  `orderind` int(11) NOT NULL,
  `saldep` text COLLATE utf8_bin NOT NULL,
  `ordetype` text COLLATE utf8_bin NOT NULL,
  `empid` int(9) NOT NULL,
  `empname` text COLLATE utf8_bin NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL DEFAULT '2099-12-31',
  `ordtxt` text COLLATE utf8_bin NOT NULL,
  `reftxt` text COLLATE utf8_bin NOT NULL,
  `orderer` text COLLATE utf8_bin NOT NULL,
  `reffile` blob NOT NULL,
  `ordauthed` int(11) NOT NULL DEFAULT 0,
  `executedate` date NOT NULL,
  `executer` text COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addressee`
--
ALTER TABLE `addressee`
  ADD PRIMARY KEY (`rowind`);

--
-- Indexes for table `emps`
--
ALTER TABLE `emps`
  ADD PRIMARY KEY (`rowind`);

--
-- Indexes for table `ordertab`
--
ALTER TABLE `ordertab`
  ADD PRIMARY KEY (`rowind`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addressee`
--
ALTER TABLE `addressee`
  MODIFY `rowind` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `emps`
--
ALTER TABLE `emps`
  MODIFY `rowind` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `ordertab`
--
ALTER TABLE `ordertab`
  MODIFY `rowind` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
