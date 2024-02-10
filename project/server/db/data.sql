-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 10, 2024 at 09:19 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `plecematepro`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
CREATE TABLE IF NOT EXISTS `data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `class` varchar(20) NOT NULL,
  `academic_performance` int(11) NOT NULL,
  `technical_skills` int(11) NOT NULL,
  `core_knowledge` int(11) NOT NULL,
  `puzzle_solving` int(11) NOT NULL,
  `programming_skills` int(11) NOT NULL,
  `group_discussion_score` int(11) NOT NULL,
  `project` int(11) NOT NULL,
  `internship` int(11) NOT NULL,
  `backlog` int(11) NOT NULL,
  `coding_skills` int(11) NOT NULL,
  `aptitude_skills` int(11) NOT NULL,
  `communication_skills` int(11) NOT NULL,
  `presentation_skills` int(11) NOT NULL,
  `english_proficiency` int(11) NOT NULL,
  `management_skills` int(11) NOT NULL,
  `training` int(11) NOT NULL,
  `result` float NOT NULL,
  `ip_address` varchar(30) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
