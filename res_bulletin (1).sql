-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2023 at 07:43 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `res bulletin`
--

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `Event_ID` varchar(100) NOT NULL,
  `General_Description` varchar(20) DEFAULT NULL,
  `RSVP_Enabled` varchar(25) DEFAULT NULL,
  `Location` varchar(50) DEFAULT NULL,
  `Time` varchar(15) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Tags` varchar(25) DEFAULT NULL,
  `CA_Name` varchar(100) DEFAULT NULL,
  `Forum_ID` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`Event_ID`, `General_Description`, `RSVP_Enabled`, `Location`, `Time`, `Date`, `Tags`, `CA_Name`, `Forum_ID`) VALUES
('1', 'Free Breakfast w/ CA', 'Yes', '525 Classrooms', '9am', '2023-03-21', 'Food', 'John Smith', '1'),
('2', 'Grocery Bingo', 'No', '610 Lobby', '7pm', '2023-04-01', 'Prizes', 'John Smith', '2');

-- --------------------------------------------------------

--
-- Table structure for table `forum`
--

CREATE TABLE `forum` (
  `Forum_ID` varchar(100) NOT NULL,
  `User_Name_ID` varchar(100) DEFAULT NULL,
  `Comments` varchar(1000) DEFAULT NULL,
  `Rating` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `forum`
--

INSERT INTO `forum` (`Forum_ID`, `User_Name_ID`, `Comments`, `Rating`) VALUES
('1', 'John Smith', 'Loved the donuts!', 4),
('2', 'Jane Doe', 'This was a lot of fun, can we do this again?', 5);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `User_Name_ID` varchar(100) NOT NULL,
  `Wit_ID` varchar(100) DEFAULT NULL,
  `Permissions` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`User_Name_ID`, `Wit_ID`, `Permissions`) VALUES
('Jane Doe', 'W00743194', 'No'),
('John Smith', 'W00882271', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`Event_ID`),
  ADD KEY `Events1_FK1` (`Forum_ID`);

--
-- Indexes for table `forum`
--
ALTER TABLE `forum`
  ADD PRIMARY KEY (`Forum_ID`),
  ADD KEY `Events_FK1` (`User_Name_ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`User_Name_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `Events1_FK1` FOREIGN KEY (`Forum_ID`) REFERENCES `forum` (`Forum_ID`);

--
-- Constraints for table `forum`
--
ALTER TABLE `forum`
  ADD CONSTRAINT `Events_FK1` FOREIGN KEY (`User_Name_ID`) REFERENCES `users` (`User_Name_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
