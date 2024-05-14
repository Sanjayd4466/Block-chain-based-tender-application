-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 26, 2021 at 04:49 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python_secure_e_tender`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_details`
--

CREATE TABLE `customer_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_details`
--

INSERT INTO `customer_details` (`id`, `name`, `contact`, `email`, `address`, `username`, `password`, `status`, `report`) VALUES
(1, 'sham', '9003682729', 'sham@gmail.com', 'tr', 'sham', '123', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `manager_details`
--

CREATE TABLE `manager_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `manager_details`
--

INSERT INTO `manager_details` (`id`, `name`, `contact`, `email`, `address`, `username`, `password`, `status`, `report`) VALUES
(1, 'arun', '9876543210', 'arun@gmail.com', 'tr', 'arun', '123', '0', 'sample');

-- --------------------------------------------------------

--
-- Table structure for table `quotation_details`
--

CREATE TABLE `quotation_details` (
  `id` int(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `tender_name` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `duration` varchar(100) NOT NULL,
  `filename` varchar(100) NOT NULL,
  `quotation_amount` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `manager` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `quotation_details`
--

INSERT INTO `quotation_details` (`id`, `username`, `tender_name`, `department`, `duration`, `filename`, `quotation_amount`, `amount`, `manager`, `status`, `report`) VALUES
(1, 'sham', 'building', 'sample', '3 years', 'sd.jpg', '490000', '490000', 'arun', 'Accept', '0'),
(2, 'sham', 'building', 'sample', '3 years', 'sd.jpg', '25555', '25555', 'arun', 'Reject', '0');

-- --------------------------------------------------------

--
-- Table structure for table `tender_details`
--

CREATE TABLE `tender_details` (
  `id` varchar(100) NOT NULL,
  `manager` varchar(100) NOT NULL,
  `tender_name` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `duration` varchar(100) NOT NULL,
  `last_date` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL,
  `filename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tender_details`
--

INSERT INTO `tender_details` (`id`, `manager`, `tender_name`, `department`, `amount`, `duration`, `last_date`, `description`, `status`, `report`, `filename`) VALUES
('1', 'arun', 'building', 'sample', '500000', '3 years', '12-05-2021', 'details', '0', '0', 'sd.jpg');
