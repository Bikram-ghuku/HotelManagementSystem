-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 29, 2022 at 12:18 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelmanagementsystem`
--

-- --------------------------------------------------------

--
-- Table structure for table `amenities`
--

CREATE TABLE `amenities` (
  `Name` varchar(15) NOT NULL,
  `noGuest` int(5) NOT NULL,
  `date` date NOT NULL,
  `type` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `USERNAME` varchar(15) DEFAULT NULL,
  `PASSWORD` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`USERNAME`, `PASSWORD`) VALUES
('bikram', 'bikram');

-- --------------------------------------------------------

--
-- Table structure for table `resturant`
--

CREATE TABLE `resturant` (
  `Name` varchar(15) NOT NULL,
  `noGuest` int(5) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `Name` varchar(15) DEFAULT NULL,
  `Guests` int(5) DEFAULT NULL,
  `rtype` varchar(5) DEFAULT NULL,
  `rnumber` varchar(5) DEFAULT NULL,
  `cindate` date DEFAULT NULL,
  `cout` date DEFAULT NULL,
  `bdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`Name`, `Guests`, `rtype`, `rnumber`, `cindate`, `cout`, `bdate`) VALUES
('Alpha', 5, 'C', 'C01', '2022-10-29', '2022-10-29', '2022-10-29'),
('Gamma', 6, 'A', 'A01', '2022-10-29', '2022-10-29', '2022-10-29'),
('delta', 4, 'B', 'B01', '2022-10-29', '2022-10-30', '2022-10-29');

-- --------------------------------------------------------

--
-- Table structure for table `roomsavail`
--

CREATE TABLE `roomsavail` (
  `Type` varchar(2) DEFAULT NULL,
  `Number` varchar(5) DEFAULT NULL,
  `charge` int(6) DEFAULT NULL,
  `booked` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roomsavail`
--

INSERT INTO `roomsavail` (`Type`, `Number`, `charge`, `booked`) VALUES
('A', 'A01', 1000, 1),
('A', 'A02', 1000, 0),
('B', 'B01', 1800, 1),
('B', 'B02', 1800, 0),
('C', 'C01', 500, 1),
('C', 'C02', 500, 0),
('C', 'C03', 500, 0),
('C', 'B04', 500, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
