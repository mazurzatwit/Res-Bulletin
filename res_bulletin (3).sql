-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2023 at 09:09 PM
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
-- Table structure for table `ca_event`
--

CREATE TABLE `ca_event` (
  `Event_Name` varchar(100) NOT NULL,
  `Event_Date` varchar(15) DEFAULT NULL,
  `Event_Time` varchar(15) DEFAULT NULL,
  `Event_Location` varchar(50) DEFAULT NULL,
  `Event_CA` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ca_event`
--

INSERT INTO `ca_event` (`Event_Name`, `Event_Date`, `Event_Time`, `Event_Location`, `Event_CA`) VALUES
('Free Breakfast w/ CA’s!', '2023-03-21', '9am', '525 Classrooms', 'John Smith'),
('Grocery Bingo', '2023-04-01', '7pm', '610 Lobby', 'John Smith');

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `Event_ID` int(11) NOT NULL,
  `Yes` varchar(10) DEFAULT NULL,
  `Maybe` varchar(10) DEFAULT NULL,
  `No` varchar(10) DEFAULT NULL,
  `Event_Name` varchar(100) DEFAULT NULL,
  `Forum_ID` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`Event_ID`, `Yes`, `Maybe`, `No`, `Event_Name`, `Forum_ID`) VALUES
(1, '15', '6', '2', 'Free Breakfast w/ CA’s!', '1'),
(2, '20', '3', '6', 'Grocery Bingo', '2');

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
-- Stand-in structure for view `student_card`
-- (See below for the actual view)
--
CREATE TABLE `student_card` (
`Event_Name` varchar(100)
,`Event_Date` varchar(15)
,`Event_Time` varchar(15)
,`Event_Location` varchar(50)
,`Event_CA` varchar(100)
,`Yes` varchar(10)
,`Maybe` varchar(10)
,`No` varchar(10)
,`Forum_ID` varchar(100)
);

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

-- --------------------------------------------------------

--
-- Structure for view `student_card`
--
DROP TABLE IF EXISTS `student_card`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `student_card`  AS SELECT `ca_event`.`Event_Name` AS `Event_Name`, `ca_event`.`Event_Date` AS `Event_Date`, `ca_event`.`Event_Time` AS `Event_Time`, `ca_event`.`Event_Location` AS `Event_Location`, `ca_event`.`Event_CA` AS `Event_CA`, `events`.`Yes` AS `Yes`, `events`.`Maybe` AS `Maybe`, `events`.`No` AS `No`, `events`.`Forum_ID` AS `Forum_ID` FROM (`ca_event` join `events`) WHERE `ca_event`.`Event_Name` = `events`.`Event_Name` AND `ca_event`.`Event_Name` = 'Grocery Bingo''Grocery Bingo'  ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ca_event`
--
ALTER TABLE `ca_event`
  ADD PRIMARY KEY (`Event_Name`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`Event_ID`),
  ADD KEY `Events_FK2` (`Event_Name`),
  ADD KEY `Events_FK3` (`Forum_ID`);

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
  ADD CONSTRAINT `Events_FK2` FOREIGN KEY (`Event_Name`) REFERENCES `ca_event` (`Event_Name`),
  ADD CONSTRAINT `Events_FK3` FOREIGN KEY (`Forum_ID`) REFERENCES `forum` (`Forum_ID`);

--
-- Constraints for table `forum`
--
ALTER TABLE `forum`
  ADD CONSTRAINT `Events_FK1` FOREIGN KEY (`User_Name_ID`) REFERENCES `users` (`User_Name_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
