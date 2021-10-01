-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 06, 2020 at 05:20 AM
-- Server version: 5.7.29-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_travelads`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_account_type`
--

CREATE TABLE `account_account_type` (
  `id` int(11) NOT NULL,
  `display_name` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL,
  `module` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_account_type`
--

INSERT INTO `account_account_type` (`id`, `display_name`, `type`, `module`, `created_at`, `description`) VALUES
(1, 'Rental Owner', 'rental_owner', 'rental', '2019-04-18 09:00:00.000000', '2019-02-13 11:40:19.000000'),
(2, 'Rental Staff', 'rental_staff', 'rental', '2019-04-17 00:00:00.000000', '2019-02-13 11:40:19.000000'),
(3, 'Travel Owner', 'travel_tour_owner', 'travel_tour', '2019-04-04 00:00:00.000000', '2019-02-13 11:40:19.000000'),
(4, 'Travel Staff', 'travel_tour_staff', 'travel_tour', '2019-04-04 00:00:00.000000', '2019-04-11 03:00:00.000000'),
(5, 'Hotel Owner ', 'hotel_owner', 'hotel', '2019-04-04 00:00:00.000000', '2019-02-13 11:40:19.000000'),
(6, 'Hotel Staff', 'hotel_staff', 'hotel', '2019-04-11 00:00:00.000000', '2019-04-11 03:00:00.000000'),
(7, 'Restaurant Owner', 'restaurant_owner', 'restaurant', '2019-04-18 10:23:32.593655', ''),
(8, 'Restaurant Staff', 'restaurant_staff', 'restaurant', '2019-04-18 09:31:32.554624', '');

-- --------------------------------------------------------

--
-- Table structure for table `account_bankdetail`
--

CREATE TABLE `account_bankdetail` (
  `id` int(11) NOT NULL,
  `bankCountry_id` int(11) DEFAULT NULL,
  `bankName` varchar(200) DEFAULT NULL,
  `swiftCode` varchar(200) DEFAULT NULL,
  `accountNumber` varchar(200) DEFAULT NULL,
  `accountName` varchar(200) DEFAULT NULL,
  `invoiceTo` varchar(200) DEFAULT NULL,
  `hotel_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_bankdetail`
--

INSERT INTO `account_bankdetail` (`id`, `bankCountry_id`, `bankName`, `swiftCode`, `accountNumber`, `accountName`, `invoiceTo`, `hotel_id`) VALUES
(1, 649, 'Nepal Bank', '12345', '987654321', 'KTM Voyage', 'Owner', 3),
(2, 649, 'Siddhartha Bank', 'ABCDEF', '123', 'KTM Voyage', 'Owner', 4),
(3, 649, NULL, NULL, NULL, NULL, NULL, 30),
(4, 649, 'Siddhartha Bank', '123', '123', 'KTM Voyage', 'Owner', 5),
(5, 649, 'Sunrise Bank limited', '123112', '00203493829392', 'Nisham', 'Owner', 34),
(6, 649, 'Sunrise Bank limited', '1233112', '00203493829392', 'Nisham', 'Company', 35),
(7, 649, 'Sunrise Bank limited', 'aabbccdd', '00203493829392', 'Nisham', 'Company', 36),
(9, 649, 'Prabhu Bank Limited', 'KBLNPKA', '00134571', 'The Everest Hotel', 'Company', 29),
(14, 649, NULL, NULL, NULL, NULL, NULL, 23),
(15, 649, 'Prabhu Bank Limited', 'KBLNPKA', '98765432109', 'Meghauli Serai, A Taj Safari Pvt Ltd.', 'Company', 20),
(16, 649, NULL, NULL, NULL, NULL, NULL, 37),
(17, 649, NULL, NULL, NULL, NULL, NULL, 38),
(18, 649, 'siddartha bank', '12267', '1234567890', 'bhadrabas', 'Company', 40);

-- --------------------------------------------------------

--
-- Table structure for table `account_faq`
--

CREATE TABLE `account_faq` (
  `id` int(11) NOT NULL,
  `question` longtext,
  `answer` longtext,
  `device` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `account_language`
--

CREATE TABLE `account_language` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_language`
--

INSERT INTO `account_language` (`id`, `name`) VALUES
(1, 'language 1'),
(2, 'language 2');

-- --------------------------------------------------------

--
-- Table structure for table `account_ownerprofile`
--

CREATE TABLE `account_ownerprofile` (
  `name` varchar(80) DEFAULT NULL,
  `contact` varchar(17) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_ownerprofile`
--

INSERT INTO `account_ownerprofile` (`name`, `contact`, `image`, `address`, `created_at`, `user_id`) VALUES
('shradddha', '9818068945', 'default.png', 'patan', '2019-04-18 11:55:49.956964', 2),
('Ms. Shraddha Shakya', '1234567890', 'default.png', 'Patan', '2019-04-18 12:34:20.627475', 4),
('Aadarsha', '9813207240', 'ads_4.jpeg', 'ktm', '2019-04-19 10:53:56.928813', 6),
('Sohan Bahadur Karki', '1234567890', 'default.png', 'Ktm', '2019-04-22 07:48:43.492919', 8),
('travel', '9849755595', 'default.png', 'ktm', '2019-04-22 11:26:37.850636', 9),
('sabin', '1234567890', 'default.png', 'owner', '2019-04-23 05:41:09.104782', 10),
('Soyesha Karki', '9898989898', 'default.png', 'ktm', '2019-08-26 07:00:19.198595', 32),
(NULL, NULL, 'default.png', NULL, '2019-08-29 07:15:01.078977', 74),
(NULL, NULL, 'default.png', NULL, '2019-09-19 05:02:15.268150', 80),
('Nisham Khadka', '9851125923', 'badadashain.png', 'Baneshor', '2019-10-02 05:57:17.302984', 81),
('rajkumar', '9849700010', 'default.png', 'tinkune', '2019-12-30 07:57:20.084842', 111);

-- --------------------------------------------------------

--
-- Table structure for table `account_passwordreset`
--

CREATE TABLE `account_passwordreset` (
  `id` int(11) NOT NULL,
  `code` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `account_staffprofile`
--

CREATE TABLE `account_staffprofile` (
  `name` varchar(80) DEFAULT NULL,
  `contact` varchar(17) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `module` varchar(80) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `owner_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_staffprofile`
--

INSERT INTO `account_staffprofile` (`name`, `contact`, `image`, `address`, `module`, `company_id`, `user_id`, `created_at`, `owner_id`) VALUES
('Ram Lakhan', '', 'default.png', 'kathmandu', 'restaurant', 2, 5, '2019-04-19 07:33:12.879607', 4),
('shyam Lakhan', '1234567890', 'default.png', 'Patan', 'restaurant', 2, 7, '2019-04-21 06:03:46.894950', 4),
('some staff123', '9813207240', 'All-Our-Kids-750x485_bH2pZZf.jpg', 'kathmandu', 'hotel', 11, 11, '2019-04-24 06:50:22.230953', 8),
('', '', 'default.png', '', 'hotel', 12, 12, '2019-04-25 06:57:54.448135', 8),
('', '', 'default.png', '', 'hotel', 1, 13, '2019-04-25 07:27:31.560330', 8),
('', '', 'default.png', '', 'hotel', 10, 14, '2019-04-25 07:28:44.424484', 8),
('', '', 'default.png', '', 'hotel', 9, 15, '2019-04-28 07:24:40.800845', 4),
('', '', 'default.png', '', 'hotel', 7, 16, '2019-04-28 07:40:28.203725', 4),
('res ko staff', '9813207241', 'Screen_Shot_2019-03-02_at_6.24.26_PM_AxfYWTi.png', 'some address', 'restaurant', 7, 17, '2019-04-28 07:49:38.330384', 4),
('Ricardo Hotel ko staff', '98132012345', 'default.png', 'Ktm', 'hotel', 3, 18, '2019-05-02 10:13:06.007156', 8),
('rentalhary', '9843618384', 'profile_S9PgjfB.jpeg', 'ktm', 'rental', 2, 19, '2019-05-03 07:25:48.305364', 10),
('Rental Ram', '9813207240', 'profile.jpeg', 'Ktm', 'rental', 1, 20, '2019-05-03 07:47:30.401381', 10),
('', '', 'default.png', '', 'hotel', 3, 21, '2019-05-03 12:27:27.716972', 8),
('', '', 'default.png', '', 'hotel', 3, 22, '2019-05-03 12:31:49.484958', 8),
('', '', 'default.png', '', 'hotel', 3, 23, '2019-05-03 12:38:16.785057', 8),
('Rental shyam ho mero Naam', '9813207240', 'profile_BdrniFK.jpeg', 'ktm', 'rental', 1, 24, '2019-05-05 07:26:11.786822', 10),
('Hotel staff', '9988776690', 'default.png', 'bhaktapur', 'restaurant', 4, 25, '2019-05-05 08:12:01.683650', 4),
('shds', '9818608945', 'default.png', 'patan', 'rental', 2, 26, '2019-05-09 06:50:01.312369', 10);

-- --------------------------------------------------------

--
-- Table structure for table `account_user`
--

CREATE TABLE `account_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `device_id` varchar(200) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `current_module` varchar(200) NOT NULL,
  `contact` varchar(17) DEFAULT NULL,
  `provider` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_user`
--

INSERT INTO `account_user` (`id`, `password`, `last_login`, `email`, `is_verified`, `is_superuser`, `is_staff`, `is_active`, `device_id`, `date_joined`, `current_module`, `contact`, `provider`) VALUES
(1, 'pbkdf2_sha256$120000$QExxgRN2iHlI$MYFS5ETrmJlDjy8Jv2wDk5jw/c/5+8fjixtYlsIpV5Y=', '2020-01-31 07:47:40.823023', 'admin@admin.com', 0, 1, 1, 1, '0', '2019-04-18 08:04:37.122455', '0', NULL, '0'),
(4, 'pbkdf2_sha256$120000$kgve878ohTfJ$UtqcLpkf/vHVvn6wopyRl02F0BK3KMcwiyyihmEH7MM=', '2020-02-28 06:33:37.654349', 'shraddhashakya74@gmail.com', 1, 0, 0, 1, '154321', '2019-04-18 12:31:06.253123', 'hotel', NULL, '0'),
(5, 'pbkdf2_sha256$120000$LHfCrCGxHHsI$kgMqeseFJD7OZvcuQ6ygIIGCfRkpz7lr6MgVMpjAXkk=', '2019-05-12 07:28:32.418101', 'staff@staff.com', 1, 0, 0, 1, '0', '2019-04-19 07:33:12.668309', 'restaurant', NULL, '0'),
(6, 'pbkdf2_sha256$120000$CJFEFhhpQj1o$1yFWWAnfVQYKca+Jks624zPPtGV77NieYYRpVS87g18=', '2020-02-04 06:06:18.075469', 'aadarshachapagain@gmail.com', 1, 0, 0, 1, '154322', '2019-04-19 10:52:36.109993', 'hotel', NULL, '0'),
(7, 'pbkdf2_sha256$120000$MPkjx0xj9X0r$KOK2SMi0nfQmIw8aJmwenAh0SD0z2HBt2HrHPXi/RHE=', '2019-04-29 07:58:45.721465', 'staff@staffrestaurant.com', 1, 0, 0, 1, '0', '2019-04-21 06:03:46.682226', 'restaurant', NULL, '0'),
(8, 'pbkdf2_sha256$120000$kgve878ohTfJ$UtqcLpkf/vHVvn6wopyRl02F0BK3KMcwiyyihmEH7MM=', '2019-12-06 07:49:11.803040', 'karki.soyeshaa@gmail.com', 1, 0, 0, 1, '0', '2019-04-22 11:25:52.050067', 'hotel', NULL, '0'),
(9, 'pbkdf2_sha256$120000$7ITQk2mJMU0S$Jg4bq2yv/dMiAcOYC1pYa2H9mUGd0e9L/8HaqevQZrI=', '2019-08-21 10:39:08.235550', 'chicharitoacis14@gmail.com', 1, 0, 0, 1, '0', '2019-04-22 11:25:52.050067', 'travel_tour', NULL, '0'),
(10, 'pbkdf2_sha256$120000$sp3egDMcPSgd$hgOu8RCIA2sqQZ45xr4gYun75RdOxpD0DvvQp8GPdBc=', '2019-12-16 05:19:36.954637', 'sabin8peace@gmail.com', 1, 0, 0, 1, '0', '2019-04-23 05:37:46.793386', 'hotel', NULL, '0'),
(11, 'pbkdf2_sha256$120000$TrAYaOABa2G2$DMO4fVpnOuQGUofe41b5WLQrGwzgeJcg0JXS07VZ5W4=', '2019-04-24 10:10:20.790869', 'staff@ymail.com', 1, 0, 0, 1, '0', '2019-04-24 06:50:21.999053', 'hotel', NULL, '0'),
(12, 'pbkdf2_sha256$120000$23gCbIbgayEG$I6YCZ0bB7PViUOpOoogsJK3B//AAqCdvBkfZcL/It8k=', '2019-05-16 09:30:03.781815', 'staff@outlook.com', 1, 0, 0, 1, '0', '2019-04-25 06:57:54.224581', '0', NULL, '0'),
(13, 'pbkdf2_sha256$120000$ccQ60jnLiaTc$vkt7u3fMbU4/PmfhVorLkwq5NQmquM6LJMi8RlaJsL4=', NULL, 'hiso@host.invalid', 1, 0, 0, 1, '0', '2019-04-25 07:27:31.358527', '0', NULL, '0'),
(14, 'pbkdf2_sha256$120000$8CPCE6OFXtQN$7wII9nl+aFUAwAc+rBAtdQFmWZS2xK3K4sU7eu5UeGA=', NULL, 'luzad@host.local', 1, 0, 0, 1, '0', '2019-04-25 07:28:44.235053', '0', NULL, '0'),
(17, 'pbkdf2_sha256$120000$lEfQyE6cJ1Zv$S4PK/A2Gc+YWwpC/Thv+cxxvC7Exs85gWuCX2WrX0Rs=', '2019-05-16 09:54:47.867840', 'rikadkis@host.local', 1, 0, 0, 1, '0', '2019-04-28 07:49:38.133133', 'restaurant', NULL, '0'),
(18, 'pbkdf2_sha256$120000$oiBEx3b4xcXF$iR1VKsaw8ZqfN81rwLl71ZWjBdbNbE83opaVArSYMkc=', '2019-05-30 08:49:46.168582', 'staff@gmail.com', 1, 0, 0, 1, '0', '2019-05-02 10:13:05.794426', 'hotel', NULL, '0'),
(19, 'pbkdf2_sha256$120000$fFAJaBlXRUrC$X04Les8JB74LYEDKu0zoNNKUjMMEXVD0MncvHvdEZNA=', '2019-05-16 09:56:05.316822', 'rental@staff.com', 1, 0, 0, 1, '0', '2019-05-03 07:25:48.062999', 'rental', NULL, '0'),
(20, 'pbkdf2_sha256$120000$pfs7C7fGYfLj$NChDlQXySiObh68BhIO8J3SpOhcZegdXZ2tqRQAPOZw=', '2019-05-09 05:18:54.295203', 'rental@gmail.com', 1, 0, 0, 1, '0', '2019-05-03 07:47:30.169445', 'rental', NULL, '0'),
(21, 'pbkdf2_sha256$120000$Mh45BVlXhVDh$rxaBIOyMD0PTdaUPzpIHHXZM1MegJ6u6Oi/6c4zPQRw=', NULL, 'hotel@staff123.com', 1, 0, 0, 1, '0', '2019-05-03 12:27:27.498087', '0', NULL, '0'),
(22, 'pbkdf2_sha256$120000$tyLhxfq1Pg13$4bGWfeZs1UTY2xhWP4LtmDyi1e+2iWSSkDypp5U68uo=', NULL, 'lorakut@host.local', 1, 0, 0, 1, '0', '2019-05-03 12:31:49.274535', '0', NULL, '0'),
(23, 'pbkdf2_sha256$120000$Polu1X1lcM8Z$gGtd9JxE54JvfZvM5lUem+icHOGRV+p/3WtGxXBANMs=', NULL, 'zukzetto@host.test', 1, 0, 0, 1, '0', '2019-05-03 12:38:16.576463', '0', NULL, '0'),
(24, 'pbkdf2_sha256$120000$9qqh6fNY4XlK$6+FE9JTh2oiDTQEUhZ7qIlNxV5EVIeVhGT87b9Hfxx4=', '2019-05-09 05:23:18.698541', 'some@staff.com', 1, 0, 0, 1, '0', '2019-05-05 07:26:11.575373', 'rental', NULL, '0'),
(25, 'pbkdf2_sha256$120000$a4mDImEnaUGE$S/b8qnuQcCmThqgPmQfsmihBZnSaOUWpRWSqqfO02Fo=', NULL, 'ewa@host.local', 1, 0, 0, 1, '0', '2019-05-05 08:12:01.459960', '0', NULL, '0'),
(26, 'pbkdf2_sha256$120000$UtJ739GnCQu4$IhaqNpyK4O2P6TtpVQ9w3Pjkr7VoAITVSCoykcp0xLs=', '2019-05-09 07:40:27.454100', 'rentalstaff@gmail123.com', 1, 0, 0, 1, '0', '2019-05-09 06:50:01.098073', 'rental', NULL, '0'),
(27, 'pbkdf2_sha256$120000$NiA22PkPY4ho$8kgnEu3FBjjJtGERgxGdWBZB3dwYp49iVSOHk4pB5QA=', NULL, 'admin@admin123.com', 0, 0, 0, 0, '0', '2019-05-28 11:21:32.072451', '0', NULL, '0'),
(28, 'pbkdf2_sha256$120000$lPHDokc5oz2E$CZEGoNpiumbw1dj6WuiL070zxBk6PtWtsqd9nsFAIMM=', NULL, 'some@some.com', 0, 0, 0, 1, '0', '2019-07-09 05:11:52.391385', '0', NULL, '0'),
(29, 'pbkdf2_sha256$120000$wyS5gDIppAqK$EfX5y5mEmGRlc7K+bkuM/DboKJXImvNJqq6ppc7co5Y=', NULL, 'rajkumari@codeforcore.com', 0, 0, 0, 1, '0', '2019-07-09 10:29:32.954892', '0', NULL, '0'),
(30, 'pbkdf2_sha256$120000$dOl89SmovyjJ$d50mOwt+v5H4e/SspIKKShf1qRoVv/yZPUaKG2hC3c4=', NULL, 'dummy@maildrop.cc', 0, 0, 0, 0, '0', '2019-08-26 06:40:33.731123', '0', NULL, '0'),
(31, 'pbkdf2_sha256$120000$YQiM9P8xzrPY$Xc6gHyvxCyxcTwlzmTeArIxhZ58uDhCr4o7zS8uwfTo=', NULL, 'bike@maildrop.cc', 0, 0, 0, 0, '0', '2019-08-26 06:44:10.798804', '0', NULL, '0'),
(32, 'pbkdf2_sha256$120000$ivzyi06yhW4W$px8ZeONglZFpFaM+M+eN8w+5ScUSCA4z1bRgsguHvys=', '2019-08-26 07:06:30.715215', 'karki.soyesha@gmail.com', 1, 0, 0, 1, '0', '2019-08-26 06:53:04.976187', 'hotel', NULL, '0'),
(68, 'pbkdf2_sha256$120000$ivzyi06yhW4W$px8ZeONglZFpFaM+M+eN8w+5ScUSCA4z1bRgsguHvys=', '2019-08-29 06:12:21.547718', 'xpramod@gmail.com1', 1, 0, 0, 1, '0', '2019-08-29 05:27:38.249543', '0', NULL, '0'),
(69, 'pbkdf2_sha256$120000$JKA2F2kJbpyf$RTpafIS6osbAgrhfyLj6T1Jc/PZaGO4owUlH80kEP9I=', NULL, 'xpramod@outlook.com', 0, 0, 0, 0, '0', '2019-08-29 05:27:48.415239', '0', NULL, '0'),
(70, 'pbkdf2_sha256$120000$HdNILmFDc2fk$TkW9JZ3LAW3rFh9BPqx0xMUEs6mwDodyWYAn7vPUWZk=', NULL, 'apar.apex@gmail.com', 0, 0, 0, 0, '0', '2019-08-29 05:27:54.229685', '0', NULL, '0'),
(71, 'pbkdf2_sha256$120000$LBX5D83CQfV2$Vx9wGPJAhtP7zSWOWDzqkO2Bt8jVto9neDt9VFanxdI=', NULL, 'xpramod@yahoo.com', 0, 0, 0, 0, '0', '2019-08-29 05:27:59.639003', '0', NULL, '0'),
(74, 'pbkdf2_sha256$120000$pAFsl7WCJRtc$pFWfsMgQjEjAL9OlgSBtt6r23lPYWTB5QCAVSymbgzU=', '2019-08-29 07:15:25.746461', 'chapagainaadarsha@yahoo.com', 1, 0, 0, 1, '0', '2019-08-29 07:14:19.200665', '0', NULL, '0'),
(77, 'pbkdf2_sha256$120000$hhaDikSg2GZw$mWQ1Njxzaz5/MBboX13L/iQ62Gvngk8o+5Dv9SMkQCU=', NULL, 'check@check.com', 0, 0, 0, 0, '0', '2019-08-29 07:36:47.233280', '0', NULL, '0'),
(78, 'pbkdf2_sha256$120000$EWCJCN5SIwVE$QmBao2ZiAOYavHOL34l/xRlIcQLtr/6+7yWhrhJzdZA=', NULL, 'me.anjanacharya@gmail.com', 0, 0, 0, 0, '0', '2019-09-19 04:55:34.312742', '0', NULL, '0'),
(79, 'pbkdf2_sha256$120000$E02M6VeWRJdF$MFSrDr8+XH28gvO1oFLJBkVhtu3zG0NYZ17o962OVko=', NULL, 'aparpramod@gmail.com', 0, 0, 0, 0, '0', '2019-09-19 04:56:49.347907', '0', NULL, '0'),
(80, 'pbkdf2_sha256$120000$UNL7g25TlWIt$MC4WpZt5LqqpNLXvrfBX9ze6fyK9194d+p3sk2YYFXI=', '2019-09-19 05:02:15.264664', 'codeforcore@gmail.com', 1, 0, 0, 1, '0', '2019-09-19 04:57:22.798613', '0', NULL, '0'),
(81, 'pbkdf2_sha256$120000$fZQjgsxfoKi3$Lt1j3BqAhRhCJP/GzvuLAo4MGE01js1YiGbO5y526UQ=', '2020-02-25 06:13:03.323036', 'khdnisham1@gmail.com', 1, 0, 0, 1, '0', '2019-10-02 05:56:38.858108', 'hotel', NULL, '0'),
(82, 'pbkdf2_sha256$120000$gzMJ6Jhmq4ov$bursQHtPN1IGuot24YZAClgGtyXNHg1hS59R63GoOdI=', NULL, 'sabin@gmail.com', 0, 0, 0, 1, '0', '2019-11-13 06:04:41.037540', '0', NULL, '0'),
(83, 'pbkdf2_sha256$120000$jqqQw3H5sqrd$zUQjva4gpG1CrxIoYYIv6Vu6zBER2HhpYhO6HR2rolc=', NULL, 'soyeshaa@gmail.com', 0, 0, 0, 1, '0', '2019-11-13 07:58:51.558963', '0', NULL, '0'),
(84, 'pbkdf2_sha256$120000$XVcx90wponCv$xrmXezewqHOiqL+s46VoyiMhwsr+YJXnypTsQvv7Bkc=', NULL, 'dsubash108@gmail.com', 0, 0, 0, 1, '0', '2019-11-27 12:01:59.080256', '0', NULL, '0'),
(85, 'pbkdf2_sha256$120000$7Ycq8LNnjZLx$Gsy/g61L+C6G+TS0AkU+4/k/vrnz22JUdb1QiKwS8dw=', NULL, 'aadarshachapagain@outlook.com', 0, 0, 0, 1, '0', '2019-11-29 12:46:49.111809', '0', '', 'outlook'),
(86, 'pbkdf2_sha256$120000$yl1AAgmKhltW$iWYHCmHo2m+NbF8CKPpC62yclBtf9+UPSjKgi5NAvwE=', NULL, 'check@gmail.com', 0, 0, 0, 1, '0', '2019-12-01 06:03:49.388742', '0', NULL, 'gmail'),
(88, 'pbkdf2_sha256$120000$aYQf46qZasOh$DvT+OnzZtF2yT7fY6g4EJDBjJfGpji+uhDlik6RtSzU=', NULL, 'nastyraj7@gmail.com', 0, 0, 0, 1, '0', '2019-12-01 06:48:32.126359', '0', NULL, 'facebook'),
(89, 'pbkdf2_sha256$120000$u1G4SN6ttARe$qxjwNIRSI22S7Aykt75zjNbjBQbcnFGtTwJ4EgrO4z0=', NULL, 'ayFxe7JRfQdOTCg5MgSKgECYCnu1@bigsafar.com', 0, 0, 0, 1, '0', '2019-12-01 08:14:19.605693', '0', NULL, 'facebook'),
(90, 'pbkdf2_sha256$120000$erxCF0xWK612$sJYf1FZXYOo8iN2EDOyFM/BODZlZB+n/05R0IistQXQ=', NULL, 'pk@bigsafar.com', 0, 0, 0, 1, '0', '2019-12-01 09:22:09.527686', '0', NULL, 'email'),
(91, 'pbkdf2_sha256$120000$aCgAGfrOsOAR$2bh+5s9XnvKbuvwmF9fsb7R34Cbbvx7TfTnwB7Ju3BU=', NULL, 'rajc4c@gmail.com', 0, 0, 0, 1, '0', '2019-12-01 10:09:49.145502', '0', NULL, 'google'),
(92, 'pbkdf2_sha256$120000$XoFPifrgYpcM$E/CAIq12UlndCo3+VTiv9WZSdL+1jTh3UeEsjjydO8s=', NULL, 'fantayraaz12@gmail.com', 0, 0, 0, 1, '0', '2019-12-01 11:07:36.104251', '0', NULL, 'facebook'),
(93, 'pbkdf2_sha256$120000$A1nf1OP0NUFv$KZjGTHV+1LMpsnieBKOWx2gZIYeIThZN0VWJ6nwJ7xI=', NULL, 'test@gmail.com', 0, 0, 0, 1, '0', '2019-12-03 10:10:25.869663', '0', NULL, '0'),
(94, 'pbkdf2_sha256$120000$j3ngKIoK2tI7$WKYqLaECpv0TSfvkBo38Y64/xORPwTRMhr+7haoZn9E=', NULL, 'postman2@gmail.com', 0, 0, 0, 1, '0', '2019-12-04 07:08:05.161863', '0', NULL, '0'),
(95, 'pbkdf2_sha256$120000$TtUepU1iIMke$ODZphQPe0tr5C/sHq8c40z9Qd8ep6yfcc2PYj7Lbu54=', NULL, 'test1@gmail.com', 0, 0, 0, 1, '0', '2019-12-04 07:27:36.333437', '0', NULL, '0'),
(96, 'pbkdf2_sha256$120000$AH2dZfP5DEPq$jlh2E4Mi8dARwU6Ua4NXh4UVeat6wbEKkkH/+GLD/XE=', NULL, 'test3@test.com', 0, 0, 0, 1, '0', '2019-12-04 07:36:00.404849', '0', NULL, '0'),
(97, 'pbkdf2_sha256$120000$ub7cWG6MqDQA$Pde+Js6RoixGDw9a+U4Wf++TjMc3HWt5sCkBs05spW4=', NULL, 'test4@gmail.com', 0, 0, 0, 1, '0', '2019-12-04 07:40:16.172148', '0', NULL, '0'),
(98, 'pbkdf2_sha256$120000$CCboUfNMBJ97$jxaMogogJbG0lqKeMxZ9JYFI1M3HcT/c6wPE/au8SqI=', NULL, 'testdata@gmail.com', 0, 0, 0, 1, '0', '2019-12-04 07:41:36.506285', '0', NULL, '0'),
(99, 'pbkdf2_sha256$120000$7IZjX77IUAkU$KbmvBytZA/iGxQQ2bP3vAy7JbQctKsqZC6jGDILoSHc=', NULL, 'testagain@gmail.com', 0, 0, 0, 1, '0', '2019-12-04 08:25:14.102265', '0', NULL, '0'),
(100, 'pbkdf2_sha256$120000$zHnsCIbF9re7$+MpTSNW/rkvWCgjEVM1vkKpMR0I/zVjYjcqULo+sUyA=', NULL, 'hhhhhh@gmail.com', 0, 0, 0, 1, '0', '2019-12-04 11:35:07.502702', '0', NULL, '0'),
(101, 'pbkdf2_sha256$120000$ICPdhr1HbN9v$+56os3HLgJGXX4O5FeGbfOq+03BNXY/NnGkeSBtGJf8=', NULL, 'newForm@gmail.com', 0, 0, 0, 1, '0', '2019-12-05 06:36:57.151675', '0', NULL, '0'),
(102, 'pbkdf2_sha256$120000$S2hvGZxD1bKp$BqBWpZX2TSczDVuhVvmgnN103wHkTQvE8gYVNfp36XI=', NULL, 'testhere@gmail.com', 0, 0, 0, 1, '0', '2019-12-08 08:18:54.558879', '0', NULL, '0'),
(103, 'pbkdf2_sha256$120000$3w2V6ixwbHgq$ky4f1Tcliv72BKtrpAu+Owp/7cBOIRuXFq9k3bdcIUc=', NULL, 'testagain2@gmail.com', 0, 0, 0, 1, '0', '2019-12-08 08:20:15.747768', '0', NULL, '0'),
(104, 'pbkdf2_sha256$120000$1kd3mZW5Pb21$cOI9BOcu3tkbK4NLzuDaVXPcMo4yzfZPzvj/el/ccTs=', NULL, 'test87@gmail.com', 0, 0, 0, 1, '0', '2019-12-08 08:21:03.190522', '0', NULL, '0'),
(105, 'pbkdf2_sha256$120000$r1iibWHz06n3$ghcC+RSpx/4/Fnix/RfXqF0kWVHHntRGMWMg0gyTLfQ=', NULL, 'postman@gmail.com', 0, 0, 0, 1, '0', '2019-12-08 10:17:03.690632', '0', NULL, '0'),
(106, 'pbkdf2_sha256$120000$rfICACzbGCOE$Pb/WaGSK1HKZ2k9kXx81Ct1JW/UF/GvTpeBOi4XNL4E=', NULL, 'testet12@gmail.com', 0, 0, 0, 1, '0', '2019-12-08 11:09:52.051110', '0', NULL, '0'),
(107, 'pbkdf2_sha256$120000$urIkc8gbbV8k$OD76f2wAOKC+XLAfwtWU48Td9ygu7CAmsWBo/8/HDO8=', NULL, 'hellodfg@gmail.com', 0, 0, 0, 1, '0', '2019-12-09 09:28:40.724141', '0', NULL, '0'),
(108, 'pbkdf2_sha256$120000$Ei9KWxUQ38jn$Bew48UvnVcopobmPXeZUhemv5xvTYQxraolknItYPUY=', NULL, 'shrsth.ameet@gmail.com', 0, 0, 0, 1, '0', '2019-12-12 05:57:01.692772', '0', NULL, 'google'),
(109, 'pbkdf2_sha256$120000$pbJNYqKzPqWO$hBdpqpPCa6BwehDhjaOpQ7QPqfKI8WTcr6TIX1ntsXo=', NULL, 'asas@asasas.com', 0, 0, 0, 1, '0', '2019-12-15 07:04:34.569882', '0', NULL, '0'),
(110, 'pbkdf2_sha256$120000$9EG0Cerue6bL$qFPHgv4nllz4ltEjufetGg2YAJiQYBveolcz8INSvyc=', NULL, 'helloheelo456@gmail.com', 0, 0, 0, 1, '0', '2019-12-15 07:10:06.546874', '0', NULL, '0'),
(111, 'pbkdf2_sha256$120000$IiCxTQGg2koc$URUbisfGHHGKD6esfVl1V9BH+UINfjFBU7sCsV13LSM=', '2020-02-28 06:33:50.020795', 'rajkumar.pudasaini25@gmail.com', 1, 0, 0, 1, '0', '2019-12-30 07:56:33.100016', 'hotel', NULL, '0'),
(112, 'pbkdf2_sha256$120000$BakW2Fs2MZQk$o+gU+jJeUWzx6I+5pNl2iDRaeTDTm4bX5KSJ8sY4Mmw=', NULL, 'checking@checking.com', 0, 0, 0, 1, '0', '2020-01-06 07:11:55.322209', '0', NULL, '0');

-- --------------------------------------------------------

--
-- Table structure for table `account_user_account_type`
--

CREATE TABLE `account_user_account_type` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `account_type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_user_account_type`
--

INSERT INTO `account_user_account_type` (`id`, `user_id`, `account_type_id`) VALUES
(1, 2, 1),
(2, 3, 7),
(65, 4, 1),
(62, 4, 3),
(63, 4, 5),
(64, 4, 7),
(4, 5, 8),
(57, 6, 1),
(55, 6, 5),
(56, 6, 7),
(6, 7, 8),
(9, 8, 5),
(10, 9, 3),
(58, 10, 1),
(60, 10, 3),
(59, 10, 5),
(12, 11, 6),
(13, 12, 6),
(14, 13, 6),
(15, 14, 6),
(16, 15, 8),
(17, 16, 8),
(18, 17, 8),
(19, 18, 6),
(20, 19, 2),
(21, 20, 2),
(22, 21, 6),
(23, 22, 6),
(24, 23, 6),
(25, 24, 2),
(26, 25, 8),
(27, 26, 2),
(30, 30, 5),
(31, 31, 5),
(32, 32, 5),
(37, 68, 5),
(38, 69, 5),
(39, 70, 5),
(40, 71, 5),
(41, 74, 5),
(44, 77, 5),
(66, 78, 1),
(47, 79, 1),
(48, 80, 3),
(51, 81, 5),
(61, 111, 5);

-- --------------------------------------------------------

--
-- Table structure for table `account_user_groups`
--

CREATE TABLE `account_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `account_user_user_permissions`
--

CREATE TABLE `account_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('00f937a225d7a54ff42c3dc26e51ca97594b1955', '2019-08-29 07:26:26.627584', 75),
('07d3782d1c6a5b8f9450073b2d1b9ebeced46bab', '2019-07-09 10:29:33.143860', 29),
('0cce17d9bc6e23bfec21b1e623444af2ceb86c1e', '2019-04-28 07:49:38.314068', 17),
('0ea3197f28fcd6475043dbc57fcdd74a66c698ad', '2019-12-04 07:08:05.264167', 94),
('126487ec1861f5584beb78ef51dc201397760666', '2019-04-21 06:03:46.854593', 7),
('1675353334449b836d481cfeb50b015bf862dd62', '2019-12-03 10:10:25.967103', 93),
('1b2348540328d44a00f2514cd1bff57de37b0c2d', '2019-04-18 11:53:56.049619', 2),
('1tdthjOdvEdqKcujGnF7W7Kew9y2', '2019-12-12 05:57:01.839150', 108),
('261d692347b5091e7a7f23d334a85521c0d06ee5', '2019-12-04 07:40:16.271049', 97),
('2aac5eef7473b3ebf68f60828f7a44595511b3e2', '2019-08-26 06:44:10.972836', 31),
('2cc6c499b0aefd146f3f1d8a77ff3d50506be9b6', '2019-08-26 06:53:05.141143', 32),
('3ade872ed8bb508fb79564671de674ed086e5a97', '2019-08-29 07:36:47.405764', 77),
('3af1786bc11541573c5a691d2bd0fc84dc772890', '2019-05-28 11:21:32.281610', 27),
('4be6a9517bef50f82f4289156a26b73652b7278c', '2019-05-03 12:27:27.693972', 21),
('4e35630b578fdeb6d2790ab1b77d16753a40748a', '2019-04-24 06:50:22.204092', 11),
('4eacda5506333db357001b031aa4d1b25f781f5e', '2019-12-15 07:04:34.662528', 109),
('572fe54b285fe8284cb43d96c001b5a8c20d8f3c', '2019-04-28 07:40:28.192240', 16),
('579c5a47e06f84afe6a0daa8ad33ee6159251ffa', '2019-08-26 06:40:33.932855', 30),
('618f518d26301bd238295c0dd7ab029564905a4d', '2019-12-09 09:28:40.823637', 107),
('6426f1a0c6ab2e0665b2273716d77b49eca58733', '2019-05-03 07:25:48.274891', 19),
('6589c9e7d9eb025c05234b785a87bed4c04d55e9', '2019-04-18 12:30:21.151969', 3),
('67c2ab66a2dd878b9b36aa5f0c0b18e4b6585bd1', '2019-04-23 05:37:46.986017', 10),
('68b421015bc4e70b2e301303759e11ac86b911b6', '2019-04-22 07:45:14.734153', 8),
('6a7e6bc38c5b79d5cdd970a0ab34da1422710fa8', '2019-12-04 07:27:36.429259', 95),
('6dccdaa3e86dad5feeddfbf628c095d15bcebc3e', '2019-11-13 07:58:51.656919', 83),
('6dd2063ede3eaa42307ef78f5e2530e1c927d2a9', '2019-08-29 07:27:57.879817', 76),
('6ea67f1ac68afc0a843d77705e3f256ae32e4563', '2019-12-08 10:17:03.803292', 105),
('74ad663ea33cb2f7fd0e8ef811a7d7605d5d5a15', '2019-04-18 08:04:37.282415', 1),
('74ba94b1bca2da2c40e147febf608eda35a2bbc9', '2019-12-04 07:36:00.497746', 96),
('79fed7095816787d6a3d96c1a823d6e5b3944a8b', '2019-12-15 07:10:06.646352', 110),
('7c3be63a4d3912039440e586e6ada0a8e9e3949e', '2019-11-13 06:04:41.133519', 82),
('7cdf03e00d5cf2361f69c847dcf6ebf4db21667b', '2019-08-29 05:27:54.409245', 70),
('80aed949f0cdf0e203c351bab2c1ca82de7aa2d3', '2019-10-02 05:56:38.967309', 81),
('830d24d380de2eb0c1e56c55ab54ca05f0a8bc3c', '2019-12-30 07:56:33.208249', 111),
('8c272019208b6a59e0dd3ea53ea817f7fb8bb53c', '2019-04-25 07:27:31.546654', 13),
('8f48528d49464207a1e3d78e29a43e53303e7eba', '2019-08-29 05:27:48.583229', 69),
('9078ce9ef8aa79e27aaa34d077cc29f4df99f4f5', '2019-04-18 12:31:06.423319', 4),
('9746281670c7de958f8ce8ef7efcb855817fcda4', '2019-12-08 08:18:54.656391', 102),
('97c20cf539353bdd9a45e803f487c05cf62cae43', '2019-05-09 06:50:01.296578', 26),
('9dc08a518d5c2aab3568247d1d90cac4c6ef3471', '2019-07-09 05:11:52.575676', 28),
('9TfgzTkIYQaVyEXwm5pYMR246LE3', '2019-11-27 12:01:59.212705', 84),
('9TfgzTkIYQaVyEXwm5pYMR246LE5', '2019-11-29 12:46:49.219459', 85),
('a4a308b8251099b9c7a7d6c6fce59c71ca6c520a', '2019-05-05 07:26:11.770742', 24),
('a764534a2090a808ef3379cf9af2897f90982a53', '2019-05-03 12:38:16.750407', 23),
('a8f04367a62f48177657b96b2badb8285d217d5a', '2019-08-29 05:27:59.807364', 71),
('aa6062cd7db633e51d90f62ba31a4d9ee36662c4', '2019-08-29 05:27:38.435718', 68),
('aa74f71eaa33da250b5d22cb61b9a2aa6f68aee7', '2020-01-06 07:11:55.415160', 112),
('ayFxe7JRfQdOTCg5MgSKgECYCnu1', '2019-12-01 08:14:19.718340', 89),
('b69aa97ad356438f302ef4a4016a4de97c4b2aa2', '2019-04-25 07:28:44.401804', 14),
('b870be22e7cac00d13b564857a914fcae6b68cb4', '2019-09-19 04:56:49.467775', 79),
('b95f5c009cc0ce9765e28cff6825755d93d3c6a9', '2019-12-05 06:36:57.255504', 101),
('bc1cd06c89077b25d9e42cb322c587169c4a6bfa', '2019-04-19 07:33:12.861954', 5),
('c739961e74554fce054d3abc7c9a8a83eae1dffe', '2019-05-05 08:12:01.663249', 25),
('ca6ad9fc8f0d963c68e88162b28b495aa8f370f7', '2019-09-19 04:57:22.957563', 80),
('cb0ddf86ad784b9ed68251cf34f354dc8078d462', '2019-12-04 08:25:14.193848', 99),
('cf14e13c63fcd7f1adeb74023882b9a02b402cd9', '2019-12-04 11:35:07.611192', 100),
('cf95cbe0d8303b486b66f5a1fe8bd8dd99d1b27c', '2019-09-19 04:55:34.476827', 78),
('cfba72265bf65f633e53436748482e05328a852f', '2019-04-25 06:57:54.423896', 12),
('e0388ee4f06411f0f6707bd73451412d4a6b517e', '2019-04-22 11:25:52.240647', 9),
('e0eda54c8f1cac4fa9a6beb29742fa084c10cc98', '2019-08-29 07:14:19.366949', 74),
('e21e2088a6c0d6c528c558fec26175c90079e5d7', '2019-12-04 07:41:36.619198', 98),
('e5af63de52439d37a849771980c79daada902e01', '2019-05-02 10:13:05.988696', 18),
('ee4359f74a253204497f6e13c93885a0dd5c3e93', '2019-12-08 08:21:03.289428', 104),
('ee8659f57655e08574a0356859afa7fd6f50e7f9', '2019-12-08 11:09:52.164696', 106),
('ee9afba797f0b97fe32d5ca67ea61809b5f663a1', '2019-12-08 08:20:15.879828', 103),
('f0c9b4177ed542151f0bc6bf95f3bb95dc60ba05', '2019-04-28 07:24:40.781316', 15),
('fab500ec2953cf6d6240a8d6e75fe9d109eefe0d', '2019-05-03 12:31:49.469892', 22),
('fd3933e2bdbd461c02fde2a838835957af6f1b38', '2019-05-03 07:47:30.390393', 20),
('KdaUVxa7kOUtEjfadAZJoz3deXJ2', '2019-12-01 09:22:09.647213', 90),
('KQljR217A9OyandFcxgCHYeeJeD3', '2019-04-19 10:52:36.306344', 6),
('SNCwPTPdJlUI4sj37ZzKFJluJs53', '2019-12-01 06:48:32.223652', 88),
('sometokenfromfirebase', '2019-12-01 06:03:49.490104', 86),
('tHRtIfbVHvSPngQwWcNQLpol1b33', '2019-12-01 11:07:36.202845', 92),
('TuqIvsI2VcYzd34ig879DeGOYL62', '2019-12-01 10:09:49.245250', 91);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add address', 1, 'add_address'),
(2, 'Can change address', 1, 'change_address'),
(3, 'Can delete address', 1, 'delete_address'),
(4, 'Can view address', 1, 'view_address'),
(5, 'Can add users', 2, 'add_users'),
(6, 'Can change users', 2, 'change_users'),
(7, 'Can delete users', 2, 'delete_users'),
(8, 'Can view users', 2, 'view_users'),
(9, 'Can add city', 3, 'add_city'),
(10, 'Can change city', 3, 'change_city'),
(11, 'Can delete city', 3, 'delete_city'),
(12, 'Can view city', 3, 'view_city'),
(13, 'Can add country', 4, 'add_country'),
(14, 'Can change country', 4, 'change_country'),
(15, 'Can delete country', 4, 'delete_country'),
(16, 'Can view country', 4, 'view_country'),
(17, 'Can add hotel amenities', 5, 'add_hotelamenities'),
(18, 'Can change hotel amenities', 5, 'change_hotelamenities'),
(19, 'Can delete hotel amenities', 5, 'delete_hotelamenities'),
(20, 'Can view hotel amenities', 5, 'view_hotelamenities'),
(21, 'Can add hotel booking', 6, 'add_hotelbooking'),
(22, 'Can change hotel booking', 6, 'change_hotelbooking'),
(23, 'Can delete hotel booking', 6, 'delete_hotelbooking'),
(24, 'Can view hotel booking', 6, 'view_hotelbooking'),
(25, 'Can add hotel facilities', 7, 'add_hotelfacilities'),
(26, 'Can change hotel facilities', 7, 'change_hotelfacilities'),
(27, 'Can delete hotel facilities', 7, 'delete_hotelfacilities'),
(28, 'Can view hotel facilities', 7, 'view_hotelfacilities'),
(29, 'Can add hotel facilities middle', 8, 'add_hotelfacilitiesmiddle'),
(30, 'Can change hotel facilities middle', 8, 'change_hotelfacilitiesmiddle'),
(31, 'Can delete hotel facilities middle', 8, 'delete_hotelfacilitiesmiddle'),
(32, 'Can view hotel facilities middle', 8, 'view_hotelfacilitiesmiddle'),
(33, 'Can add hotel gallery', 9, 'add_hotelgallery'),
(34, 'Can change hotel gallery', 9, 'change_hotelgallery'),
(35, 'Can delete hotel gallery', 9, 'delete_hotelgallery'),
(36, 'Can view hotel gallery', 9, 'view_hotelgallery'),
(37, 'Can add hotel inventory', 10, 'add_hotelinventory'),
(38, 'Can change hotel inventory', 10, 'change_hotelinventory'),
(39, 'Can delete hotel inventory', 10, 'delete_hotelinventory'),
(40, 'Can view hotel inventory', 10, 'view_hotelinventory'),
(41, 'Can add hotelinventory_amenities', 11, 'add_hotelinventory_amenities'),
(42, 'Can change hotelinventory_amenities', 11, 'change_hotelinventory_amenities'),
(43, 'Can delete hotelinventory_amenities', 11, 'delete_hotelinventory_amenities'),
(44, 'Can view hotelinventory_amenities', 11, 'view_hotelinventory_amenities'),
(45, 'Can add hotelinventory_roomfeatures', 12, 'add_hotelinventory_roomfeatures'),
(46, 'Can change hotelinventory_roomfeatures', 12, 'change_hotelinventory_roomfeatures'),
(47, 'Can delete hotelinventory_roomfeatures', 12, 'delete_hotelinventory_roomfeatures'),
(48, 'Can view hotelinventory_roomfeatures', 12, 'view_hotelinventory_roomfeatures'),
(49, 'Can add hotelinventory_roomtype', 13, 'add_hotelinventory_roomtype'),
(50, 'Can change hotelinventory_roomtype', 13, 'change_hotelinventory_roomtype'),
(51, 'Can delete hotelinventory_roomtype', 13, 'delete_hotelinventory_roomtype'),
(52, 'Can view hotelinventory_roomtype', 13, 'view_hotelinventory_roomtype'),
(53, 'Can add hotel log', 14, 'add_hotellog'),
(54, 'Can change hotel log', 14, 'change_hotellog'),
(55, 'Can delete hotel log', 14, 'delete_hotellog'),
(56, 'Can view hotel log', 14, 'view_hotellog'),
(57, 'Can add hotel owner', 15, 'add_hotelowner'),
(58, 'Can change hotel owner', 15, 'change_hotelowner'),
(59, 'Can delete hotel owner', 15, 'delete_hotelowner'),
(60, 'Can view hotel owner', 15, 'view_hotelowner'),
(61, 'Can add hotel review', 16, 'add_hotelreview'),
(62, 'Can change hotel review', 16, 'change_hotelreview'),
(63, 'Can delete hotel review', 16, 'delete_hotelreview'),
(64, 'Can view hotel review', 16, 'view_hotelreview'),
(65, 'Can add hotel room feature', 17, 'add_hotelroomfeature'),
(66, 'Can change hotel room feature', 17, 'change_hotelroomfeature'),
(67, 'Can delete hotel room feature', 17, 'delete_hotelroomfeature'),
(68, 'Can view hotel room feature', 17, 'view_hotelroomfeature'),
(69, 'Can add hotel room type', 18, 'add_hotelroomtype'),
(70, 'Can change hotel room type', 18, 'change_hotelroomtype'),
(71, 'Can delete hotel room type', 18, 'delete_hotelroomtype'),
(72, 'Can view hotel room type', 18, 'view_hotelroomtype'),
(73, 'Can add hotels', 19, 'add_hotels'),
(74, 'Can change hotels', 19, 'change_hotels'),
(75, 'Can delete hotels', 19, 'delete_hotels'),
(76, 'Can view hotels', 19, 'view_hotels'),
(77, 'Can add hotel staff', 20, 'add_hotelstaff'),
(78, 'Can change hotel staff', 20, 'change_hotelstaff'),
(79, 'Can delete hotel staff', 20, 'delete_hotelstaff'),
(80, 'Can view hotel staff', 20, 'view_hotelstaff'),
(81, 'Can add inventory gallery', 21, 'add_inventorygallery'),
(82, 'Can change inventory gallery', 21, 'change_inventorygallery'),
(83, 'Can delete inventory gallery', 21, 'delete_inventorygallery'),
(84, 'Can view inventory gallery', 21, 'view_inventorygallery'),
(85, 'Can add landmark', 22, 'add_landmark'),
(86, 'Can change landmark', 22, 'change_landmark'),
(87, 'Can delete landmark', 22, 'delete_landmark'),
(88, 'Can view landmark', 22, 'view_landmark'),
(89, 'Can add state', 23, 'add_state'),
(90, 'Can change state', 23, 'change_state'),
(91, 'Can delete state', 23, 'delete_state'),
(92, 'Can view state', 23, 'view_state'),
(93, 'Can add hotel address', 24, 'add_hoteladdress'),
(94, 'Can change hotel address', 24, 'change_hoteladdress'),
(95, 'Can delete hotel address', 24, 'delete_hoteladdress'),
(96, 'Can view hotel address', 24, 'view_hoteladdress'),
(97, 'Can add tour gallery', 25, 'add_tourgallery'),
(98, 'Can change tour gallery', 25, 'change_tourgallery'),
(99, 'Can delete tour gallery', 25, 'delete_tourgallery'),
(100, 'Can view tour gallery', 25, 'view_tourgallery'),
(101, 'Can add tour package', 26, 'add_tourpackage'),
(102, 'Can change tour package', 26, 'change_tourpackage'),
(103, 'Can delete tour package', 26, 'delete_tourpackage'),
(104, 'Can view tour package', 26, 'view_tourpackage'),
(105, 'Can add tour package theme', 27, 'add_tourpackagetheme'),
(106, 'Can change tour package theme', 27, 'change_tourpackagetheme'),
(107, 'Can delete tour package theme', 27, 'delete_tourpackagetheme'),
(108, 'Can view tour package theme', 27, 'view_tourpackagetheme'),
(109, 'Can add tour package theme middle', 28, 'add_tourpackagethememiddle'),
(110, 'Can change tour package theme middle', 28, 'change_tourpackagethememiddle'),
(111, 'Can delete tour package theme middle', 28, 'delete_tourpackagethememiddle'),
(112, 'Can view tour package theme middle', 28, 'view_tourpackagethememiddle'),
(113, 'Can add tour pkg review', 29, 'add_tourpkgreview'),
(114, 'Can change tour pkg review', 29, 'change_tourpkgreview'),
(115, 'Can delete tour pkg review', 29, 'delete_tourpkgreview'),
(116, 'Can view tour pkg review', 29, 'view_tourpkgreview'),
(117, 'Can add travel_ tour owner', 30, 'add_travel_tourowner'),
(118, 'Can change travel_ tour owner', 30, 'change_travel_tourowner'),
(119, 'Can delete travel_ tour owner', 30, 'delete_travel_tourowner'),
(120, 'Can view travel_ tour owner', 30, 'view_travel_tourowner'),
(121, 'Can add travel company', 31, 'add_travelcompany'),
(122, 'Can change travel company', 31, 'change_travelcompany'),
(123, 'Can delete travel company', 31, 'delete_travelcompany'),
(124, 'Can view travel company', 31, 'view_travelcompany'),
(125, 'Can add travel facilities', 32, 'add_travelfacilities'),
(126, 'Can change travel facilities', 32, 'change_travelfacilities'),
(127, 'Can delete travel facilities', 32, 'delete_travelfacilities'),
(128, 'Can view travel facilities', 32, 'view_travelfacilities'),
(129, 'Can add travel facilities middle', 33, 'add_travelfacilitiesmiddle'),
(130, 'Can change travel facilities middle', 33, 'change_travelfacilitiesmiddle'),
(131, 'Can delete travel facilities middle', 33, 'delete_travelfacilitiesmiddle'),
(132, 'Can view travel facilities middle', 33, 'view_travelfacilitiesmiddle'),
(133, 'Can add travel include', 34, 'add_travelinclude'),
(134, 'Can change travel include', 34, 'change_travelinclude'),
(135, 'Can delete travel include', 34, 'delete_travelinclude'),
(136, 'Can view travel include', 34, 'view_travelinclude'),
(137, 'Can add travel itenary', 35, 'add_travelitenary'),
(138, 'Can change travel itenary', 35, 'change_travelitenary'),
(139, 'Can delete travel itenary', 35, 'delete_travelitenary'),
(140, 'Can view travel itenary', 35, 'view_travelitenary'),
(141, 'Can add travel staff', 36, 'add_travelstaff'),
(142, 'Can change travel staff', 36, 'change_travelstaff'),
(143, 'Can delete travel staff', 36, 'delete_travelstaff'),
(144, 'Can view travel staff', 36, 'view_travelstaff'),
(145, 'Can add tour company address', 37, 'add_tourcompanyaddress'),
(146, 'Can change tour company address', 37, 'change_tourcompanyaddress'),
(147, 'Can delete tour company address', 37, 'delete_tourcompanyaddress'),
(148, 'Can view tour company address', 37, 'view_tourcompanyaddress'),
(149, 'Can add user', 38, 'add_user'),
(150, 'Can change user', 38, 'change_user'),
(151, 'Can delete user', 38, 'delete_user'),
(152, 'Can view user', 38, 'view_user'),
(153, 'Can add account_ type', 39, 'add_account_type'),
(154, 'Can change account_ type', 39, 'change_account_type'),
(155, 'Can delete account_ type', 39, 'delete_account_type'),
(156, 'Can view account_ type', 39, 'view_account_type'),
(157, 'Can add owner profile', 40, 'add_ownerprofile'),
(158, 'Can change owner profile', 40, 'change_ownerprofile'),
(159, 'Can delete owner profile', 40, 'delete_ownerprofile'),
(160, 'Can view owner profile', 40, 'view_ownerprofile'),
(161, 'Can add staff profile', 41, 'add_staffprofile'),
(162, 'Can change staff profile', 41, 'change_staffprofile'),
(163, 'Can delete staff profile', 41, 'delete_staffprofile'),
(164, 'Can view staff profile', 41, 'view_staffprofile'),
(165, 'Can add rental company', 42, 'add_rentalcompany'),
(166, 'Can change rental company', 42, 'change_rentalcompany'),
(167, 'Can delete rental company', 42, 'delete_rentalcompany'),
(168, 'Can view rental company', 42, 'view_rentalcompany'),
(169, 'Can add rentals facilities', 43, 'add_rentalsfacilities'),
(170, 'Can change rentals facilities', 43, 'change_rentalsfacilities'),
(171, 'Can delete rentals facilities', 43, 'delete_rentalsfacilities'),
(172, 'Can view rentals facilities', 43, 'view_rentalsfacilities'),
(173, 'Can add vehicle category', 44, 'add_vehiclecategory'),
(174, 'Can change vehicle category', 44, 'change_vehiclecategory'),
(175, 'Can delete vehicle category', 44, 'delete_vehiclecategory'),
(176, 'Can view vehicle category', 44, 'view_vehiclecategory'),
(177, 'Can add vehicle detail', 45, 'add_vehicledetail'),
(178, 'Can change vehicle detail', 45, 'change_vehicledetail'),
(179, 'Can delete vehicle detail', 45, 'delete_vehicledetail'),
(180, 'Can view vehicle detail', 45, 'view_vehicledetail'),
(181, 'Can add vehicle inventory', 46, 'add_vehicleinventory'),
(182, 'Can change vehicle inventory', 46, 'change_vehicleinventory'),
(183, 'Can delete vehicle inventory', 46, 'delete_vehicleinventory'),
(184, 'Can view vehicle inventory', 46, 'view_vehicleinventory'),
(185, 'Can add vehicleinventory_vehiclefacilities', 47, 'add_vehicleinventory_vehiclefacilities'),
(186, 'Can change vehicleinventory_vehiclefacilities', 47, 'change_vehicleinventory_vehiclefacilities'),
(187, 'Can delete vehicleinventory_vehiclefacilities', 47, 'delete_vehicleinventory_vehiclefacilities'),
(188, 'Can view vehicleinventory_vehiclefacilities', 47, 'view_vehicleinventory_vehiclefacilities'),
(189, 'Can add vehicle inventory gallery', 48, 'add_vehicleinventorygallery'),
(190, 'Can change vehicle inventory gallery', 48, 'change_vehicleinventorygallery'),
(191, 'Can delete vehicle inventory gallery', 48, 'delete_vehicleinventorygallery'),
(192, 'Can view vehicle inventory gallery', 48, 'view_vehicleinventorygallery'),
(193, 'Can add rental company address', 49, 'add_rentalcompanyaddress'),
(194, 'Can change rental company address', 49, 'change_rentalcompanyaddress'),
(195, 'Can delete rental company address', 49, 'delete_rentalcompanyaddress'),
(196, 'Can view rental company address', 49, 'view_rentalcompanyaddress'),
(197, 'Can add restaurant category', 50, 'add_restaurantcategory'),
(198, 'Can change restaurant category', 50, 'change_restaurantcategory'),
(199, 'Can delete restaurant category', 50, 'delete_restaurantcategory'),
(200, 'Can view restaurant category', 50, 'view_restaurantcategory'),
(201, 'Can add restaurant company', 51, 'add_restaurantcompany'),
(202, 'Can change restaurant company', 51, 'change_restaurantcompany'),
(203, 'Can delete restaurant company', 51, 'delete_restaurantcompany'),
(204, 'Can view restaurant company', 51, 'view_restaurantcompany'),
(205, 'Can add restaurant facilities', 52, 'add_restaurantfacilities'),
(206, 'Can change restaurant facilities', 52, 'change_restaurantfacilities'),
(207, 'Can delete restaurant facilities', 52, 'delete_restaurantfacilities'),
(208, 'Can view restaurant facilities', 52, 'view_restaurantfacilities'),
(209, 'Can add restaurantfacilitys', 53, 'add_restaurantfacilitys'),
(210, 'Can change restaurantfacilitys', 53, 'change_restaurantfacilitys'),
(211, 'Can delete restaurantfacilitys', 53, 'delete_restaurantfacilitys'),
(212, 'Can view restaurantfacilitys', 53, 'view_restaurantfacilitys'),
(213, 'Can add restaurant gallery', 54, 'add_restaurantgallery'),
(214, 'Can change restaurant gallery', 54, 'change_restaurantgallery'),
(215, 'Can delete restaurant gallery', 54, 'delete_restaurantgallery'),
(216, 'Can view restaurant gallery', 54, 'view_restaurantgallery'),
(217, 'Can add restaurant inventory', 55, 'add_restaurantinventory'),
(218, 'Can change restaurant inventory', 55, 'change_restaurantinventory'),
(219, 'Can delete restaurant inventory', 55, 'delete_restaurantinventory'),
(220, 'Can view restaurant inventory', 55, 'view_restaurantinventory'),
(221, 'Can add restaurant menu', 56, 'add_restaurantmenu'),
(222, 'Can change restaurant menu', 56, 'change_restaurantmenu'),
(223, 'Can delete restaurant menu', 56, 'delete_restaurantmenu'),
(224, 'Can view restaurant menu', 56, 'view_restaurantmenu'),
(225, 'Can add restaurant special', 57, 'add_restaurantspecial'),
(226, 'Can change restaurant special', 57, 'change_restaurantspecial'),
(227, 'Can delete restaurant special', 57, 'delete_restaurantspecial'),
(228, 'Can view restaurant special', 57, 'view_restaurantspecial'),
(229, 'Can add restaurant table category', 58, 'add_restauranttablecategory'),
(230, 'Can change restaurant table category', 58, 'change_restauranttablecategory'),
(231, 'Can delete restaurant table category', 58, 'delete_restauranttablecategory'),
(232, 'Can view restaurant table category', 58, 'view_restauranttablecategory'),
(233, 'Can add restaurant company address', 59, 'add_restaurantcompanyaddress'),
(234, 'Can change restaurant company address', 59, 'change_restaurantcompanyaddress'),
(235, 'Can delete restaurant company address', 59, 'delete_restaurantcompanyaddress'),
(236, 'Can view restaurant company address', 59, 'view_restaurantcompanyaddress'),
(237, 'Can add Token', 60, 'add_token'),
(238, 'Can change Token', 60, 'change_token'),
(239, 'Can delete Token', 60, 'delete_token'),
(240, 'Can view Token', 60, 'view_token'),
(241, 'Can add log entry', 61, 'add_logentry'),
(242, 'Can change log entry', 61, 'change_logentry'),
(243, 'Can delete log entry', 61, 'delete_logentry'),
(244, 'Can view log entry', 61, 'view_logentry'),
(245, 'Can add permission', 62, 'add_permission'),
(246, 'Can change permission', 62, 'change_permission'),
(247, 'Can delete permission', 62, 'delete_permission'),
(248, 'Can view permission', 62, 'view_permission'),
(249, 'Can add group', 63, 'add_group'),
(250, 'Can change group', 63, 'change_group'),
(251, 'Can delete group', 63, 'delete_group'),
(252, 'Can view group', 63, 'view_group'),
(253, 'Can add content type', 64, 'add_contenttype'),
(254, 'Can change content type', 64, 'change_contenttype'),
(255, 'Can delete content type', 64, 'delete_contenttype'),
(256, 'Can view content type', 64, 'view_contenttype'),
(257, 'Can add session', 65, 'add_session'),
(258, 'Can change session', 65, 'change_session'),
(259, 'Can delete session', 65, 'delete_session'),
(260, 'Can view session', 65, 'view_session'),
(261, 'Can add hotels new', 66, 'add_hotelsnew'),
(262, 'Can change hotels new', 66, 'change_hotelsnew'),
(263, 'Can delete hotels new', 66, 'delete_hotelsnew'),
(264, 'Can view hotels new', 66, 'view_hotelsnew'),
(265, 'Can add hotel facilities middle new', 67, 'add_hotelfacilitiesmiddlenew'),
(266, 'Can change hotel facilities middle new', 67, 'change_hotelfacilitiesmiddlenew'),
(267, 'Can delete hotel facilities middle new', 67, 'delete_hotelfacilitiesmiddlenew'),
(268, 'Can view hotel facilities middle new', 67, 'view_hotelfacilitiesmiddlenew'),
(269, 'Can add travel excluded', 68, 'add_travelexcluded'),
(270, 'Can change travel excluded', 68, 'change_travelexcluded'),
(271, 'Can delete travel excluded', 68, 'delete_travelexcluded'),
(272, 'Can view travel excluded', 68, 'view_travelexcluded'),
(273, 'Can add cancellation_ policy', 69, 'add_cancellation_policy'),
(274, 'Can change cancellation_ policy', 69, 'change_cancellation_policy'),
(275, 'Can delete cancellation_ policy', 69, 'delete_cancellation_policy'),
(276, 'Can view cancellation_ policy', 69, 'view_cancellation_policy'),
(277, 'Can add hotel language middle', 70, 'add_hotellanguagemiddle'),
(278, 'Can change hotel language middle', 70, 'change_hotellanguagemiddle'),
(279, 'Can delete hotel language middle', 70, 'delete_hotellanguagemiddle'),
(280, 'Can view hotel language middle', 70, 'view_hotellanguagemiddle'),
(281, 'Can add language', 71, 'add_language'),
(282, 'Can change language', 71, 'change_language'),
(283, 'Can delete language', 71, 'delete_language'),
(284, 'Can view language', 71, 'view_language'),
(285, 'Can add bed type', 72, 'add_bedtype'),
(286, 'Can change bed type', 72, 'change_bedtype'),
(287, 'Can delete bed type', 72, 'delete_bedtype'),
(288, 'Can view bed type', 72, 'view_bedtype'),
(289, 'Can add inventory_ bed_ type', 73, 'add_inventory_bed_type'),
(290, 'Can change inventory_ bed_ type', 73, 'change_inventory_bed_type'),
(291, 'Can delete inventory_ bed_ type', 73, 'delete_inventory_bed_type'),
(292, 'Can view inventory_ bed_ type', 73, 'view_inventory_bed_type'),
(293, 'Can add customer', 74, 'add_customer'),
(294, 'Can change customer', 74, 'change_customer'),
(295, 'Can delete customer', 74, 'delete_customer'),
(296, 'Can view customer', 74, 'view_customer'),
(297, 'Can add guest detail', 75, 'add_guestdetail'),
(298, 'Can change guest detail', 75, 'change_guestdetail'),
(299, 'Can delete guest detail', 75, 'delete_guestdetail'),
(300, 'Can view guest detail', 75, 'view_guestdetail'),
(301, 'Can add guest doc detail', 76, 'add_guestdocdetail'),
(302, 'Can change guest doc detail', 76, 'change_guestdocdetail'),
(303, 'Can delete guest doc detail', 76, 'delete_guestdocdetail'),
(304, 'Can view guest doc detail', 76, 'view_guestdocdetail'),
(305, 'Can add booking table', 77, 'add_bookingtable'),
(306, 'Can change booking table', 77, 'change_bookingtable'),
(307, 'Can delete booking table', 77, 'delete_bookingtable'),
(308, 'Can view booking table', 77, 'view_bookingtable'),
(309, 'Can add module booking', 78, 'add_modulebooking'),
(310, 'Can change module booking', 78, 'change_modulebooking'),
(311, 'Can delete module booking', 78, 'delete_modulebooking'),
(312, 'Can view module booking', 78, 'view_modulebooking'),
(313, 'Can add reward', 79, 'add_reward'),
(314, 'Can change reward', 79, 'change_reward'),
(315, 'Can delete reward', 79, 'delete_reward'),
(316, 'Can view reward', 79, 'view_reward'),
(317, 'Can add reward point', 80, 'add_rewardpoint'),
(318, 'Can change reward point', 80, 'change_rewardpoint'),
(319, 'Can delete reward point', 80, 'delete_rewardpoint'),
(320, 'Can view reward point', 80, 'view_rewardpoint'),
(321, 'Can add membership_plan', 81, 'add_membership_plan'),
(322, 'Can change membership_plan', 81, 'change_membership_plan'),
(323, 'Can delete membership_plan', 81, 'delete_membership_plan'),
(324, 'Can view membership_plan', 81, 'view_membership_plan'),
(325, 'Can add credit point', 82, 'add_creditpoint'),
(326, 'Can change credit point', 82, 'change_creditpoint'),
(327, 'Can delete credit point', 82, 'delete_creditpoint'),
(328, 'Can view credit point', 82, 'view_creditpoint'),
(329, 'Can add virtual point', 83, 'add_virtualpoint'),
(330, 'Can change virtual point', 83, 'change_virtualpoint'),
(331, 'Can delete virtual point', 83, 'delete_virtualpoint'),
(332, 'Can view virtual point', 83, 'view_virtualpoint'),
(333, 'Can add point setting', 84, 'add_pointsetting'),
(334, 'Can change point setting', 84, 'change_pointsetting'),
(335, 'Can delete point setting', 84, 'delete_pointsetting'),
(336, 'Can view point setting', 84, 'view_pointsetting'),
(337, 'Can add business partners', 85, 'add_businesspartners'),
(338, 'Can change business partners', 85, 'change_businesspartners'),
(339, 'Can delete business partners', 85, 'delete_businesspartners'),
(340, 'Can view business partners', 85, 'view_businesspartners'),
(341, 'Can add points on sale', 86, 'add_pointsonsale'),
(342, 'Can change points on sale', 86, 'change_pointsonsale'),
(343, 'Can delete points on sale', 86, 'delete_pointsonsale'),
(344, 'Can view points on sale', 86, 'view_pointsonsale'),
(345, 'Can add referee and referred', 87, 'add_refereeandreferred'),
(346, 'Can change referee and referred', 87, 'change_refereeandreferred'),
(347, 'Can delete referee and referred', 87, 'delete_refereeandreferred'),
(348, 'Can view referee and referred', 87, 'view_refereeandreferred'),
(349, 'Can add team leader', 88, 'add_teamleader'),
(350, 'Can change team leader', 88, 'change_teamleader'),
(351, 'Can delete team leader', 88, 'delete_teamleader'),
(352, 'Can view team leader', 88, 'view_teamleader'),
(353, 'Can add points log', 89, 'add_pointslog'),
(354, 'Can change points log', 89, 'change_pointslog'),
(355, 'Can delete points log', 89, 'delete_pointslog'),
(356, 'Can view points log', 89, 'view_pointslog'),
(357, 'Can add business cash bonus', 90, 'add_businesscashbonus'),
(358, 'Can change business cash bonus', 90, 'change_businesscashbonus'),
(359, 'Can delete business cash bonus', 90, 'delete_businesscashbonus'),
(360, 'Can view business cash bonus', 90, 'view_businesscashbonus'),
(361, 'Can add spotlight', 91, 'add_spotlight'),
(362, 'Can change spotlight', 91, 'change_spotlight'),
(363, 'Can delete spotlight', 91, 'delete_spotlight'),
(364, 'Can view spotlight', 91, 'view_spotlight'),
(365, 'Can add offers', 92, 'add_offers'),
(366, 'Can change offers', 92, 'change_offers'),
(367, 'Can delete offers', 92, 'delete_offers'),
(368, 'Can view offers', 92, 'view_offers'),
(369, 'Can add inventory offers', 93, 'add_inventoryoffers'),
(370, 'Can change inventory offers', 93, 'change_inventoryoffers'),
(371, 'Can delete inventory offers', 93, 'delete_inventoryoffers'),
(372, 'Can view inventory offers', 93, 'view_inventoryoffers'),
(373, 'Can add add on hotel', 94, 'add_addonhotel'),
(374, 'Can change add on hotel', 94, 'change_addonhotel'),
(375, 'Can delete add on hotel', 94, 'delete_addonhotel'),
(376, 'Can view add on hotel', 94, 'view_addonhotel'),
(377, 'Can add add on transport', 95, 'add_addontransport'),
(378, 'Can change add on transport', 95, 'change_addontransport'),
(379, 'Can delete add on transport', 95, 'delete_addontransport'),
(380, 'Can view add on transport', 95, 'view_addontransport'),
(381, 'Can add addon activities', 96, 'add_addonactivities'),
(382, 'Can change addon activities', 96, 'change_addonactivities'),
(383, 'Can delete addon activities', 96, 'delete_addonactivities'),
(384, 'Can view addon activities', 96, 'view_addonactivities'),
(385, 'Can add addon cuisine', 97, 'add_addoncuisine'),
(386, 'Can change addon cuisine', 97, 'change_addoncuisine'),
(387, 'Can delete addon cuisine', 97, 'delete_addoncuisine'),
(388, 'Can view addon cuisine', 97, 'view_addoncuisine'),
(389, 'Can add spotlight', 98, 'add_spotlight'),
(390, 'Can change spotlight', 98, 'change_spotlight'),
(391, 'Can delete spotlight', 98, 'delete_spotlight'),
(392, 'Can view spotlight', 98, 'view_spotlight'),
(393, 'Can add blog', 99, 'add_blog'),
(394, 'Can change blog', 99, 'change_blog'),
(395, 'Can delete blog', 99, 'delete_blog'),
(396, 'Can view blog', 99, 'view_blog'),
(397, 'Can add package offers', 100, 'add_packageoffers'),
(398, 'Can change package offers', 100, 'change_packageoffers'),
(399, 'Can delete package offers', 100, 'delete_packageoffers'),
(400, 'Can view package offers', 100, 'view_packageoffers'),
(401, 'Can add spotlight', 101, 'add_spotlight'),
(402, 'Can change spotlight', 101, 'change_spotlight'),
(403, 'Can delete spotlight', 101, 'delete_spotlight'),
(404, 'Can view spotlight', 101, 'view_spotlight'),
(405, 'Can add vehicle offers', 102, 'add_vehicleoffers'),
(406, 'Can change vehicle offers', 102, 'change_vehicleoffers'),
(407, 'Can delete vehicle offers', 102, 'delete_vehicleoffers'),
(408, 'Can view vehicle offers', 102, 'view_vehicleoffers'),
(409, 'Can add rental offers', 103, 'add_rentaloffers'),
(410, 'Can change rental offers', 103, 'change_rentaloffers'),
(411, 'Can delete rental offers', 103, 'delete_rentaloffers'),
(412, 'Can view rental offers', 103, 'view_rentaloffers'),
(413, 'Can add travel offers', 104, 'add_traveloffers'),
(414, 'Can change travel offers', 104, 'change_traveloffers'),
(415, 'Can delete travel offers', 104, 'delete_traveloffers'),
(416, 'Can view travel offers', 104, 'view_traveloffers'),
(417, 'Can add spotlight', 105, 'add_spotlight'),
(418, 'Can change spotlight', 105, 'change_spotlight'),
(419, 'Can delete spotlight', 105, 'delete_spotlight'),
(420, 'Can view spotlight', 105, 'view_spotlight'),
(421, 'Can add restaurant offers', 106, 'add_restaurantoffers'),
(422, 'Can change restaurant offers', 106, 'change_restaurantoffers'),
(423, 'Can delete restaurant offers', 106, 'delete_restaurantoffers'),
(424, 'Can view restaurant offers', 106, 'view_restaurantoffers'),
(425, 'Can add password reset', 107, 'add_passwordreset'),
(426, 'Can change password reset', 107, 'change_passwordreset'),
(427, 'Can delete password reset', 107, 'delete_passwordreset'),
(428, 'Can view password reset', 107, 'view_passwordreset'),
(429, 'Can add bank detail', 108, 'add_bankdetail'),
(430, 'Can change bank detail', 108, 'change_bankdetail'),
(431, 'Can delete bank detail', 108, 'delete_bankdetail'),
(432, 'Can view bank detail', 108, 'view_bankdetail'),
(433, 'Can add hotel booking log', 109, 'add_hotelbookinglog'),
(434, 'Can change hotel booking log', 109, 'change_hotelbookinglog'),
(435, 'Can delete hotel booking log', 109, 'delete_hotelbookinglog'),
(436, 'Can view hotel booking log', 109, 'view_hotelbookinglog'),
(437, 'Can add vehicle brand', 110, 'add_vehiclebrand'),
(438, 'Can change vehicle brand', 110, 'change_vehiclebrand'),
(439, 'Can delete vehicle brand', 110, 'delete_vehiclebrand'),
(440, 'Can view vehicle brand', 110, 'view_vehiclebrand'),
(441, 'Can add bank detail', 111, 'add_bankdetail'),
(442, 'Can change bank detail', 111, 'change_bankdetail'),
(443, 'Can delete bank detail', 111, 'delete_bankdetail'),
(444, 'Can view bank detail', 111, 'view_bankdetail'),
(445, 'Can add favourites', 112, 'add_favourites'),
(446, 'Can change favourites', 112, 'change_favourites'),
(447, 'Can delete favourites', 112, 'delete_favourites'),
(448, 'Can view favourites', 112, 'view_favourites'),
(449, 'Can add faq', 113, 'add_faq'),
(450, 'Can change faq', 113, 'change_faq'),
(451, 'Can delete faq', 113, 'delete_faq'),
(452, 'Can view faq', 113, 'view_faq'),
(453, 'Can add inventory update', 114, 'add_inventoryupdate'),
(454, 'Can change inventory update', 114, 'change_inventoryupdate'),
(455, 'Can delete inventory update', 114, 'delete_inventoryupdate'),
(456, 'Can view inventory update', 114, 'view_inventoryupdate');

-- --------------------------------------------------------

--
-- Table structure for table `blog_blog`
--

CREATE TABLE `blog_blog` (
  `id` int(11) NOT NULL,
  `writer` varchar(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `package_id` int(11) DEFAULT NULL,
  `description` longtext,
  `created_at` datetime(6) NOT NULL,
  `date` datetime(6) DEFAULT NULL,
  `module` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blog_blog`
--

INSERT INTO `blog_blog` (`id`, `writer`, `url`, `company_id`, `package_id`, `description`, `created_at`, `date`, `module`) VALUES
(12, 'some writer edited', 'some url 1234', 4, 9, 'some descccccc', '2019-07-26 08:01:51.861207', '2019-01-01 00:00:00.000000', 'travel_tour '),
(13, 'khaleed husaain', 'fd.com', 4, 9, 'some desccc', '2019-07-26 08:04:05.324518', '2019-01-01 00:00:00.000000', 'travel_tour '),
(14, 'wroter12333', 'some url', 4, 3, 'some desc', '2019-07-26 10:37:18.766115', '2019-01-01 00:00:00.000000', 'travel_tour '),
(15, 'wroter12333', 'some url', 1, 3, 'some desc', '2019-07-26 10:37:18.766115', '2019-01-01 00:00:00.000000', 'rental '),
(16, 'khaleed husaain', 'fd.com', 4, NULL, 'some desccc', '2019-07-26 08:04:05.324518', '2019-01-01 00:00:00.000000', 'travel_tour ');

-- --------------------------------------------------------

--
-- Table structure for table `booking_bookingtable`
--

CREATE TABLE `booking_bookingtable` (
  `id` int(11) NOT NULL,
  `payment_method` varchar(250) DEFAULT NULL,
  `payment_type` varchar(250) DEFAULT NULL,
  `payment_status` varchar(250) DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `total_discount` decimal(10,2) DEFAULT NULL,
  `total_tax` decimal(10,2) DEFAULT NULL,
  `booked_date` date DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `seenStatus` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_businesscashbonus`
--

CREATE TABLE `booking_businesscashbonus` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `cash_bonus_amount` decimal(10,2) DEFAULT NULL,
  `net_total` decimal(10,2) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `transaction_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `booking_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_businesspartners`
--

CREATE TABLE `booking_businesspartners` (
  `id` int(11) NOT NULL,
  `type` varchar(200) DEFAULT NULL,
  `setupcost` decimal(10,2) DEFAULT NULL,
  `renewalcost` decimal(10,2) DEFAULT NULL,
  `acctransferable` tinyint(1) DEFAULT NULL,
  `refundable` tinyint(1) DEFAULT NULL,
  `flightincludedCb` decimal(10,2) DEFAULT NULL,
  `flightexcludedCb` decimal(10,2) DEFAULT NULL,
  `flightincludedVb` decimal(10,2) DEFAULT NULL,
  `package_worth` decimal(10,2) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `return_ticket_worth` decimal(10,2) DEFAULT NULL,
  `countforreturnticket` int(11) DEFAULT NULL,
  `credit_point_for_old` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_customer`
--

CREATE TABLE `booking_customer` (
  `name` varchar(60) DEFAULT NULL,
  `contact` varchar(17) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `address` varchar(80) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `reward` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `uniqtoken` varchar(100) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  `memplan_id` int(11) DEFAULT NULL,
  `partnerplan_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking_customer`
--

INSERT INTO `booking_customer` (`name`, `contact`, `status`, `address`, `gender`, `dob`, `image`, `reward`, `created_at`, `user_id`, `uniqtoken`, `country_id`, `memplan_id`, `partnerplan_id`) VALUES
('Sabin Bajgain', '9813207240', 1, 'jadibuti', 'male', '1997-12-16', 'default.png', NULL, '2019-12-30 12:33:35.686788', 82, NULL, 649, NULL, NULL),
('Raj Shah', '9813207240', 1, 'jadibuti', 'male', '1997-12-16', 'default.png', NULL, '2019-12-30 12:33:35.686788', 91, NULL, 649, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `booking_guestdetail`
--

CREATE TABLE `booking_guestdetail` (
  `id` int(11) NOT NULL,
  `name` varchar(60) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `contact` varchar(17) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `address` varchar(80) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `booking_id` int(11) DEFAULT NULL,
  `city` varchar(80) DEFAULT NULL,
  `country` varchar(80) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_guestdocdetail`
--

CREATE TABLE `booking_guestdocdetail` (
  `id` int(11) NOT NULL,
  `document_type` varchar(60) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `document_number` varchar(60) DEFAULT NULL,
  `doc_file` varchar(100) NOT NULL,
  `visa_required` varchar(60) DEFAULT NULL,
  `visa_expiry` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `guest_detail_id` int(11) DEFAULT NULL,
  `issuing_country` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking_guestdocdetail`
--

INSERT INTO `booking_guestdocdetail` (`id`, `document_type`, `status`, `document_number`, `doc_file`, `visa_required`, `visa_expiry`, `created_at`, `guest_detail_id`, `issuing_country`) VALUES
(1, NULL, 0, NULL, '', NULL, NULL, '2020-01-10 11:26:03.977786', 3, NULL),
(2, NULL, 0, NULL, '', NULL, NULL, '2020-01-10 11:26:03.993896', 4, NULL),
(3, NULL, 0, NULL, '', NULL, NULL, '2020-01-10 11:30:32.418536', 5, NULL),
(4, NULL, 0, NULL, '', NULL, NULL, '2020-01-10 11:35:12.538280', 6, NULL),
(5, NULL, 0, NULL, '', NULL, NULL, '2020-01-10 11:53:00.275956', 7, NULL),
(6, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 06:27:15.700896', 8, NULL),
(7, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 07:02:39.380944', 9, NULL),
(8, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 07:21:56.239285', 10, NULL),
(9, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 10:23:04.639140', 11, NULL),
(10, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 10:34:33.237057', 12, NULL),
(11, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 11:14:34.609531', 13, NULL),
(12, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 11:26:13.209538', 14, NULL),
(13, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 11:28:28.552911', 15, NULL),
(14, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 11:34:17.618806', 16, NULL),
(15, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 11:38:10.205317', 17, NULL),
(16, NULL, 0, NULL, '', NULL, NULL, '2020-01-12 11:38:10.214058', 18, NULL),
(17, NULL, 0, NULL, '', NULL, NULL, '2020-01-13 05:32:26.587547', 19, NULL),
(18, NULL, 0, NULL, '', NULL, NULL, '2020-01-13 05:32:26.595360', 20, NULL),
(19, NULL, 0, NULL, '', NULL, NULL, '2020-01-13 05:32:26.603458', 21, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `booking_hotelbookinglog`
--

CREATE TABLE `booking_hotelbookinglog` (
  `id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `checkin_date` date DEFAULT NULL,
  `checkout_date` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `booking_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_modulebooking`
--

CREATE TABLE `booking_modulebooking` (
  `id` int(11) NOT NULL,
  `module_name` varchar(250) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `sub_total` decimal(10,2) DEFAULT NULL,
  `discount` decimal(10,2) DEFAULT NULL,
  `tax` decimal(10,2) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  `inventory_id` int(11) DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `booking_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_pointslog`
--

CREATE TABLE `booking_pointslog` (
  `id` int(11) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `points` int(11) DEFAULT NULL,
  `available` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_pointsonsale`
--

CREATE TABLE `booking_pointsonsale` (
  `id` int(11) NOT NULL,
  `sale_type` varchar(200) DEFAULT NULL,
  `credit_point` int(11) DEFAULT NULL,
  `virtualpoint` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_refereeandreferred`
--

CREATE TABLE `booking_refereeandreferred` (
  `id` int(11) NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `by_id` int(11) NOT NULL,
  `partnership_id` int(11) DEFAULT NULL,
  `to_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_reward`
--

CREATE TABLE `booking_reward` (
  `id` int(11) NOT NULL,
  `reward_type` varchar(250) DEFAULT NULL,
  `total_reward` decimal(10,2) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `booking_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_teamleader`
--

CREATE TABLE `booking_teamleader` (
  `id` int(11) NOT NULL,
  `type` varchar(200) DEFAULT NULL,
  `bonus_credit_point` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(39, 'account', 'account_type'),
(108, 'account', 'bankdetail'),
(113, 'account', 'faq'),
(71, 'account', 'language'),
(40, 'account', 'ownerprofile'),
(107, 'account', 'passwordreset'),
(41, 'account', 'staffprofile'),
(38, 'account', 'user'),
(61, 'admin', 'logentry'),
(63, 'auth', 'group'),
(62, 'auth', 'permission'),
(60, 'authtoken', 'token'),
(99, 'blog', 'blog'),
(77, 'booking', 'bookingtable'),
(90, 'booking', 'businesscashbonus'),
(85, 'booking', 'businesspartners'),
(74, 'booking', 'customer'),
(75, 'booking', 'guestdetail'),
(76, 'booking', 'guestdocdetail'),
(109, 'booking', 'hotelbookinglog'),
(78, 'booking', 'modulebooking'),
(89, 'booking', 'pointslog'),
(86, 'booking', 'pointsonsale'),
(87, 'booking', 'refereeandreferred'),
(79, 'booking', 'reward'),
(88, 'booking', 'teamleader'),
(64, 'contenttypes', 'contenttype'),
(72, 'hotel', 'bedtype'),
(69, 'hotel', 'cancellation_policy'),
(3, 'hotel', 'city'),
(4, 'hotel', 'country'),
(112, 'hotel', 'favourites'),
(24, 'hotel', 'hoteladdress'),
(5, 'hotel', 'hotelamenities'),
(6, 'hotel', 'hotelbooking'),
(7, 'hotel', 'hotelfacilities'),
(8, 'hotel', 'hotelfacilitiesmiddle'),
(67, 'hotel', 'hotelfacilitiesmiddlenew'),
(9, 'hotel', 'hotelgallery'),
(10, 'hotel', 'hotelinventory'),
(11, 'hotel', 'hotelinventory_amenities'),
(12, 'hotel', 'hotelinventory_roomfeatures'),
(13, 'hotel', 'hotelinventory_roomtype'),
(70, 'hotel', 'hotellanguagemiddle'),
(14, 'hotel', 'hotellog'),
(15, 'hotel', 'hotelowner'),
(16, 'hotel', 'hotelreview'),
(17, 'hotel', 'hotelroomfeature'),
(18, 'hotel', 'hotelroomtype'),
(19, 'hotel', 'hotels'),
(66, 'hotel', 'hotelsnew'),
(20, 'hotel', 'hotelstaff'),
(21, 'hotel', 'inventorygallery'),
(93, 'hotel', 'inventoryoffers'),
(114, 'hotel', 'inventoryupdate'),
(73, 'hotel', 'inventory_bed_type'),
(22, 'hotel', 'landmark'),
(92, 'hotel', 'offers'),
(91, 'hotel', 'spotlight'),
(23, 'hotel', 'state'),
(82, 'points', 'creditpoint'),
(81, 'points', 'membership_plan'),
(84, 'points', 'pointsetting'),
(80, 'points', 'rewardpoint'),
(83, 'points', 'virtualpoint'),
(111, 'rental', 'bankdetail'),
(42, 'rental', 'rentalcompany'),
(49, 'rental', 'rentalcompanyaddress'),
(103, 'rental', 'rentaloffers'),
(43, 'rental', 'rentalsfacilities'),
(101, 'rental', 'spotlight'),
(110, 'rental', 'vehiclebrand'),
(44, 'rental', 'vehiclecategory'),
(45, 'rental', 'vehicledetail'),
(46, 'rental', 'vehicleinventory'),
(48, 'rental', 'vehicleinventorygallery'),
(47, 'rental', 'vehicleinventory_vehiclefacilities'),
(102, 'rental', 'vehicleoffers'),
(50, 'restaurant', 'restaurantcategory'),
(51, 'restaurant', 'restaurantcompany'),
(59, 'restaurant', 'restaurantcompanyaddress'),
(52, 'restaurant', 'restaurantfacilities'),
(53, 'restaurant', 'restaurantfacilitys'),
(54, 'restaurant', 'restaurantgallery'),
(55, 'restaurant', 'restaurantinventory'),
(56, 'restaurant', 'restaurantmenu'),
(106, 'restaurant', 'restaurantoffers'),
(57, 'restaurant', 'restaurantspecial'),
(58, 'restaurant', 'restauranttablecategory'),
(105, 'restaurant', 'spotlight'),
(65, 'sessions', 'session'),
(96, 'travel_tour', 'addonactivities'),
(97, 'travel_tour', 'addoncuisine'),
(94, 'travel_tour', 'addonhotel'),
(95, 'travel_tour', 'addontransport'),
(100, 'travel_tour', 'packageoffers'),
(98, 'travel_tour', 'spotlight'),
(37, 'travel_tour', 'tourcompanyaddress'),
(25, 'travel_tour', 'tourgallery'),
(26, 'travel_tour', 'tourpackage'),
(27, 'travel_tour', 'tourpackagetheme'),
(28, 'travel_tour', 'tourpackagethememiddle'),
(29, 'travel_tour', 'tourpkgreview'),
(31, 'travel_tour', 'travelcompany'),
(68, 'travel_tour', 'travelexcluded'),
(32, 'travel_tour', 'travelfacilities'),
(33, 'travel_tour', 'travelfacilitiesmiddle'),
(34, 'travel_tour', 'travelinclude'),
(35, 'travel_tour', 'travelitenary'),
(104, 'travel_tour', 'traveloffers'),
(36, 'travel_tour', 'travelstaff'),
(30, 'travel_tour', 'travel_tourowner'),
(1, 'users', 'address'),
(2, 'users', 'users');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-04-18 08:03:18.764753'),
(2, 'contenttypes', '0002_remove_content_type_name', '2019-04-18 08:03:18.885413'),
(3, 'auth', '0001_initial', '2019-04-18 08:03:19.300293'),
(4, 'auth', '0002_alter_permission_name_max_length', '2019-04-18 08:03:19.385927'),
(5, 'auth', '0003_alter_user_email_max_length', '2019-04-18 08:03:19.396922'),
(6, 'auth', '0004_alter_user_username_opts', '2019-04-18 08:03:19.406806'),
(7, 'auth', '0005_alter_user_last_login_null', '2019-04-18 08:03:19.424144'),
(8, 'auth', '0006_require_contenttypes_0002', '2019-04-18 08:03:19.430195'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2019-04-18 08:03:19.444328'),
(10, 'auth', '0008_alter_user_username_max_length', '2019-04-18 08:03:19.457308'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2019-04-18 08:03:19.468839'),
(12, 'account', '0001_initial', '2019-04-18 08:03:20.476097'),
(13, 'account', '0002_account_type_description', '2019-04-18 08:03:20.530529'),
(14, 'admin', '0001_initial', '2019-04-18 08:03:20.734611'),
(15, 'admin', '0002_logentry_remove_auto_add', '2019-04-18 08:03:20.767152'),
(16, 'admin', '0003_logentry_add_action_flag_choices', '2019-04-18 08:03:20.795010'),
(17, 'authtoken', '0001_initial', '2019-04-18 08:03:20.907652'),
(18, 'authtoken', '0002_auto_20160226_1747', '2019-04-18 08:03:21.053388'),
(19, 'users', '0001_initial', '2019-04-18 08:03:21.321361'),
(20, 'hotel', '0001_initial', '2019-04-18 08:03:26.132933'),
(21, 'rental', '0001_initial', '2019-04-18 08:03:27.783603'),
(22, 'rental', '0002_vehicleinventory_description', '2019-04-18 08:03:27.866895'),
(23, 'rental', '0003_auto_20190412_0834', '2019-04-18 08:03:27.896751'),
(24, 'rental', '0004_auto_20190415_0605', '2019-04-18 08:03:28.130862'),
(25, 'rental', '0003_auto_20190414_0830', '2019-04-18 08:03:28.159959'),
(26, 'rental', '0005_merge_20190415_0730', '2019-04-18 08:03:28.169154'),
(27, 'rental', '0006_vehicleinventory_door_count', '2019-04-18 08:03:28.278816'),
(28, 'rental', '0005_merge_20190415_1337', '2019-04-18 08:03:28.286648'),
(29, 'rental', '0007_merge_20190415_1420', '2019-04-18 08:03:28.296401'),
(31, 'sessions', '0001_initial', '2019-04-18 08:03:30.933590'),
(32, 'travel_tour', '0001_initial', '2019-04-18 08:03:34.150538'),
(33, 'account', '0003_auto_20190423_1242', '2019-04-24 06:35:42.217403'),
(34, 'account', '0004_auto_20190423_1248', '2019-04-24 06:35:42.318519'),
(35, 'account', '0005_auto_20190423_1251', '2019-04-24 06:35:42.420584'),
(36, 'account', '0006_auto_20190423_1256', '2019-04-24 06:35:42.643607'),
(37, 'rental', '0008_vehicledetail_description', '2019-04-24 06:35:42.791669'),
(38, 'travel_tour', '0002_remove_tourpackage_address', '2019-04-24 06:35:42.931120'),
(39, 'travel_tour', '0003_auto_20190423_1754', '2019-04-24 06:35:43.170275'),
(40, 'travel_tour', '0004_auto_20190423_1754', '2019-04-24 06:35:43.390825'),
(41, 'travel_tour', '0005_auto_20190428_1352', '2019-04-29 05:43:48.822047'),
(42, 'travel_tour', '0006_auto_20190428_1355', '2019-04-29 05:43:49.041446'),
(43, 'travel_tour', '0007_auto_20190428_1402', '2019-04-29 05:43:49.503569'),
(44, 'hotel', '0002_auto_20190430_1131', '2019-04-30 11:31:40.654968'),
(45, 'hotel', '0003_auto_20190501_0150', '2019-05-01 01:51:03.369253'),
(46, 'hotel', '0003_auto_20190501_0229', '2019-05-01 02:30:00.245138'),
(47, 'account', '0007_auto_20190502_1534', '2019-05-02 13:27:29.533712'),
(48, 'travel_tour', '0008_auto_20190429_1028', '2019-05-02 13:27:29.819820'),
(49, 'travel_tour', '0009_auto_20190429_1115', '2019-05-02 13:27:29.848732'),
(50, 'travel_tour', '0010_auto_20190429_1118', '2019-05-02 13:27:29.876727'),
(51, 'travel_tour', '0011_auto_20190430_1628', '2019-05-02 13:27:29.920878'),
(52, 'travel_tour', '0012_auto_20190502_1158', '2019-05-02 13:27:30.059508'),
(53, 'travel_tour', '0013_auto_20190502_1800', '2019-05-02 13:27:30.200415'),
(54, 'account', '0008_auto_20190503_1015', '2019-05-03 05:31:39.388488'),
(55, 'hotel', '0004_auto_20190503_0531', '2019-05-03 05:31:39.695091'),
(56, 'travel_tour', '0014_auto_20190503_1015', '2019-05-03 05:31:40.019151'),
(57, 'account', '0009_auto_20190503_1127', '2019-05-05 13:16:50.173564'),
(58, 'travel_tour', '0015_auto_20190503_1803', '2019-05-05 13:16:50.273330'),
(59, 'travel_tour', '0016_auto_20190503_1804', '2019-05-05 13:16:50.346670'),
(60, 'account', '0010_auto_20190506_1250', '2019-05-07 05:15:59.577957'),
(61, 'account', '0011_auto_20190506_1306', '2019-05-07 05:15:59.635129'),
(62, 'rental', '0009_auto_20190507_1410', '2019-05-08 05:17:44.740994'),
(63, 'rental', '0010_auto_20190508_0517', '2019-05-08 05:17:44.882671'),
(66, 'travel_tour', '0017_travelexcluded', '2019-05-08 05:17:45.690362'),
(68, 'rental', '0011_auto_20190509_0641', '2019-05-09 06:41:25.527921'),
(69, 'rental', '0012_auto_20190510_1050', '2019-05-10 11:19:44.727684'),
(73, 'travel_tour', '0018_auto_20190510_1050', '2019-05-10 11:19:45.343624'),
(75, 'hotel', '0005_auto_20190510_1148', '2019-05-12 08:09:11.437646'),
(76, 'hotel', '0006_auto_20190513_1116', '2019-05-13 11:17:25.733717'),
(77, 'rental', '0013_auto_20190513_1116', '2019-05-13 11:17:25.758331'),
(79, 'hotel', '0002_auto_20190514_0553', '2019-05-14 05:53:54.123956'),
(80, 'hotel', '0003_auto_20190517_0713', '2019-05-17 07:14:22.691263'),
(81, 'hotel', '0004_auto_20190517_0827', '2019-05-17 08:27:13.070231'),
(82, 'hotel', '0003_hotels_star_rating', '2019-05-19 05:04:46.458405'),
(83, 'hotel', '0004_auto_20190517_1212', '2019-05-19 05:04:46.642814'),
(84, 'hotel', '0005_hotels_cancellation', '2019-05-19 05:04:46.733300'),
(85, 'hotel', '0006_hotels_cancellation_price', '2019-05-19 05:04:46.851244'),
(86, 'hotel', '0007_auto_20190517_1309', '2019-05-19 05:04:46.921533'),
(87, 'hotel', '0008_auto_20190517_1310', '2019-05-19 05:04:46.962151'),
(88, 'hotel', '0009_auto_20190517_1311', '2019-05-19 05:04:46.999073'),
(89, 'hotel', '0010_auto_20190517_1314', '2019-05-19 05:04:47.038421'),
(90, 'hotel', '0011_auto_20190517_1423', '2019-05-19 05:04:47.223632'),
(91, 'hotel', '0012_cancellation_policy', '2019-05-19 05:04:47.458860'),
(92, 'hotel', '0013_merge_20190519_0504', '2019-05-19 05:04:47.476337'),
(93, 'hotel', '0014_auto_20190519_1142', '2019-05-19 11:44:05.423737'),
(94, 'account', '0002_language', '2019-05-20 07:01:48.309840'),
(95, 'hotel', '0014_auto_20190519_1718', '2019-05-20 07:01:48.786952'),
(96, 'hotel', '0015_merge_20190519_1332', '2019-05-20 07:01:48.801194'),
(97, 'hotel', '0016_auto_20190520_1041', '2019-05-20 10:42:39.258222'),
(98, 'hotel', '0017_auto_20190520_1044', '2019-05-20 10:45:07.071609'),
(99, 'hotel', '0018_auto_20190520_1058', '2019-05-20 10:58:32.353292'),
(100, 'hotel', '0019_auto_20190520_1700', '2019-05-20 17:00:42.101690'),
(101, 'hotel', '0016_bedtype', '2019-05-20 17:14:30.300335'),
(102, 'hotel', '0017_inventory_bed_type', '2019-05-20 17:14:30.585604'),
(103, 'hotel', '0020_merge_20190520_1713', '2019-05-20 17:14:30.596961'),
(111, 'hotel', '0021_auto_20190530_0630', '2019-05-30 06:30:35.195676'),
(112, 'hotel', '0022_auto_20190531_0854', '2019-05-31 08:55:52.968161'),
(128, 'hotel', '0002_city_image', '2019-06-10 10:56:19.117312'),
(136, 'hotel', '0003_remove_hotelinventory_hoteladdress', '2019-06-18 06:12:09.170766'),
(137, 'travel_tour', '0002_auto_20190616_0635', '2019-06-20 06:17:33.892862'),
(163, 'hotel', '0004_auto_20190705_1645', '2019-07-07 08:05:13.696899'),
(164, 'hotel', '0005_auto_20190705_1725', '2019-07-07 08:05:13.884878'),
(183, 'hotel', '0006_country_country_code', '2019-07-11 05:48:53.374248'),
(185, 'hotel', '0007_remove_country_country_code', '2019-07-11 06:08:01.469655'),
(187, 'hotel', '0008_spotlight', '2019-07-14 08:09:03.532563'),
(188, 'hotel', '0009_auto_20190714_1034', '2019-07-14 10:34:55.127029'),
(189, 'hotel', '0006_offers', '2019-07-23 06:16:40.714459'),
(192, 'hotel', '0007_inventoryoffers', '2019-07-23 06:28:01.595130'),
(193, 'hotel', '0010_merge_20190722_0756', '2019-07-23 06:28:01.608212'),
(195, 'travel_tour', '0003_addonhotel', '2019-07-23 06:28:06.445353'),
(196, 'travel_tour', '0004_addontransport', '2019-07-23 06:31:46.103269'),
(197, 'hotel', '0010_merge_20190722_1647', '2019-07-24 04:47:48.660849'),
(198, 'hotel', '0011_merge_20190724_0447', '2019-07-24 04:47:48.692682'),
(199, 'travel_tour', '0003_addonactivities', '2019-07-24 04:47:49.051530'),
(200, 'travel_tour', '0004_addoncuisine', '2019-07-24 04:47:49.283221'),
(201, 'travel_tour', '0005_travelitenary_image', '2019-07-24 04:47:49.415180'),
(202, 'travel_tour', '0006_merge_20190724_0447', '2019-07-24 04:47:49.432284'),
(203, 'hotel', '0011_merge_20190723_1628', '2019-07-24 04:51:23.275815'),
(204, 'hotel', '0012_merge_20190724_0450', '2019-07-24 04:55:04.263609'),
(205, 'travel_tour', '0006_merge_20190723_1628', '2019-07-24 04:55:04.275445'),
(206, 'travel_tour', '0007_auto_20190724_0707', '2019-07-24 04:55:04.457714'),
(207, 'travel_tour', '0008_merge_20190724_0450', '2019-07-24 04:55:04.468642'),
(211, 'travel_tour', '0009_spotlight', '2019-07-24 07:17:02.292804'),
(212, 'blog', '0001_initial', '2019-07-24 12:51:24.348222'),
(213, 'blog', '0002_blog_module', '2019-07-26 08:01:18.346251'),
(214, 'hotel', '0013_hotelreview_module', '2019-07-26 11:29:03.241826'),
(215, 'hotel', '0012_offers_module', '2019-07-28 05:30:26.740467'),
(216, 'hotel', '0013_offers_creator', '2019-07-28 05:30:27.038162'),
(217, 'hotel', '0014_merge_20190728_0529', '2019-07-28 05:30:27.049686'),
(218, 'hotel', '0015_country_country_code', '2019-07-28 05:30:27.144045'),
(219, 'travel_tour', '0008_auto_20190724_1023', '2019-07-28 05:30:27.197136'),
(220, 'travel_tour', '0009_packageoffers', '2019-07-28 05:30:27.509404'),
(221, 'travel_tour', '0010_auto_20190725_0759', '2019-07-28 05:30:27.733396'),
(222, 'travel_tour', '0011_merge_20190728_0529', '2019-07-28 05:30:27.744702'),
(223, 'hotel', '0014_merge_20190728_0815', '2019-07-28 08:15:50.531515'),
(224, 'travel_tour', '0011_auto_20190725_1619', '2019-07-28 08:15:50.706942'),
(225, 'travel_tour', '0012_merge_20190728_0815', '2019-07-28 08:15:50.717462'),
(229, 'hotel', '0002_auto_20190801_0749', '2019-08-01 07:50:13.419384'),
(235, 'hotel', '0002_auto_20190801_1420', '2019-08-04 07:40:26.486309'),
(236, 'hotel', '0003_merge_20190804_0711', '2019-08-04 07:40:26.498098'),
(237, 'rental', '0002_auto_20190804_0735', '2019-08-04 07:40:27.491154'),
(238, 'travel_tour', '0002_auto_20190801_1346', '2019-08-04 07:40:27.743482'),
(239, 'travel_tour', '0003_tourpackagetheme_image', '2019-08-04 07:40:27.845160'),
(240, 'rental', '0003_remove_vehicledetail_door_count', '2019-08-04 07:49:15.823064'),
(241, 'rental', '0004_remove_vehicledetail_name', '2019-08-04 07:53:00.955816'),
(242, 'rental', '0005_vehicleinventory_vehicle_location', '2019-08-04 08:24:11.978519'),
(243, 'rental', '0006_spotlight', '2019-08-04 10:46:51.232580'),
(244, 'hotel', '0003_merge_20190804_1248', '2019-08-06 06:47:04.591969'),
(245, 'hotel', '0004_merge_20190805_1031', '2019-08-06 06:47:04.609852'),
(246, 'rental', '0002_rentaloffers', '2019-08-06 06:47:04.968691'),
(247, 'rental', '0003_vehicleoffers', '2019-08-06 06:47:05.328001'),
(248, 'rental', '0007_merge_20190805_1031', '2019-08-06 06:47:05.339852'),
(249, 'rental', '0008_vehicledetail_rental_company', '2019-08-06 06:47:05.718053'),
(250, 'hotel', '0003_merge_20190802_0807', '2019-08-08 04:47:45.467481'),
(251, 'hotel', '0005_merge_20190808_0437', '2019-08-08 04:47:45.487638'),
(252, 'travel_tour', '0004_traveloffers', '2019-08-08 04:47:45.850390'),
(254, 'travel_tour', '0005_auto_20190808_1055', '2019-08-08 10:56:04.454021'),
(266, 'restaurant', '0001_initial', '2019-08-18 11:37:54.762534'),
(267, 'account', '0002_remove_user_username', '2019-08-26 10:39:18.285540'),
(268, 'hotel', '0002_auto_20191002_1158', '2019-10-04 05:24:08.815718'),
(269, 'hotel', '0003_auto_20191002_1202', '2019-10-04 05:24:09.085831'),
(270, 'hotel', '0002_hotels_estd_date', '2019-10-04 05:24:09.179260'),
(271, 'hotel', '0004_merge_20191002_1638', '2019-10-04 05:24:09.188367'),
(272, 'account', '0002_passwordreset', '2019-10-04 05:24:09.351781'),
(273, 'account', '0003_bankdetail', '2019-10-04 05:24:09.374082'),
(274, 'account', '0004_bankdetail_invoiceto', '2019-10-04 05:24:09.402663'),
(275, 'account', '0005_bankdetail_hotel', '2019-10-04 05:24:09.561399'),
(278, 'hotel', '0003_auto_20191003_0656', '2019-10-04 05:24:11.555803'),
(279, 'hotel', '0005_merge_20191003_1747', '2019-10-04 05:24:11.566053'),
(281, 'hotel', '0006_auto_20191018_0931', '2019-10-18 09:31:32.775729'),
(282, 'account', '0006_auto_20191022_0516', '2019-10-22 05:16:46.504504'),
(285, 'hotel', '0006_auto_20191018_1343', '2019-10-22 05:20:44.946367'),
(286, 'hotel', '0007_auto_20191018_1348', '2019-10-22 05:20:44.994827'),
(288, 'account', '0006_auto_20191022_1054', '2019-11-06 07:03:56.125991'),
(289, 'booking', '0001_initial', '2019-11-06 07:13:08.624740'),
(290, 'points', '0001_initial', '2019-11-06 07:13:09.243843'),
(291, 'booking', '0002_auto_20191002_1639', '2019-11-06 07:13:13.071076'),
(292, 'booking', '0003_auto_20191106_0512', '2019-11-06 07:13:13.228794'),
(293, 'booking', '0004_auto_20191106_0514', '2019-11-06 07:13:13.387934'),
(294, 'booking', '0005_remove_refereeandreferred_membership', '2019-11-06 07:13:13.549455'),
(295, 'hotel', '0008_hotelinventory_infant_max', '2019-11-13 06:05:58.270436'),
(296, 'rental', '0002_auto_20191110_0814', '2019-11-13 06:05:58.521507'),
(297, 'rental', '0003_auto_20191110_1001', '2019-11-13 06:05:58.778534'),
(298, 'rental', '0004_auto_20191110_1038', '2019-11-13 06:05:58.933510'),
(299, 'rental', '0005_vehicleinventory_vehicle_boot', '2019-11-13 06:05:59.017439'),
(300, 'rental', '0002_vehicleinventory_created_at', '2019-11-13 06:05:59.087888'),
(301, 'rental', '0003_auto_20191112_0648', '2019-11-13 06:05:59.174163'),
(302, 'rental', '0006_merge_20191113_0535', '2019-11-13 06:05:59.181264'),
(303, 'booking', '0006_auto_20191114_1209', '2019-11-14 06:36:43.585817'),
(304, 'rental', '0007_vehicleinventory_seats', '2019-11-14 06:36:43.678243'),
(305, 'rental', '0008_auto_20191113_1130', '2019-11-14 06:36:43.739827'),
(306, 'rental', '0009_vehicledetail_car_group', '2019-11-14 06:36:43.811723'),
(307, 'rental', '0006_vehicledetail_make', '2019-11-14 06:36:43.881985'),
(308, 'rental', '0007_merge_20191112_1636', '2019-11-14 06:36:43.889397'),
(309, 'rental', '0010_merge_20191114_1206', '2019-11-14 06:36:43.896824'),
(310, 'rental', '0010_merge_20191114_0534', '2019-11-22 11:24:25.531468'),
(311, 'rental', '0011_merge_20191114_1239', '2019-11-22 11:24:25.539683'),
(312, 'rental', '0012_auto_20191114_1259', '2019-11-22 11:24:25.952632'),
(313, 'hotel', '0009_auto_20191127_1139', '2019-11-28 07:22:51.592938'),
(314, 'hotel', '0010_auto_20191127_1246', '2019-11-28 07:22:51.642755'),
(315, 'hotel', '0011_auto_20191127_1302', '2019-11-28 07:22:51.687933'),
(316, 'hotel', '0012_auto_20191127_1339', '2019-11-28 07:22:51.743415'),
(317, 'hotel', '0013_auto_20191127_1357', '2019-11-28 07:22:51.769598'),
(318, 'hotel', '0014_auto_20191127_1515', '2019-11-28 07:22:51.798203'),
(319, 'hotel', '0015_auto_20191127_1517', '2019-11-28 07:22:51.829475'),
(320, 'hotel', '0016_auto_20191127_1531', '2019-11-28 07:22:51.920107'),
(321, 'travel_tour', '0002_auto_20191125_1253', '2019-11-28 07:22:51.953348'),
(322, 'account', '0007_user_contact', '2019-11-29 12:42:25.171684'),
(323, 'account', '0008_user_provider', '2019-11-29 12:42:25.266946'),
(324, 'hotel', '0017_hotelinventory_status', '2019-11-29 12:42:25.384817'),
(325, 'hotel', '0018_auto_20191201_1211', '2019-12-08 06:33:47.725781'),
(326, 'hotel', '0018_auto_20191201_1030', '2019-12-08 06:33:47.794553'),
(327, 'hotel', '0019_merge_20191202_0651', '2019-12-08 06:33:47.811550'),
(328, 'hotel', '0020_auto_20191203_0541', '2019-12-08 06:33:47.919892'),
(329, 'rental', '0013_auto_20191203_0541', '2019-12-08 06:33:48.075821'),
(330, 'rental', '0014_auto_20191203_0601', '2019-12-08 06:33:48.229402'),
(331, 'rental', '0015_auto_20191203_0606', '2019-12-08 06:33:48.304921'),
(332, 'rental', '0016_auto_20191203_0613', '2019-12-08 06:33:48.484933'),
(333, 'rental', '0017_vehiclebrand', '2019-12-08 06:33:48.521241'),
(334, 'rental', '0018_vehicledetail_vehicle_brand', '2019-12-08 06:33:48.711618'),
(335, 'rental', '0019_auto_20191204_0656', '2019-12-08 06:33:48.940131'),
(336, 'rental', '0020_vehicleinventory_vehicle_brand', '2019-12-08 06:33:49.139261'),
(337, 'rental', '0021_auto_20191206_0717', '2019-12-08 06:33:49.590045'),
(338, 'rental', '0022_auto_20191206_1043', '2019-12-08 06:33:49.835302'),
(339, 'booking', '0007_remove_modulebooking_booking', '2019-12-19 07:13:25.152062'),
(340, 'booking', '0008_bookingtable_booking', '2019-12-19 07:13:25.357631'),
(341, 'booking', '0009_modulebooking_updated_at', '2019-12-19 07:13:25.433130'),
(342, 'rental', '0023_bankdetail', '2019-12-19 07:13:25.595159'),
(343, 'rental', '0024_auto_20191208_1602', '2019-12-19 07:13:26.052598'),
(344, 'rental', '0025_auto_20191209_0730', '2019-12-19 07:13:26.492282'),
(345, 'travel_tour', '0003_auto_20191211_1113', '2019-12-19 07:13:26.660993'),
(346, 'travel_tour', '0004_tourpackage_country', '2019-12-19 07:13:26.786355'),
(347, 'travel_tour', '0005_auto_20191211_1541', '2019-12-19 07:13:26.900312'),
(348, 'travel_tour', '0006_auto_20191211_1556', '2019-12-19 07:13:27.129069'),
(349, 'travel_tour', '0007_travelitenary_detail', '2019-12-19 07:13:27.193077'),
(350, 'travel_tour', '0008_remove_travelitenary_detail', '2019-12-19 07:13:27.252043'),
(351, 'travel_tour', '0003_auto_20191210_0558', '2019-12-19 07:13:27.538724'),
(352, 'travel_tour', '0009_merge_20191214_1019', '2019-12-19 07:13:27.545804'),
(353, 'account', '0009_faq', '2019-12-22 10:42:35.044641'),
(354, 'account', '0010_faq_device', '2019-12-22 10:42:35.072010'),
(355, 'hotel', '0021_favourites', '2019-12-22 10:42:35.234755'),
(356, 'booking', '0010_auto_20191225_1340', '2019-12-30 07:28:59.285590'),
(357, 'hotel', '0022_auto_20191225_1317', '2019-12-30 07:28:59.421953'),
(358, 'rental', '0026_vehiclebrand_category', '2019-12-30 07:28:59.578690'),
(359, 'rental', '0027_vehicleinventory_vehicle_category', '2019-12-30 07:28:59.866381'),
(360, 'rental', '0028_auto_20191227_0742', '2019-12-30 07:29:00.017470'),
(361, 'restaurant', '0002_restaurantcompany_star_rating', '2019-12-30 07:29:00.100666'),
(362, 'restaurant', '0003_remove_restaurantcompany_star_rating', '2019-12-30 07:29:00.185454'),
(363, 'booking', '0011_auto_20200103_1137', '2020-01-05 10:28:09.170527'),
(364, 'booking', '0012_remove_businesscashbonus_booking', '2020-01-05 10:28:09.489913'),
(365, 'booking', '0013_businesscashbonus_booking', '2020-01-05 10:28:09.654203'),
(366, 'hotel', '0023_inventoryupdate', '2020-01-05 10:28:09.835094'),
(367, 'points', '0002_auto_20200103_1224', '2020-01-05 10:28:10.550325'),
(368, 'points', '0003_auto_20200103_1235', '2020-01-05 10:28:11.563751'),
(369, 'account', '0011_auto_20200113_1343', '2020-01-20 10:57:44.890547'),
(370, 'hotel', '0024_auto_20200108_1143', '2020-01-20 10:57:44.995249'),
(371, 'hotel', '0025_auto_20200116_0535', '2020-01-20 10:57:45.053652'),
(372, 'hotel', '0025_auto_20200112_1348', '2020-01-20 10:57:45.101183'),
(373, 'hotel', '0026_merge_20200117_0655', '2020-01-20 10:57:45.108189'),
(374, 'hotel', '0027_favourites_inventory_id', '2020-01-20 10:57:45.161756'),
(375, 'booking', '0014_remove_modulebooking_customer', '2020-01-23 11:56:04.406617'),
(376, 'booking', '0015_auto_20200120_1707', '2020-01-23 11:56:04.713809'),
(377, 'rental', '0029_auto_20200121_1458', '2020-01-23 11:56:04.873034'),
(378, 'rental', '0030_auto_20200122_1238', '2020-01-23 11:56:04.997336'),
(379, 'rental', '0031_auto_20200122_1352', '2020-01-23 11:56:05.136537'),
(380, 'booking', '0016_auto_20200126_1249', '2020-01-28 09:05:21.332711'),
(381, 'booking', '0017_bookingtable_seenstatus', '2020-01-28 09:05:21.413012');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('085seiw1p76p2hi45qbobbg0m72rodbj', 'OGI5MDhkYTUwZWE1NzU2MzVlNGYzZDIwNTVlYzY1ZGM1NjdkYmVjNzp7Il9hdXRoX3VzZXJfaWQiOiIxMTEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVhYjFjY2RmN2E1ODJiNzZhYTgwMGQ2Mjc1MjlmZWMxZjIxMDJjZDMiLCJfc2Vzc2lvbl9zZWN1cml0eSI6IjIwMTktMTItMzBUMTQ6MzM6NDUuODE1MjcyIn0=', '2020-01-13 14:33:45.818302'),
('0aog7pgs2gzm3wqxgbfkyc2v2et3hnxg', 'ZGQ0ZTkxNGZjOWI2YjgyYjM0MWMzMDAyZTNmODQwOTllYzY5Y2YzNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA5LTA4VDA1OjI2OjA1Ljg0NjcyMiJ9', '2019-09-22 05:26:05.952121'),
('0l2jtdifzs5ugbwjvyleopd48rtcffol', 'YWUzMmEzZDM4M2QwOGJmYTVlMjQ3OTc1MGM3ZjJkZGI5NzcwMzkwZjp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMi0wOFQwNzo1Nzo1NS40MTkxNjYifQ==', '2019-12-22 07:57:55.458760'),
('1suv6sv0givxmdltk3hlzx2cz5lbdv7s', 'MzE3Y2E4MDlhYzk1OTUzM2QzMjQ2ZTNhOTA4ZjBkNDdmZjVmYzA5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA1LTAzVDExOjE3OjMxLjg3MzUwMSJ9', '2019-05-17 11:17:31.874855'),
('1vkcapoktgt7rljmb96ljq2qcbcep90l', 'MTU1NDAxNDE4NWQyMjNjYmZkNzg4NWVmM2UyOTY0MjJhZTY3MmVmYzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2In0=', '2019-11-26 06:41:09.332063'),
('2rwr5fe5j3rk0z9b18as6ftljgbbkqbs', 'NzQ1NmI0YTI3NDc3ZWJlNzU5MmJmZDRlNDViZjM2OWViZjVlZGY0NDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMC0yNVQwNzo0ODowNi45NTkzNjYifQ==', '2019-11-08 07:48:07.010784'),
('2wcbciv1r2mom8b0glj20k5kbqm4vn7d', 'NjlmZDM4ZjU0ZWI4MDU5ZjU2MDViOGVlODI2Yjg4MzY0OTVhMDlkOTp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMC0yOFQwMzoyMzowMi43NDY1NTkifQ==', '2019-11-11 03:23:02.748149'),
('2wi3kivzujsn8vq9pjews019d5e9nz4w', 'MjMwODVhOTI2NmNhMDhmODIyYzVmNzI4YjM0ODgzMDliM2Q1NTYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0In0=', '2019-08-22 10:33:40.371049'),
('3lw6gadvf6g62h0vveviubkg1k81w9ln', 'MTQwZGE1YWE2YjEwMTExNmJiMjdhNDVmMDEzNTNjNTAwMWJjYTE4Yjp7Il9hdXRoX3VzZXJfaWQiOiI4MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2JmMWYyNjU3YWJhYzg4ZTZmMDFlODYzZTk5OTUxNmM0Mzk3ZGY3ZSIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAyMC0wMi0yNVQwNjoxMzowMy41ODc1OTEifQ==', '2020-03-10 06:13:03.634420'),
('4qayp7ekzwqey1doodbv62d927meure4', 'YTg2MzRmYmJkZGRhMzZhZjRlNjkyYjJlODQ2ZWIxZjA4MzIwYzQ3YTp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDExOjM1OjQ3LjYyOTI4OCJ9', '2019-05-09 11:35:47.673994'),
('5illc7qy9wthva2c9r3s58s95iqgv3rn', 'Y2EyM2IyNzJkNzY0Mjk3NzVmNWQ1NTY1YTYzNzBkNGVmMGMzZTk0NDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMC0xOFQwNDoyMjoxOS4xMTI0OTcifQ==', '2019-11-01 04:22:19.118456'),
('5mnqj36eb2fbw0s3qhakjpbzl02xy7nz', 'Yjk3NjE1NTU2ZjI4MzQ5YmFiNThkYzBmMjkwY2MxNGVkZmYwOGQ2Mzp7Il9hdXRoX3VzZXJfaWQiOiI4MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2JmMWYyNjU3YWJhYzg4ZTZmMDFlODYzZTk5OTUxNmM0Mzk3ZGY3ZSIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMS0xM1QwNzo0OToxMi4wMTQ2OTYifQ==', '2019-11-27 07:49:12.084377'),
('6f47icjp0h4fzd3z4jhopivih6hwk5k2', 'MTc0NjEyNWQ5OTE4MTZkMDI2NmZkZjhiZDYwYWFiMzhjYjZjNjEzNzp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0wOS0yNVQwNTozMToxNi4yMDgxMzkifQ==', '2019-10-09 05:31:16.255227'),
('6mg2ypmd4r5m23r4mbtyr8rpirigj7x2', 'NTU4ODlhNTQzYTA4ZjU1ZDNjZDdiMDEzYzM2OTY0YjBjZDk3NWQzNjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAxLTMxVDA1OjUzOjU3LjA2MTM4OSIsImhvdGVsX2lkIjoiNSJ9', '2020-02-14 05:53:57.064439'),
('6mzmvx7aunokkry0415f7t3xuctqnsyz', 'MjMwODVhOTI2NmNhMDhmODIyYzVmNzI4YjM0ODgzMDliM2Q1NTYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0In0=', '2019-10-04 07:28:13.870946'),
('6orr5bkd92ygovriesxts0knv97nzhxb', 'NGRhN2FiYTdjMDY2ZTRkZGI4Y2FkYzFjNWFhZTI3NzNjYWI5ZmVkZDp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNzZkNDIwMjkxMjVjMzk2OTIzOTcwNmJiZTQ4ZjIxYWJmZjJlZTA5IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAxLTIzVDEyOjAzOjQyLjI5OTA3NyJ9', '2020-02-06 12:23:42.299798'),
('72pgkupr1kyetgpe5rjndh9d0dnzfd1w', 'NzMzNzIxNmU5MWY0Zjg4YTUyZDk4ZDgwNTNkMDBhZTc5Y2E2ZWVmYjp7Il9hdXRoX3VzZXJfaWQiOiI4MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2JmMWYyNjU3YWJhYzg4ZTZmMDFlODYzZTk5OTUxNmM0Mzk3ZGY3ZSJ9', '2019-11-27 07:47:28.537490'),
('74909qwp8iz0c7w8mgyz2rqiackme4uf', 'YTFlZGVjY2ZmZmM3MzUyNzQ4M2RmMWNmMTE5M2M1ZmQ0M2U5YTg1Njp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMS0wM1QwNTozMjo0NS41MTM1MzIifQ==', '2019-11-17 05:32:45.515357'),
('77lt49tuibtrvqi1gkyczf639swdx5tt', 'ZDAxYzYyYzJkNDgxMzE5NThjZWE4NDFlMDA3Yzc1YWMwYjhkNGNmNDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI0VDEyOjA3OjQ3Ljg1ODQ0NCJ9', '2019-05-08 12:07:47.864998'),
('7ifm7l6vozvd128u6u7muhzt92gvgz32', 'ZjM2NTA2OWExNDE5MGMzYTMyMzgwZjA1MGVhZWEwMmMxNTdiMTNjNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA4LTMwVDA2OjE1OjU4LjQ3MTc3MiJ9', '2019-09-13 06:15:58.504494'),
('7iocvm05vwx0vq4p6vs9kq4vw6w6niv4', 'YTNjMzAwNDk3MmRkNzBlNjU2YjhjZTZmNjdiNmUxODU3OTcyODk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMi0xNVQwNjoyOTo1NS43MTc0MjQifQ==', '2019-12-29 06:44:09.718314'),
('7ogayon197tap3n447w6xegzzi3jzw8s', 'N2Q4MmIwN2I3NDZlZDc2ZWE3ZjE2YThhY2M1ZWYyNDY5NjUwMDU1NTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAyLTAyVDA4OjAxOjAxLjg4ODQ4NyIsImhvdGVsX2lkIjoiNCJ9', '2020-02-16 08:01:01.891788'),
('7ykvlpoj5a9cqdxygqfktpl1f0tnb2me', 'Yjc0OTRiNjkzZGIyNGJjNDRkM2I2OTFlNDJhMGJlOWY2ZDk1MDlkMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTExLTA3VDExOjEyOjMyLjE2NDY5OSJ9', '2019-11-21 11:12:32.364846'),
('7zxnop0nsxooupikmvcv3aqx0qximdfs', 'ZTEyNmM4OTU0MDE3Y2ViZTM5NzRjMWFjZjU4NDVlNjFhOTk2NzlhMDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMi0wNFQxMDo1NDo1Mi4yNjM4NzkifQ==', '2019-12-18 10:54:52.348149'),
('9jnhb2ygegmjsem65nkvk4oqs10lxhoj', 'M2JiNzE0N2NkYzBlZmY1MDZjZjgyZmE3MDU5OTNkODFhNDRjNGE5Zjp7Il9hdXRoX3VzZXJfaWQiOiIxMTEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVhYjFjY2RmN2E1ODJiNzZhYTgwMGQ2Mjc1MjlmZWMxZjIxMDJjZDMifQ==', '2020-03-13 06:33:50.023932'),
('9v50xvttnbeplcqausq2mwoynj54tunu', 'MzRmM2JhYmRkYmNjY2M5NzE5N2UxYzUwMjllNWUyMTc5ZDQxZjI3Nzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAxLTI2VDA2OjAxOjI5LjIwMzgzOCIsImhvdGVsX2lkIjoiNCJ9', '2020-02-09 06:01:29.206898'),
('9wzjk5ommlojn00y9i6ljxoccvxcli5w', 'YWEzZWI5NmIxZWEwNTUxNWQ3NTA0MDUwMDJhYzgzYWIxYjFhYTFjYTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAxLTA5VDExOjAxOjQwLjE3MTMzMCJ9', '2020-01-23 11:01:40.205811'),
('a8c3q5v1ps8yu1xv2e2ukj97xe5js2kc', 'MzNlOTA5MzAwNjBhNTk3Yjc0ZTc5ZGE0M2NmMTUyZWRkOTFiMzk5OTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA1LTA1VDE2OjU2OjUzLjYyMzI2MyJ9', '2019-05-19 16:56:53.675803'),
('af3ffl3gy7hg8rzl0c4deotl0a6mn35h', 'Njc3Nzk0YmJkNGQ3MDViYWJiYjQ5N2VmOTkwZGUxNmI3MjE0OGI0Zjp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNzZkNDIwMjkxMjVjMzk2OTIzOTcwNmJiZTQ4ZjIxYWJmZjJlZTA5IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTEyLTI3VDA1OjM0OjI3LjcxMDQyMyJ9', '2020-01-10 05:34:27.712491'),
('akmw6wfmwg1map79iqrbpjdqacvol52c', 'NjQ3NDc4YzRiNjJkZmI3MjExMjJhMzcxYzEzNzZmZmFhYmM5NjE3YTp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA1LTEzVDEyOjQwOjU3LjA5MzM0OSJ9', '2019-05-27 12:41:04.792087'),
('b6jt97lpq8g46ex749gg9qm02g1macwp', 'YTc2MGUwYTk3NDY0ZjJjYTZkNGU0YmVkMmEzN2NjZDAzZjU2YzE0ODp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDEwOjU4OjQwLjk1MzY5MCJ9', '2019-05-09 10:58:40.959554'),
('blj71a3bvx6opuoxn1jukt89452cvogh', 'M2ZiNjcxNDMzNGIxZGQ1YWVhOTg2NDYyNDVmZjkxNjkxMmIwY2YwYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA5LTE2VDA1OjMwOjA5Ljg0OTU1OSJ9', '2019-09-30 05:30:09.982286'),
('bxq2ru6icypfamb6pt6u7qofjl2a8pzm', 'NDU3NTFmMDE5NTI5M2U2MTliYTViZTU3MDc1NTY1ZTVmYjc1YzM1MDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDEwOjI2OjIwLjg5MDcwNSJ9', '2019-05-09 10:26:20.901354'),
('cfuwefdvuhgh9gnsg70m1wux33rojauc', 'NjJmNzRlOGIwYWM2ZDdiZTJmZGYzZWZhMzdmODQ0ODM5ZjllNzgxMjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA4LTE4VDExOjE3OjQ3Ljg1NDIwMyJ9', '2019-09-01 11:17:47.873316'),
('ddcrj2atrxpty32ktmc64ileqi8ye87o', 'M2M4NTBkOThkYzk3YmFmOWQ4ZTQ3ODk1YWE3Njc3NjU4NTM3NzVmNTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTExLTE0VDE0OjA3OjE0LjQzNjg3NiJ9', '2019-11-28 14:07:14.438236'),
('epx0qqmv4g766y2phrzvff3fwjehtk72', 'YmYyYmQ5YmFjZjk2YjU1YzE4OTRmN2Y4MDE0OTZjNTRmOWY2MGQ4ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA5LTE4VDEyOjQ0OjE5LjcyOTQ0OSJ9', '2019-10-02 12:44:19.764430'),
('euakdltcyunt60wk2fq5mplu8ypb4ond', 'N2EyZDI2NjJmMzdiYzJmNjJhYjU3MTM1ZWNmNmIxZDQ1YTVjYTUxNzp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNzZkNDIwMjkxMjVjMzk2OTIzOTcwNmJiZTQ4ZjIxYWJmZjJlZTA5IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTEyLTI5VDEzOjIwOjI0LjIwMTM5OCJ9', '2020-01-12 13:20:24.203579'),
('ex530b8p8ewi98aol1rf3msbu3pr6nsm', 'MjQwNmI4MWMxY2Y5ZGU2M2RmNTg0MWEwY2Q5YjQyOTZkYWZhMzI3Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTIyVDExOjU0OjMzLjA2Mzg3OCJ9', '2019-05-06 11:54:33.069450'),
('f1v2crw7v6jt1hilju9rmeufvefms5ou', 'MmJlM2M0NzRlYTUyM2E5MjA0YjQ1NjgyMzczYmFiMjhkM2JhY2MzNDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDExOjA5OjU4LjE1MTU1OSJ9', '2019-05-09 11:09:58.161025'),
('fmlzrkv3gheycb5zsna56m0kv3jn4v54', 'OGQ4MzY1NWU4ODYzODk3MWIwYjZmYjk4NmRkYWRkNjRlZWJhODUzNzp7Il9hdXRoX3VzZXJfaWQiOiI2OCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDM3MjY4ODY1NjZkOGE2NGQyYjkxNjAzZGM5YWViOGQyMDE3MGExMCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0wOC0yOVQwNjoxMjoyMy41MDc2MzkifQ==', '2019-09-12 06:12:23.530111'),
('gzoyt4dnmozq1rshlh3upn92ugr8r3jm', 'MDBkYTFkOWE3M2MyNDhmOGFiNjMzNWQ1ZjI1MTQ3YTcxYzg0Mzk0Yjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI4VDEyOjA5OjExLjc2ODYzNSJ9', '2019-05-12 12:09:11.820523'),
('h2931x0vv8qw0x0i1eyf508a66rt5kho', 'ZDk4MWVmNjYxOTIzNTFhOTA0OTcyMDQzMGQwNGQ2NDA0NDRjNmMyYjp7Il9hdXRoX3VzZXJfaWQiOiI4MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2JmMWYyNjU3YWJhYzg4ZTZmMDFlODYzZTk5OTUxNmM0Mzk3ZGY3ZSIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMC0wM1QwNTowNToxNC4xOTU0NDYifQ==', '2019-10-17 05:05:14.239571'),
('hmk5zhxhl59qbdvi4ouvb6n0upgrrkkk', 'NjE5MDM4NTI4MWE5NDZhYThiNWZjODk1Mjk4OTQ2NGMzMWJlOTgxMjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA5LTIwVDA3OjMyOjQ1Ljk2OTc5MyJ9', '2019-10-04 07:32:45.974873'),
('ig2zvfkdizxgukexwxrho3u11ajtxs18', 'M2VkZmYwMDhkM2MyOTI5ZTM0NjAxOWRjZWMyNWQyYmMwYmRiZmZhMzp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMC0yMlQxMDoxMjozOS44MjY4NjEifQ==', '2019-11-05 10:12:39.837672'),
('ilg44fmck9k3vrgdfrg7402ugpyqeiz5', 'ODdhMzE0MTY0ZDY1OWY4ZjZlZDc3ZjdkMGZjMjBlZThjODc4NWRhNjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAxLTI0VDA2OjExOjQyLjYzNDUyOSIsImhvdGVsX2lkIjoiNCJ9', '2020-02-07 06:11:42.637508'),
('inltu4tloi5t4ro9wxdy3eai1c9ghmv9', 'MWI0ZGRjNDE3MTRjNWI0MDk3M2ViOGI0ZWIxNWYzMzliNTA2MWE4Mzp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA1LTEwVDA1OjQ5OjI5LjQwNjUwMSJ9', '2019-05-24 05:49:29.415380'),
('j9g04vuf0fuvxvdaorhuy0idaou14iuh', 'MzZkY2M0ZTliODMxMTgyY2ViZTRlYTVlZGQ0ZTQ1ZGQ2ZTE1M2ZjMzp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDEwOjU5OjIwLjM0MjEzNCJ9', '2019-05-09 10:59:20.350274'),
('klcqxe5y9zxpl5h1ha4wpfivbu9ncoxj', 'NjBmNjkxZDhkOTJmNWZlOGIxZGUzNjA1ZWY0MTM4NzMzN2JhYTM4MDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIn0=', '2019-05-09 10:28:08.621675'),
('ko2vcoj7tqye5xoa4cby55zulo5ez3gv', 'NTQxNGFlOWJjZmE1ZjVhMzJlYjIxMzE4YmQ1YjEzZTJlZGMyNmE0Yzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTEwLTIwVDEyOjE1OjI5LjEzNjQ5MiJ9', '2019-11-03 12:15:29.144682'),
('lb809eqkwgdp2yo33z5fiv53lr36q9l7', 'YTk0NzdhYzcxY2M0MDIzNWJmMDBiZWMzNTMxYmU4MjllOTA2NDY3Zjp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMC0yMlQwNToxMDo0OS40MTc5NzgifQ==', '2019-11-05 05:10:49.461677'),
('lqpl1fmekx4tykhci9q2kmenj4c3ik4k', 'NTk2NjZiYzZkOWIzZTcyYzFmMDMzMTMwN2U5ZWM0MzliY2ZhZDFmNTp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDExOjQyOjQyLjg3MjUwNCJ9', '2019-05-09 11:42:42.873880'),
('lsw85l0ebvvz8ox11ltyl65dwxkhfff9', 'NzEwMjg4MDEzMTg0MmYyZTg3NTk2ZDkxZjdlYWY0Y2YwNTI3MTQ5Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI2VDA3OjUwOjE1LjUxMjc2NyJ9', '2019-05-10 07:50:15.566496'),
('mw95194pgpbgm07f6c050wx4ndmvdvst', 'NzIwOTYzMmFhMzJmNWRkMzQ4NWY2MDk4NzM4ZjE5YzcwMWU4N2ZmZTp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNzZkNDIwMjkxMjVjMzk2OTIzOTcwNmJiZTQ4ZjIxYWJmZjJlZTA5IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAxLTI0VDA1OjQzOjMyLjIyMzU5OSJ9', '2020-02-07 05:43:32.254317'),
('n5jf6la1xmpk0zih9bo105d576dwhbl2', 'Yjg1NjFjYjdiYjY5OGE2YTk3ZDIyYjg1NTIyZDQ1ZTIxNGU1MzRkODp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDExOjI3OjAxLjA3NzY5MSJ9', '2019-05-09 11:27:01.083356'),
('nv3w3gcgoodilkaiwtams2v62j7daxma', 'MjMwODVhOTI2NmNhMDhmODIyYzVmNzI4YjM0ODgzMDliM2Q1NTYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0In0=', '2019-10-04 07:27:45.873780'),
('o25ljqfs0ygcaxw4q9sp4p8b3izw5b5r', 'MzJlYjVjNTEwYTdkMDRiZjJhOThiMTA4OWFlZGE5YjNmMjFkYzc3Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA5LTE5VDA0OjU3OjMwLjI0MTYzNSJ9', '2019-10-03 04:57:30.277132'),
('oknjdcak4vswnl3u3siaiahg0yucs2up', 'NjRhZWZhNGVkMmJiOWQ3ODBhMDRkMWNmZjZiYjFhN2IzZTU3N2NkZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI4VDEwOjI0OjA3LjU3MTQ4NyJ9', '2019-05-12 10:24:07.602527'),
('orn662g1smsyju9uxuey5hwfcqkluqv1', 'ZDc4MDg3OGI3Yjc5MzM0ZmEwZGIzODVlNDE1MjMzZjc3MmM5YmIxMTp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTExLTI1VDExOjEwOjM3LjA0NTI3NiJ9', '2019-12-09 11:10:37.114908'),
('p651956ism8kznpkxwkmg2l6uvagm4wk', 'MGZhMDgzYTZjNzRhZDIwZDAwNzhmN2U3N2JmNjI3YjhiYTUwNjdlMDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMi0wMlQxMToyNjowOC4wNDYxMzAifQ==', '2019-12-16 11:26:08.047296'),
('puw5txwriz7yn8yg5uurmkmveurbscqy', 'MjMwODVhOTI2NmNhMDhmODIyYzVmNzI4YjM0ODgzMDliM2Q1NTYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0In0=', '2019-10-03 05:42:34.662472'),
('q6g9dma9begkw3cbb51lnyscsdfehqjw', 'YjY0N2RhYjUyNWU2MThjNzEzMjI5OGU5ZGI3NmViZGYyZmY0YWUwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA5LTIwVDA3OjU4OjQwLjg5MDUwNyJ9', '2019-10-04 07:58:41.116991'),
('qahxjtogc118d0mrdkm8nvjdv1t0cf94', 'NjVkMzdmMzA5OWFlYWRiM2IzMjcxMmViYTE1MmRmNjMxODI4NjE5ZTp7Il9hdXRoX3VzZXJfaWQiOiI4MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2JmMWYyNjU3YWJhYzg4ZTZmMDFlODYzZTk5OTUxNmM0Mzk3ZGY3ZSIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMS0xM1QwNzo1NjoyNy45MzMxMTQifQ==', '2019-11-27 07:56:27.934005'),
('qxc83xgbvq7ov9mkh41t5spcmatnc1ds', 'MGU0MjhkY2JhZmI5NWFiMWU3NGIxMThjNWJiOTgwMmE4NzdlNmRiZjp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDExOjQzOjIwLjMzMTI5NCJ9', '2019-05-09 11:43:20.425296'),
('qys4f2nzv9hy3c7plvh0l0ykimar16os', 'OGUwY2VhOTNkNTg3YmZkYzVjYzU5YjYyNDE3ZDBiOGEzYTczYTIyMTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAxLTI4VDA5OjAyOjI4LjA5MzM2NiIsImhvdGVsX2lkIjoiNCJ9', '2020-02-11 09:02:28.098312'),
('sah0nng40cwgbkld1ow8d7t5qml9uk1h', 'NzFlMDQ2ZGRmN2I4YWQ1Y2Q2ZGJkYmFmNjIzMjI0NmNiZDY0ZjI0Zjp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTExLTI2VDA2OjQyOjE2Ljg0ODgyMCJ9', '2019-12-10 06:42:16.891030'),
('sb8zgrtrph2zt0f9iqxhuedbjktpxyl9', 'OTQ4NjVkYjRiNGIyNmVlZWIwZjNlZDFlY2JlMmU4Nzg2NDU1NTU2MDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMS0yNVQwOTo1MDo1OC40MDIwMzQifQ==', '2019-12-09 09:50:58.442177'),
('snoaqrf8uig76gceqvr0h0a9be2750i1', 'ZGZiYjgxZDg2YzM1NWJhZGZkYzgwYTg3YmZkYzllYTg1MmUwNzNhYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA5LTEyVDEyOjQ0OjQ2LjkzODU4OCJ9', '2019-09-26 12:44:47.093190'),
('sr8fmk4baw9jabvlg6j0s1do70909d4h', 'NGQ1Mzc1Y2UyMjNmYTIwMDE1MzkwMDdhYTgwM2M3YzMzMDM5MGYyNDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI4VDExOjI2OjQxLjkzMjE1MiJ9', '2019-05-12 11:26:41.967086'),
('st8t14emi1x6a0y5gpz0m1d4b6s1am2w', 'MjMwODVhOTI2NmNhMDhmODIyYzVmNzI4YjM0ODgzMDliM2Q1NTYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0In0=', '2019-10-03 04:40:31.223250'),
('tf6g6cfbrugeyu796lo0si828l1ulrdl', 'NzcyZWE2ZDFkOTM0NTFkZWI3M2VlMDNhMDU3Y2VhZmNlNmZlMGE3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA4LTI5VDA3OjUwOjQ0LjMxOTgzNCJ9', '2019-09-12 07:50:44.423118'),
('th3wid8esbit0m0ccaoaqc6xirwsor23', 'MDM2NjY4OWEzYzEzYTY1Mzk1NGNiNzgxMGM1ODI0ZjA0ODUyY2MyYjp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMi0xM1QwOTozOTowMy4xNTI1NzgifQ==', '2019-12-27 09:59:03.885475'),
('twoa0j4fvazdb2gszn5i0es69r4ux7n1', 'OTMwOGRmNDJlOTg5NWY1NmNhYzY1ZWQ0YjAzZmY5YTI4MzJlNGE2NTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAxLTI5VDA1OjU0OjIxLjQ0OTM5NSJ9', '2020-02-12 05:55:42.450179'),
('ub81lmymgqdsciye8wxpms3su4fndoer', 'ZGM4NDFmNDQ5NDU5MzJjZDJhNGFiZTIwMDAwMzQwNjg1N2FhMDQ3Yzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA5LTI0VDEwOjUyOjIyLjk5NTI5OCJ9', '2019-10-08 10:52:22.999630'),
('ufki4603xpbsz1wqrp1414bqr5oirzo6', 'ZTM3ZDRlNmY5NzA4NWQ4NWJiZjBlYjk3ZTczMmJkZDk1MmNiZTBmNDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMC0xOFQwNzozMzoxNS4wNDIyMzYifQ==', '2019-11-01 07:33:15.073519'),
('vaec6eybevht5vlw9g93xktrm5un4cd9', 'YTU2YTljNDE1NjMxNjIyY2IxNGM1NjI5ZWI0NWJiYTZiYmM4NzliZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTEwLTAyVDA2OjQxOjEzLjU1NTMxMyJ9', '2019-10-16 06:41:13.670478'),
('vsh6snzjza63aeasijixblnbotulsviu', 'ZDYxYjc1MmE4MTIxYzc4MjNlYTVkNjliOGQ4YWE3MDcxMDkxZjQ3MTp7Il9hdXRoX3VzZXJfaWQiOiIxMTEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVhYjFjY2RmN2E1ODJiNzZhYTgwMGQ2Mjc1MjlmZWMxZjIxMDJjZDMiLCJfc2Vzc2lvbl9zZWN1cml0eSI6IjIwMjAtMDEtMTZUMTA6MjA6MjAuMDUxOTExIn0=', '2020-01-30 10:20:20.093049'),
('vyxvvh958x9bh62ktwi2h3tnnxzm3uwo', 'YmRjZTNiOWJlYzgyNGYxMDdiMDdlMWRhNjI1OWQzY2E0NGE5ODJjMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTEyLTI5VDA5OjUwOjM1LjAzODUwNyJ9', '2020-01-12 09:50:35.318261'),
('w4mhps0yd83y8eenx49294r23lp2aor9', 'YmFhMDhlMjQ2YjZiOTFhMDM0ODc5YjgzNDZkOWJlYWM5ZDAyYzkwNTp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDEwOjUyOjI0LjU0Nzc3NiJ9', '2019-05-09 10:52:24.551733'),
('w7y3uyws83105ta9fwovurpp3rlyytth', 'NmNiNzYyZGRlOTk1NDdiMjg1Yjc1YjA1ZjQxZjE2MjNmNzY4ZjY2Mzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAxLTI3VDA2OjQ1OjU3LjgxODUxMiJ9', '2020-02-10 06:45:57.819259'),
('wclh7r3rtdwwwxfdavv63ghz3gk4uaeo', 'ODEwYmQyYzU3ODQ4MDVkNmU4Y2FmMmQ5Njk0OTNlMjVmNTIyMjJlYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTExLTIyVDExOjMzOjUzLjAyNDU2OCJ9', '2019-12-06 11:33:53.059113'),
('wr7v74c7ci5kfe3j8560hlxdcu8g9dpb', 'MjcyN2FkZGMwYTdhNWRjN2I5YjdhZmUzNGNjMzlmMjYzZDAzZDk3MTp7Il9hdXRoX3VzZXJfaWQiOiIxMTEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVhYjFjY2RmN2E1ODJiNzZhYTgwMGQ2Mjc1MjlmZWMxZjIxMDJjZDMiLCJfc2Vzc2lvbl9zZWN1cml0eSI6IjIwMjAtMDEtMjdUMDk6MjY6MjcuMTc5NTIxIn0=', '2020-02-10 09:26:27.210504'),
('x39aqqmutofcte8wrjz79lojlevb5n3j', 'OGFhNDUxNzQ0YjYzZDU3ZGI4OTNiNzFlYWRmNjU5ZDU1ZWQ3NzA1Yjp7Il9hdXRoX3VzZXJfaWQiOiI4MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2JmMWYyNjU3YWJhYzg4ZTZmMDFlODYzZTk5OTUxNmM0Mzk3ZGY3ZSIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAyMC0wMS0xM1QwNTo1NDoyMC44MTU1NTYifQ==', '2020-01-27 05:54:20.834712'),
('xe69asv4arytvy97vgeyqu02me1b2faq', 'Njc4ZjEyMGE2MWYwMWU5ODc3MmJjMDg3YTJlZDI0Yjc4MWRiNGRjMjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDIwLTAyLTI4VDA2OjM0OjE5LjAxMzAyNiJ9', '2020-03-13 06:34:19.020129'),
('xg93m8w9inqnoyyt172cyozr0mx5fd98', 'YWQ5NzNkYWRkY2YzYWE5ZThlY2M1YjA3OTNlODFhNTY4Mjg2YzY5Mjp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMC0yMFQxNDoyMTo1My4wMzYzMTIifQ==', '2019-11-03 14:21:53.070512'),
('xuy67hje6n8jc32fvl52svio010193gb', 'YzJmOWM3MDY4YzU5Y2Q4MGMxOGY2NDZjYjVmZmViZGQ0MzgwMzMyYTp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjhhZTc5MjE4YmJkZTlhODFhYTdkMzlhNzRkMTU1M2ExMmU3YzIyZCIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMi0xMlQwNjo0NjozNy45Mzg1MjIifQ==', '2019-12-26 06:46:37.947335'),
('y052tso51nojmid0nbyin3arxdv687i4', 'Mjk3NzZhZTBiNTFhNmE1YjM0Yzk2ZWIzMmNmNTMyNWE2Y2M5M2U5Mzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDU3YzAwNDdmYmFkOGNkODUzODUyODRkNzhjNjI1NzM1NmFiYjA2IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTExLTA3VDExOjA4OjUyLjY3NTAzNCJ9', '2019-11-21 11:08:52.709406'),
('y2yobjgxcysdhjati3ccvmaky9zlkzxw', 'YTg3ODg0MzA4ZjE0MGNmYTRmMzFmNmQ0M2VhNjAyZTVmOWU4MThhMTp7Il9hdXRoX3VzZXJfaWQiOiIxMTEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVhYjFjY2RmN2E1ODJiNzZhYTgwMGQ2Mjc1MjlmZWMxZjIxMDJjZDMiLCJfc2Vzc2lvbl9zZWN1cml0eSI6IjIwMTktMTItMzBUMDg6MjA6NTcuMzk3NjczIn0=', '2020-01-13 08:20:57.398588'),
('yugwbif621n0wqj2ufddemrazpvtp5zt', 'N2M2MDcwYjU3MTYxODQzOTA2YWU4ZWM5MDNkYmZmNWExYjYyODA1Yjp7Il9hdXRoX3VzZXJfaWQiOiI4MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2JmMWYyNjU3YWJhYzg4ZTZmMDFlODYzZTk5OTUxNmM0Mzk3ZGY3ZSIsIl9zZXNzaW9uX3NlY3VyaXR5IjoiMjAxOS0xMC0wMlQwNzo0OToxMy4zNTkyNzAifQ==', '2019-10-16 07:49:13.417301'),
('z0ppumfvkzeivywms1g0n0qzk4ex1yws', 'MjQwOWY1MDllYTU4ZmViYmU3NGY3ODk3MmE3ZGU0ZWJjOGQxNTEzNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTE5VDExOjA0OjMzLjQ0MzYxNiJ9', '2019-05-03 11:04:33.486585'),
('z78ki5n0ah85tfs9t2f59h8ur1y4rb8o', 'OTBjODgwOWY1ZjMwNGZlMzdhMTZkN2NkODFiN2JhMjBkYmUzM2RmMjp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGM4OWFlMmFlNGZiYjdkYWQ2MmNmZDUzYzFhMTFhM2UyNzgwMjBlIiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTA0LTI1VDExOjM0OjQ1LjYyOTMwOSJ9', '2019-05-09 11:34:45.633197'),
('zdthdh3a03nc8ztqu3ywpaedd7x9lob8', 'ZTZhNzAyMGExZTYwNDQzNGViMzZkZTIyNTVjYTI4NjBhMWJiMzJhNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGVkOWQ5ODQ4ZmFjZTA3M2Y4YmQ3YWM2N2RhZTViYjlkNTE0MGU0IiwiX3Nlc3Npb25fc2VjdXJpdHkiOiIyMDE5LTExLTEzVDA3OjU5OjA4Ljc0OTI2MCJ9', '2019-11-27 07:59:08.954654'),
('zerl4ehx9y0h4umeag06g3t2bqx1g00n', 'NDcwMjlkMzcxOTBhMTZlZDdhMmE3NzU4NDU5MWFkMjMyYjE4YzkyZDp7Il9hdXRoX3VzZXJfaWQiOiIxMTEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVhYjFjY2RmN2E1ODJiNzZhYTgwMGQ2Mjc1MjlmZWMxZjIxMDJjZDMiLCJfc2Vzc2lvbl9zZWN1cml0eSI6IjIwMjAtMDEtMTdUMDk6NDQ6MjcuOTM3MzEyIiwiaG90ZWxfaWQiOiIzNyJ9', '2020-01-31 09:44:27.991640');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_bedtype`
--

CREATE TABLE `hotel_bedtype` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_bedtype`
--

INSERT INTO `hotel_bedtype` (`id`, `name`, `description`) VALUES
(1, 'Twin bed(s) 90-130 cm wide', 'Twin Bed'),
(2, 'Full Bed', '131-150 cm wide'),
(3, 'Twin Bed – 39”x 75', 'The twin is generally made to accommodate one child or one adult sleeper. Twin is a great size for smaller guest spaces, bunk beds, and daybeds.'),
(4, 'Twin-XL 39”x 80” •', 'The XL stands for extra long, and at 5 inches longer than the standard twin, this size is great for taller youth or adults. This is also is the same length as a queen or king. Thus, two of them side by side equals a king.');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_cancellation_policy`
--

CREATE TABLE `hotel_cancellation_policy` (
  `id` int(11) NOT NULL,
  `hour` int(11) DEFAULT NULL,
  `price` decimal(5,2) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `hotel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_cancellation_policy`
--

INSERT INTO `hotel_cancellation_policy` (`id`, `hour`, `price`, `created_at`, `hotel_id`) VALUES
(1, 1, '100.00', '2019-05-19 06:00:28.663191', 18),
(2, 1, '2.00', '2019-05-19 08:41:37.719837', 19),
(3, 1, '20.00', '2019-05-19 12:45:40.798646', 20),
(4, 1, '10.00', '2019-05-19 12:48:05.531594', 21),
(5, 1, '20.00', '2019-05-19 13:26:48.332726', 22),
(6, 2, '12.00', '2019-05-21 05:14:17.789645', 7),
(7, 2, '1.00', '2019-10-17 07:08:54.823934', 4),
(8, 2, '1.00', '2019-10-17 07:12:19.936455', 4),
(9, 1, '1.00', '2019-10-17 07:13:24.391894', 4),
(10, 24, '50.00', '2019-10-18 04:19:44.451354', 30),
(11, 24, '40.00', '2019-12-30 08:08:42.293418', 37),
(12, 3, '20.00', '2019-12-30 08:26:30.946303', 38),
(13, 24, '20.00', '2020-01-19 10:24:47.748755', 39);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_city`
--

CREATE TABLE `hotel_city` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `state_id` int(11) NOT NULL,
  `country_id` int(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_city`
--

INSERT INTO `hotel_city` (`id`, `name`, `state_id`, `country_id`, `image`) VALUES
(1, 'Dharan', 5, 649, 'dharan-clock-tower_ROwL3Y7.jpg'),
(2, 'Biratnagar', 5, 649, 'biratnagar-gate.jpg'),
(3, 'Itahari', 5, 649, 'itahari.jpg'),
(4, 'Inaruwa', 5, 649, 'inaruwa.jpg'),
(5, 'Mechinagar', 5, 649, '2016-08-09.jpg'),
(6, 'Triyuga', 5, 649, 'Triyuga.jpg'),
(7, 'Birtamod', 5, 649, '60711607.jpg'),
(8, 'Sundar Haraincha', 5, 649, 'download_9.jpg'),
(9, 'Barahachhetra', 5, 649, 'Barhachhetra.jpg'),
(10, 'Damak', 5, 649, 'Damak.jpg'),
(11, 'Belbari', 5, 649, 'Belbari.jpg'),
(12, 'Bhadrapur', 5, 649, 'Bhadrapur.jpg'),
(13, 'Shivasataxi', 5, 649, 'download_10.jpg'),
(14, 'Pathari Sanischare', 5, 649, 'Pathari_Sanischare.jpg'),
(15, 'Arjundhara', 5, 649, 'Arjundhra.jpg'),
(16, 'Illam', 5, 649, 'illam.jpg'),
(17, 'Urlabari', 5, 649, 'default.png'),
(18, 'Udayapur', 5, 649, 'Udayapur.jpg'),
(19, 'Duhabi', 5, 649, 'duhabi-bazar.jpg'),
(20, 'Dhankuta', 5, 649, 'default.png'),
(21, 'Solukhumbu', 5, 649, 'solukhumbu.jpg'),
(22, 'Terhathum', 5, 649, 'terhathum.jpg'),
(23, 'Panchthar', 5, 649, 'phidim.JPG'),
(24, 'Okhaldhunga', 5, 649, '69_831491542883390.jpeg'),
(25, 'Diktel', 5, 649, 'Diktel.jpg'),
(26, 'Sankhuwasabha', 5, 649, 'Sakhuwasabha.jpg'),
(27, 'Bhojpur', 5, 649, 'Bhojpur.jpg'),
(28, 'Lalitpur', 1, 649, 'lalitpur.jpg'),
(29, 'Chitwan', 1, 649, 'Chitwan.jpg'),
(30, 'Hetauda', 1, 649, 'hetauda-bazar.jpg'),
(31, 'Budhanilkantha', 1, 649, 'Budhanilkantha.jpg'),
(32, 'Tokha', 1, 649, 'tokha.jpg'),
(33, 'Chandragiri', 1, 649, 'chandragiri-hill-randonnee-nepal.jpg'),
(34, 'Madhyapur Thimi', 1, 649, 'Madhyapur_thimi.jpg'),
(35, 'Tarakeshor', 1, 649, 'tarkesor.jpg'),
(36, 'Suryabinayak', 1, 649, 'Suryabinayak.jpg'),
(37, 'Godawari', 1, 649, 'Godavari.jpg'),
(38, 'Sindhuli', 1, 649, 'Sindhuli.jpg'),
(39, 'Nuwakot', 1, 649, '18.Nuwakot-Bazar.jpg'),
(40, 'Dolakha', 1, 649, 'Dolakha.jpg'),
(41, 'Kavrepalanchok', 1, 649, 'kavrepalanchowk.jpg'),
(42, 'Ramechap', 1, 649, 'Ramechap.jpg'),
(43, 'Rasuwa', 1, 649, 'Rasuwa.jpg'),
(44, 'Baglung', 2, 649, 'baglung-bazar-960x540.jpg'),
(45, 'Gorkha', 2, 649, 'Gorkha.png'),
(46, 'Kaski', 2, 649, 'Kaski_DA_office.jpg'),
(47, 'Lamjung', 2, 649, 'Lamjung.jpg'),
(48, 'Manang', 2, 649, 'Manang.jpg'),
(49, 'Mustang', 2, 649, 'Mustang-Nepal--1280x640.jpg'),
(50, 'Myagdi', 2, 649, 'Myagdi.jpg'),
(51, 'Nawalpur', 2, 649, 'nawalparasi-kumsot-village-1024x540.jpg'),
(52, 'Parbat', 2, 649, 'Parbat.jpg'),
(53, 'Syanga', 2, 649, 'Syanga.jpg'),
(54, 'Tanahun', 2, 649, 'Bandipur-Tanahun1.jpg'),
(55, 'Pokhara', 2, 649, 'pokhar.jpg'),
(56, 'Kawasoti', 2, 649, 'kawasoti.jpg'),
(57, 'Gaidakot', 2, 649, '220px-Narayani_bridge_in_Gaindakot.jpg'),
(58, 'Waling', 2, 649, 'Waling.jpg'),
(59, 'Waling', 2, 649, 'Waling_wPX3TgC.jpg'),
(60, 'Putalibazar', 2, 649, 'putalibazar.jpg'),
(61, 'Kushma', 2, 649, 'Kushma-bazaar.jpg'),
(62, 'Besishahar', 2, 649, 'Besishahar.jpg'),
(63, 'Palungtar', 2, 649, 'Palungtar_Municipality_Premises.jpg'),
(64, 'Beni', 2, 649, 'Beni-bazar.jpg'),
(65, 'Galkot', 2, 649, 'Galkot.jpg'),
(66, 'Saptari', 3, 649, 'Saptari.jpg'),
(67, 'Sarlahi', 3, 649, 'default.png'),
(68, 'Rajbiraj', 3, 649, '300px-Tribhuvan_Chowk.jpg'),
(69, 'Birgunj', 3, 649, 'Birgunj1.jpg'),
(70, 'Malangwa', 3, 649, 'default.png'),
(71, 'Kalaiya', 3, 649, 'Kalaiya_1_1539767496m.jpg'),
(72, 'Siraha', 3, 649, 'Siraha.jpg'),
(73, 'Janakpur', 3, 649, 'ram-janaki-mandir-things-to-do-in-janakpur-nepal.jpg'),
(74, 'Gaur', 3, 649, 'Gaur.jpg'),
(75, 'Jaleshwar', 3, 649, 'jaleshor.jpg'),
(76, 'Lahan', 3, 649, 'Lahan.jpg'),
(77, 'Chandrapur', 3, 649, 'Chandrapur.jpg'),
(79, 'Gaushala', 3, 649, 'fb_img_1548779300539.jpg'),
(80, 'Bardibas', 3, 649, 'bardibas.jpg'),
(81, 'Lalbandi', 3, 649, 'lalbandi1.JPG'),
(82, 'Jaleshwar', 3, 649, 'jaleshor_zT0CitI.jpg'),
(83, 'Mahagadhimai', 3, 649, 'mahagadimai.jpg'),
(84, 'Golbazar', 3, 649, 'golbazar.jpg'),
(85, 'Garuda', 3, 649, 'Rautahat-2.jpg'),
(86, 'Mirchaiya', 3, 649, 'Mirchaiya.jpg'),
(87, 'Simraungadh', 3, 649, 'default.png'),
(88, 'Bara', 3, 649, 'Baera.jpg'),
(89, 'Mahottari', 3, 649, 'default.png'),
(90, 'Ghorahi', 6, 649, 'Gorahi_Dang.jpg'),
(91, 'Tulshipur', 6, 649, 'tulshipur.jpg'),
(92, 'Nepalgunj', 6, 649, 'Nepaljung.jpg'),
(93, 'Butwal', 6, 649, 'butwal-746x768.jpg'),
(94, 'Tilittama', 6, 649, 'tilottama.jpg'),
(95, 'Kapilvastu', 6, 649, 'Kapilbastu.jpg'),
(96, 'Kohalpur', 6, 649, 'Kohalpur.jpg'),
(97, 'Bardiya', 6, 649, 'Bardiya.jpg'),
(98, 'Gulariya', 6, 649, 'Gulariya.jpg'),
(99, 'Siddharthanagar', 6, 649, 'siddharthanagar_1539758072m.jpg'),
(100, 'Krishnanagar', 6, 649, 'Krishnanagar.jpeg'),
(101, 'Sainamaina', 6, 649, 'download_11.jpg'),
(102, 'Sunwal', 6, 649, 'Sunwal.jpg'),
(103, 'Rupandehi', 6, 649, 'Rupandehi.jpg'),
(104, 'Palpa', 6, 649, 'Palpa.jpg'),
(105, 'Dhangadi', 7, 649, 'dhangadi.jpg'),
(106, 'Kanchanpur', 7, 649, 'Kanchanpur.jpg'),
(107, 'Bhimdatta', 7, 649, 'default.png'),
(108, 'Patan', 1, 649, 'patan.jpg'),
(109, 'Dhulikhel', 1, 649, 'dhulkhel.jpg'),
(110, 'Mahendranagar', 7, 649, 'default.png'),
(111, 'Panauti', 1, 649, 'Panauti.jpg'),
(112, 'Ghodaghodi', 7, 649, 'ghodaghodi.jpg'),
(113, 'Punarbas', 7, 649, 'punarbas.jpg'),
(114, 'Phidim', 5, 649, 'Phidim-bazaar.jpg'),
(115, 'Manthali', 1, 649, 'manthali.jpg'),
(116, 'Pyuthan', 6, 649, 'pyuthan.jpg'),
(117, 'Namobuddha', 1, 649, 'NamoBuddha_1474537068.jpg'),
(118, 'Bandipur', 2, 649, 'Bandipur.jpg'),
(119, 'Byas', 2, 649, 'default.png'),
(120, 'Damauli', 2, 649, 'Damauli.jpg'),
(121, 'Kirtipur', 1, 649, 'kirtipur.jpg'),
(122, 'Khokana', 1, 649, 'khokana-the-village-with.jpg'),
(123, 'Kathmandu', 1, 649, 'ktm_city.jpg'),
(124, 'Lumbini', 6, 649, 'lumbini.jpg'),
(125, 'Nagarkot', 1, 649, 'chisapani-nagarkot-dhulikhel-trek_73.jpg_large_1138_464.jpg'),
(126, 'Chisapani', 1, 649, 'Chisapani.jpg'),
(127, 'Dolpa', 4, 649, 'Dolpa.jpg'),
(128, 'Dunei Bazar', 4, 649, 'Dolpa_nXHoUum.jpg'),
(129, 'Dailekh', 4, 649, 'Dailekh.jpg'),
(130, 'Surkhet', 4, 649, 'Surkhet.jpg'),
(131, 'Salyan', 4, 649, 'Salyan-district.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_country`
--

CREATE TABLE `hotel_country` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `country_code` varchar(200) DEFAULT NULL,
  `code` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_country`
--

INSERT INTO `hotel_country` (`id`, `name`, `country_code`, `code`) VALUES
(495, 'Afghanistan', 'AF', NULL),
(496, 'Albania', 'AL', NULL),
(497, 'Algeria', 'DZ', NULL),
(498, 'American Samoa', 'DS', NULL),
(499, 'Andorra', 'AD', NULL),
(500, 'Angola', 'AO', NULL),
(501, 'Anguilla', 'AI', NULL),
(502, 'Antarctica', 'AQ', NULL),
(503, 'Antigua and Barbuda', 'AG', NULL),
(504, 'Argentina', 'AR', NULL),
(505, 'Armenia', 'AM', NULL),
(506, 'Aruba', 'AW', NULL),
(507, 'Australia', 'AU', NULL),
(508, 'Austria', 'AT', NULL),
(509, 'Azerbaijan', 'AZ', NULL),
(510, 'Bahamas', 'BS', NULL),
(511, 'Bahrain', 'BH', NULL),
(512, 'Bangladesh', 'BD', NULL),
(513, 'Barbados', 'BB', NULL),
(514, 'Belarus', 'BY', NULL),
(515, 'Belgium', 'BE', NULL),
(516, 'Belize', 'BZ', NULL),
(517, 'Benin', 'BJ', NULL),
(518, 'Bermuda', 'BM', NULL),
(519, 'Bhutan', 'BT', NULL),
(520, 'Bolivia', 'BO', NULL),
(521, 'Bosnia and Herzegovina', 'BA', NULL),
(522, 'Botswana', 'BW', NULL),
(523, 'Bouvet Island', 'BV', NULL),
(524, 'Brazil', 'BR', NULL),
(525, 'British Indian Ocean Territory', 'IO', NULL),
(526, 'Brunei Darussalam', 'BN', NULL),
(527, 'Bulgaria', 'BG', NULL),
(528, 'Burkina Faso', 'BF', NULL),
(529, 'Burundi', 'BI', NULL),
(530, 'Cambodia', 'KH', NULL),
(531, 'Cameroon', 'CM', NULL),
(532, 'Canada', 'CA', NULL),
(533, 'Cape Verde', 'CV', NULL),
(534, 'Cayman Islands', 'KY', NULL),
(535, 'Central African Republic', 'CF', NULL),
(536, 'Chad', 'TD', NULL),
(537, 'Chile', 'CL', NULL),
(538, 'China', 'CN', '+86'),
(539, 'Christmas Island', 'CX', NULL),
(540, 'Cocos (Keeling) Islands', 'CC', NULL),
(541, 'Colombia', 'CO', NULL),
(542, 'Comoros', 'KM', NULL),
(543, 'Democratic Republic of the Congo', 'CD', NULL),
(544, 'Republic of Congo', 'CG', NULL),
(545, 'Cook Islands', 'CK', NULL),
(546, 'Costa Rica', 'CR', NULL),
(547, 'Croatia (Hrvatska)', 'HR', NULL),
(548, 'Cuba', 'CU', NULL),
(549, 'Cyprus', 'CY', NULL),
(550, 'Czech Republic', 'CZ', NULL),
(551, 'Denmark', 'DK', NULL),
(552, 'Djibouti', 'DJ', NULL),
(553, 'Dominica', 'DM', NULL),
(554, 'Dominican Republic', 'DO', NULL),
(555, 'East Timor', 'TP', NULL),
(556, 'Ecuador', 'EC', NULL),
(557, 'Egypt', 'EG', NULL),
(558, 'El Salvador', 'SV', NULL),
(559, 'Equatorial Guinea', 'GQ', NULL),
(560, 'Eritrea', 'ER', NULL),
(561, 'Estonia', 'EE', NULL),
(562, 'Ethiopia', 'ET', NULL),
(563, 'Falkland Islands (Malvinas)', 'FK', NULL),
(564, 'Faroe Islands', 'FO', NULL),
(565, 'Fiji', 'FJ', NULL),
(566, 'Finland', 'FI', NULL),
(567, 'France', 'FR', NULL),
(568, 'France, Metropolitan', 'FX', NULL),
(569, 'French Guiana', 'GF', NULL),
(570, 'French Polynesia', 'PF', NULL),
(571, 'French Southern Territories', 'TF', NULL),
(572, 'Gabon', 'GA', NULL),
(573, 'Gambia', 'GM', NULL),
(574, 'Georgia', 'GE', NULL),
(575, 'Germany', 'DE', NULL),
(576, 'Ghana', 'GH', NULL),
(577, 'Gibraltar', 'GI', NULL),
(578, 'Guernsey', 'GK', NULL),
(579, 'Greece', 'GR', NULL),
(580, 'Greenland', 'GL', NULL),
(581, 'Grenada', 'GD', NULL),
(582, 'Guadeloupe', 'GP', NULL),
(583, 'Guam', 'GU', NULL),
(584, 'Guatemala', 'GT', NULL),
(585, 'Guinea', 'GN', NULL),
(586, 'Guinea-Bissau', 'GW', NULL),
(587, 'Guyana', 'GY', NULL),
(588, 'Haiti', 'HT', NULL),
(589, 'Heard and Mc Donald Islands', 'HM', NULL),
(590, 'Honduras', 'HN', NULL),
(591, 'Hong Kong', 'HK', NULL),
(592, 'Hungary', 'HU', NULL),
(593, 'Iceland', 'IS', NULL),
(594, 'India', 'IN', '+91'),
(595, 'Isle of Man', 'IM', NULL),
(596, 'Indonesia', 'ID', NULL),
(597, 'Iran (Islamic Republic of)', 'IR', NULL),
(598, 'Iraq', 'IQ', NULL),
(599, 'Ireland', 'IE', NULL),
(600, 'Israel', 'IL', NULL),
(601, 'Italy', 'IT', NULL),
(602, 'Ivory Coast', 'CI', NULL),
(603, 'Jersey', 'JE', NULL),
(604, 'Jamaica', 'JM', NULL),
(605, 'Japan', 'JP', NULL),
(606, 'Jordan', 'JO', NULL),
(607, 'Kazakhstan', 'KZ', NULL),
(608, 'Kenya', 'KE', NULL),
(609, 'Kiribati', 'KI', NULL),
(610, 'Korea, Democratic People\'s Republic of', 'KP', NULL),
(611, 'Korea, Republic of', 'KR', NULL),
(612, 'Kosovo', 'XK', NULL),
(613, 'Kuwait', 'KW', NULL),
(614, 'Kyrgyzstan', 'KG', NULL),
(615, 'Lao People\'s Democratic Republic', 'LA', NULL),
(616, 'Latvia', 'LV', NULL),
(617, 'Lebanon', 'LB', NULL),
(618, 'Lesotho', 'LS', NULL),
(619, 'Liberia', 'LR', NULL),
(620, 'Libyan Arab Jamahiriya', 'LY', NULL),
(621, 'Liechtenstein', 'LI', NULL),
(622, 'Lithuania', 'LT', NULL),
(623, 'Luxembourg', 'LU', NULL),
(624, 'Macau', 'MO', NULL),
(625, 'North Macedonia', 'MK', NULL),
(626, 'Madagascar', 'MG', NULL),
(627, 'Malawi', 'MW', NULL),
(628, 'Malaysia', 'MY', NULL),
(629, 'Maldives', 'MV', NULL),
(630, 'Mali', 'ML', NULL),
(631, 'Malta', 'MT', NULL),
(632, 'Marshall Islands', 'MH', NULL),
(633, 'Martinique', 'MQ', NULL),
(634, 'Mauritania', 'MR', NULL),
(635, 'Mauritius', 'MU', NULL),
(636, 'Mayotte', 'TY', NULL),
(637, 'Mexico', 'MX', NULL),
(638, 'Micronesia, Federated States of', 'FM', NULL),
(639, 'Moldova, Republic of', 'MD', NULL),
(640, 'Monaco', 'MC', NULL),
(641, 'Mongolia', 'MN', NULL),
(642, 'Montenegro', 'ME', NULL),
(643, 'Montserrat', 'MS', NULL),
(644, 'Morocco', 'MA', NULL),
(645, 'Mozambique', 'MZ', NULL),
(646, 'Myanmar', 'MM', NULL),
(647, 'Namibia', 'NA', NULL),
(648, 'Nauru', 'NR', NULL),
(649, 'Nepal', 'NP', '+977'),
(650, 'Netherlands', 'NL', NULL),
(651, 'Netherlands Antilles', 'AN', NULL),
(652, 'New Caledonia', 'NC', NULL),
(653, 'New Zealand', 'NZ', NULL),
(654, 'Nicaragua', 'NI', NULL),
(655, 'Niger', 'NE', NULL),
(656, 'Nigeria', 'NG', NULL),
(657, 'Niue', 'NU', NULL),
(658, 'Norfolk Island', 'NF', NULL),
(659, 'Northern Mariana Islands', 'MP', NULL),
(660, 'Norway', 'NO', NULL),
(661, 'Oman', 'OM', NULL),
(662, 'Pakistan', 'PK', NULL),
(663, 'Palau', 'PW', NULL),
(664, 'Palestine', 'PS', NULL),
(665, 'Panama', 'PA', NULL),
(666, 'Papua New Guinea', 'PG', NULL),
(667, 'Paraguay', 'PY', NULL),
(668, 'Peru', 'PE', NULL),
(669, 'Philippines', 'PH', NULL),
(670, 'Pitcairn', 'PN', NULL),
(671, 'Poland', 'PL', NULL),
(672, 'Portugal', 'PT', NULL),
(673, 'Puerto Rico', 'PR', NULL),
(674, 'Qatar', 'QA', NULL),
(675, 'Reunion', 'RE', NULL),
(676, 'Romania', 'RO', NULL),
(677, 'Russian Federation', 'RU', NULL),
(678, 'Rwanda', 'RW', NULL),
(679, 'Saint Kitts and Nevis', 'KN', NULL),
(680, 'Saint Lucia', 'LC', NULL),
(681, 'Saint Vincent and the Grenadines', 'VC', NULL),
(682, 'Samoa', 'WS', NULL),
(683, 'San Marino', 'SM', NULL),
(684, 'Sao Tome and Principe', 'ST', NULL),
(685, 'Saudi Arabia', 'SA', NULL),
(686, 'Senegal', 'SN', NULL),
(687, 'Serbia', 'RS', NULL),
(688, 'Seychelles', 'SC', NULL),
(689, 'Sierra Leone', 'SL', NULL),
(690, 'Singapore', 'SG', NULL),
(691, 'Slovakia', 'SK', NULL),
(692, 'Slovenia', 'SI', NULL),
(693, 'Solomon Islands', 'SB', NULL),
(694, 'Somalia', 'SO', NULL),
(695, 'South Africa', 'ZA', NULL),
(696, 'South Georgia South Sandwich Islands', 'GS', NULL),
(697, 'South Sudan', 'SS', NULL),
(698, 'Spain', 'ES', NULL),
(699, 'Sri Lanka', 'LK', NULL),
(700, 'St. Helena', 'SH', NULL),
(701, 'St. Pierre and Miquelon', 'PM', NULL),
(702, 'Sudan', 'SD', NULL),
(703, 'Suriname', 'SR', NULL),
(704, 'Svalbard and Jan Mayen Islands', 'SJ', NULL),
(705, 'Swaziland', 'SZ', NULL),
(706, 'Sweden', 'SE', NULL),
(707, 'Switzerland', 'CH', NULL),
(708, 'Syrian Arab Republic', 'SY', NULL),
(709, 'Taiwan', 'TW', NULL),
(710, 'Tajikistan', 'TJ', NULL),
(711, 'Tanzania, United Republic of', 'TZ', NULL),
(712, 'Thailand', 'TH', NULL),
(713, 'Togo', 'TG', NULL),
(714, 'Tokelau', 'TK', NULL),
(715, 'Tonga', 'TO', NULL),
(716, 'Trinidad and Tobago', 'TT', NULL),
(717, 'Tunisia', 'TN', NULL),
(718, 'Turkey', 'TR', NULL),
(719, 'Turkmenistan', 'TM', NULL),
(720, 'Turks and Caicos Islands', 'TC', NULL),
(721, 'Tuvalu', 'TV', NULL),
(722, 'Uganda', 'UG', NULL),
(723, 'Ukraine', 'UA', NULL),
(724, 'United Arab Emirates', 'AE', NULL),
(725, 'United Kingdom', 'GB', NULL),
(726, 'United States', 'US', NULL),
(727, 'United States minor outlying islands', 'UM', NULL),
(728, 'Uruguay', 'UY', NULL),
(729, 'Uzbekistan', 'UZ', NULL),
(730, 'Vanuatu', 'VU', NULL),
(731, 'Vatican City State', 'VA', NULL),
(732, 'Venezuela', 'VE', NULL),
(733, 'Vietnam', 'VN', NULL),
(734, 'Virgin Islands (British)', 'VG', NULL),
(735, 'Virgin Islands (U.S.)', 'VI', NULL),
(736, 'Wallis and Futuna Islands', 'WF', NULL),
(737, 'Western Sahara', 'EH', NULL),
(738, 'Yemen', 'YE', NULL),
(739, 'Zambia', 'ZM', NULL),
(740, 'Zimbabwe', 'ZW', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_favourites`
--

CREATE TABLE `hotel_favourites` (
  `id` int(11) NOT NULL,
  `module` varchar(80) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `favourite` tinyint(1) NOT NULL,
  `saved` tinyint(1) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `inventory_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hoteladdress`
--

CREATE TABLE `hotel_hoteladdress` (
  `hotel_id` int(11) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `contact1` varchar(17) DEFAULT NULL,
  `contact2` varchar(17) DEFAULT NULL,
  `latitude` decimal(20,12) DEFAULT NULL,
  `longitude` decimal(20,12) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `city_id` int(11) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hoteladdress`
--

INSERT INTO `hotel_hoteladdress` (`hotel_id`, `address`, `contact1`, `contact2`, `latitude`, `longitude`, `created_at`, `city_id`, `country_id`, `state_id`) VALUES
(3, '1932 Kauze Pike', '5287117730', '9616272754', '27.717200000000', '85.324000000000', '2019-04-22 10:46:52.749355', 123, 649, 1),
(4, 'lalitpur nepal', '+977-9813207240', '+977-9813207240', '27.666040928328', '85.314751211301', '2019-04-22 11:01:37.211632', 123, 649, 1),
(5, '1556 Nedeto Center', '+977-9849755595', '+977-9849755595', '27.717200000000', '85.324000000000', '2019-04-22 11:14:59.112127', 68, 649, 3),
(16, '1813 Rupce Boulevard', '3819812923', '9778337380', '27.717200000000', '85.324000000000', '2019-04-25 12:08:43.084664', 123, 649, 1),
(18, '1433 Dofjak Highway', '9633515232', NULL, '27.717200000000', '85.324000000000', '2019-05-02 05:46:37.046129', 123, 649, 1),
(19, '1433 Dofjak Highway', '9633515232', NULL, '27.717200000000', '85.324000000000', '2019-05-02 05:46:49.927473', 123, 649, 1),
(20, 'Meghauli Ward no 1 , Narayani Nager Palika , 44207', '2388462632', '5695538978', '27.569590642285', '84.201851296924', '2019-05-03 05:37:56.125200', 29, 649, 1),
(23, '969 Weuca Avenue', '4853295724', '2432867553', '0.000000000000', '0.000000000000', '2019-06-13 06:57:14.766915', 123, 649, 1),
(29, 'Baneshwore', '97714438955', NULL, '27.689047500000', '85.333561000000', '2019-10-02 06:00:37.807668', 123, 649, 1),
(30, 'anamnagar', '97714438955', '9812333334', '28.256769593526', '83.823519060156', '2019-10-18 04:18:15.193042', 29, 649, 1),
(31, 'Baneshor', '97714438955', '9812333334', '27.708436852622', '85.325138499414', '2019-10-18 07:13:04.186201', 59, 649, 2),
(32, 'anamnagar', '97714438955', '9812333334', '27.708436852622', '85.325138499414', '2019-10-20 07:44:14.268418', 47, 649, 2),
(33, 'Anamnagar', '97714438955', '9812333334', '27.708436852622', '85.325138499414', '2019-10-20 14:18:08.062517', 37, 649, 1),
(34, 'aananssa', '97714438955', '9812333334', '27.708436852622', '85.325138499414', '2019-10-21 06:30:22.034554', 109, 649, 1),
(35, 'Baneshor', '97714438955', NULL, '27.708436852622', '85.325138499414', '2019-10-22 05:02:47.623375', 33, 649, 1),
(36, 'Sauraha', '97714438955', '9851125923', '27.708436852622', '85.325138499414', '2019-10-31 05:43:44.827100', 29, 649, 1),
(37, 'tinkune', '+977-9841123456', '+977-9841123456', '27.686087936871', '85.345016147855', '2019-12-30 08:04:12.658056', 108, 649, 1),
(38, 'kalanki', '+977-9841123456', '+977-9841123456', '27.693947900000', '85.281466100000', '2019-12-30 08:18:49.841403', 28, 649, 1),
(39, 'danchhi', '+977-9849755595', '+977-9849755595', '27.736649500000', '85.423370800000', '2020-01-19 10:20:25.371665', 28, 649, 1),
(40, 'Tinkune,Sayognagar', '+977-9849755595', '+977-9849755595', '27.718432511230', '85.324926095245', '2020-01-24 06:06:49.981636', 123, 649, 1);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hoteladdress_landmarks`
--

CREATE TABLE `hotel_hoteladdress_landmarks` (
  `id` int(11) NOT NULL,
  `hoteladdress_id` int(11) NOT NULL,
  `landmark_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hoteladdress_landmarks`
--

INSERT INTO `hotel_hoteladdress_landmarks` (`id`, `hoteladdress_id`, `landmark_id`) VALUES
(133, 3, 3),
(132, 3, 77),
(168, 4, 77),
(169, 4, 82),
(170, 4, 83),
(23, 16, 1),
(22, 16, 2),
(11, 17, 2),
(165, 20, 2),
(156, 28, 78),
(157, 28, 79),
(162, 29, 77),
(163, 30, 2),
(173, 37, 1),
(176, 38, 86),
(177, 38, 87),
(180, 39, 1),
(179, 39, 88),
(181, 40, 84),
(182, 40, 85);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelamenities`
--

CREATE TABLE `hotel_hotelamenities` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelamenities`
--

INSERT INTO `hotel_hotelamenities` (`id`, `name`, `image`, `created_at`) VALUES
(3, 'AC', 'air-conditioner.png', '2019-04-22 07:01:33.382875'),
(4, 'Wifi', 'wifi.png', '2019-04-22 07:01:39.620181'),
(5, 'BreakFast', 'food-service.png', '2019-06-02 10:44:44.299772'),
(6, 'Laundry', 'washing-machine_1.png', '2019-06-02 10:44:51.362402'),
(7, 'Room Service', 'food-service_yUQ2r7W.png', '2019-06-02 10:45:05.193481'),
(8, 'Free Wine', 'drink.png', '2019-06-02 10:45:11.686485'),
(9, 'Free beverage', 'cereals.png', '2019-06-02 10:45:22.726451'),
(10, 'TV', 'computer.png', '2019-06-02 10:45:35.469310'),
(11, 'Smart TV', 'computer_5JjvCov.png', '2019-06-02 10:45:42.219277');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelbooking`
--

CREATE TABLE `hotel_hotelbooking` (
  `id` int(11) NOT NULL,
  `checkin_date` date NOT NULL,
  `checkout_date` date NOT NULL,
  `price` decimal(5,2) NOT NULL,
  `no_of_adult` int(11) NOT NULL,
  `no_of_child` int(11) NOT NULL,
  `no_of_room` decimal(3,0) NOT NULL,
  `pay_mode` varchar(10) NOT NULL,
  `pay_status` tinyint(1) NOT NULL,
  `hotelinventory_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelfacilities`
--

CREATE TABLE `hotel_hotelfacilities` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelfacilities`
--

INSERT INTO `hotel_hotelfacilities` (`id`, `name`, `image`, `created_at`) VALUES
(1, 'swimming pool', 'swimming-pool.png', '2019-04-21 12:05:50.757040'),
(2, 'site seeing', 'site_seeing.png', '2019-04-21 12:05:59.505601'),
(3, 'parking', 'parking.png', '2019-11-12 07:08:23.361489'),
(4, 'BAR OR LOUNGE', 'bar.png', '2019-11-12 07:08:59.822907'),
(5, 'FITNESS CENTER', 'weightlifter.png', '2019-11-12 07:16:19.751239'),
(6, 'rental', 'rental-car.png', '2019-11-12 07:20:56.403798'),
(7, 'restaurant', 'plate-fork-and-knife.png', '2019-11-12 07:22:55.101222'),
(8, 'sauna spa', 'hot-spring.png', '2019-11-12 07:24:57.487690');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelfacilitiesmiddle`
--

CREATE TABLE `hotel_hotelfacilitiesmiddle` (
  `id` int(11) NOT NULL,
  `hotels_id` int(11) NOT NULL,
  `hotelsfacilities_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelfacilitiesmiddle`
--

INSERT INTO `hotel_hotelfacilitiesmiddle` (`id`, `hotels_id`, `hotelsfacilities_id`) VALUES
(7, 17, 1),
(8, 17, 2),
(42, 21, 1),
(55, 21, 1),
(64, 22, 1),
(65, 22, 2),
(73, 24, 1),
(74, 25, 1),
(75, 26, 1),
(76, 27, 2),
(77, 28, 1),
(94, 5, 1),
(95, 5, 2),
(96, 5, 3),
(97, 5, 4),
(98, 5, 5),
(99, 5, 6),
(100, 5, 7),
(101, 5, 8),
(109, 29, 3),
(110, 29, 4),
(111, 29, 5),
(112, 29, 6),
(113, 29, 7),
(114, 29, 8),
(115, 29, 1),
(116, 30, 1),
(117, 30, 2),
(118, 30, 3),
(119, 30, 4),
(120, 30, 5),
(121, 30, 6),
(122, 30, 7),
(123, 30, 8),
(124, 33, 1),
(125, 33, 2),
(126, 33, 3),
(127, 33, 4),
(128, 33, 5),
(129, 33, 6),
(130, 33, 7),
(131, 33, 8),
(132, 34, 1),
(133, 34, 2),
(134, 34, 3),
(135, 34, 4),
(136, 34, 5),
(137, 34, 6),
(138, 34, 7),
(139, 34, 8),
(140, 35, 1),
(141, 35, 2),
(142, 35, 3),
(143, 35, 4),
(144, 35, 5),
(145, 35, 6),
(146, 35, 7),
(147, 35, 8),
(148, 36, 1),
(149, 36, 2),
(150, 36, 3),
(151, 36, 4),
(152, 36, 5),
(153, 36, 6),
(154, 36, 7),
(155, 36, 8),
(164, 3, 3),
(165, 3, 4),
(166, 3, 5),
(167, 3, 6),
(168, 3, 7),
(169, 3, 8),
(170, 3, 1),
(171, 3, 2),
(172, 16, 2),
(173, 16, 3),
(174, 16, 4),
(175, 16, 5),
(176, 16, 6),
(177, 16, 7),
(178, 16, 8),
(179, 16, 1),
(180, 20, 1),
(190, 19, 1),
(191, 19, 4),
(192, 19, 5),
(193, 19, 6),
(194, 19, 7),
(195, 19, 8),
(196, 19, 2),
(197, 31, 1),
(198, 31, 2),
(199, 31, 3),
(200, 31, 4),
(201, 31, 5),
(202, 31, 6),
(211, 18, 1),
(212, 18, 3),
(213, 18, 4),
(214, 18, 5),
(215, 18, 6),
(216, 18, 7),
(217, 18, 8),
(218, 18, 2),
(219, 37, 1),
(220, 37, 2),
(221, 37, 4),
(222, 37, 5),
(223, 37, 6),
(224, 37, 7),
(225, 37, 8),
(226, 38, 1),
(227, 38, 2),
(228, 38, 3),
(229, 38, 4),
(230, 38, 6),
(231, 38, 7),
(232, 39, 1),
(233, 39, 2),
(234, 39, 3),
(235, 39, 4),
(236, 39, 5),
(237, 39, 6),
(238, 39, 7),
(239, 39, 8),
(240, 23, 3),
(241, 23, 4),
(242, 23, 5),
(243, 23, 6),
(244, 23, 7),
(245, 23, 8),
(246, 23, 1),
(247, 23, 2),
(248, 4, 2),
(249, 4, 3),
(250, 4, 4),
(251, 4, 5),
(252, 4, 6),
(253, 4, 7),
(254, 4, 8),
(255, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelfacilitiesmiddlenew`
--

CREATE TABLE `hotel_hotelfacilitiesmiddlenew` (
  `id` int(11) NOT NULL,
  `hotels_id` int(11) NOT NULL,
  `hotelsfacilities_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelfacilitiesmiddlenew`
--

INSERT INTO `hotel_hotelfacilitiesmiddlenew` (`id`, `hotels_id`, `hotelsfacilities_id`) VALUES
(1, 2, 1),
(2, 2, 2),
(3, 3, 1),
(4, 3, 2),
(5, 4, 1),
(6, 4, 2),
(7, 6, 1),
(8, 6, 2),
(9, 7, 1),
(10, 7, 2),
(11, 8, 1),
(12, 8, 2),
(13, 9, 1),
(14, 9, 2),
(15, 10, 1),
(16, 10, 2),
(17, 11, 1),
(18, 11, 2);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelgallery`
--

CREATE TABLE `hotel_hotelgallery` (
  `id` int(11) NOT NULL,
  `image` varchar(500) NOT NULL,
  `title` varchar(200) NOT NULL,
  `hotel_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelgallery`
--

INSERT INTO `hotel_hotelgallery` (`id`, `image`, `title`, `hotel_id_id`) VALUES
(5, 'IMG_0221_7SIsUh3.jpg', 'Building', 3),
(6, 'IMG_0227.jpg', 'Kitchen', 3),
(9, '178848583.jpg', 'Building', 5),
(10, '178523823.jpg', 'Kitchen', 5),
(23, '12_PvmLjEb.jpg', 'Building', 16),
(24, 'IMG_0221_HofHPGp.jpg', 'Building', 3),
(25, 'holiday-inn.jpeg', 'Building', 17),
(26, 'All-Our-Kids-750x485_9JwRZiE.jpg', 'Kitchen', 17),
(27, 'Meghaul-Serai_TryrbXL.jpg', 'Building', 20),
(28, 'V8ffUYWzbLX4KVAnV6roBimeDACuqp3M7R4Frej5.jpeg', 'Kitchen', 20),
(29, 'taj.jpg', 'Lobby', 20),
(30, 'hotel_visitors_inn_ZfaDTn0.jpg', 'Building', 18),
(31, 'lobby_l3DQWpF.jpg', 'Kitchen', 18),
(32, 'kitchen_Og0HCR2.jpg', 'Lobby', 18),
(33, '178848583_NFo5RAu.jpg', 'Building', 19),
(34, '178525052.jpg', 'Kitchen', 19),
(35, '178371930_5XFve4d.jpg', 'Lobby', 19),
(36, '4_adlvdkY.jpg', 'Building', 16),
(37, '2_xZFiRKT.jpg', 'Kitchen', 16),
(38, '26169175_542907659421598_9195368196238474952_n_UbPqOnp.jpg', 'Lobby', 16),
(39, 'Screen_Shot_2019-03-02_at_6.24.26_PM_HVfZL04.png', 'Building', 17),
(40, 'UcRbT_Untitled-1_g8w9Hqj.jpg', 'Building', 29),
(41, 'dining_H1lW16P.jpg', 'Restaurant', 29),
(42, 'Lobby.jpg', 'Lobby', 29),
(43, 'CHmoH_swimming-pool.jpg', 'Building', 29),
(44, 'dining_jYbn5c2.jpg', 'Restaurant', 29),
(49, 'FB_IMG_1531726262058_6Sl3eNW.jpg', 'Building', 4),
(50, 'kitchen.jpg', 'Restaurant', 4),
(51, 'lobby.jpg', 'Lobby', 4),
(52, 'hotel_visitors_inn_gFKvEPD.jpg', 'Building', 30),
(53, 'kitchen_tMW9mSg.jpg', 'Restaurant', 30),
(54, 'lobby_UFBztrO.jpg', 'Lobby', 30),
(55, 'IMG_0217_-_Copy.jpg', 'Building', 32),
(56, 'IMG_0224.jpg', 'Restaurant', 32),
(57, 'IMG_0271.jpg', 'Lobby', 32),
(58, 'hotel_g2wwbpg.jpg', 'Building', 33),
(59, '26169175_542907659421598_9195368196238474952_n.jpg', 'Restaurant', 33),
(60, '51935342_792481974464164_4257143752407121920_o.jpg', 'Lobby', 33),
(61, '12_JTSWaLQ.jpg', 'Building', 34),
(62, '2_dWci799.jpg', 'Restaurant', 34),
(63, '6_53M7oq7.jpg', 'Lobby', 34),
(64, 'IMG_0212.jpg', 'Building', 23),
(65, 'IMG_0271_aeMUgmR.jpg', 'Restaurant', 23),
(66, 'IMG_0202_-_Copy.jpg', 'Lobby', 23),
(67, '38/hotel_isxLnE7HW9.jpg', 'Building', 38),
(68, '39/hotel_ba14lDXFuH.jpg', 'Building', 39),
(69, '39/hotel_zWYrQrMQL8.jpg', 'Restaurant', 39),
(70, '39/hotel_BGEz5KOW6k.jpg', 'Lobby', 39),
(71, '40/hotel_0TSDRJxvoK.jpg', 'Building', 40),
(72, '40/hotel_aFmxNgGyo7.jpg', 'Restaurant', 40),
(73, '40/hotel_5mDVOEqyVR.jpg', 'Lobby', 40),
(74, '5/hotel_1dAXsRGcoD.jpg', 'Building', 5);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelinventory`
--

CREATE TABLE `hotel_hotelinventory` (
  `id` int(11) NOT NULL,
  `room_name` varchar(30) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `description` longtext,
  `child_max` int(11) NOT NULL,
  `extra_bed` tinyint(1) NOT NULL,
  `adult_max` int(11) NOT NULL,
  `no_of_rooms` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `image` varchar(500) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `priceforadult` longtext NOT NULL,
  `no_of_extra_bed` int(11) DEFAULT NULL,
  `ppextrabed` decimal(10,2) DEFAULT NULL,
  `agerangeforchild` varchar(30) DEFAULT NULL,
  `agerangeforinfant` varchar(30) DEFAULT NULL,
  `discountforchild` decimal(10,2) DEFAULT NULL,
  `discountforinfant` decimal(10,2) DEFAULT NULL,
  `infant_max` int(11) DEFAULT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelinventory`
--

INSERT INTO `hotel_hotelinventory` (`id`, `room_name`, `price`, `description`, `child_max`, `extra_bed`, `adult_max`, `no_of_rooms`, `created_at`, `is_active`, `image`, `hotel_id`, `user_id`, `priceforadult`, `no_of_extra_bed`, `ppextrabed`, `agerangeforchild`, `agerangeforinfant`, `discountforchild`, `discountforinfant`, `infant_max`, `status`) VALUES
(5, 'Single Room', '4500.00', 'A room assigned to one person. May have one or more beds.\r\nThe room size or area of Single Rooms are generally between 37 m² to 45 m².', 2, 1, 2, 7, '2019-04-25 12:09:26.807042', 1, '178848583_o5HaIZq.jpg', 16, 8, '{\"adult0\": \"30\"}', 2, '2.00', '16', '2', '20.00', '20.00', 2, 0),
(6, 'London', '12000.00', 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their room. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 2, 0, 2, 6, '2019-04-26 07:54:22.410278', 1, '187946005.jpg', 5, 4, '{\"adult0\": \"30\"}', 2, NULL, '12', '2', '20.00', '20.00', 2, 1),
(7, 'Quad Bedroom', '5000.00', 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their room. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 1, 1, 4, 4, '2019-05-12 06:38:27.552791', 1, '193843438.jpg', 5, 4, '{\"adult0\": \"30\", \"adult1\": \"40\", \"adult2\": \"50\"}', 2, '2000.00', '14', '5', '20.00', '20.00', 2, 1),
(8, 'Christine Price', '800.00', 'A room that can accommodate two persons with two twin beds joined together by a common headboard. Most of the budget hotels tend to provide many of these room settings which cater both couples and parties in two.', 1, 1, 1, 10, '2019-05-17 09:34:18.255139', 1, 'IMG_0893_Ig2YoTi.jpg', 3, 8, '\"\"', 2, '2000.00', '12', '2', '20.00', '20.00', 2, 0),
(10, 'Double Twin Bedroom ', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 33, 8, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(11, 'Queen', '5090.00', 'A room with a queen-sized bed. May be occupied by one or more people.', 2, 0, 2, 2, '2019-05-17 10:28:52.486820', 1, 'IMG_0893_Ig2YoTi.jpg', 3, 8, '\"\"', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(13, 'King Room', '611.93', 'A room with a king-sized bed. May be occupied by one or more people.', 1, 0, 1, 4, '2019-05-17 10:34:19.844958', 1, '1_9XYVS14.jpg', 3, 8, '\"\"', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(14, 'Hollywood Quad Room', '5000.00', 'A room that can accommodate two persons with two twin beds joined together by a common headboard. Most of the budget hotels tend to provide many of these room settings which cater both couples and parties in two.', 2, 0, 1, 4, '2019-05-17 10:36:59.662014', 1, '1_9XYVS14.jpg', 3, 8, '\"\"', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(69, 'Christine Price', '800.00', 'A room that can accommodate two persons with two twin beds joined together by a common headboard. Most of the budget hotels tend to provide many of these room settings which cater both couples and parties in two.', 1, 1, 1, 10, '2019-05-17 09:34:18.255139', 1, '1_9XYVS14.jpg', 3, 8, '\"\"', 2, '2000.00', '12', '2', '20.00', '20.00', 2, 0),
(70, 'Hollywood Quad Room', '5000.00', 'A room that can accommodate two persons with two twin beds joined together by a common headboard. Most of the budget hotels tend to provide many of these room settings which cater both couples and parties in two.', 2, 0, 1, 4, '2019-05-17 10:36:59.662014', 1, '1_9XYVS14.jpg', 3, 8, '\"\"', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(71, 'King Room', '611.93', 'A room with a king-sized bed. May be occupied by one or more people.', 1, 0, 1, 4, '2019-05-17 10:34:19.844958', 1, '1_9XYVS14.jpg', 3, 8, '\"\"', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(72, 'London', '12000.00', 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their room. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 2, 0, 2, 100, '2019-04-26 07:54:22.410278', 1, '187946005.jpg', 5, 4, '{\"adult0\": \"30\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 1),
(73, 'Quad Bedroom', '5000.00', 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their room. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 1, 1, 4, 4, '2019-05-12 06:38:27.552791', 1, '193843438.jpg', 5, 4, '{\"adult0\": \"30\", \"adult1\": \"40\", \"adult2\": \"50\"}', 2, '2000.00', '14', '5', '20.00', '20.00', 2, 1),
(74, 'Queen', '5090.00', 'A room with a queen-sized bed. May be occupied by one or more people.', 2, 0, 1, 2, '2019-05-17 10:28:52.486820', 1, 'IMG_0893_Ig2YoTi.jpg', 3, 8, '\"\"', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(75, 'Single Room', '4500.00', 'A room assigned to one person. May have one or more beds.\r\nThe room size or area of Single Rooms are generally between 37 m² to 45 m².', 2, 1, 2, 7, '2019-04-25 12:09:26.807042', 1, '178848583_o5HaIZq.jpg', 16, 8, '{\"adult0\": \"30\"}', 2, '2.00', '16', '2', '20.00', '20.00', 2, 0),
(76, 'Twin Bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 33, 10, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(77, 'Bagmati', '3000.00', 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 2, 0, 1, 3, '2019-11-25 11:01:06.075591', 1, 'IMG_0893_Ig2YoTi.jpg', 19, 8, '\"0\"', NULL, NULL, '12', '2', '0.00', '0.00', 2, 0),
(78, 'Damuli', '4000.00', 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 2, 0, 3, 4, '2019-11-25 11:03:17.177476', 1, '197439141.jpg', 20, 8, '{}', NULL, NULL, '12', '2', '0.00', '0.00', 3, 0),
(79, 'Double Twin Bedroom ', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 31, 8, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(80, 'Queen', '5090.00', 'A room with a queen-sized bed. May be occupied by one or more people.', 2, 0, 1, 2, '2019-05-17 10:28:52.486820', 1, 'IMG_0893_Ig2YoTi.jpg', 31, 8, '\"\"', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(81, 'Single Room', '4500.00', 'A room assigned to one person. May have one or more beds.\r\nThe room size or area of Single Rooms are generally between 37 m² to 45 m².', 2, 1, 2, 7, '2019-04-25 12:09:26.807042', 1, '178848583_o5HaIZq.jpg', 32, 8, '{\"adult0\": \"30\"}', 2, '2.00', '16', '2', '20.00', '20.00', 2, 0),
(82, 'Tywin Bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 32, 10, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(83, 'Queen size bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 29, 8, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(84, 'Twin Bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 29, 8, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(85, 'King Room', '611.93', 'A room with a king-sized bed. May be occupied by one or more people.', 1, 0, 1, 4, '2019-05-17 10:34:19.844958', 1, '1_9XYVS14.jpg', 30, 8, '{\"adult0\": \"10\"}', 2, '2.00', '12', '2', '20.00', '20.00', 2, 0),
(86, 'Queen size bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 35, 8, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(87, 'Twin Bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 35, 10, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(88, 'Kathmandu INN', '670.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 0, 'IMG_0282_z8d2m6r.jpg', 4, 4, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 1),
(89, 'annapurna room', '5000.00', 'this is annapurna room', 1, 0, 3, 3, '2019-12-04 07:08:25.195464', 1, '4/hotel_ZTUdVwi2kc.jpg', 4, 4, '{}', NULL, NULL, '12', '2', '0.00', '0.00', 1, 0),
(90, 'manaslu', '2000.00', 'this is manaslu room', 1, 0, 3, 3, '2019-12-04 07:11:43.426479', 1, '4/hotel_wfcNfAIWOr.jpg', 4, 4, '{}', NULL, NULL, '12', '2', '0.00', '0.00', 2, 0),
(91, 'Queen size bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 23, 8, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(92, 'Twin Bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 23, 8, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(93, 'King Room', '611.93', 'A room with a king-sized bed. May be occupied by one or more people.', 1, 0, 1, 4, '2019-05-17 10:34:19.844958', 1, '1_9XYVS14.jpg', 23, 8, '{\"adult0\": \"10\"}', 2, '2.00', '12', '2', '20.00', '20.00', 2, 0),
(94, 'Queen', '5090.00', 'A room with a queen-sized bed. May be occupied by one or more people.', 2, 0, 1, 2, '2019-05-17 10:28:52.486820', 1, 'IMG_0893_Ig2YoTi.jpg', 34, 10, '\"\"', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(95, 'Single Room', '4500.00', 'A room assigned to one person. May have one or more beds.\r\nThe room size or area of Single Rooms are generally between 37 m² to 45 m².', 2, 1, 2, 7, '2019-04-25 12:09:26.807042', 1, '178848583_o5HaIZq.jpg', 34, 10, '{\"adult0\": \"30\"}', 2, '2.00', '16', '2', '20.00', '20.00', 2, 0),
(96, 'London', '12000.00', 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their room. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 2, 0, 2, 6, '2019-04-26 07:54:22.410278', 1, '187946005.jpg', 34, 10, '{\"adult0\": \"30\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 1),
(97, 'Quad Bedroom', '5000.00', 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their room. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 1, 1, 4, 4, '2019-05-12 06:38:27.552791', 1, '193843438.jpg', 34, 10, '{\"adult0\": \"30\", \"adult1\": \"40\", \"adult2\": \"50\"}', 2, '2000.00', '14', '5', '20.00', '20.00', 2, 1),
(98, 'Queen size bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 36, 10, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(99, 'Twin Bedroom', '650.00', 'A room with two twin beds. May be occupied by one or more people.\r\n\r\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m².', 1, 0, 2, 2, '2019-05-17 09:50:04.269890', 1, 'IMG_0282_z8d2m6r.jpg', 36, 10, '{\"adult0\": \"10\"}', NULL, NULL, '12', '2', '20.00', '20.00', 2, 0),
(100, 'makalu', '3000.00', 'this is makalu room', 2, 0, 2, 3, '2019-12-06 07:53:41.554303', 1, '18/hotel_kkmyBiic8n.jpg', 18, 8, '{}', NULL, NULL, '12', '2', '0.00', '0.00', 2, 0),
(101, 'rara room', '1000.00', 'this isroom', 1, 0, 3, 3, '2019-12-30 08:11:00.709563', 0, 'default.png', 37, 111, '{}', NULL, NULL, '12', '2', '0.00', '0.00', 2, 0),
(102, 'deluxe', '1300.00', 'this  is very good room', 2, 0, 1, 3, '2019-12-30 09:05:19.305500', 0, 'default.png', 38, 111, '\"0\"', NULL, NULL, '12', '2', '0.00', '0.00', 1, 0),
(103, 'annapurna room', '5000.00', 'this is annapurna room', 1, 0, 3, 3, '2019-12-04 07:08:25.195464', 1, '4/hotel_ZTUdVwi2kc.jpg', 4, 4, '{}', NULL, NULL, '12', '2', '0.00', '0.00', 1, 0),
(104, 'rara room', '5000.00', 'this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room this is a test room', 1, 0, 2, 5, '2020-01-24 06:21:17.414483', 0, '40/hotel_OZ2ogBlZhR.jpg', 40, 6, '{\"adult0\": \"0\"}', NULL, NULL, '16', '5', '5.00', '10.00', 2, 0),
(105, 'Kathmandu Inn', '3500.00', 'some description', 2, 1, 2, 3, '2020-01-26 07:33:30.854938', 0, 'default.png', 23, 4, '{\"adult0\": \"12\"}', 2, '200.00', '16', '5', '0.00', '0.00', 2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelinventory_amenities`
--

CREATE TABLE `hotel_hotelinventory_amenities` (
  `id` int(11) NOT NULL,
  `hotelamenities_id` int(11) NOT NULL,
  `hotelinventory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelinventory_amenities`
--

INSERT INTO `hotel_hotelinventory_amenities` (`id`, `hotelamenities_id`, `hotelinventory_id`) VALUES
(56, 4, 9),
(57, 3, 9),
(60, 4, 12),
(65, 4, 15),
(68, 3, 17),
(72, 4, 18),
(78, 3, 19),
(81, 3, 21),
(88, 3, 20),
(89, 4, 20),
(90, 3, 22),
(91, 4, 23),
(92, 4, 24),
(93, 4, 25),
(94, 3, 25),
(95, 4, 26),
(96, 4, 27),
(97, 4, 28),
(98, 4, 29),
(99, 4, 30),
(100, 4, 31),
(101, 4, 32),
(102, 3, 33),
(103, 3, 34),
(104, 4, 35),
(105, 3, 36),
(106, 4, 37),
(107, 3, 38),
(108, 3, 39),
(109, 4, 40),
(110, 3, 41),
(127, 4, 42),
(128, 3, 42),
(129, 4, 43),
(130, 3, 43),
(133, 4, 45),
(134, 4, 49),
(156, 4, 44),
(157, 3, 44),
(241, 3, 51),
(242, 4, 51),
(243, 5, 51),
(244, 11, 51),
(245, 10, 51),
(246, 9, 51),
(247, 8, 51),
(248, 7, 51),
(249, 6, 51),
(250, 3, 55),
(251, 4, 55),
(252, 5, 55),
(253, 6, 55),
(254, 7, 55),
(255, 8, 55),
(256, 9, 55),
(257, 10, 55),
(258, 11, 55),
(277, 3, 56),
(278, 4, 56),
(279, 5, 56),
(280, 6, 56),
(281, 7, 56),
(282, 8, 56),
(283, 9, 56),
(284, 10, 56),
(285, 11, 56),
(286, 3, 57),
(287, 4, 57),
(288, 5, 57),
(289, 6, 57),
(290, 7, 57),
(291, 8, 57),
(292, 9, 57),
(293, 10, 57),
(294, 11, 57),
(295, 5, 6),
(296, 8, 6),
(297, 11, 6),
(298, 3, 6),
(299, 4, 6),
(300, 6, 6),
(301, 7, 6),
(302, 9, 6),
(303, 10, 6),
(338, 4, 16),
(339, 5, 16),
(340, 6, 16),
(341, 7, 16),
(342, 8, 16),
(343, 11, 16),
(344, 3, 16),
(345, 11, 50),
(346, 10, 50),
(347, 9, 50),
(348, 8, 50),
(349, 7, 50),
(350, 6, 50),
(351, 5, 50),
(352, 4, 50),
(353, 3, 50),
(354, 11, 61),
(355, 10, 61),
(356, 9, 61),
(357, 8, 61),
(358, 7, 61),
(359, 6, 61),
(360, 5, 61),
(361, 4, 61),
(362, 3, 61),
(363, 11, 62),
(364, 10, 62),
(365, 9, 62),
(366, 8, 62),
(367, 7, 62),
(368, 6, 62),
(369, 5, 62),
(370, 4, 62),
(371, 3, 62),
(381, 11, 63),
(382, 10, 63),
(383, 9, 63),
(384, 8, 63),
(385, 7, 63),
(386, 6, 63),
(387, 5, 63),
(388, 4, 63),
(389, 3, 63),
(390, 11, 64),
(391, 10, 64),
(392, 9, 64),
(393, 8, 64),
(394, 7, 64),
(395, 6, 64),
(396, 5, 64),
(397, 4, 64),
(398, 3, 64),
(399, 11, 65),
(400, 10, 65),
(401, 9, 65),
(402, 8, 65),
(403, 7, 65),
(404, 6, 65),
(405, 5, 65),
(406, 4, 65),
(407, 3, 65),
(408, 10, 66),
(409, 9, 66),
(410, 8, 66),
(411, 7, 66),
(412, 6, 66),
(413, 5, 66),
(414, 4, 66),
(415, 3, 66),
(416, 11, 67),
(417, 10, 67),
(418, 9, 67),
(419, 8, 67),
(420, 7, 67),
(421, 6, 67),
(422, 5, 67),
(423, 4, 67),
(424, 3, 67),
(429, 3, 53),
(430, 5, 53),
(431, 6, 53),
(432, 11, 53),
(460, 3, 10),
(461, 5, 10),
(462, 6, 10),
(463, 7, 10),
(464, 8, 10),
(465, 9, 10),
(466, 10, 10),
(467, 11, 10),
(468, 4, 10),
(469, 4, 11),
(470, 5, 11),
(471, 7, 11),
(472, 8, 11),
(473, 9, 11),
(474, 10, 11),
(475, 11, 11),
(476, 3, 11),
(478, 4, 14),
(479, 5, 14),
(480, 7, 14),
(481, 8, 14),
(482, 9, 14),
(483, 11, 14),
(484, 3, 14),
(489, 3, 68),
(490, 5, 68),
(491, 6, 68),
(492, 9, 68),
(499, 11, 77),
(500, 10, 77),
(501, 9, 77),
(502, 8, 77),
(503, 7, 77),
(504, 6, 77),
(505, 5, 77),
(506, 4, 77),
(507, 3, 77),
(508, 11, 78),
(509, 10, 78),
(510, 9, 78),
(511, 8, 78),
(512, 7, 78),
(513, 6, 78),
(514, 5, 78),
(515, 4, 78),
(516, 3, 78),
(517, 3, 80),
(518, 4, 80),
(519, 5, 80),
(520, 6, 80),
(521, 7, 80),
(522, 8, 80),
(523, 9, 80),
(524, 10, 83),
(525, 11, 84),
(526, 7, 86),
(527, 8, 86),
(528, 9, 86),
(529, 10, 86),
(530, 11, 86),
(531, 4, 81),
(532, 5, 81),
(533, 6, 81),
(534, 7, 81),
(535, 8, 81),
(536, 5, 85),
(537, 6, 85),
(538, 7, 85),
(539, 8, 85),
(540, 5, 84),
(541, 6, 84),
(542, 7, 84),
(543, 8, 84),
(544, 5, 83),
(545, 6, 83),
(546, 7, 83),
(547, 8, 83),
(548, 5, 79),
(549, 6, 79),
(550, 7, 79),
(551, 8, 79),
(552, 5, 80),
(553, 6, 80),
(554, 7, 80),
(555, 8, 80),
(565, 11, 89),
(566, 10, 89),
(567, 9, 89),
(568, 8, 89),
(569, 7, 89),
(570, 6, 89),
(571, 5, 89),
(572, 4, 89),
(573, 3, 89),
(574, 11, 90),
(575, 10, 90),
(576, 9, 90),
(577, 8, 90),
(578, 7, 90),
(579, 6, 90),
(580, 5, 90),
(581, 4, 90),
(582, 3, 90),
(592, 5, 7),
(593, 6, 7),
(594, 7, 7),
(595, 8, 7),
(596, 9, 7),
(597, 10, 7),
(598, 11, 7),
(599, 3, 7),
(600, 4, 7),
(601, 3, 72),
(602, 4, 72),
(603, 5, 72),
(604, 6, 72),
(605, 7, 72),
(606, 8, 72),
(607, 9, 72),
(608, 10, 72),
(609, 11, 72),
(610, 3, 73),
(611, 4, 73),
(612, 5, 73),
(613, 6, 73),
(614, 7, 73),
(615, 8, 73),
(616, 9, 73),
(617, 10, 73),
(618, 11, 73),
(619, 3, 13),
(620, 5, 13),
(621, 6, 13),
(622, 7, 13),
(623, 8, 13),
(624, 9, 13),
(625, 10, 13),
(626, 11, 13),
(627, 4, 13),
(628, 3, 69),
(629, 4, 69),
(630, 5, 69),
(631, 6, 69),
(632, 7, 69),
(633, 8, 69),
(634, 9, 69),
(635, 10, 69),
(636, 11, 69),
(637, 3, 70),
(638, 4, 70),
(639, 5, 70),
(640, 6, 70),
(641, 7, 70),
(642, 8, 70),
(643, 9, 70),
(644, 10, 70),
(645, 11, 70),
(646, 3, 71),
(647, 4, 71),
(648, 5, 71),
(649, 6, 71),
(650, 7, 71),
(651, 8, 71),
(652, 9, 71),
(653, 10, 71),
(654, 11, 71),
(655, 3, 8),
(656, 4, 8),
(657, 5, 8),
(658, 6, 8),
(659, 7, 8),
(660, 8, 8),
(661, 9, 8),
(662, 10, 8),
(663, 11, 8),
(664, 3, 74),
(665, 4, 74),
(666, 5, 74),
(667, 6, 74),
(668, 7, 74),
(669, 8, 74),
(670, 9, 74),
(671, 10, 74),
(672, 11, 74),
(673, 4, 5),
(674, 5, 5),
(675, 7, 5),
(676, 8, 5),
(677, 10, 5),
(678, 11, 5),
(679, 3, 5),
(680, 6, 5),
(681, 9, 5),
(682, 3, 75),
(683, 4, 75),
(684, 5, 75),
(685, 6, 75),
(686, 7, 75),
(687, 8, 75),
(688, 9, 75),
(689, 10, 75),
(690, 11, 75),
(691, 3, 82),
(692, 4, 82),
(693, 5, 82),
(694, 6, 82),
(695, 7, 82),
(696, 8, 82),
(697, 9, 82),
(698, 10, 82),
(699, 11, 82),
(700, 3, 76),
(701, 4, 76),
(702, 5, 76),
(703, 6, 76),
(704, 7, 76),
(705, 8, 76),
(706, 9, 76),
(707, 10, 76),
(708, 11, 76),
(709, 3, 87),
(710, 4, 87),
(711, 5, 87),
(712, 6, 87),
(713, 7, 87),
(714, 8, 87),
(715, 9, 87),
(716, 10, 87),
(717, 11, 87),
(718, 3, 94),
(719, 4, 94),
(720, 5, 94),
(721, 6, 94),
(722, 7, 94),
(723, 8, 94),
(724, 9, 94),
(725, 10, 94),
(726, 11, 94),
(727, 3, 95),
(728, 4, 95),
(729, 5, 95),
(730, 6, 95),
(731, 7, 95),
(732, 8, 95),
(733, 9, 95),
(734, 10, 95),
(735, 11, 95),
(736, 3, 96),
(737, 4, 96),
(738, 5, 96),
(739, 6, 96),
(740, 7, 96),
(741, 8, 96),
(742, 9, 96),
(743, 10, 96),
(744, 11, 96),
(745, 3, 97),
(746, 4, 97),
(747, 5, 97),
(748, 6, 97),
(749, 7, 97),
(750, 8, 97),
(751, 9, 97),
(752, 10, 97),
(753, 11, 97),
(754, 3, 99),
(755, 4, 99),
(756, 5, 99),
(757, 6, 99),
(758, 7, 99),
(759, 8, 99),
(760, 9, 99),
(761, 10, 99),
(762, 11, 99),
(763, 3, 98),
(764, 4, 98),
(765, 5, 98),
(766, 6, 98),
(767, 7, 98),
(768, 8, 98),
(769, 9, 98),
(770, 10, 98),
(771, 11, 98),
(772, 11, 100),
(773, 10, 100),
(774, 9, 100),
(775, 8, 100),
(776, 7, 100),
(777, 6, 100),
(778, 5, 100),
(779, 4, 100),
(780, 3, 100),
(781, 11, 101),
(782, 10, 101),
(783, 8, 101),
(784, 7, 101),
(785, 6, 101),
(786, 5, 101),
(787, 4, 101),
(788, 3, 101),
(789, 3, 88),
(790, 4, 88),
(791, 5, 88),
(792, 6, 88),
(793, 7, 88),
(794, 8, 88),
(795, 9, 88),
(796, 10, 88),
(797, 11, 88),
(798, 11, 104),
(799, 10, 104),
(800, 9, 104),
(801, 8, 104),
(802, 7, 104),
(803, 6, 104),
(804, 5, 104),
(805, 4, 104),
(806, 3, 104),
(809, 9, 105),
(810, 6, 105);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelinventory_roomfeatures`
--

CREATE TABLE `hotel_hotelinventory_roomfeatures` (
  `id` int(11) NOT NULL,
  `hotelinventory_id` int(11) NOT NULL,
  `hotelroomfeature_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelinventory_roomfeatures`
--

INSERT INTO `hotel_hotelinventory_roomfeatures` (`id`, `hotelinventory_id`, `hotelroomfeature_id`) VALUES
(46, 9, 2),
(47, 9, 1),
(50, 12, 1),
(55, 15, 2),
(58, 17, 2),
(61, 18, 1),
(65, 19, 2),
(67, 21, 1),
(71, 20, 2),
(72, 22, 1),
(73, 23, 1),
(74, 24, 1),
(75, 25, 2),
(76, 26, 2),
(77, 27, 1),
(78, 28, 2),
(79, 29, 1),
(80, 30, 1),
(81, 31, 1),
(82, 32, 1),
(83, 33, 1),
(84, 34, 1),
(85, 35, 2),
(86, 36, 1),
(87, 37, 1),
(88, 38, 1),
(89, 39, 1),
(90, 40, 1),
(91, 41, 1),
(105, 42, 2),
(106, 42, 1),
(107, 43, 2),
(108, 43, 1),
(110, 45, 2),
(111, 49, 2),
(112, 49, 1),
(130, 44, 2),
(154, 52, 1),
(164, 51, 3),
(165, 51, 4),
(166, 51, 2),
(167, 51, 1),
(168, 55, 1),
(169, 55, 2),
(170, 55, 3),
(171, 55, 4),
(180, 56, 1),
(181, 56, 2),
(182, 56, 3),
(183, 56, 4),
(184, 57, 1),
(185, 57, 2),
(186, 57, 3),
(187, 57, 4),
(188, 6, 3),
(189, 6, 4),
(190, 6, 1),
(191, 6, 2),
(203, 16, 1),
(204, 16, 2),
(205, 16, 3),
(206, 16, 4),
(207, 50, 3),
(208, 50, 4),
(209, 50, 1),
(210, 50, 2),
(211, 61, 2),
(212, 61, 3),
(213, 61, 4),
(214, 62, 1),
(215, 62, 2),
(216, 62, 3),
(217, 62, 4),
(222, 63, 1),
(223, 63, 2),
(224, 63, 3),
(225, 63, 4),
(226, 64, 1),
(227, 64, 2),
(228, 64, 4),
(229, 65, 2),
(230, 65, 3),
(231, 65, 4),
(232, 66, 1),
(233, 66, 2),
(234, 66, 3),
(235, 66, 4),
(236, 67, 1),
(237, 67, 2),
(238, 67, 3),
(239, 67, 4),
(242, 53, 2),
(243, 53, 3),
(257, 10, 3),
(258, 10, 1),
(259, 11, 2),
(260, 11, 3),
(261, 11, 4),
(262, 11, 1),
(264, 14, 3),
(265, 14, 4),
(266, 14, 1),
(268, 68, 2),
(271, 77, 1),
(272, 77, 2),
(273, 77, 3),
(274, 77, 4),
(275, 78, 1),
(276, 78, 2),
(277, 78, 3),
(278, 78, 4),
(283, 83, 1),
(284, 83, 1),
(285, 83, 2),
(286, 83, 1),
(287, 85, 2),
(288, 85, 1),
(289, 79, 2),
(290, 79, 1),
(293, 81, 2),
(294, 81, 1),
(297, 86, 2),
(298, 86, 1),
(299, 84, 2),
(300, 84, 1),
(303, 83, 2),
(304, 83, 1),
(305, 85, 2),
(306, 85, 1),
(307, 80, 2),
(308, 80, 1),
(313, 89, 1),
(314, 89, 2),
(315, 89, 3),
(316, 89, 4),
(317, 90, 1),
(318, 90, 2),
(319, 90, 3),
(320, 90, 4),
(325, 7, 1),
(326, 7, 3),
(327, 7, 4),
(328, 7, 2),
(329, 72, 1),
(330, 72, 2),
(331, 72, 3),
(332, 72, 4),
(333, 73, 1),
(334, 73, 2),
(335, 73, 3),
(336, 73, 4),
(337, 13, 1),
(338, 13, 3),
(339, 13, 4),
(340, 13, 2),
(341, 69, 1),
(342, 69, 2),
(343, 69, 3),
(344, 69, 4),
(345, 70, 1),
(346, 70, 2),
(347, 70, 3),
(348, 70, 4),
(349, 71, 1),
(350, 71, 2),
(351, 71, 3),
(352, 71, 4),
(353, 8, 1),
(354, 8, 2),
(355, 8, 3),
(356, 8, 4),
(357, 74, 1),
(358, 74, 2),
(359, 74, 3),
(360, 74, 4),
(361, 5, 1),
(362, 5, 3),
(363, 5, 4),
(364, 5, 2),
(365, 75, 1),
(366, 75, 2),
(367, 75, 3),
(368, 75, 4),
(369, 82, 1),
(370, 82, 1),
(371, 82, 2),
(372, 82, 2),
(373, 76, 2),
(374, 76, 1),
(375, 87, 1),
(376, 87, 2),
(377, 87, 3),
(378, 87, 4),
(379, 94, 1),
(380, 94, 2),
(381, 94, 3),
(382, 94, 4),
(383, 95, 1),
(384, 95, 2),
(385, 95, 3),
(386, 95, 4),
(387, 96, 1),
(388, 96, 2),
(389, 96, 3),
(390, 96, 4),
(391, 97, 1),
(392, 97, 2),
(393, 97, 3),
(394, 97, 4),
(399, 99, 1),
(400, 99, 2),
(401, 99, 3),
(402, 99, 4),
(403, 98, 1),
(404, 98, 1),
(405, 98, 1),
(406, 98, 2),
(407, 100, 1),
(408, 100, 2),
(409, 100, 3),
(410, 100, 4),
(411, 101, 1),
(412, 101, 2),
(413, 101, 3),
(414, 101, 4),
(415, 88, 1),
(416, 88, 2),
(417, 88, 3),
(418, 88, 4),
(419, 104, 4),
(420, 104, 3),
(421, 104, 2),
(422, 104, 1),
(424, 105, 2);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelinventory_roomtype`
--

CREATE TABLE `hotel_hotelinventory_roomtype` (
  `id` int(11) NOT NULL,
  `hotelinventory_id` int(11) NOT NULL,
  `hotelroomtype_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelinventory_roomtype`
--

INSERT INTO `hotel_hotelinventory_roomtype` (`id`, `hotelinventory_id`, `hotelroomtype_id`) VALUES
(35, 9, 1),
(38, 12, 1),
(43, 15, 1),
(44, 17, 1),
(47, 18, 1),
(51, 19, 1),
(53, 21, 1),
(57, 20, 1),
(58, 22, 1),
(59, 23, 1),
(60, 24, 1),
(61, 25, 1),
(62, 27, 1),
(63, 28, 1),
(64, 29, 1),
(65, 30, 1),
(66, 31, 1),
(67, 32, 1),
(68, 33, 1),
(69, 34, 1),
(70, 35, 1),
(71, 36, 1),
(72, 37, 1),
(73, 38, 1),
(74, 39, 1),
(75, 40, 1),
(76, 41, 1),
(90, 43, 1),
(92, 45, 1),
(93, 49, 1),
(111, 44, 1),
(132, 52, 1),
(140, 59, 1),
(141, 60, 1),
(144, 51, 1),
(145, 55, 3),
(148, 56, 1),
(149, 57, 1),
(150, 6, 13),
(156, 16, 4),
(157, 50, 1),
(158, 61, 12),
(159, 62, 11),
(160, 62, 10),
(162, 63, 6),
(163, 64, 12),
(164, 65, 13),
(165, 66, 12),
(166, 66, 10),
(167, 67, 12),
(170, 54, 1),
(175, 53, 1),
(180, 10, 1),
(181, 11, 1),
(183, 14, 1),
(185, 68, 1),
(188, 77, 12),
(189, 78, 13),
(191, 89, 4),
(192, 90, 11),
(194, 7, 12),
(195, 13, 1),
(196, 8, 1),
(197, 5, 1),
(198, 87, 3),
(199, 94, 2),
(200, 95, 3),
(201, 96, 5),
(202, 97, 6),
(203, 99, 2),
(204, 98, 4),
(205, 100, 13),
(206, 101, 14),
(207, 102, 13),
(208, 88, 4),
(209, 104, 13),
(210, 104, 12),
(212, 105, 11);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotellanguagemiddle`
--

CREATE TABLE `hotel_hotellanguagemiddle` (
  `id` int(11) NOT NULL,
  `hotels_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotellanguagemiddle`
--

INSERT INTO `hotel_hotellanguagemiddle` (`id`, `hotels_id`, `language_id`) VALUES
(18, 21, 1),
(19, 21, 2),
(28, 22, 1),
(29, 22, 2),
(37, 24, 1),
(38, 25, 1),
(39, 26, 2),
(40, 27, 2),
(41, 28, 1),
(47, 5, 1),
(48, 5, 2),
(50, 29, 1),
(53, 3, 1),
(54, 3, 2),
(55, 16, 1),
(56, 16, 2),
(59, 37, 1),
(60, 37, 2),
(61, 39, 2),
(62, 40, 2),
(63, 23, 1),
(64, 23, 2),
(65, 4, 1),
(66, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotellog`
--

CREATE TABLE `hotel_hotellog` (
  `id` int(11) NOT NULL,
  `logs` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelowner`
--

CREATE TABLE `hotel_hotelowner` (
  `name` varchar(80) DEFAULT NULL,
  `contact` bigint(20) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `current_hotel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelreview`
--

CREATE TABLE `hotel_hotelreview` (
  `id` int(11) NOT NULL,
  `rating` double NOT NULL,
  `review` longtext NOT NULL,
  `user_id_id` int(11) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  `inventory_id` int(11) DEFAULT NULL,
  `module` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelreview`
--

INSERT INTO `hotel_hotelreview` (`id`, `rating`, `review`, `user_id_id`, `company_id`, `inventory_id`, `module`) VALUES
(2, 3, 'We had a rat in our room and poo all over our stuff. Also manager using private information (from booking reservation) to look for the place we live and work, we thought that was creepy. The manager’s verbal word of refund did not occur and we were fully charged after the fact upon returning home, not cool!', 82, 5, 6, 'travel_tour'),
(3, 3, 'We had a rat in our room and poo all over our stuff. Also manager using private information (from booking reservation) to look for the place we live and work, we thought that was creepy. The manager’s verbal word of refund did not occur and we were fully charged after the fact upon returning home, not cool!', 82, 5, 7, 'hotel'),
(11, 4, 'It is a good period of staying at this wonderful hotel. My birthday was during my stay at the Grand Majestic Plaza hotel. It was surprising to me I received a bottle of champagne for the gift from the hotel. Thank you very much.', 82, 4, 89, 'hotel'),
(12, 5, 'It is a good period of staying at this wonderful hotel. My birthday was during my stay at the Grand Majestic Plaza hotel. It was surprising to me I received a bottle of champagne for the gift from the hotel. Thank you very much.', 82, 4, 90, 'hotel'),
(14, 3, 'It is a good period of staying at this wonderful hotel. My birthday was during my stay at the Grand Majestic Plaza hotel. It was surprising to me I received a bottle of champagne for the gift from the hotel. Thank you very much.', 82, 4, 90, 'hotel'),
(15, 2, 'It is a good period of staying at this wonderful hotel. My birthday was during my stay at the Grand Majestic Plaza hotel. It was surprising to me I received a bottle of champagne for the gift from the hotel. Thank you very much.', 82, 4, 103, 'hotel'),
(16, 5, 'It is a good period of staying at this wonderful hotel. My birthday was during my stay at the Grand Majestic Plaza hotel. It was surprising to me I received a bottle of champagne for the gift from the hotel. Thank you very much.', 82, 4, 89, 'hotel');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelroomfeature`
--

CREATE TABLE `hotel_hotelroomfeature` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelroomfeature`
--

INSERT INTO `hotel_hotelroomfeature` (`id`, `name`) VALUES
(1, 'Ocean View'),
(2, 'SUNRISE VIEW'),
(3, 'Mountain View Room'),
(4, 'lake side room view');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelroomtype`
--

CREATE TABLE `hotel_hotelroomtype` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelroomtype`
--

INSERT INTO `hotel_hotelroomtype` (`id`, `name`) VALUES
(1, 'Double'),
(2, 'Single'),
(3, 'Triple'),
(4, 'Quad'),
(5, 'Queen'),
(6, 'King'),
(7, 'Twin'),
(8, 'Double-double'),
(9, 'Studio:'),
(10, 'Master Suite'),
(11, 'Mini-Suite or Junior Suite'),
(12, 'Connecting rooms'),
(13, 'Adjoining rooms'),
(14, 'Adjacent rooms');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotels`
--

CREATE TABLE `hotel_hotels` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `number_of_room` int(11) NOT NULL,
  `number_of_staff` int(11) NOT NULL,
  `wordsbyowner` longtext NOT NULL,
  `description` longtext,
  `is_active` tinyint(1) NOT NULL,
  `image` varchar(500) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `owner_id_id` int(11) NOT NULL,
  `star_rating` varchar(40) NOT NULL,
  `check_in` time(6) DEFAULT NULL,
  `check_out` time(6) DEFAULT NULL,
  `rateforforeign` decimal(10,2) DEFAULT NULL,
  `ratefornepali` decimal(10,2) DEFAULT NULL,
  `rateforsaarc` decimal(10,2) DEFAULT NULL,
  `estd_date` varchar(60) DEFAULT NULL,
  `cino` varchar(60) DEFAULT NULL,
  `cname` varchar(60) DEFAULT NULL,
  `nameonpancard` varchar(60) DEFAULT NULL,
  `pannumber` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotels`
--

INSERT INTO `hotel_hotels` (`id`, `name`, `number_of_room`, `number_of_staff`, `wordsbyowner`, `description`, `is_active`, `image`, `created_at`, `owner_id_id`, `star_rating`, `check_in`, `check_out`, `rateforforeign`, `ratefornepali`, `rateforsaarc`, `estd_date`, `cino`, `cname`, `nameonpancard`, `pannumber`) VALUES
(3, 'Hyatt Regency Kathmandu', 21, 12, 'Nice and big room, clean and well supplied. Food and beverage from very good quality and a lot of choice. Perfect pool for people in need of exercise. Gym and spa center offering the necessary for the customers. Hotel well situated, with shuttle to the city center. Staff providing all the info required to go...', 'Hyatt Regency Kathmandu is a five-star luxury hotel and resort in Kathmandu,  set on 37 acres of landscaped grounds and created in the traditional Newari style of Nepalese architecture. This beautiful hotel and resort is located on the road to the Boudhanath Stupa: the most holy of all Tibetan Buddhist shrines outside of Tibet and a UNESCO World Heritage Site located within a five-minute walk from the hotel. The hotel is just four kilometres (2.4 miles) from the Tribhuvan International Airport and six kilometres (3.7 miles) from the city center of Kathmandu.', 1, 'IMG_0221_yc5kuV2.jpg', '2019-04-22 10:46:52.668059', 8, '5 Star', '05:22:00.000000', '07:28:00.000000', NULL, NULL, NULL, '1991-12-12', '1234567', 'Hyatt', 'hyatt', '123456789'),
(4, 'Kathmandu Marriott Hotel', 5, 2, 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their room. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 'Experience Nepal\'s historic capital city from the elevated comfort of Fairfield by Marriott Kathmandu. Impeccably located in Thamel, Kathmandu\'s most vibrant and buzz-worthy area, our hotel offers everything travelers need for a productive and relaxing stay. Easily tour noteworthy attractions like Pashupathinath Temple, Swayambhunath Stupa and Garden of Dreams, all of which are located close to our hotel. After a busy day of sightseeing, retreat to our inviting guest rooms, which boast luxury amenities, plush bedding, complimentary high-speed Wi-Fi and 24-hour room service. Dine anytime at Kava, which showcases a tempting breakfast buffet, or get your heart rate pumping at our on-site fitness center. For those seeking business facilities, find flexible meeting room space and modern amenities in the heart of Thamel. Come discover the many sides of Nepal\'s most wondrous city at Fairfield by Marriott Kathmandu.', 0, 'FB_IMG_1531726262058.jpg', '2019-04-22 11:01:37.202623', 4, '2 Star', '05:32:00.000000', '05:22:00.000000', '15.00', '0.00', '10.00', '2019-01-01', '12345678', 'patan dhoka hotel', 'patan dhoka hotel', '124509381'),
(5, 'Hotel Annapurna', 12, 4, 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their room. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their room. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 1, '12.jpg', '2019-04-22 11:14:58.804914', 4, 'Tourist Standard', '06:00:00.000000', '00:09:00.000000', '15.00', '0.00', '10.00', '2019-01-01', '123456', 'Hotel Annapurna', 'Hotel Annapurna', '123456789'),
(16, 'Baber Mahal Vilas The Boutique Hotel', 500, 2, 'The vision behind the boutique property is to create a hospitality model where in, luxury and service are provided in a historically and culturally significant ambience in the center Kathmandu Valley. To host our guests in an atmosphere that illustrates the grand lifestyle of the Rana era mixed with the original architectural heritage of Newar, Mustang and Terai cultures. Though modest in size the property is attached to BABER MAHAL REVISITED complex. Acting as an extension to the Vilas, Revisited offers a host of shops offering quality traditional products, and some of the finest dining options in the city.', 'A hotel is an establishment that provides paid lodging on a short-term basis. ... Hotel rooms are usually numbered (or named in some smaller hotels and B&Bs) to allow guests to identify their rooms. Some boutique, high-end hotels have custom decorated rooms. Some hotels offer meals as part of a room and board arrangement', 1, '12_ewZPhD8.jpg', '2019-04-25 12:08:43.076561', 8, '7 Star', '04:00:00.000000', '14:00:00.000000', '15.00', '0.00', '10.00', '1991-11-11', '1234567', 'Baber', 'None', '12345678'),
(18, 'Tiger Palace ResortHotel Pokhara Grande', 85, 82, 'Pokhara Grande is the ideal retreat for the nature lovers seeking style and authenticity in panoramic and adventurous city of Pokhara. Discover the perfect blend of nature and comfort. Pokhara Grande is situated at the crossroad of Pokhara, an easy walk or bicycle ride to the sights, restaurants, market and Phewa Lake – but away from the hustle and bustle.', 'Pokhara Grande is the five star hotel of Pokhara, Nepal providing the right blend of service, luxury and quiet efficiency. Internationally acclaimed for all-round excellence and unparalleled levels of service, we have got our name listed among 10 best hotels of Nepal.', 0, 'hotel_visitors_inn_14PXBrT.jpg', '2019-05-02 05:46:36.736726', 8, 'Tourist Standard', '11:11:00.000000', '12:12:00.000000', '15.00', '0.00', '10.00', '1991-12-12', NULL, NULL, NULL, NULL),
(19, 'The Pavilions Himalayas', 12, 12, 'From the moment we decided to open The Pavilions Himalayas, we had the mission that it would be an example to our team, our guests and the local community. While it would be a unique luxurious back-to-nature experience, it had to be sustainable and without detriment to the surrounding area.', 'Our ultimate objective is that The Pavilions Himalayas is a social business where we provide a large majority of our net profits to our various social activities which the co owner\'s Douglas and Insuba have been engaged in collectively for the past twenty years.', 1, 'Best-Places-to-Visit-in-Pokhara-1024x540.jpg', '2019-05-02 05:46:49.918014', 8, '4 Star', '10:40:00.000000', '09:35:00.000000', NULL, NULL, NULL, '2010-12-12', '1234567', 'The pavilions', 'None', '123456780'),
(20, 'Meghauli Serai, A Taj Safari', 82, 83, 'The lodge embraces local décor and aesthetics with an abundant use of local art and artefacts. The large Newari door leading to the lobby has been procured from a local Tharu village. A large infinity pool with a viewing deck and a ‘machan’ over the river for private dining and wildlife viewing add to the charm of this jungle lodge at Chitwan.', 'Standing on the banks of the river Rapti, Meghauli Serai overlooks a vast expanse of rippling waters and the core of Chitwan National Park. This 30 room lodge is designed to showcase the spectacular wilderness and rooms as well as guest areas afford uninterrupted views of the jungle. The main lounge with an imposing chandelier made with 10,000 Nepalese hand painted beads. The lodge embraces local décor and aesthetics with an abundant use of local art and artefacts. The large Newari door leading to the lobby has been procured from a local Tharu village. A large infinity pool with a viewing deck and a ‘machan’ over the river for private dining and wildlife viewing add to the charm of this jungle lodge at Chitwan.', 1, 'Meghaul-Serai.jpg', '2019-05-03 05:37:55.748180', 8, '7 Star', '09:32:00.000000', '09:33:00.000000', '15.00', '0.00', '10.00', '1999-12-12', 'None', 'Meghauli Serai Pvt. Ltd', 'None', 'None'),
(23, 'Hotel threestar', 15, 24, 'During the 15th century, the valley disintegrated into the three kingdoms of Kathmandu, Lalitpur and Bhaktapur. This disintegration led to the creation of a Durbar Square (palatial complexes) in each of the cities and remains emblematic of the rich architectural traditions that existed in the valley. Durbar squares, temple squares, sacred courtyards, stupas, open air shrines, dance platforms, sunken water fountains, public rest houses, bazaars, multi-storied houses with elaborate carved windows and compact streets are the characteristics of the traditional design of towns.', 'People have settled in the Kathmandu Valley for over 2000 years. Throughout this period, the valley has witnessed the migration of people from the high plateaus of Tibet, the fertile plains of the Ganges, and everywhere between. This intermingling of people and cultures created a vibrant and diverse society within the valley. By the 12th century, the inhabitants of the Kathmandu Valley had developed a unique civilisation indigenous to the region and were known throughout the region as the Newars. They shared – and continue to share – a linguistic and cultural community bound together by a common language and culture called Newari.\r\n\r\nNewari civilisation flourished during the reign of the Malla Kings from the 12th to the 18th century. The Malla Kings profited from being a major destination along the trade route between India and Tibet, and invested heavily in their arts and culture. Part of the valley’s exports included skilled craftsmen like sculptors, painters and carvers to India and Tibet. Together, the wood works contain the centuries of love and dedication that these craftsmen had towards this artistic tradition.', 0, 'Dubai-skyline_16d7de0fdce_large.jpeg', '2019-06-13 06:57:14.748470', 6, '4 Star', '11:00:00.000000', '14:00:00.000000', NULL, NULL, NULL, '1991-12-12', '23456789', 'threestar', 'Dawrikathreestar', '1234567890'),
(29, 'Hotel Everest', 55, 120, 'The Everest Hotel is named after the world\'s highest peak Mt. Everest or Sagarmatha in the Nepali language.  The given name is also means the ‘roof of the world’ and the history that is embedded in Nepal\'s rich cultural and religious heritage. The Everest Hotel is a fantastic combination of international standards with Nepali hospitality, situated in the new city center of the capital, Kathmandu just 3 kilometers away from the Tribhuwan Intl. Airport. The Everest Hotel is ever ready to cater to the needs of its diverse categories of guests, dismissing all notions that business and pleasure cannot be mixed.', 'The Everest Hotel is named after the world\'s highest peak Mt. Everest or Sagarmatha in the Nepali language.  The given name is also means the ‘roof of the world’ and the history that is embedded in Nepal\'s rich cultural and religious heritage. The Everest Hotel is a fantastic combination of international standards with Nepali hospitality, situated in the new city center of the capital, Kathmandu just 3 kilometers away from the Tribhuwan Intl. Airport. The Everest Hotel is ever ready to cater to the needs of its diverse categories of guests, dismissing all notions that business and pleasure cannot be mixed.', 1, 'UcRbT_Untitled-1.jpg', '2019-10-02 06:00:37.791802', 81, '5 Star', '12:00:00.000000', '13:00:00.000000', NULL, NULL, NULL, '1991-10-10', '456862900', 'Hotel Everest Pvt Ltd.', 'Hotel Everest Pvt Ltd.', '606862900'),
(30, 'Hotel Yak & Yeti\n', 15, 12, 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 1, 'Dubai-skyline_16d7de0fdce_large.jpeg', '2019-10-18 04:18:15.177937', 10, '3 Star', '00:00:00.000000', '13:00:00.000000', NULL, NULL, NULL, '2018-12-12', '12344678', 'None', 'Fewa taal Hotel', '123456789'),
(31, 'Shangri-La Hotel Kathmandu', 13, 12, 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 1, 'images.jpeg', '2019-10-18 07:13:04.175413', 10, '1 Star', '00:00:00.000000', '13:00:00.000000', NULL, NULL, NULL, '2018-12-12', 'None', 'None', 'None', 'None'),
(32, 'Hotel Ambassdor', 13, 14, 'The Ambassador\'s journey started in 1963 as a residential bungalow converted into a ten room hotel. The Ambassador now stands tall at the center of Kathmandu but, while the building may be new, it still carries the legacy of providing guests with an unparalleled hospitality experience for an unprecedented value.', 'The Ambassador is a four-star hotel at the heart of Kathmandu. Located in one the most vibrant areas of Kathmandu (Lazimpat), it is an ideal choice for guests who want to experience everything great that the city has to offer, without having to venture too far. Within walking distance of the buzzing alleys of Thamel and the upmarket shopping boulevard,..', 1, 'IMG_0216.jpg', '2019-10-20 07:44:14.257098', 10, '3 Star', '00:00:00.000000', '13:00:00.000000', NULL, NULL, NULL, '2018-12-11', 'None', 'None', 'None', 'None'),
(33, 'Yellow Pagoda Hotel', 12, 4, 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 1, 'hotel.jpg', '2019-10-20 14:18:08.049727', 10, '1 Star', '12:00:00.000000', '13:00:00.000000', NULL, NULL, NULL, '2019-01-01', 'Non', 'None', 'None', 'None'),
(34, 'Scorpio Hotel', 12, 13, 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 'Winner of the Pacific Asia Travel Association (PATA) Heritage Award, EDEN Hotel is inspired by Kathmandu Valley’s rich cultural heritage. It features an outdoor pool and 4 food and beverage options.\r\n\r\nFeaturing an extensive collection of artefacts from the 13th century, EDEN Hotel is modelled after the palaces of Newar Kings. Pashupatinath Temple is 500 m away while Kathmandu International Airport and the Buddhist site of Boudhanath are both 2 km from the hotel. Durbar Marg Street is 5 km away.\r\n\r\nThe air-conditioned rooms, which are equipped with a satellite TV and seating area. Private bathroom comes with a bathtub, shower and free toiletries.\r\n\r\nRecreation facilities available include massage services and a spa. A 24-hour reception welcomes guests. Free private parking is provided.\r\n\r\nGuests can choose to dine at Krishnarpan, which specialises in local cuisine. The hotel also serves Japanese dishes at Mako’s and Continental dishes at Toran. Local and international drinks can be ordered from Fusion Bar.\r\n\r\nCouples particularly like the location — they rated it 8.7 for a two-person trip.\r\n\r\nWe speak your language!', 1, '12_OLKr7wK.jpg', '2019-10-21 06:30:22.018407', 10, 'Tourist Standard', '00:00:00.000000', '12:00:00.000000', NULL, NULL, NULL, '2019-01-15', 'None', 'None', 'None', 'None'),
(35, 'Jurassic Resort & Villas', 12, 14, 'Jurassic is positioned to provide an integrated experience of comfort, luxury, recreation, spa, adventure and so much more promising a concept of leisure and recreation, redefined. Hidden away from hustling and bustling, busy city it is just a 20 minute drive away from the domestic airport. The resort amenities, facilities and the scenic beauty seen from the resort will make you feel like you are in a different world.', 'Jurassic resort is a perfect place to relax and indulge yourself if you wish to have a top-end stay in Nepal. The resort is a unique spot right above Pokhara city which opens divine 360 degree view on the surroundings.  The Jurassic hill features a mixed forest and a large park with wide number of rare plants and extraordinary installations.The breathtaking view of Annapurna mountain range, calm green water of Fewa lake and Pokhara city top up to the unparalleled beauty of the place.', 1, '12_QmR9BGD.jpg', '2019-10-22 05:02:47.611567', 10, 'Tourist Standard', '12:00:00.000000', '13:00:00.000000', NULL, NULL, NULL, '2013-01-01', 'None', 'None', 'None', 'None'),
(36, 'Radisson Hotel Kathmandu', 16, 12, 'Situated near several embassies and consulates, the Radisson offers attractive event space in the quiet Lazimpat section of Kathmandu. Plan a rooftop birthday celebration at The Terrace Garden, or host a conference in Begnas Hall. Along with free Wi-Fi and on-site catering options, our seven flexible meeting rooms can turn any occasion into a memorable moment.', 'Radisson Hotel Kathmandu, located in the heart of Nepal\'s thriving capital, places you close to corporate offices and popular attractions like the entertainment district of Thamel. Once you arrive at Tribhuvan International Airport (KTM), we can transport you in our airport shuttle to the hotel, where you can unwind with a treatment at our Tranquility Spa. Business travellers can also enjoy our Business Class Lounge, perfect for small meet-and-greets accompanied by a two-hour offering of free drinks and assorted snacks.', 1, 'IMG_0216_AFrf4mW.jpg', '2019-10-31 05:43:44.815906', 10, 'Tourist Standard', '13:00:00.000000', '14:00:00.000000', NULL, NULL, NULL, '2018-01-02', 'None', 'None', 'None', 'None'),
(37, 'hotel taj', 5, 12, 'gfrefghjkl', 'this is hotel', 0, 'default.png', '2019-12-30 08:04:12.650406', 111, 'Tourist Standard', '11:11:00.000000', '11:11:00.000000', '40.00', '0.00', '0.00', '2013-01-01', '156781', 'hotel taj', NULL, '23788008765'),
(38, 'makalu', 9, 14, '', 'this is a hotel', 0, 'None/hotel_LxB0ZcPpMm.jpg', '2019-12-30 08:18:49.757990', 111, 'Tourist Standard', '14:00:00.000000', '09:00:00.000000', NULL, '0.00', '15.00', '2015-02-05', '246815', 'makalu', 'makalu', '469871'),
(39, 'hotel bhadrabas', 11, 12, 'this is hotel bhadrabas ..you can enjoy snowfall every year', 'this is hotel bhadrabas', 0, 'None/hotel_j0fjySUeMT.png', '2020-01-19 10:20:25.291788', 4, 'Tourist Standard', '11:11:00.000000', '11:11:00.000000', NULL, '0.00', NULL, '1991-12-31', '123456789', 'bhadrabas', 'Rajkumar', '123456789'),
(40, 'Dwarika Hotel', 12, 12, 'this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd', 'this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd this is tesst data for Dwarika Hotel Pvt Ltd', 0, 'None/hotel_SRFoPXJXzI.jpeg', '2020-01-24 06:06:49.814836', 6, '2 Star', '00:12:00.000000', '00:12:00.000000', NULL, '0.00', NULL, '2017-11-16', '123456', 'Dwarika Hotel Pvt Ltd', 'Dwarika Hotel Pvt Ltd', '123456789');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelsnew`
--

CREATE TABLE `hotel_hotelsnew` (
  `id` int(11) NOT NULL,
  `oldhotelid` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `number_of_room` int(11) NOT NULL,
  `number_of_staff` int(11) NOT NULL,
  `wordsbyowner` longtext NOT NULL,
  `description` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `owner_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_hotelsnew`
--

INSERT INTO `hotel_hotelsnew` (`id`, `oldhotelid`, `name`, `number_of_room`, `number_of_staff`, `wordsbyowner`, `description`, `is_active`, `image`, `created_at`, `owner_id_id`) VALUES
(10, 3, 'Ricardo McKinney', 2, 2, 'some words', 'some description about hotel', 0, 'holiday-inn_6ow0OMe.jpeg', '2019-05-01 04:59:00.622113', 8),
(11, 3, 'Ricardo McKinney123', 2, 2, 'some words123', 'some description about hotel123', 0, 'holiday-inn_F35X5TD.jpeg', '2019-05-01 05:03:06.789924', 8);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_hotelstaff`
--

CREATE TABLE `hotel_hotelstaff` (
  `name` varchar(80) DEFAULT NULL,
  `contact` bigint(20) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `hotel_id` int(11) DEFAULT NULL,
  `owner_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `hotel_inventorygallery`
--

CREATE TABLE `hotel_inventorygallery` (
  `id` int(11) NOT NULL,
  `image` varchar(500) NOT NULL,
  `title` varchar(200) NOT NULL,
  `hotel_inventory_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_inventorygallery`
--

INSERT INTO `hotel_inventorygallery` (`id`, `image`, `title`, `hotel_inventory_id_id`) VALUES
(18, '178848583_dioskri.jpg', 'building', 5),
(19, '178371930_Ri6Z9AH.jpg', 'gym', 5),
(20, '5/hotel_PtDEhCePvP.jpg', 'bathroom', 6),
(21, '178528489.jpg', 'GYM', 7),
(22, 'IMG_0279_mECxu9O.jpg', 'Hotel', 8),
(23, 'dining_BzGVPqQ.jpg', 'Front view', 53),
(24, 'deluxe_room_EtOohg6.jpg', 'Family Table', 53),
(25, 'FB_IMG_1525275052967_XYag3Lv.jpg', 'asd', 55),
(26, '6.jpg', 'bedroom', 56),
(27, '2.jpg', 'balcony', 57),
(28, 'Screenshot_1_7wzXxUT.png', 'Bedroom', 59),
(29, 'FB_IMG_1525275052967.jpg', 'wardrops', 16),
(30, 'FB_IMG_1525275056327.jpg', 'kitchen', 16),
(31, 'FB_IMG_1525275082186.jpg', 'hall', 16),
(32, 'FB_IMG_1525777834597.jpg', 'sofa', 16),
(33, 'lobby_a920gVa.jpg', 'lobby', 50),
(34, 'kitchen_w83kRNX.jpg', 'kitchen', 50),
(35, 'such-a-beautiful-stay.jpg', 'restaurant', 61),
(36, 'room.jpg', 'bed', 61),
(37, 'rooms__wYGcbwR.jpg', 'bed', 61),
(38, 'twin_et97gUm.jpg', 'bed', 61),
(39, 'rooms__zv1tXOw.jpg', 'bed', 62),
(40, 'room_dSTE8zO.jpg', 'bed', 62),
(41, 'rooms__LG0qidn.jpg', 'bed', 63),
(42, 'twin_xOjmdMT.jpg', 'bed', 63),
(43, 'IMG_0271_TdGGOr9.jpg', 'wardrops', 64),
(44, 'IMG_0273.jpg', 'bed', 64),
(45, 'IMG_0279.jpg', 'bed', 64),
(46, '178848583_mJ4VM1h.jpg', 'building', 65),
(47, '178371942.jpg', 'room', 65),
(48, '178371930.jpg', 'GYM', 65),
(49, '178371927.jpg', 'BAR', 65),
(50, '1.jpg', 'bed', 66),
(51, '2_qK2RXmB.jpg', 'balcony', 66),
(52, '3.jpg', 'triple Bed', 66),
(53, '4.jpg', 'toilet', 66),
(54, 'IMG_0893.jpg', 'bed', 67),
(56, 'IMG_1024.jpg', 'toilet', 67),
(57, 'IMG_1026.jpg', 'bathroom', 67),
(58, 'IMG_1028.jpg', 'bathroom', 67),
(59, 'IMG_0273_jsG9AWd.jpg', 'bed', 54),
(60, 'IMG_0279_umVDK8m.jpg', 'bed', 54),
(61, 'IMG_0282.jpg', 'bed', 54),
(62, 'IMG_0317.jpg', 'bed', 10),
(63, 'IMG_0320.jpg', 'bed', 10),
(64, 'IMG_0322.jpg', 'bed', 10),
(65, 'IMG_0317_QkXupbJ.jpg', 'bed', 11),
(66, 'IMG_0320_vrNE1ms.jpg', 'bed', 11),
(67, 'IMG_0322_gJog08e.jpg', 'bed', 11),
(68, 'Room-Type-Hollywood-Twin-Room_EiWxiW9.jpg', 'Bed', 68),
(69, '5.jpg', 'bathroom', 14),
(70, '6_B9yW678.jpg', 'bedroom', 14),
(71, '187945991.jpg', 'bed', 77),
(72, '187946005_h5OstYN.jpg', 'bed', 77),
(73, '193843438_03CH6uc.jpg', 'bed', 77),
(74, '187945991_S8RVyNX.jpg', 'bed', 78),
(75, '187946005_zBXItcE.jpg', 'bed', 78),
(76, '193843438_T3pKqGm.jpg', 'bed', 78),
(77, 'rooms__zv1tXOw.jpg', 'bed', 81),
(78, 'room_dSTE8zO.jpg', 'bed', 81),
(79, 'rooms__LG0qidn.jpg', 'bed', 81),
(80, 'twin_xOjmdMT.jpg', 'bed', 81),
(81, 'rooms__zv1tXOw.jpg', 'bed', 82),
(82, 'room_dSTE8zO.jpg', 'bed', 82),
(83, 'rooms__LG0qidn.jpg', 'bed', 82),
(84, 'twin_xOjmdMT.jpg', 'bed', 82),
(85, 'rooms__zv1tXOw.jpg', 'bed', 83),
(86, 'room_dSTE8zO.jpg', 'bed', 83),
(87, 'rooms__LG0qidn.jpg', 'bed', 83),
(88, 'twin_xOjmdMT.jpg', 'bed', 83),
(89, 'rooms__zv1tXOw.jpg', 'bed', 84),
(90, 'room_dSTE8zO.jpg', 'bed', 84),
(91, 'rooms__LG0qidn.jpg', 'bed', 84),
(92, 'twin_xOjmdMT.jpg', 'bed', 84),
(93, 'rooms__zv1tXOw.jpg', 'bed', 85),
(94, 'room_dSTE8zO.jpg', 'bed', 85),
(95, 'rooms__LG0qidn.jpg', 'bed', 85),
(96, 'twin_xOjmdMT.jpg', 'bed', 85),
(97, 'rooms__zv1tXOw.jpg', 'bed', 86),
(98, 'room_dSTE8zO.jpg', 'bed', 86),
(99, 'rooms__LG0qidn.jpg', 'bed', 86),
(100, 'twin_xOjmdMT.jpg', 'bed', 86),
(101, 'rooms__zv1tXOw.jpg', 'bed', 79),
(102, 'room_dSTE8zO.jpg', 'bed', 79),
(103, 'rooms__LG0qidn.jpg', 'bed', 79),
(104, 'twin_xOjmdMT.jpg', 'bed', 79),
(105, 'rooms__zv1tXOw.jpg', 'bed', 80),
(106, 'room_dSTE8zO.jpg', 'bed', 80),
(107, 'rooms__LG0qidn.jpg', 'bed', 80),
(108, 'twin_xOjmdMT.jpg', 'bed', 80),
(109, '4/hotel_sKETbyOWiZ.jpg', 'front view', 88),
(110, '4/hotel_QaOMudOHyS.jpg', 'bed', 88),
(111, '4/hotel_UDliNwx76V.jpg', 'bed', 88),
(112, '4/hotel_fdeAfCDyHM.jpg', 'bathroom', 88),
(113, '4/hotel_zoZ5OdWFqF.jpg', 'front view', 89),
(114, '4/hotel_UQ9LdW7Yhs.jpg', 'bed', 89),
(115, '4/hotel_9yb6IQ9NdH.jpg', 'bed', 89),
(116, '4/hotel_LkttieNrMM.jpg', 'bathroom', 89),
(117, '4/hotel_PLMhRYp10p.jpg', 'front view', 90),
(118, '4/hotel_b3ccE9g9l0.jpg', 'lift', 90),
(119, '4/hotel_iHJR7pamde.jpg', 'bed', 90),
(120, '4/hotel_JcepBdjvhw.jpg', 'bathroom', 90),
(121, '5/hotel_vVxCUIzkH2.jpg', 'bed', 6),
(122, '5/hotel_bTk9y7f3hu.jpg', 'wardrops', 6),
(123, '5/hotel_NPurKsEmjj.jpg', 'Top', 6),
(124, '5/hotel_Euftq1h8OA.jpg', 'front view', 7),
(125, '5/hotel_XbRxvpW6LU.jpg', 'building', 7),
(126, '5/hotel_wAFWwGfXyN.jpg', 'bed', 7),
(127, '5/hotel_7GKw6Qe9dD.jpg', 'bed', 7),
(128, '5/hotel_6uzKCo1VWO.jpg', 'kitchen', 7),
(129, '5/hotel_DLLfNTc536.jpg', 'bed', 72),
(130, '5/hotel_KonrKvxsrv.jpg', 'bathroom', 72),
(131, '5/hotel_7hie0I8I7l.jpg', 'bathroom', 72),
(132, '5/hotel_X12j6cYuLS.jpg', 'wardrops', 72),
(133, '5/hotel_KJQZ1M0Foq.jpg', 'kitchen', 73),
(134, '5/hotel_xDL9TcfVBn.jpg', 'bed', 73),
(135, '5/hotel_ovSSZ1Zsoe.jpg', 'bed', 73),
(136, '5/hotel_GSJrKBpS5E.jpg', 'bathroom', 73),
(137, '3/hotel_0s3vpA1yml.jpg', 'bed', 13),
(138, '3/hotel_pUM1lzHqZZ.jpg', 'front view', 13),
(139, '3/hotel_WzuCfoIBsx.jpg', 'bed', 13),
(140, '3/hotel_PPJKcuv5R5.jpg', 'bathroom', 13),
(141, '3/hotel_P9VQGCEWXE.jpg', 'bathroom', 13),
(142, '3/hotel_YSMPE5lZMh.jpg', 'bed', 13),
(143, '3/hotel_NnxBcU4YTM.jpg', 'bed', 13),
(144, '3/hotel_JmUqvfPFuV.jpg', 'bed', 69),
(145, '3/hotel_DWtkyEfYsZ.jpg', 'kitchen', 69),
(146, '3/hotel_h3gUSGKUEr.jpg', 'bed', 69),
(147, '3/hotel_nNbKyzrMX0.jpg', 'bed', 69),
(148, '3/hotel_nnci8CHHlX.jpg', 'bed', 69),
(149, '3/hotel_ILRrER3lwU.jpg', 'front view', 69),
(150, '3/hotel_kRqg92mJeY.jpg', 'lobby', 70),
(151, '3/hotel_jFWueqrPFn.jpg', 'gym', 70),
(152, '3/hotel_edNZHV2Vg0.jpg', 'bed', 70),
(153, '3/hotel_2OBRLHwfxd.jpg', 'bed', 70),
(154, '3/hotel_KxR35LauMk.jpg', 'bed', 70),
(155, '3/hotel_7W4HWQRjW8.jpg', 'lobby', 70),
(156, '3/hotel_lrqTdlmUSY.jpg', 'GYM', 71),
(157, '3/hotel_ZYSAIoLDMq.jpg', 'front view', 71),
(158, '3/hotel_QrZS4WrOpH.jpg', 'bed', 71),
(159, '3/hotel_ddrosXD3kv.jpg', 'bed', 71),
(160, '3/hotel_jDtZkD6ikF.jpg', 'bed', 71),
(161, '3/hotel_KKk63KeZ8B.jpg', 'POOl', 71),
(162, '3/hotel_mW9hpRNp3Z.jpg', 'bed', 71),
(163, '3/hotel_Ww6Udc2Cav.jpg', 'bed', 74),
(164, '3/hotel_otvqGhfSD8.jpg', 'lobby', 74),
(165, '3/hotel_pd1Jc1DgRh.jpg', 'bed', 74),
(166, '3/hotel_ynlKYYHLmA.jpg', 'kitchen', 74),
(167, '3/hotel_obrrHIR8mp.jpg', 'bed', 74),
(168, '3/hotel_653YyQCdji.jpg', 'Pool', 74),
(169, '16/hotel_qcO2sfAJJx.jpg', 'bed', 75),
(170, '16/hotel_4dgzBoXWsP.jpg', 'Top', 75),
(171, '16/hotel_XMFsGYVfGt.jpg', 'bed', 75),
(172, '16/hotel_AH4OfOax8E.jpg', 'bathroom', 75),
(173, '16/hotel_2bZdtr39j1.jpg', 'bathroom', 75),
(174, '16/hotel_x3Sxiv1AP2.jpg', 'bed', 75),
(175, '16/hotel_NNE6b7uys5.jpg', 'bed', 75),
(176, '16/hotel_zNkjzR3fsF.jpg', 'front view', 75),
(177, '33/hotel_EoZkWlnV2I.jpg', 'bathroom', 76),
(178, '33/hotel_M78csTO4gF.jpg', 'bed', 76),
(179, '33/hotel_QgPFWxNDWv.jpg', 'bed', 76),
(180, '33/hotel_pyoxDN51Qg.jpg', 'front view', 76),
(181, '35/hotel_s7z7kQYYVN.jpg', 'bed', 87),
(182, '35/hotel_Yo7n9Jyf5P.jpg', 'front view', 87),
(183, '35/hotel_JBRuiGJD4l.jpg', 'bed', 87),
(184, '35/hotel_VIGLtqYTWI.jpg', 'bathroom', 87),
(185, '34/hotel_NJKEpqMiTZ.jpg', 'GYM', 94),
(186, '34/hotel_70Z3p52dXI.jpg', 'bed', 94),
(187, '34/hotel_f0mPAjT8Dh.jpg', 'bed', 94),
(188, '34/hotel_UnjFYGdNXn.jpg', 'bed', 94),
(189, '34/hotel_rxEU4HVueV.jpg', 'lobby', 94),
(190, '34/hotel_t6ekof4NJ9.jpg', 'bed', 94),
(191, '34/hotel_hnKvK62I40.jpg', 'lobby', 95),
(192, '34/hotel_awmDQ7qpij.jpg', 'kitchen', 95),
(193, '34/hotel_7sk8kERnRe.jpg', 'GYM', 95),
(194, '34/hotel_TwT9hIblRA.jpg', 'front view', 95),
(195, '34/hotel_05Jdb4u0ps.jpg', 'bed', 96),
(196, '34/hotel_x4A6Pp9i98.jpg', 'bed', 96),
(197, '34/hotel_eiRKjocQ1L.jpg', 'Pool', 96),
(198, '34/hotel_IGajdit6C9.jpg', 'bed', 96),
(199, '34/hotel_kmEVxiUGSX.jpg', 'bed', 97),
(200, '34/hotel_g4PNPD4SjU.jpg', 'lobby', 97),
(201, '34/hotel_VmetAZ7Gai.jpg', 'bed', 97),
(202, '34/hotel_rzm6iaGzvJ.jpg', 'bed', 97),
(203, '34/hotel_F7ZuCa6zEv.jpg', 'bed', 97),
(204, '36/hotel_XvFKLGoUyc.jpg', 'bed', 99),
(205, '36/hotel_4g6K9VCZye.jpg', 'bed', 99),
(206, '36/hotel_LYVP3CDnON.jpg', 'GYM', 99),
(207, '36/hotel_N7CVQtCvKn.jpg', 'front view', 99),
(208, '36/hotel_n8ItcZPHAy.jpg', 'bed', 98),
(209, '36/hotel_XMz64ezl6J.jpg', 'kitchen', 98),
(210, '36/hotel_60NgbZsjJ0.jpg', 'bathroom', 98),
(211, '36/hotel_0kR4sdR8P5.jpg', 'bed', 98),
(212, '36/hotel_Wvx1aoXlWD.jpg', 'Pool', 98),
(213, '36/hotel_NOrZBuNRBw.jpg', 'bed', 98),
(214, '18/hotel_GSmOnM5N7B.jpg', 'bed', 100),
(215, '18/hotel_8kGfWCOGrS.jpg', 'bed', 100),
(216, '18/hotel_5hgiIsD6hT.jpg', 'bathroom', 100),
(217, '18/hotel_4S2053tFbP.jpg', 'bed', 100),
(218, '18/hotel_MDa6gmFsr3.jpg', 'bathroom', 100),
(219, '18/hotel_OIWl8WRa5Y.jpg', 'lobby', 100),
(220, '40/hotel_nSs0mdP757.jpg', 'building', 104),
(221, '40/hotel_if5jtzMo2w.jpg', 'side view', 104),
(222, '40/hotel_WPYOTD5e4Z.jpg', 'front', 104),
(223, '40/hotel_JxoZT8SeYU.jpg', 'top', 104),
(224, '40/hotel_u3fKmM4Qun.jpg', 'balcony', 104),
(225, '40/hotel_Cx7dmf6Tj6.jpg', 'room', 104),
(226, '40/hotel_yKjAniHTtt.jpg', 'wardrops', 104),
(227, '4/hotel_vVlTiu57hx.jpg', 'Tittle 1', 103),
(228, '4/hotel_GDxhuu4n9m.png', 'Tittle 2', 103),
(229, '4/hotel_KTnsWpvhB3.jpeg', 'Tittle 3', 103),
(230, '4/hotel_44cdYE6DNR.jpg', 'Tittle 4', 103),
(231, '23/hotel_qG7BnD7Bnb.jpg', 'kitchen', 91),
(232, '23/hotel_A2KCcaO93k.jpg', 'bed', 91),
(233, '23/hotel_UzPoJjZNQi.png', 'bed', 91);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_inventoryoffers`
--

CREATE TABLE `hotel_inventoryoffers` (
  `id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `hotel_inventory_id` int(11) NOT NULL,
  `offer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_inventoryoffers`
--

INSERT INTO `hotel_inventoryoffers` (`id`, `status`, `created_at`, `hotel_inventory_id`, `offer_id`) VALUES
(1, 0, '2019-08-21 10:38:21.658844', 8, 1),
(2, 0, '2019-08-21 10:38:21.675702', 69, 1),
(3, 0, '2019-08-21 10:38:21.688941', 14, 1),
(4, 0, '2019-08-21 10:38:21.702760', 70, 1),
(6, 1, '2019-10-22 06:51:34.552820', 71, 2),
(7, 1, '2019-10-22 06:51:34.560237', 6, 2),
(8, 1, '2019-10-22 06:51:34.569226', 73, 2),
(9, 1, '2019-10-22 06:51:34.577177', 5, 2),
(10, 0, '2019-11-25 11:08:34.756549', 78, 1);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_inventoryupdate`
--

CREATE TABLE `hotel_inventoryupdate` (
  `id` int(11) NOT NULL,
  `status` varchar(80) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `date` date NOT NULL,
  `hotel_id` int(11) DEFAULT NULL,
  `inventory_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_inventoryupdate`
--

INSERT INTO `hotel_inventoryupdate` (`id`, `status`, `quantity`, `date`, `hotel_id`, `inventory_id`) VALUES
(1, 'Closed', 2, '2020-01-02', 29, 83),
(2, 'Open', 2, '2020-01-14', 29, 83),
(3, 'Open', 2, '2020-01-14', 29, 84),
(4, 'Open', 2, '2020-01-15', 29, 83),
(5, 'Open', 2, '2020-01-16', 29, 83),
(6, 'Open', 2, '2020-01-16', 29, 84),
(7, 'Open', 1, '2020-01-17', 29, 83),
(8, 'Open', 1, '2020-01-17', 29, 84);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_inventory_bed_type`
--

CREATE TABLE `hotel_inventory_bed_type` (
  `id` int(11) NOT NULL,
  `bed_count` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `bed_type_id` int(11) NOT NULL,
  `inventory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_inventory_bed_type`
--

INSERT INTO `hotel_inventory_bed_type` (`id`, `bed_count`, `created_at`, `bed_type_id`, `inventory_id`) VALUES
(1, 2, '2019-05-21 05:17:34.659559', 1, 7),
(19, 1, '2019-11-08 05:19:57.290245', 1, 6),
(33, 4, '2019-11-25 10:40:50.776046', 1, 8),
(34, 3, '2019-11-25 10:40:50.779587', 2, 8),
(35, 3, '2019-11-25 10:43:13.589056', 1, 10),
(36, 4, '2019-11-25 10:43:13.592694', 2, 10),
(38, 4, '2019-11-25 11:01:11.757734', 1, 77),
(39, 3, '2019-11-25 11:03:24.592944', 1, 78),
(40, 2, '2019-12-04 07:09:51.044790', 4, 89),
(64, 3, '2019-12-04 07:55:10.495253', 1, 5),
(65, 4, '2019-12-04 07:55:10.502216', 2, 5),
(66, 3, '2019-12-04 07:55:10.505644', 3, 5),
(67, 6, '2019-12-04 07:57:47.572316', 1, 75),
(68, 4, '2019-12-04 07:57:47.577449', 2, 75),
(69, 6, '2019-12-04 07:57:47.581043', 3, 75),
(70, 7, '2019-12-04 07:57:47.584744', 4, 75),
(71, 4, '2019-12-04 08:07:09.544126', 1, 81),
(72, 3, '2019-12-04 08:07:25.967108', 2, 81),
(73, 6, '2019-12-04 08:07:25.971261', 3, 81),
(74, 6, '2019-12-04 08:07:25.976106', 4, 81),
(75, 3, '2019-12-04 08:08:13.682289', 1, 82),
(76, 4, '2019-12-04 08:08:13.685529', 2, 82),
(77, 6, '2019-12-04 08:08:13.688512', 3, 82),
(78, 7, '2019-12-04 08:08:13.691245', 4, 82),
(79, 6, '2019-12-04 08:10:09.852650', 1, 76),
(80, 6, '2019-12-04 08:10:09.855902', 1, 76),
(81, 2, '2019-12-04 08:10:09.858496', 3, 76),
(82, 9, '2019-12-04 08:10:09.861650', 4, 76),
(83, 5, '2019-12-04 08:12:37.201471', 1, 86),
(84, 7, '2019-12-04 08:12:37.206502', 2, 86),
(85, 9, '2019-12-04 08:12:37.209733', 3, 86),
(86, 5, '2019-12-04 08:13:36.335359', 1, 87),
(87, 7, '2019-12-04 08:13:36.338637', 2, 87),
(88, 3, '2019-12-04 08:13:36.341950', 3, 87),
(89, 8, '2019-12-04 08:13:36.344904', 4, 87),
(90, 6, '2019-12-04 08:15:22.377071', 1, 94),
(91, 4, '2019-12-04 08:15:22.381477', 2, 94),
(92, 7, '2019-12-04 08:15:22.385112', 3, 94),
(93, 2, '2019-12-04 08:16:48.747134', 1, 95),
(94, 5, '2019-12-04 08:16:48.750438', 2, 95),
(95, 3, '2019-12-04 08:17:53.588889', 1, 96),
(96, 6, '2019-12-04 08:17:53.592327', 3, 96),
(97, 4, '2019-12-04 08:19:07.286352', 1, 97),
(98, 5, '2019-12-04 08:19:07.289600', 3, 97),
(99, 3, '2019-12-04 08:26:15.649830', 1, 99),
(100, 5, '2019-12-04 08:26:15.653242', 2, 99),
(101, 7, '2019-12-04 08:26:15.656373', 3, 99),
(102, 3, '2019-12-04 08:29:00.701137', 1, 98),
(103, 6, '2019-12-04 08:29:00.704495', 2, 98),
(104, 7, '2019-12-04 08:29:00.707173', 4, 98),
(105, 3, '2019-12-06 07:53:47.653408', 3, 100),
(106, 3, '2019-12-06 07:53:47.653408', 3, 83),
(107, 2, '2019-12-30 08:11:14.300300', 2, 101),
(108, 1, '2019-12-30 09:05:50.817088', 2, 102),
(109, 1, '2019-12-30 09:05:50.817088', 4, 103),
(110, 2, '2019-12-04 07:09:51.044790', 4, 90),
(111, 2, '2020-01-24 06:21:24.804947', 2, 104),
(112, 2, '2020-01-26 07:33:34.325599', 1, 105);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_landmark`
--

CREATE TABLE `hotel_landmark` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_landmark`
--

INSERT INTO `hotel_landmark` (`id`, `name`) VALUES
(1, 'landmark 1'),
(2, 'some landmark'),
(3, 'andmark23'),
(4, 'bandmark23'),
(5, 'candmark23'),
(6, 'dandmark23'),
(7, 'eandmark23'),
(8, 'fandmark23'),
(9, 'gandmark23'),
(77, 'patan'),
(78, 'some again'),
(79, 'kkkkkk'),
(80, 'jjjjjjjjj'),
(81, 'lllllll'),
(82, 'Bus Park'),
(83, 'Some Landmark'),
(84, 'Temple'),
(85, 'pipal bot'),
(86, ''),
(87, ''),
(88, 'sarswati mandir');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_offers`
--

CREATE TABLE `hotel_offers` (
  `id` int(11) NOT NULL,
  `offer_name` varchar(80) DEFAULT NULL,
  `description` longtext NOT NULL,
  `start_date` datetime(6) DEFAULT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `banner_image` varchar(100) NOT NULL,
  `rate` decimal(20,2) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `module` varchar(80) DEFAULT NULL,
  `creator_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_offers`
--

INSERT INTO `hotel_offers` (`id`, `offer_name`, `description`, `start_date`, `end_date`, `banner_image`, `rate`, `status`, `module`, `creator_id`) VALUES
(1, 'Kevin Tucker', 'viridvubozme', '2019-01-01 00:00:00.000000', '2020-11-30 00:00:00.000000', '178528421.jpg', '12.00', 1, 'hotel', 8),
(2, 'Tihar Offer', 'This is description about tihar offer.', '2019-01-01 00:00:00.000000', '2020-10-31 00:00:00.000000', 'IMG_9224.JPG', '12.00', 1, 'hotel', 4);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_spotlight`
--

CREATE TABLE `hotel_spotlight` (
  `id` int(11) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `nameofdepositor` varchar(80) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `contact1` varchar(17) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `hotel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_spotlight`
--

INSERT INTO `hotel_spotlight` (`id`, `start_date`, `end_date`, `nameofdepositor`, `price`, `contact1`, `status`, `created_at`, `hotel_id`) VALUES
(1, '2019-09-01', '2019-10-02', 'Raj shah', '5000.00', NULL, 0, '2019-09-20 06:28:11.574712', 5),
(5, '2019-09-05', '2019-10-10', 'Aadarsha chapagain', '4500.00', NULL, 0, '2019-09-20 06:37:17.964951', 4),
(9, '2019-09-10', '2019-10-20', 'shaw', '4500.00', NULL, 0, '2019-09-20 07:58:40.769672', 23);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_state`
--

CREATE TABLE `hotel_state` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `country_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_state`
--

INSERT INTO `hotel_state` (`id`, `name`, `country_id`) VALUES
(1, 'Bagmati', 649),
(2, 'Gandaki', 649),
(3, 'Janakpur', 649),
(4, 'Karnali', 649),
(5, 'Koshi', 649),
(6, 'Lumbini', 649),
(7, 'Sudurpaschimanchal', 649),
(8, 'Andhra Pradesh', 594),
(9, 'Arunachal Pradesh', 594),
(10, 'Assam', 594),
(11, 'Bihar', 594),
(12, 'Chhattisgarh', 594),
(13, 'Chhattisgarh', 594),
(14, 'Goa', 594),
(15, 'Goa', 594),
(16, 'Gujarat', 594),
(17, 'Haryana', 594),
(18, 'Himachal Pradesh', 594),
(19, 'Jammu and Kashmir', 594),
(20, 'Jharkhand', 594),
(21, 'Karnataka', 594),
(22, 'Kerala', 594),
(23, 'Madhya Pradesh', 594),
(24, 'Maharashtra', 594),
(25, 'Manipur', 594),
(26, 'Meghalaya', 594),
(27, 'Mizoram', 594),
(28, 'Nagaland', 594),
(29, 'Odisha', 594),
(30, 'Punjab', 594),
(31, 'Rajasthan', 594),
(32, 'Sikkim', 594),
(33, 'Tamil Nadu', 594),
(34, 'Telangana', 594),
(35, 'Tripura', 594),
(36, 'Uttar Pradesh', 594),
(37, 'Uttarakhand', 594),
(38, 'West Bengal', 594);

-- --------------------------------------------------------

--
-- Table structure for table `points_creditpoint`
--

CREATE TABLE `points_creditpoint` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `transaction_amount` int(11) DEFAULT NULL,
  `net_total` int(11) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `transaction_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `booking_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `points_membership_plan`
--

CREATE TABLE `points_membership_plan` (
  `id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `purchase_price` decimal(10,2) DEFAULT NULL,
  `renewal_cost` decimal(10,2) DEFAULT NULL,
  `reward_point` int(11) DEFAULT NULL,
  `virtual_point` int(11) DEFAULT NULL,
  `virtual_point_for_old` int(11) DEFAULT NULL,
  `credit_point_for_old` int(11) DEFAULT NULL,
  `upgrade_reward_point` int(11) DEFAULT NULL,
  `position` int(11) DEFAULT NULL,
  `renewal_cond` int(11) DEFAULT NULL,
  `expiry_cond` int(11) DEFAULT NULL,
  `maturity_time` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `points_pointsetting`
--

CREATE TABLE `points_pointsetting` (
  `id` int(11) NOT NULL,
  `frompoint` varchar(200) NOT NULL,
  `topoint` varchar(200) NOT NULL,
  `conversion_ratio` decimal(10,2) NOT NULL,
  `maturity_time` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `points_rewardpoint`
--

CREATE TABLE `points_rewardpoint` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `transaction_amount` int(11) DEFAULT NULL,
  `net_total` int(11) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `transaction_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `booking_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `points_virtualpoint`
--

CREATE TABLE `points_virtualpoint` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `transaction_amount` int(11) DEFAULT NULL,
  `net_total` int(11) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `transaction_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `booking_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `rental_bankdetail`
--

CREATE TABLE `rental_bankdetail` (
  `id` int(11) NOT NULL,
  `bankCountry_id` int(11) DEFAULT NULL,
  `bankName` varchar(200) DEFAULT NULL,
  `swiftCode` varchar(200) DEFAULT NULL,
  `accountNumber` varchar(200) DEFAULT NULL,
  `accountName` varchar(200) DEFAULT NULL,
  `invoiceTo` varchar(200) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `rental_rentalcompany`
--

CREATE TABLE `rental_rentalcompany` (
  `id` int(11) NOT NULL,
  `name` varchar(60) DEFAULT NULL,
  `description` longtext NOT NULL,
  `words_by_owner` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` int(11) DEFAULT NULL,
  `is_active` int(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `cino` varchar(60) DEFAULT NULL,
  `cname` varchar(60) DEFAULT NULL,
  `estd_date` varchar(60) DEFAULT NULL,
  `nameonpancard` varchar(60) DEFAULT NULL,
  `pannumber` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_rentalcompany`
--

INSERT INTO `rental_rentalcompany` (`id`, `name`, `description`, `words_by_owner`, `created_at`, `status`, `is_active`, `image`, `owner_id`, `cino`, `cname`, `estd_date`, `nameonpancard`, `pannumber`) VALUES
(1, 'Garrett Campbell', 'wuahtuw', 'suludko', '2019-04-23 05:42:12.278386', 0, 0, 'vehicle.jpg', 10, NULL, NULL, NULL, NULL, NULL),
(2, 'Final Rental Company', 'some description', 'some words by rental owner', '2019-05-09 06:32:52.977204', 0, 0, 'restaurant_lyaHn8C.jpeg', 10, NULL, NULL, NULL, NULL, NULL),
(3, 'Scorpio', 'dsdzdad', 'zdczcz', '2019-10-22 10:12:26.444112', 0, 0, 'default.png', 10, NULL, NULL, NULL, NULL, NULL),
(4, 'XYZ Motors', 'A good company', 'It is very good service provider company', '2019-11-29 06:58:59.232417', 0, 0, 'download_5.jpg', 10, NULL, NULL, NULL, NULL, NULL),
(5, 'ABC Motors', 'A nice company', 'A reputed and well known company in the martek', '2019-11-29 07:17:50.358267', 0, 0, 'download_5_16rzfTq.jpg', 10, NULL, NULL, NULL, NULL, NULL),
(6, 'Rental Company Abc', 'some Description', 'Some Words by Owner', '2019-12-02 06:36:36.345887', 0, 0, 'default.png', 6, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rental_rentalcompanyaddress`
--

CREATE TABLE `rental_rentalcompanyaddress` (
  `company_id` int(11) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `contact1` varchar(17) DEFAULT NULL,
  `contact2` varchar(17) DEFAULT NULL,
  `latitude` decimal(22,16) DEFAULT NULL,
  `longitude` decimal(22,16) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `city_id` int(11) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_rentalcompanyaddress`
--

INSERT INTO `rental_rentalcompanyaddress` (`company_id`, `address`, `contact1`, `contact2`, `latitude`, `longitude`, `created_at`, `city_id`, `country_id`, `state_id`) VALUES
(1, '2000 Omete Loop', '4474405985', '4463631262', '66.0000000000000000', '14.0000000000000000', '2019-04-23 05:42:12.290055', 2, 2, 2),
(2, '1962 Ugitot Extension', '7203806134', '2837669374', '75.2200000000000000', '23.3340000000000000', '2019-05-09 06:32:53.326196', 4, 2, 2),
(3, NULL, NULL, NULL, NULL, NULL, '2019-10-22 10:12:26.453970', NULL, NULL, NULL),
(4, 'Narayanthan', '97714438955', '9812333334', '27.7836652000000000', '85.3702465000000100', '2019-11-29 06:58:59.311256', 31, 649, 1),
(5, 'Anamnagar', '97714438955', '9812333334', '27.7084368526219330', '85.3251384994140400', '2019-11-29 07:17:50.367571', 31, 649, 1),
(6, 'Lolang', '9813207240', '9813207240', '27.7084368526219330', '85.3251384994140400', '2019-12-02 06:36:36.352235', 35, 649, 1);

-- --------------------------------------------------------

--
-- Table structure for table `rental_rentalcompanyaddress_landmarks`
--

CREATE TABLE `rental_rentalcompanyaddress_landmarks` (
  `id` int(11) NOT NULL,
  `rentalcompanyaddress_id` int(11) NOT NULL,
  `landmark_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_rentalcompanyaddress_landmarks`
--

INSERT INTO `rental_rentalcompanyaddress_landmarks` (`id`, `rentalcompanyaddress_id`, `landmark_id`) VALUES
(9, 1, 2),
(8, 2, 1),
(7, 2, 2),
(10, 4, 4),
(11, 5, 3),
(13, 6, 84);

-- --------------------------------------------------------

--
-- Table structure for table `rental_rentaloffers`
--

CREATE TABLE `rental_rentaloffers` (
  `id` int(11) NOT NULL,
  `offer_name` varchar(80) DEFAULT NULL,
  `description` longtext NOT NULL,
  `start_date` datetime(6) DEFAULT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `banner_image` varchar(100) NOT NULL,
  `rate` decimal(20,2) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `module` varchar(80) DEFAULT NULL,
  `creator_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_rentaloffers`
--

INSERT INTO `rental_rentaloffers` (`id`, `offer_name`, `description`, `start_date`, `end_date`, `banner_image`, `rate`, `status`, `module`, `creator_id`) VALUES
(1, 'offer1', 'some offer', '2019-01-01 00:00:00.000000', '2019-09-01 00:00:00.000000', 'default.png', '200.00', 0, 'rental', 10);

-- --------------------------------------------------------

--
-- Table structure for table `rental_rentalsfacilities`
--

CREATE TABLE `rental_rentalsfacilities` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_rentalsfacilities`
--

INSERT INTO `rental_rentalsfacilities` (`id`, `name`, `image`, `status`, `created_at`) VALUES
(1, 'AC', 'default.png', 1, '2019-04-23 05:46:06.425613'),
(2, 'fac', 'default.png', 1, '2019-04-23 05:46:17.639263');

-- --------------------------------------------------------

--
-- Table structure for table `rental_spotlight`
--

CREATE TABLE `rental_spotlight` (
  `id` int(11) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `nameofdepositor` varchar(80) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `contact1` varchar(17) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `vehicle_inventory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_spotlight`
--

INSERT INTO `rental_spotlight` (`id`, `start_date`, `end_date`, `nameofdepositor`, `price`, `contact1`, `status`, `created_at`, `vehicle_inventory_id`) VALUES
(1, '2019-01-01', '2019-01-01', 'some descriptor123', '1200.00', NULL, 0, '2019-08-04 10:55:53.387086', 3),
(3, '2019-01-01', '2019-02-01', 'some description', '3400.00', NULL, 0, '2019-08-04 10:57:19.461748', 4);

-- --------------------------------------------------------

--
-- Table structure for table `rental_vehiclebrand`
--

CREATE TABLE `rental_vehiclebrand` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_vehiclebrand`
--

INSERT INTO `rental_vehiclebrand` (`id`, `name`, `status`, `category_id`) VALUES
(1, 'Honda', 0, 1),
(2, 'Suzuki', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `rental_vehiclecategory`
--

CREATE TABLE `rental_vehiclecategory` (
  `id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_vehiclecategory`
--

INSERT INTO `rental_vehiclecategory` (`id`, `image`, `name`, `status`) VALUES
(1, 'default.png', 'car', 1),
(2, 'default.png', 'Mountain Bike', 0);

-- --------------------------------------------------------

--
-- Table structure for table `rental_vehicledetail`
--

CREATE TABLE `rental_vehicledetail` (
  `id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `drive` varchar(200) DEFAULT NULL,
  `fuel_type` varchar(200) DEFAULT NULL,
  `gear_box` varchar(200) DEFAULT NULL,
  `brake` varchar(200) DEFAULT NULL,
  `mileage` varchar(200) DEFAULT NULL,
  `boot_capacity` decimal(10,2) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `vehicle_category_id` int(11) DEFAULT NULL,
  `description` longtext NOT NULL,
  `air_bag_count` int(11) DEFAULT NULL,
  `model` varchar(30) DEFAULT NULL,
  `seating_capacity` int(11) DEFAULT NULL,
  `rental_company_id` int(11) NOT NULL,
  `car_group` varchar(200) DEFAULT NULL,
  `bikegroup` varchar(20) DEFAULT NULL,
  `enginecc` varchar(20) DEFAULT NULL,
  `gear` varchar(20) DEFAULT NULL,
  `vehicle_brand_id` int(11) DEFAULT NULL,
  `no_of_doors` int(11) DEFAULT NULL,
  `tank_capacity` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_vehicledetail`
--

INSERT INTO `rental_vehicledetail` (`id`, `image`, `drive`, `fuel_type`, `gear_box`, `brake`, `mileage`, `boot_capacity`, `status`, `vehicle_category_id`, `description`, `air_bag_count`, `model`, `seating_capacity`, `rental_company_id`, `car_group`, `bikegroup`, `enginecc`, `gear`, `vehicle_brand_id`, `no_of_doors`, `tank_capacity`) VALUES
(1, 'default.png', 'puzsa', 'Petrol', 'Automatic', 'Anti Locking Braking System', 'civobnem', '10.00', 0, 1, '', 0, 'some model', 4, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'default.png', 'sehhice', 'Diesel', 'Automatic', 'Drum Brake', 'hosam', '10.00', 0, 1, '', 0, 'car ko some model', 4, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'default.png', '4wd', 'Petrol', 'Automatic', 'Anti Locking Braking System', '10', '20.00', 0, 1, 'lorem50', 2, 'Desire', 2, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'default.png', '-', 'Other', 'Manual', 'Other', '0', '0.00', 0, 2, 'some description', 0, 'BMX', 2, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'Gorkha-Nepal_8Oblhi6.png', '2WD', 'Petrol', 'Automatic', 'Anti Locking Braking System', NULL, NULL, 0, 1, 'This is simple description about 2019.', 0, '2019', 4, 1, 'suv', 'dirt', 'None', 'None', NULL, NULL, NULL),
(6, 'adobe-illustrator-euclidean-vector-yellow-little-sun_PVhNwgU.png', '2WD', 'Petrol', 'Automatic', 'Anti Locking Braking System', NULL, NULL, 0, 1, 'This is simple description about Nisham.', 0, 'Nisham', 4, 1, 'suv', 'dirt', NULL, NULL, NULL, NULL, NULL),
(7, 'vehicle_onhire_cYXElB8.jpg', '4WD', 'Petrol', 'Automatic', 'Anti Locking Braking System', NULL, NULL, 0, 1, 'A good car', 0, '2014', 4, 5, 'suv', 'dirt', NULL, NULL, NULL, NULL, NULL),
(8, '_Remote_Control-512.png', '4WD', 'Petrol', 'Automatic', 'Anti Locking Braking System', NULL, NULL, 1, 1, 'A good car', 0, '2014', 4, 4, 'suv', 'dirt', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rental_vehicleinventory`
--

CREATE TABLE `rental_vehicleinventory` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `driver_type` varchar(30) DEFAULT NULL,
  `insurance` varchar(30) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `rental_company_id` int(11) NOT NULL,
  `vehicle_detail_id` int(11) NOT NULL,
  `description` longtext,
  `vehicle_type` varchar(50) NOT NULL,
  `vehicle_location_id` int(11) DEFAULT NULL,
  `vehicle_boot` varchar(10) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `seats` int(11) DEFAULT NULL,
  `color` varchar(30) DEFAULT NULL,
  `suspension` varchar(30) DEFAULT NULL,
  `weight` varchar(30) DEFAULT NULL,
  `vehicle_brand_id` int(11) DEFAULT NULL,
  `priceperday` decimal(10,2) DEFAULT NULL,
  `priceperhr` decimal(10,2) DEFAULT NULL,
  `priceperkm` decimal(10,2) DEFAULT NULL,
  `fitness_no` varchar(20) DEFAULT NULL,
  `make` varchar(5) DEFAULT NULL,
  `number_plate` varchar(15) DEFAULT NULL,
  `reg_no` varchar(15) DEFAULT NULL,
  `tax_token_no` varchar(15) DEFAULT NULL,
  `vehicle_category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_vehicleinventory`
--

INSERT INTO `rental_vehicleinventory` (`id`, `name`, `driver_type`, `insurance`, `status`, `is_verified`, `rental_company_id`, `vehicle_detail_id`, `description`, `vehicle_type`, `vehicle_location_id`, `vehicle_boot`, `created_at`, `seats`, `color`, `suspension`, `weight`, `vehicle_brand_id`, `priceperday`, `priceperhr`, `priceperkm`, `fitness_no`, `make`, `number_plate`, `reg_no`, `tax_token_no`, `vehicle_category_id`) VALUES
(1, 'Estelle McLaughlin', 'Self Driven', 'First Party', 0, 1, 1, 2, 'some desc', 'Economic', 1, NULL, '2019-11-13 06:05:59.052487', 4, NULL, NULL, NULL, NULL, '0.00', '0.00', '0.00', NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'Bernice Patterson', 'Self Driven', 'First Party', 0, 1, 1, 2, 'some desc', 'Economic', 1, NULL, '2019-11-13 06:05:59.052487', 4, NULL, NULL, NULL, NULL, '0.00', '0.00', '0.00', NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'Henry Barnett', 'Driver Included', 'Third Party', 0, 1, 1, 1, 'some desc', 'Economic', 1, NULL, '2019-11-13 06:05:59.052487', 4, NULL, NULL, NULL, NULL, '0.00', '0.00', '0.00', NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'Henry Washington', 'Self Driven', 'First Party', 1, 0, 2, 1, '', 'Economic', 1, NULL, '2019-11-13 06:05:59.052487', 4, NULL, NULL, NULL, NULL, '0.00', '0.00', '0.00', NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'Suzuki Desire', 'Self Driven', 'First Party', 1, 0, 1, 1, 'some description', 'Economic', 1, NULL, '2019-11-13 06:05:59.052487', 4, NULL, NULL, NULL, NULL, '0.00', '0.00', '0.00', NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'hero cycle', 'Self Driven', 'First Party', 1, 0, 2, 4, 'some descc', 'Economic', 1, NULL, '2019-11-13 06:05:59.052487', 4, NULL, NULL, NULL, NULL, '0.00', '0.00', '0.00', NULL, NULL, NULL, NULL, NULL, NULL),
(7, NULL, 'Self Driven', 'First Party', 1, 0, 4, 8, '', '', 1, 'yes', '2019-12-02 10:19:56.648482', 4, 'red', NULL, NULL, NULL, '0.00', '0.00', '0.00', NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rental_vehicleinventorygallery`
--

CREATE TABLE `rental_vehicleinventorygallery` (
  `id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `rentalInventory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_vehicleinventorygallery`
--

INSERT INTO `rental_vehicleinventorygallery` (`id`, `image`, `title`, `status`, `rentalInventory_id`) VALUES
(1, 'rivverrunner_mVYFyWN.jpeg', 'titleboat', 1, 1),
(2, 'vehicle_BoDeVRV.jpg', 'Green tank', 1, 2),
(3, 'vehicle_RbrYKh1.jpg', 'some title', 1, 4),
(4, 'skydive_sanfrancisco_banner_hEdIcMK.jpg', 'some title', 1, 4),
(5, 'restaurant_q6xNloq.jpg', 'some title', 1, 4),
(6, '8-512.png', 'Front view', 0, 7);

-- --------------------------------------------------------

--
-- Table structure for table `rental_vehicleinventory_vehiclefacilities`
--

CREATE TABLE `rental_vehicleinventory_vehiclefacilities` (
  `id` int(11) NOT NULL,
  `vehicleFacilities_id` int(11) NOT NULL,
  `vehicleinventory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_vehicleinventory_vehiclefacilities`
--

INSERT INTO `rental_vehicleinventory_vehiclefacilities` (`id`, `vehicleFacilities_id`, `vehicleinventory_id`) VALUES
(3, 2, 3),
(9, 2, 2),
(14, 1, 1),
(15, 2, 1),
(18, 1, 5),
(23, 2, 4),
(24, 1, 6),
(25, 1, 7);

-- --------------------------------------------------------

--
-- Table structure for table `rental_vehicleoffers`
--

CREATE TABLE `rental_vehicleoffers` (
  `id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `offer_id` int(11) NOT NULL,
  `vehicle_inventory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rental_vehicleoffers`
--

INSERT INTO `rental_vehicleoffers` (`id`, `status`, `created_at`, `offer_id`, `vehicle_inventory_id`) VALUES
(1, 0, '2019-08-21 10:23:12.946473', 1, 4),
(2, 0, '2019-08-21 10:23:12.955231', 1, 6);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantcategory`
--

CREATE TABLE `restaurant_restaurantcategory` (
  `id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `star_count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantcategory`
--

INSERT INTO `restaurant_restaurantcategory` (`id`, `image`, `name`, `status`, `star_count`) VALUES
(1, 'default.png', 'Cafe', 0, 4),
(2, 'default.png', 'Bar', 0, 5);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantcompany`
--

CREATE TABLE `restaurant_restaurantcompany` (
  `id` int(11) NOT NULL,
  `name` varchar(60) DEFAULT NULL,
  `opening_time` varchar(60) DEFAULT NULL,
  `closing_time` varchar(60) DEFAULT NULL,
  `estd_date` varchar(60) DEFAULT NULL,
  `dress_code` varchar(60) DEFAULT NULL,
  `description` longtext NOT NULL,
  `words_by_owner` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` int(11) DEFAULT NULL,
  `is_active` int(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `category_id` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantcompany`
--

INSERT INTO `restaurant_restaurantcompany` (`id`, `name`, `opening_time`, `closing_time`, `estd_date`, `dress_code`, `description`, `words_by_owner`, `created_at`, `status`, `is_active`, `image`, `category_id`, `owner_id`) VALUES
(1, 'Red Mud cafe', '01:00', '01:00', '2019-01-01', 'Not Specified', 'some description', 'some words by owner', '2019-08-18 11:42:36.498288', 0, 0, 'lobby_nVGuwK2.jpg', 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantcompanyaddress`
--

CREATE TABLE `restaurant_restaurantcompanyaddress` (
  `company_id` int(11) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `contact1` varchar(17) DEFAULT NULL,
  `contact2` varchar(17) DEFAULT NULL,
  `latitude` decimal(22,16) DEFAULT NULL,
  `longitude` decimal(22,16) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `city_id` int(11) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantcompanyaddress`
--

INSERT INTO `restaurant_restaurantcompanyaddress` (`company_id`, `address`, `contact1`, `contact2`, `latitude`, `longitude`, `created_at`, `city_id`, `country_id`, `state_id`) VALUES
(1, 'some address', '9813207240', '9813207240', '0.0000000000000000', '0.0000000000000000', '2019-08-18 11:42:36.536603', 28, 649, 1);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantcompanyaddress_landmarks`
--

CREATE TABLE `restaurant_restaurantcompanyaddress_landmarks` (
  `id` int(11) NOT NULL,
  `restaurantcompanyaddress_id` int(11) NOT NULL,
  `landmark_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantcompanyaddress_landmarks`
--

INSERT INTO `restaurant_restaurantcompanyaddress_landmarks` (`id`, `restaurantcompanyaddress_id`, `landmark_id`) VALUES
(2, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantfacilities`
--

CREATE TABLE `restaurant_restaurantfacilities` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantfacilities`
--

INSERT INTO `restaurant_restaurantfacilities` (`id`, `name`, `image`, `status`, `created_at`) VALUES
(1, 'Fac 1', 'default.png', 0, '2019-08-18 11:40:13.278867'),
(2, 'Fac 2', 'default.png', 0, '2019-08-18 11:40:19.043179');

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantfacilitys`
--

CREATE TABLE `restaurant_restaurantfacilitys` (
  `id` int(11) NOT NULL,
  `restaurantcompany_id` int(11) NOT NULL,
  `restaurantfacility_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantfacilitys`
--

INSERT INTO `restaurant_restaurantfacilitys` (`id`, `restaurantcompany_id`, `restaurantfacility_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 1),
(4, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantgallery`
--

CREATE TABLE `restaurant_restaurantgallery` (
  `id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `restaurant_company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantgallery`
--

INSERT INTO `restaurant_restaurantgallery` (`id`, `image`, `title`, `status`, `restaurant_company_id`) VALUES
(1, 'crispy-fried-chicken-1_lDBelfd.jpg', 'fried chicken', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantinventory`
--

CREATE TABLE `restaurant_restaurantinventory` (
  `id` int(11) NOT NULL,
  `table_name` varchar(30) NOT NULL,
  `chair_count` int(11) NOT NULL,
  `max_seat_capacity` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image` varchar(100) NOT NULL,
  `table_count` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `company_id` int(11) NOT NULL,
  `table_category_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantinventory`
--

INSERT INTO `restaurant_restaurantinventory` (`id`, `table_name`, `chair_count`, `max_seat_capacity`, `price`, `image`, `table_count`, `description`, `is_verified`, `status`, `created_at`, `company_id`, `table_category_id`) VALUES
(1, 'table 1', 12, 5, '2300.00', 'kitchen_bS8uTAF.jpg', 3, 'some description', 0, 0, '2019-08-18 11:47:55.783339', 1, 2),
(2, 'table 1', 12, 5, '2300.00', 'default.png', 3, 'some description', 0, 0, '2019-08-18 11:48:16.729643', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantmenu`
--

CREATE TABLE `restaurant_restaurantmenu` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image` varchar(100) NOT NULL,
  `is_special` tinyint(1) NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `restaurant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantmenu`
--

INSERT INTO `restaurant_restaurantmenu` (`id`, `name`, `price`, `image`, `is_special`, `description`, `status`, `is_verified`, `restaurant_id`) VALUES
(1, 'Pizza', '230.00', 'pizza.png', 0, '', 0, 0, 1),
(2, 'fried chicken', '300.00', 'crispy-fried-chicken-1.jpg', 0, '', 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantoffers`
--

CREATE TABLE `restaurant_restaurantoffers` (
  `id` int(11) NOT NULL,
  `offer_name` varchar(80) DEFAULT NULL,
  `description` longtext NOT NULL,
  `start_date` datetime(6) DEFAULT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `banner_image` varchar(100) NOT NULL,
  `rate` decimal(20,2) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `module` varchar(80) DEFAULT NULL,
  `creator_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantoffers`
--

INSERT INTO `restaurant_restaurantoffers` (`id`, `offer_name`, `description`, `start_date`, `end_date`, `banner_image`, `rate`, `status`, `module`, `creator_id`) VALUES
(1, 'new year offer', 'this is new year offer', '2019-11-11 00:00:00.000000', '2020-11-11 00:00:00.000000', 'crispy-fried-chicken-1_wLlyAdC.jpg', '200.00', 0, 'restaurant', 4);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restaurantspecial`
--

CREATE TABLE `restaurant_restaurantspecial` (
  `id` int(11) NOT NULL,
  `title` varchar(30) NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `image` varchar(100) NOT NULL,
  `day` longtext NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `restaurant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restaurantspecial`
--

INSERT INTO `restaurant_restaurantspecial` (`id`, `title`, `start_time`, `end_time`, `image`, `day`, `description`, `status`, `is_verified`, `restaurant_id`) VALUES
(1, 'happy new year', '11:11:00.000000', '12:12:00.000000', 'crispy-fried-chicken-1_lVubmEV.jpg', ' Friday', 'this is for free till november', 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_restauranttablecategory`
--

CREATE TABLE `restaurant_restauranttablecategory` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `icon` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_restauranttablecategory`
--

INSERT INTO `restaurant_restauranttablecategory` (`id`, `title`, `icon`, `status`, `created_at`) VALUES
(1, 'Couple', 'default.png', 0, '2019-08-18 11:40:30.117886'),
(2, 'Family', 'default.png', 0, '2019-08-18 11:40:37.494980');

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_spotlight`
--

CREATE TABLE `restaurant_spotlight` (
  `id` int(11) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `nameofdepositor` varchar(80) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `contact1` varchar(17) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `restaurant_company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant_spotlight`
--

INSERT INTO `restaurant_spotlight` (`id`, `start_date`, `end_date`, `nameofdepositor`, `price`, `contact1`, `status`, `created_at`, `restaurant_company_id`) VALUES
(1, '2019-07-15', '2019-08-05', 'some depositor', '1200.00', '9813207240', 1, '2019-08-09 00:00:00.000000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_addonactivities`
--

CREATE TABLE `travel_tour_addonactivities` (
  `id` int(11) NOT NULL,
  `name` varchar(220) NOT NULL,
  `description` longtext NOT NULL,
  `rate` decimal(20,2) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `tour_package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_addonactivities`
--

INSERT INTO `travel_tour_addonactivities` (`id`, `name`, `description`, `rate`, `created_at`, `tour_package_id`) VALUES
(1, 'some activity', 'some descc', '120.00', '2019-07-24 05:22:47.619595', 9),
(2, 'some activity123', 'some descc', '120.00', '2019-07-24 05:22:47.619595', 9),
(3, 'some activity again', 'some descc again', '120.00', '2019-07-24 05:22:47.619595', 9),
(4, 'Bunjee', '', '4500.00', '2019-12-04 09:57:02.636834', 16);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_addoncuisine`
--

CREATE TABLE `travel_tour_addoncuisine` (
  `id` int(11) NOT NULL,
  `name` varchar(220) NOT NULL,
  `description` longtext NOT NULL,
  `rate` decimal(20,2) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `tour_package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_addoncuisine`
--

INSERT INTO `travel_tour_addoncuisine` (`id`, `name`, `description`, `rate`, `created_at`, `tour_package_id`) VALUES
(1, 'Joshua Watson', 'caubo', '1200.00', '2019-07-24 05:22:19.268079', 9);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_addonhotel`
--

CREATE TABLE `travel_tour_addonhotel` (
  `id` int(11) NOT NULL,
  `name` longtext NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `tour_package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_addonhotel`
--

INSERT INTO `travel_tour_addonhotel` (`id`, `name`, `description`, `price`, `tour_package_id`) VALUES
(2, 'name abc changed to xyz', 'some desccc', '1200.00', 9),
(4, 'Hotel Abc changed to 123', 'some description about abc', '3400.00', 9),
(5, 'Hotel XYZ', 'some description about xyz', '3500.00', 9),
(6, 'hotel 1 ', 'desccc 1', '1200.00', 10),
(7, 'hotel2 ', 'some more dess', '2400.00', 10),
(8, 'hotel 1', 'some descc', '1200.00', 10),
(9, 'hotel 2', 'some more descc', '2400.00', 10),
(10, 'hotel 1', 'some descc', '1200.00', 10),
(11, 'hotel 1', 'some descc', '1200.00', 10),
(12, 'hote 2', 'some mored descc', '2400.00', 10),
(13, 'some hotel', 'some desc', '3400.00', 11),
(14, 'hotel 1', 'some descc', '3400.00', 12),
(15, 'hotel2', 'some descc again', '3500.00', 12),
(16, 'hotel 1', 'some descc', '1200.00', 12),
(17, 'hotel 2', 'some more descc', '2400.00', 12),
(18, 'hotel 1', 'some descc', '1200.00', 12),
(19, 'hotel 1', 'some descc', '1200.00', 12),
(20, 'hotel1', 'some descc', '1200.00', 9),
(21, 'hotel1', 'some descc', '1200.00', 9),
(22, 'some name', 'no desc', '12.00', 9),
(23, 'some name', '', '12.00', 9),
(24, 'Hotel Swapnabagh', '', '200.00', 16);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_addontransport`
--

CREATE TABLE `travel_tour_addontransport` (
  `id` int(11) NOT NULL,
  `name` longtext NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `tour_package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_addontransport`
--

INSERT INTO `travel_tour_addontransport` (`id`, `name`, `description`, `price`, `tour_package_id`) VALUES
(1, 'Ford Figo123456', 'some description2341111', '1500.00', 3),
(2, 'some more name of vehicle', 'some more desccccc', '2300.00', 3),
(4, 'suv', 'some descc', '4500.00', 10),
(5, 'some vehicle 123', 'some more descc', '234.00', 12),
(6, 'forfffff', 'sosssfff', '12345.00', 12),
(7, 'Mabelle Miles', 'igju', '65.22', 9),
(8, 'SUV', '', '500.00', 16);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_packageoffers`
--

CREATE TABLE `travel_tour_packageoffers` (
  `id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `offer_id` int(11) NOT NULL,
  `tour_package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_packageoffers`
--

INSERT INTO `travel_tour_packageoffers` (`id`, `status`, `created_at`, `offer_id`, `tour_package_id`) VALUES
(1, 0, '2019-08-21 10:39:55.372315', 1, 3),
(2, 0, '2019-08-21 10:39:55.393701', 1, 7),
(3, 0, '2019-08-21 10:39:55.402925', 1, 10),
(4, 0, '2019-08-21 10:39:55.414102', 1, 13);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_spotlight`
--

CREATE TABLE `travel_tour_spotlight` (
  `id` int(11) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `nameofdepositor` varchar(80) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `contact1` varchar(17) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `tour_package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_spotlight`
--

INSERT INTO `travel_tour_spotlight` (`id`, `start_date`, `end_date`, `nameofdepositor`, `price`, `contact1`, `status`, `created_at`, `tour_package_id`) VALUES
(4, '2019-01-01', '2019-02-01', 'Katharine French', '450.35', NULL, 1, '2019-07-24 08:13:37.727799', 9),
(5, '2019-01-01', '2019-02-01', 'some depositor', '3400.00', NULL, 1, '2019-07-24 08:13:37.727799', 15);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_tourcompanyaddress`
--

CREATE TABLE `travel_tour_tourcompanyaddress` (
  `company_id` int(11) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `contact1` varchar(17) DEFAULT NULL,
  `contact2` varchar(17) DEFAULT NULL,
  `latitude` decimal(22,16) DEFAULT NULL,
  `longitude` decimal(22,16) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `city_id` int(11) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_tourcompanyaddress`
--

INSERT INTO `travel_tour_tourcompanyaddress` (`company_id`, `address`, `contact1`, `contact2`, `latitude`, `longitude`, `created_at`, `city_id`, `country_id`, `state_id`) VALUES
(1, '196 Lebu Pike', '8042893027', '8042893027', '18.0000000000000000', '93.0000000000000000', '2019-04-24 06:49:14.407948', 4, 1, 2),
(2, '1817 Hewur Highway', '9086574884', '9086574884', '22.0000000000000000', '75.0000000000000000', '2019-05-06 06:56:09.915246', 4, 2, 2),
(3, '584 Kebu Drive', '3696736601', '3696736601', '14.0000000000000000', '56.0000000000000000', '2019-05-06 07:05:34.802460', 1, 1, 1),
(4, '1914 Nehvig Grove', '7585725974', '4407918137', '57.0000000000000000', '78.0000000000000000', '2019-05-06 07:17:53.156235', 2, 2, 2),
(5, '638 Sowwel Loop', '2435389982', '8233261414', '78.0000000000000000', '29.0000000000000000', '2019-05-24 05:44:36.085117', 2, 2, 2),
(6, '1067 Cezago Key', '2506925727', '9469822969', '51.0000000000000000', '41.0000000000000000', '2019-07-22 10:58:16.346114', 1, 402, 1),
(7, '905 Coagu Extension', '6663096907', '6357017254', '65.0000000000000000', '16.0000000000000000', '2019-07-24 05:07:46.214537', 4, 402, 1),
(8, '12', '9849755595', '9849755595', '27.7068410915090980', '85.3270696899047600', '2019-11-22 11:25:59.905250', 38, 649, 1),
(9, 'Gairidhara', '+97714438955', '9801905958', '27.7191397000000000', '85.3275057000000700', '2019-12-04 09:46:57.613343', 123, 649, 1);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_tourcompanyaddress_landmarks`
--

CREATE TABLE `travel_tour_tourcompanyaddress_landmarks` (
  `id` int(11) NOT NULL,
  `tourcompanyaddress_id` int(11) NOT NULL,
  `landmark_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_tourcompanyaddress_landmarks`
--

INSERT INTO `travel_tour_tourcompanyaddress_landmarks` (`id`, `tourcompanyaddress_id`, `landmark_id`) VALUES
(2, 1, 1),
(4, 2, 1),
(6, 3, 2),
(8, 4, 2),
(9, 5, 1),
(10, 7, 1),
(11, 8, 2),
(12, 8, 3),
(13, 9, 2);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_tourgallery`
--

CREATE TABLE `travel_tour_tourgallery` (
  `id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `travel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_tourgallery`
--

INSERT INTO `travel_tour_tourgallery` (`id`, `image`, `title`, `travel_id`) VALUES
(1, 'rivverrunner.jpeg', 'some title', 9),
(2, 'holiday-inn_l1tDOkH.jpeg', 'some title', 9),
(3, 'All-Our-Kids-750x485_bBMFwQi.jpg', 'some title', 9),
(4, 'restaurant_oAUoYU6.jpeg', 'some title', 9),
(5, 'skydive_sanfrancisco_banner_Y0KHd4n.jpg', 'some title', 9),
(6, 'background.jpg', 'erfghj,k.', 9),
(7, 'pokhara4_7FSxSHK.jpg', 'Pokhara', 16);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_tourpackage`
--

CREATE TABLE `travel_tour_tourpackage` (
  `id` int(11) NOT NULL,
  `package_name` varchar(250) DEFAULT NULL,
  `description` longtext NOT NULL,
  `accomodation` longtext NOT NULL,
  `transportation` longtext NOT NULL,
  `fooding` longtext NOT NULL,
  `activities` longtext NOT NULL,
  `best_time` varchar(300) DEFAULT NULL,
  `day_count` bigint(20) DEFAULT NULL,
  `night_count` bigint(20) DEFAULT NULL,
  `group_size` bigint(20) DEFAULT NULL,
  `booked_count` bigint(20) NOT NULL,
  `tour_cost` decimal(20,2) DEFAULT NULL,
  `service_cost` decimal(20,2) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `banner_image` varchar(500) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  `distination_city_id` int(11) DEFAULT NULL,
  `start_city_id` int(11) DEFAULT NULL,
  `flight` tinyint(1) NOT NULL,
  `trip_grade` varchar(300) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_tourpackage`
--

INSERT INTO `travel_tour_tourpackage` (`id`, `package_name`, `description`, `accomodation`, `transportation`, `fooding`, `activities`, `best_time`, `day_count`, `night_count`, `group_size`, `booked_count`, `tour_cost`, `service_cost`, `status`, `is_verified`, `banner_image`, `created_at`, `company_id`, `distination_city_id`, `start_city_id`, `flight`, `trip_grade`, `country_id`) VALUES
(1, 'some package', 'some description', '4562192038402647', 'va', 'cilnu', 'cu', 'Jan, Feb', NULL, NULL, 94, 0, '100.00', '100.00', 0, 0, 'Picture1_dqxKtdw.png', '2019-05-02 13:33:39.129345', 4, 4, 4, 0, NULL, NULL),
(2, 'Herman Gonzales', 'acmik', '4357608456577684', 'cin', 'len', 'giwifira', 'Jan, Feb', NULL, NULL, 32, 0, '100.00', '200.00', 0, 0, 'holiday-inn_zcZEsB3.jpeg', '2019-05-03 05:54:13.874178', 4, 1, 2, 0, NULL, NULL),
(3, 'Aaron Wagner', 'uzi', '4384477144446844', 'faw', 'apfupvej', 'bejaka', 'Jan, Feb', NULL, NULL, 56, 0, '100.00', '200.00', 0, 0, 'skydive_sanfrancisco_banner.jpg', '2019-05-06 07:39:25.460092', 4, 4, 11, 0, NULL, NULL),
(4, 'kayak2', 'some desc', 'some acc', 'some transportation', 'some food', 'some activity', 'Jan, Feb', NULL, NULL, 2, 0, '100.00', '200.00', 0, 0, 'default.png', '2019-05-24 05:54:56.556322', 5, 10, 10, 0, NULL, NULL),
(5, 'Jeremy Hogan', 'bepmuk', '4105390408786128', 'ra', 'jisgirzed', 'kalo', 'Jan, Feb', NULL, NULL, 10, 0, '2000.00', '23000.00', 0, 0, 'default.png', '2019-07-22 11:01:12.462072', 6, 8, 11, 0, NULL, NULL),
(6, 'Cecilia Fisher', 'mu', '4331955607667471', 'fedahi', 'facje', 'nizat', 'Jan, Feb', NULL, NULL, 12, 0, '3400.00', '2300.00', 0, 0, 'default.png', '2019-07-22 11:50:43.464342', 4, 8, 1, 0, NULL, NULL),
(7, 'Cecilia Fisher', 'mu', '4331955607667471', 'fedahi', 'facje', 'nizat', 'Jan, Feb', NULL, NULL, 12, 0, '3400.00', '2300.00', 0, 0, 'default.png', '2019-07-22 11:50:49.962421', 4, 8, 1, 0, NULL, NULL),
(8, 'Mae Munoz', 'opzuv', '4212229502787394', 'hefhuir', 'nosoj', 'girivzuz', 'Jan, Feb', NULL, NULL, 12, 0, '100.00', '2300.00', 0, 0, 'default.png', '2019-07-22 12:28:18.096108', 5, 7, 6, 0, NULL, NULL),
(9, 'Jacob Lindsey', 'olira', '4657635884026080', 'gevban', 'pimcud', 'uv', 'Jan, Feb', NULL, NULL, 23, 0, '3400.00', '200.00', 0, 0, 'default.png', '2019-07-22 12:43:40.410703', 4, 9, 4, 0, NULL, NULL),
(10, 'Manuel Jones', 'uwa', '4064074197944895', 'dada', 'ok', 'gi', 'Jan, Feb', NULL, NULL, 23, 0, '2300.00', '4500.00', 0, 0, 'default.png', '2019-07-23 08:05:58.244275', 4, 2, 1, 0, NULL, NULL),
(11, 'John Rose', 'kipzu', '4224866190690194', 'jinin', 'arisha', 'ja', 'Jan, Feb', NULL, NULL, 10, 0, '3400.00', '400.00', 0, 0, 'default.png', '2019-07-23 08:24:36.475615', 4, 9, 7, 0, NULL, NULL),
(12, 'Frederick Morrison', 'lubemni', '4100962314037948', 'verus', 'idadovo', 'horoeki', 'Jan, Feb', NULL, NULL, 23, 0, '4500.00', '344.00', 0, 0, 'default.png', '2019-07-23 10:15:12.606261', 6, 4, 10, 0, NULL, NULL),
(13, 'Jason Santiago', 'bujenaj', '4430768048810893', 'fof', 'ulolevad', 'gewwe', 'Jan, Feb', NULL, NULL, 12, 0, '400.00', '3400.00', 0, 0, 'default.png', '2019-07-24 05:03:16.468199', 4, 2, 7, 0, NULL, NULL),
(14, 'Hester Sullivan', 'zosun', '4455856213504589', 'lalah', 'dugat', 'tumufeez', 'Jan, Feb', NULL, NULL, 12, 0, '3400.00', '3200.00', 0, 0, 'default.png', '2019-07-24 05:04:31.371516', 4, 2, 9, 0, NULL, NULL),
(15, 'Lilly Anderson', 'tevow', '4564596027343232', 'gufru', 'zi', 'bijgiseb', 'Jan, Feb', NULL, NULL, 23, 0, '2300.00', '3200.00', 0, 0, 'default.png', '2019-07-24 05:08:41.595776', 7, 4, 2, 0, NULL, NULL),
(16, 'Pokhara Tour', 'Kathmandu is the capital of Nepal. Furthermore, it is also the heritage city. Here, you travel\r\naround places of world heritage monuments. This carefully designed trip takes you to the major\r\nsightseeing destinations in Kathmandu, such as Durbar Square of Hanuman Dhoka, Buddhist\r\nStupa of Swoyambhunath and Boudhanath, and the Hindu temples of Pashupatinath and Changu\r\nNarayan. After Kathmandu, you will get to visit the famous cultural and religious sites of Patan\r\nlike Patan Durbar Square, Mahaboudha Temple, Kumbeshwor Temple, Krishna Temple, Golden\r\nTemple, etc and Bhaktapur Durbar square. After sightseeing in Kathmandu, Patan and\r\nBhaktapur, your next destination is Pokhara. Next, Pokhara is a beautiful city full of natural\r\nsights. You obviously relax and refresh staying in Pokhara. Lying 200 km away from\r\nKathmandu, Pokhara is overlooked by the beautiful Annapurna Ranges and spectacular snow-\r\ncapped mountains. During the course of this trip, you will be guided to the most popular places\r\nin Pokhara such as Phewa Lake, Begnas Lake, Rupa Lake, Mahendra Gupha, the Davis Fall, and\r\nthe gorge of the Seti River. Your stay in Pokhara with spectacular Machapuchhre as a backdrop\r\namidst the enchanting ambience of nature, bestows you with an experience of a lifetime. For the\r\nadventure lovers, we can arrange activities like paragliding, Sky diving, Bunjee &amp; Zip flyer upon\r\nyou request. KTM Voyage offers its itineraries anytime, or alternatively we can be in contact so\r\nyou may personally tailor your own itinerary.', '3 star hotel', 'Private A/C Vehicle', 'Breakfast', '', 'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec', NULL, NULL, 2, 0, '25000.00', '5000.00', 0, 0, 'pokhara4.jpg', '2019-12-04 09:51:05.873569', 9, 55, 123, 0, NULL, NULL),
(17, 'Bali Tour', 'Bali is a good place for relaxation', '3 star', 'ac vehicle', 'breakfast', 'beach', 'Jan', NULL, NULL, 2, 0, '25000.00', '5000.00', 0, 0, 'default.png', '2019-12-05 06:07:22.016170', 9, 6, 131, 0, NULL, NULL),
(18, 'Bali Tour', 'Bali is a good place for relaxation', '3 star', 'ac vehicle', 'breakfast', 'beach', 'Jan', NULL, NULL, 2, 0, '25000.00', '5000.00', 0, 0, 'default.png', '2019-12-05 07:35:39.658297', 9, 6, 123, 0, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_tourpackagetheme`
--

CREATE TABLE `travel_tour_tourpackagetheme` (
  `id` int(11) NOT NULL,
  `title` varchar(60) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_tourpackagetheme`
--

INSERT INTO `travel_tour_tourpackagetheme` (`id`, `title`, `created_at`, `status`, `image`) VALUES
(1, 'Honeymoon', '2019-05-02 13:30:34.159027', 1, 'default.png'),
(2, 'Theme 2', '2019-05-02 13:31:09.529825', 1, 'default.png');

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_tourpackagethememiddle`
--

CREATE TABLE `travel_tour_tourpackagethememiddle` (
  `id` int(11) NOT NULL,
  `tourPackage_id` int(11) NOT NULL,
  `tourpackagetheme_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_tourpackagethememiddle`
--

INSERT INTO `travel_tour_tourpackagethememiddle` (`id`, `tourPackage_id`, `tourpackagetheme_id`) VALUES
(3, 9, 1),
(4, 9, 2),
(11, 9, 1),
(12, 9, 2),
(13, 16, 1),
(14, 16, 2),
(16, 18, 2),
(17, 17, 2);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_tourpkgreview`
--

CREATE TABLE `travel_tour_tourpkgreview` (
  `id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `star_count` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `tour_pkg_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_travelcompany`
--

CREATE TABLE `travel_tour_travelcompany` (
  `id` int(11) NOT NULL,
  `name` varchar(60) DEFAULT NULL,
  `description` longtext NOT NULL,
  `words_by_owner` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` int(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `is_active` tinyint(1) DEFAULT '0',
  `is_verified` tinyint(1) DEFAULT '0',
  `rateforforeign` decimal(10,2) DEFAULT NULL,
  `ratefornepali` decimal(10,2) DEFAULT NULL,
  `rateforsaarc` decimal(10,2) DEFAULT NULL,
  `cino` varchar(60) DEFAULT NULL,
  `estd_date` varchar(60) DEFAULT NULL,
  `iata` tinyint(1) NOT NULL,
  `nameonpancard` varchar(60) DEFAULT NULL,
  `pannumber` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_travelcompany`
--

INSERT INTO `travel_tour_travelcompany` (`id`, `name`, `description`, `words_by_owner`, `created_at`, `status`, `image`, `owner_id`, `is_active`, `is_verified`, `rateforforeign`, `ratefornepali`, `rateforsaarc`, `cino`, `estd_date`, `iata`, `nameonpancard`, `pannumber`) VALUES
(4, 'Earl Hawkins', 'wubehij', 'wastu', '2019-05-06 07:17:53.147028', 0, 'rivverrunner_MJrYxGF.jpeg', 9, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL),
(5, 'Thomas Lopez', 'ageapa', 'zi', '2019-05-24 05:44:36.069255', 0, 'default.png', 9, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL),
(6, 'Flora Townsend', 'some descripton', 'ocuguwom', '2019-07-22 10:58:16.323085', 0, 'default.png', 9, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL),
(7, 'Lois Cannon', 'apuz', 'wihub', '2019-07-24 05:07:46.205011', 0, 'default.png', 9, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL),
(8, 'asd', 'asd', 'sad', '2019-11-22 11:25:59.819098', 0, 'adobe-illustrator-euclidean-vector-yellow-little-sun.png', 4, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL),
(9, 'KTM Voyage Travel and Tours', 'A travel company providing all travel related services such as flight ticket, tour packages, hotel bookings and many more', 'We are the leading travel service provider company', '2019-12-04 09:46:57.556526', 0, 'KTM_logo_1.png', 10, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_travelexcluded`
--

CREATE TABLE `travel_tour_travelexcluded` (
  `id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `tour_package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_travelexcluded`
--

INSERT INTO `travel_tour_travelexcluded` (`id`, `description`, `created_at`, `tour_package_id`) VALUES
(1, 'some more desc', '2019-05-24 05:56:02.754075', 4),
(2, 'some desccc', '2019-07-22 11:02:41.013552', 9),
(4, 'some description2', '2019-07-22 12:16:13.067813', 2),
(5, 'some item', '2019-07-22 12:28:46.800960', 8),
(6, 'some desc', '2019-07-22 12:44:01.567328', 9),
(7, 'some dess', '2019-07-22 12:50:24.225827', 9),
(8, 'some dess', '2019-07-22 12:54:10.325453', 9),
(9, 'some description', '2019-07-23 06:02:57.527818', 9),
(10, 'some more description', '2019-07-23 06:02:57.541014', 9),
(11, 'some description', '2019-07-23 06:08:24.566314', 9),
(12, 'excluded item 1', '2019-07-23 08:06:49.736462', 10),
(13, 'excluded item 2', '2019-07-23 08:06:49.740853', 10),
(14, 'no excluded item', '2019-07-23 08:24:59.956823', 11),
(15, 'excluded 1', '2019-07-23 10:15:38.185253', 12),
(16, 'International Airfare &amp; Airport tax', '2019-12-04 09:54:42.221245', 16),
(17, 'Insurance Fee', '2019-12-04 09:54:42.223562', 16),
(18, 'Lunch in Kathmandu & Pokhara', '2019-12-04 09:54:42.225314', 16),
(19, 'Any other expenses not mentioned in the above cost', '2019-12-04 09:54:42.230905', 16),
(20, 'Manakamana Cable Car tickets', '2019-12-04 09:54:42.232933', 16),
(21, 'Personal Expenses', '2019-12-05 09:04:37.771976', 17);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_travelfacilities`
--

CREATE TABLE `travel_tour_travelfacilities` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_travelfacilities`
--

INSERT INTO `travel_tour_travelfacilities` (`id`, `name`, `image`, `created_at`) VALUES
(1, 'Fac 1', 'default.png', '2019-05-02 13:30:45.086805'),
(2, 'Fac 2', 'default.png', '2019-05-02 13:30:50.791743'),
(3, 'Fac 3', 'default.png', '2019-05-02 13:30:57.057672');

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_travelfacilitiesmiddle`
--

CREATE TABLE `travel_tour_travelfacilitiesmiddle` (
  `id` int(11) NOT NULL,
  `travel_tours_id` int(11) NOT NULL,
  `travelsfacilities_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_travelfacilitiesmiddle`
--

INSERT INTO `travel_tour_travelfacilitiesmiddle` (`id`, `travel_tours_id`, `travelsfacilities_id`) VALUES
(3, 1, 1),
(4, 1, 2),
(5, 2, 1),
(6, 2, 3),
(15, 4, 1),
(16, 4, 2),
(20, 5, 3),
(24, 3, 1),
(25, 3, 2),
(26, 3, 3),
(27, 6, 3),
(28, 7, 3),
(29, 8, 3),
(30, 9, 1),
(31, 10, 2),
(32, 11, 1),
(33, 11, 2),
(34, 12, 2),
(35, 13, 2),
(36, 14, 3),
(37, 15, 1),
(38, 16, 1),
(39, 16, 2),
(41, 18, 2),
(42, 17, 2);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_travelinclude`
--

CREATE TABLE `travel_tour_travelinclude` (
  `id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `tour_package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_travelinclude`
--

INSERT INTO `travel_tour_travelinclude` (`id`, `description`, `created_at`, `tour_package_id`) VALUES
(1, 'included 1', '2019-05-02 13:35:08.501917', 1),
(2, 'Included 2', '2019-05-02 13:35:08.506691', 1),
(3, 'some description', '2019-05-03 05:54:47.516408', 2),
(4, 'some description', '2019-05-06 07:40:22.065395', 3),
(5, 'some description', '2019-05-24 05:55:53.015399', 4),
(6, 'some items are included', '2019-07-22 11:01:43.732330', 5),
(7, 'some description', '2019-07-22 11:51:30.720716', 7),
(8, 'some descccc', '2019-07-22 12:28:38.048362', 8),
(9, 'some descc', '2019-07-22 12:43:56.463245', 9),
(10, 'iicluded item 1', '2019-07-23 08:06:33.177887', 10),
(11, 'included item 2', '2019-07-23 08:06:33.181760', 10),
(12, 'some descc', '2019-07-23 08:24:48.758223', 11),
(13, 'included 1', '2019-07-23 10:15:30.255303', 12),
(14, '05 Nights accommodation at Respective Hotel on Half Board basis [B/fast &amp; Dinner]\r\n', '2019-12-04 09:52:49.053457', 16),
(15, 'Arrival and departure transfer and sightseeing tours A/C Vehicle', '2019-12-04 09:52:49.055865', 16),
(16, 'All current government taxes as applicable', '2019-12-04 09:52:49.057706', 16),
(17, 'Breakfast Everyday', '2019-12-04 09:52:49.060769', 16),
(18, 'Roundtrip airfare', '2019-12-05 09:04:24.221917', 17);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_travelitenary`
--

CREATE TABLE `travel_tour_travelitenary` (
  `id` int(11) NOT NULL,
  `day` varchar(60) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `tour_package_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `activities` varchar(1000) DEFAULT NULL,
  `hotel` varchar(500) DEFAULT NULL,
  `meal` varchar(100) DEFAULT NULL,
  `transfer` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_travelitenary`
--

INSERT INTO `travel_tour_travelitenary` (`id`, `day`, `description`, `created_at`, `tour_package_id`, `image`, `activities`, `hotel`, `meal`, `transfer`) VALUES
(1, 'Day1 ', 'some description', '2019-05-02 13:34:20.794305', 1, 'default.png', NULL, NULL, NULL, NULL),
(2, 'Day2 ', 'some description', '2019-05-02 13:34:20.801986', 1, 'default.png', NULL, NULL, NULL, NULL),
(3, 'day 2', 'some description', '2019-05-03 05:54:33.730806', 2, 'default.png', NULL, NULL, NULL, NULL),
(4, '1', 'lud', '2019-05-06 07:40:15.207515', 3, 'default.png', NULL, NULL, NULL, NULL),
(5, '2', 'some description', '2019-05-06 07:40:15.212984', 3, 'default.png', NULL, NULL, NULL, NULL),
(6, 'day 1', 'some activity', '2019-05-24 05:55:31.194591', 4, 'default.png', NULL, NULL, NULL, NULL),
(7, '1', 'some description', '2019-07-22 11:01:30.789603', 5, 'default.png', NULL, NULL, NULL, NULL),
(8, 'day 1', 'some desc', '2019-07-22 11:51:04.045398', 7, 'default.png', NULL, NULL, NULL, NULL),
(9, 'day 1', 'some desc', '2019-07-22 12:28:31.035877', 8, 'default.png', NULL, NULL, NULL, NULL),
(10, 'day 1', 'some desc', '2019-07-22 12:43:51.121384', 9, 'default.png', NULL, NULL, NULL, NULL),
(11, '1', 'some activity', '2019-07-23 08:06:16.246220', 10, 'default.png', NULL, NULL, NULL, NULL),
(12, '1', 'some activity', '2019-07-23 08:24:44.498719', 11, 'default.png', NULL, NULL, NULL, NULL),
(13, '1', 'some activity', '2019-07-23 10:15:21.880175', 12, 'default.png', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_traveloffers`
--

CREATE TABLE `travel_tour_traveloffers` (
  `id` int(11) NOT NULL,
  `offer_name` varchar(80) DEFAULT NULL,
  `description` longtext NOT NULL,
  `start_date` datetime(6) DEFAULT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `banner_image` varchar(100) NOT NULL,
  `rate` decimal(20,2) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `module` varchar(80) DEFAULT NULL,
  `creator_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `travel_tour_traveloffers`
--

INSERT INTO `travel_tour_traveloffers` (`id`, `offer_name`, `description`, `start_date`, `end_date`, `banner_image`, `rate`, `status`, `module`, `creator_id`) VALUES
(1, 'Olive Bradley', 'some descc', '2019-01-01 00:00:00.000000', '2019-10-01 00:00:00.000000', 'default.png', '12.00', 1, 'travel_tour', 9);

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_travelstaff`
--

CREATE TABLE `travel_tour_travelstaff` (
  `name` varchar(80) DEFAULT NULL,
  `contact` bigint(20) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `current_package` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `owner_id_id` int(11) DEFAULT NULL,
  `travel_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `travel_tour_travel_tourowner`
--

CREATE TABLE `travel_tour_travel_tourowner` (
  `name` varchar(80) DEFAULT NULL,
  `contact` bigint(20) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `address` varchar(80) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `current_company` int(11) NOT NULL,
  `current_package` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users_address`
--

CREATE TABLE `users_address` (
  `id` int(11) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `address1` varchar(100) NOT NULL,
  `address2` varchar(100) NOT NULL,
  `contactno` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `is_primary` varchar(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users_users`
--

CREATE TABLE `users_users` (
  `contact` bigint(20) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `gender` varchar(8) DEFAULT NULL,
  `dob` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_account_type`
--
ALTER TABLE `account_account_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `account_bankdetail`
--
ALTER TABLE `account_bankdetail`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_bankdetail_hotel_id_2b92b967_fk_hotel_hotels_id` (`hotel_id`),
  ADD KEY `account_bankdetail_bankCountry_id_ef0a2402` (`bankCountry_id`);

--
-- Indexes for table `account_faq`
--
ALTER TABLE `account_faq`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `account_language`
--
ALTER TABLE `account_language`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `account_ownerprofile`
--
ALTER TABLE `account_ownerprofile`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `account_passwordreset`
--
ALTER TABLE `account_passwordreset`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `account_staffprofile`
--
ALTER TABLE `account_staffprofile`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `account_staffprofile_owner_id_b6299f26_fk_account_o` (`owner_id`);

--
-- Indexes for table `account_user`
--
ALTER TABLE `account_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `account_user_account_type`
--
ALTER TABLE `account_user_account_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_user_account_type_user_id_account_type_id_ab2bb134_uniq` (`user_id`,`account_type_id`),
  ADD KEY `account_user_account_account_type_id_4264ed94_fk_account_a` (`account_type_id`);

--
-- Indexes for table `account_user_groups`
--
ALTER TABLE `account_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_user_groups_user_id_group_id_4d09af3e_uniq` (`user_id`,`group_id`),
  ADD KEY `account_user_groups_group_id_6c71f749_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `account_user_user_permissions`
--
ALTER TABLE `account_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_user_user_permis_user_id_permission_id_48bdd28b_uniq` (`user_id`,`permission_id`),
  ADD KEY `account_user_user_pe_permission_id_66c44191_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `blog_blog`
--
ALTER TABLE `blog_blog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking_bookingtable`
--
ALTER TABLE `booking_bookingtable`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_bookingtable_customer_id_6d50345f_fk_booking_c` (`customer_id`);

--
-- Indexes for table `booking_businesscashbonus`
--
ALTER TABLE `booking_businesscashbonus`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_businesscash_transaction_id_819255eb_fk_booking_b` (`transaction_id`),
  ADD KEY `booking_businesscash_user_id_bc8ec509_fk_booking_c` (`user_id`),
  ADD KEY `booking_businesscash_booking_id_d58bb0c2_fk_booking_m` (`booking_id`);

--
-- Indexes for table `booking_businesspartners`
--
ALTER TABLE `booking_businesspartners`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking_customer`
--
ALTER TABLE `booking_customer`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `booking_customer_country_id_73bfa8d1_fk_hotel_country_id` (`country_id`),
  ADD KEY `booking_customer_partnerplan_id_ad442ab0_fk_booking_b` (`partnerplan_id`),
  ADD KEY `booking_customer_memplan_id_831d8b97_fk_points_me` (`memplan_id`);

--
-- Indexes for table `booking_guestdetail`
--
ALTER TABLE `booking_guestdetail`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_guestdetail_customer_id_7de78b0e_fk_booking_c` (`customer_id`),
  ADD KEY `booking_guestdetail_booking_id_9dff880c_fk_booking_b` (`booking_id`);

--
-- Indexes for table `booking_guestdocdetail`
--
ALTER TABLE `booking_guestdocdetail`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_guestdocdeta_guest_detail_id_caa887bb_fk_booking_g` (`guest_detail_id`);

--
-- Indexes for table `booking_hotelbookinglog`
--
ALTER TABLE `booking_hotelbookinglog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_hotelbooking_staff_id_d5995c2f_fk_account_s` (`staff_id`),
  ADD KEY `booking_hotelbooking_booking_id_d94252cb_fk_booking_b` (`booking_id`);

--
-- Indexes for table `booking_modulebooking`
--
ALTER TABLE `booking_modulebooking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_modulebookin_booking_id_e693ebcf_fk_booking_b` (`booking_id`);

--
-- Indexes for table `booking_pointslog`
--
ALTER TABLE `booking_pointslog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_pointslog_customer_id_fcfe2496_fk_booking_c` (`customer_id`);

--
-- Indexes for table `booking_pointsonsale`
--
ALTER TABLE `booking_pointsonsale`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking_refereeandreferred`
--
ALTER TABLE `booking_refereeandreferred`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `to_id` (`to_id`),
  ADD KEY `booking_refereeandre_by_id_bfa705f3_fk_booking_c` (`by_id`),
  ADD KEY `booking_refereeandre_partnership_id_f112a0ce_fk_booking_b` (`partnership_id`);

--
-- Indexes for table `booking_reward`
--
ALTER TABLE `booking_reward`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_reward_booking_id_fa1179f1_fk_booking_bookingtable_id` (`booking_id`),
  ADD KEY `booking_reward_customer_id_c924b6d3_fk_booking_customer_user_id` (`customer_id`);

--
-- Indexes for table `booking_teamleader`
--
ALTER TABLE `booking_teamleader`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_account_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `hotel_bedtype`
--
ALTER TABLE `hotel_bedtype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_cancellation_policy`
--
ALTER TABLE `hotel_cancellation_policy`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_cancellation_p_inventory_id_9b8f041e_fk_hotel_hot` (`hotel_id`);

--
-- Indexes for table `hotel_city`
--
ALTER TABLE `hotel_city`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_city_state_id_e7b31ebb_fk_hotel_state_id` (`state_id`),
  ADD KEY `hotel_city_country_id_8f22dd6c_fk_hotel_country_id` (`country_id`);

--
-- Indexes for table `hotel_country`
--
ALTER TABLE `hotel_country`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_favourites`
--
ALTER TABLE `hotel_favourites`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_favourites_user_id_9619e1b5_fk_account_user_id` (`user_id`);

--
-- Indexes for table `hotel_hoteladdress`
--
ALTER TABLE `hotel_hoteladdress`
  ADD PRIMARY KEY (`hotel_id`),
  ADD KEY `hotel_hoteladdress_city_id_95410556_fk_hotel_city_id` (`city_id`),
  ADD KEY `hotel_hoteladdress_country_id_0a2772b5_fk_hotel_country_id` (`country_id`),
  ADD KEY `hotel_hoteladdress_state_id_4038bb06_fk_hotel_state_id` (`state_id`);

--
-- Indexes for table `hotel_hoteladdress_landmarks`
--
ALTER TABLE `hotel_hoteladdress_landmarks`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `hotel_hoteladdress_landm_hoteladdress_id_landmark_fba4fdcd_uniq` (`hoteladdress_id`,`landmark_id`),
  ADD KEY `hotel_hoteladdress_l_landmark_id_5a74cc4c_fk_hotel_lan` (`landmark_id`);

--
-- Indexes for table `hotel_hotelamenities`
--
ALTER TABLE `hotel_hotelamenities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_hotelbooking`
--
ALTER TABLE `hotel_hotelbooking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelbooking_hotelinventory_id_id_c4db1930_fk_hotel_hot` (`hotelinventory_id_id`),
  ADD KEY `hotel_hotelbooking_user_id_id_e11e1da9_fk_users_users_user_id` (`user_id_id`);

--
-- Indexes for table `hotel_hotelfacilities`
--
ALTER TABLE `hotel_hotelfacilities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_hotelfacilitiesmiddle`
--
ALTER TABLE `hotel_hotelfacilitiesmiddle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelfacilitie_hotels_id_02fcfcd3_fk_hotel_hot` (`hotels_id`),
  ADD KEY `hotel_hotelfacilitie_hotelsfacilities_id_ef23a558_fk_hotel_hot` (`hotelsfacilities_id`);

--
-- Indexes for table `hotel_hotelfacilitiesmiddlenew`
--
ALTER TABLE `hotel_hotelfacilitiesmiddlenew`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelfacilitie_hotels_id_96607b20_fk_hotel_hot` (`hotels_id`),
  ADD KEY `hotel_hotelfacilitie_hotelsfacilities_id_962a59ee_fk_hotel_hot` (`hotelsfacilities_id`);

--
-- Indexes for table `hotel_hotelgallery`
--
ALTER TABLE `hotel_hotelgallery`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelgallery_hotel_id_id_fb586548_fk_hotel_hotels_id` (`hotel_id_id`);

--
-- Indexes for table `hotel_hotelinventory`
--
ALTER TABLE `hotel_hotelinventory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelinventory_hotel_id_6016c85a_fk_hotel_hotels_id` (`hotel_id`),
  ADD KEY `hotel_hotelinventory_user_id_3f66c4ac_fk_account_user_id` (`user_id`);

--
-- Indexes for table `hotel_hotelinventory_amenities`
--
ALTER TABLE `hotel_hotelinventory_amenities`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelinventory_hotelamenities_id_c5dd189d_fk_hotel_hot` (`hotelamenities_id`),
  ADD KEY `hotel_hotelinventory_hotelinventory_id_2acfbd32_fk_hotel_hot` (`hotelinventory_id`);

--
-- Indexes for table `hotel_hotelinventory_roomfeatures`
--
ALTER TABLE `hotel_hotelinventory_roomfeatures`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelinventory_hotelinventory_id_da2c2a4c_fk_hotel_hot` (`hotelinventory_id`),
  ADD KEY `hotel_hotelinventory_hotelroomfeature_id_f3996ebf_fk_hotel_hot` (`hotelroomfeature_id`);

--
-- Indexes for table `hotel_hotelinventory_roomtype`
--
ALTER TABLE `hotel_hotelinventory_roomtype`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelinventory_hotelinventory_id_acab3e1f_fk_hotel_hot` (`hotelinventory_id`),
  ADD KEY `hotel_hotelinventory_hotelroomtype_id_cff1b38d_fk_hotel_hot` (`hotelroomtype_id`);

--
-- Indexes for table `hotel_hotellanguagemiddle`
--
ALTER TABLE `hotel_hotellanguagemiddle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotellanguagemiddle_hotels_id_f84df061_fk_hotel_hotels_id` (`hotels_id`),
  ADD KEY `hotel_hotellanguagem_language_id_b13456ca_fk_account_l` (`language_id`);

--
-- Indexes for table `hotel_hotellog`
--
ALTER TABLE `hotel_hotellog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotellog_user_id_id_74a1b8c9_fk_users_users_user_id` (`user_id_id`);

--
-- Indexes for table `hotel_hotelowner`
--
ALTER TABLE `hotel_hotelowner`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `hotel_hotelreview`
--
ALTER TABLE `hotel_hotelreview`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelreview_user_id_id_1c2ce23b_fk_account_user_id` (`user_id_id`);

--
-- Indexes for table `hotel_hotelroomfeature`
--
ALTER TABLE `hotel_hotelroomfeature`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_hotelroomtype`
--
ALTER TABLE `hotel_hotelroomtype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_hotels`
--
ALTER TABLE `hotel_hotels`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotels_owner_id_id_109d5e0a_fk_account_o` (`owner_id_id`);

--
-- Indexes for table `hotel_hotelsnew`
--
ALTER TABLE `hotel_hotelsnew`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_hotelsnew_owner_id_id_3750d8e8_fk_account_o` (`owner_id_id`);

--
-- Indexes for table `hotel_hotelstaff`
--
ALTER TABLE `hotel_hotelstaff`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `contact` (`contact`),
  ADD KEY `hotel_hotelstaff_hotel_id_43793fd1_fk_hotel_hotels_id` (`hotel_id`),
  ADD KEY `hotel_hotelstaff_owner_id_id_8b5dba89_fk_hotel_hot` (`owner_id_id`);

--
-- Indexes for table `hotel_inventorygallery`
--
ALTER TABLE `hotel_inventorygallery`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_inventorygalle_hotel_inventory_id_i_9f84f676_fk_hotel_hot` (`hotel_inventory_id_id`);

--
-- Indexes for table `hotel_inventoryoffers`
--
ALTER TABLE `hotel_inventoryoffers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_inventoryoffers_offer_id_6f148ed5_fk_hotel_offers_id` (`offer_id`),
  ADD KEY `hotel_inventoryoffer_hotel_inventory_id_058b00ce_fk_hotel_hot` (`hotel_inventory_id`);

--
-- Indexes for table `hotel_inventoryupdate`
--
ALTER TABLE `hotel_inventoryupdate`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_inventoryupdate_hotel_id_8d9b6a3b_fk_hotel_hotels_id` (`hotel_id`),
  ADD KEY `hotel_inventoryupdat_inventory_id_a8e2753c_fk_hotel_hot` (`inventory_id`);

--
-- Indexes for table `hotel_inventory_bed_type`
--
ALTER TABLE `hotel_inventory_bed_type`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_inventory_bed__bed_type_id_93261249_fk_hotel_bed` (`bed_type_id`),
  ADD KEY `hotel_inventory_bed__inventory_id_5c461884_fk_hotel_hot` (`inventory_id`);

--
-- Indexes for table `hotel_landmark`
--
ALTER TABLE `hotel_landmark`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_offers`
--
ALTER TABLE `hotel_offers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_offers_creator_id_fd1fe983_fk_account_ownerprofile_user_id` (`creator_id`);

--
-- Indexes for table `hotel_spotlight`
--
ALTER TABLE `hotel_spotlight`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_spotlight_hotel_id_0c0196a4` (`hotel_id`);

--
-- Indexes for table `hotel_state`
--
ALTER TABLE `hotel_state`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_state_country_id_ea0d4d29_fk_hotel_country_id` (`country_id`);

--
-- Indexes for table `points_creditpoint`
--
ALTER TABLE `points_creditpoint`
  ADD PRIMARY KEY (`id`),
  ADD KEY `points_creditpoint_transaction_id_0c78ac5b_fk_booking_b` (`transaction_id`),
  ADD KEY `points_creditpoint_user_id_bbdaba18_fk_booking_customer_user_id` (`user_id`),
  ADD KEY `points_creditpoint_booking_id_9059397f_fk_booking_m` (`booking_id`);

--
-- Indexes for table `points_membership_plan`
--
ALTER TABLE `points_membership_plan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `points_pointsetting`
--
ALTER TABLE `points_pointsetting`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `points_rewardpoint`
--
ALTER TABLE `points_rewardpoint`
  ADD PRIMARY KEY (`id`),
  ADD KEY `points_rewardpoint_transaction_id_d7671e2a_fk_booking_b` (`transaction_id`),
  ADD KEY `points_rewardpoint_user_id_4c0eb96c_fk_booking_customer_user_id` (`user_id`),
  ADD KEY `points_rewardpoint_booking_id_27153d34_fk_booking_m` (`booking_id`);

--
-- Indexes for table `points_virtualpoint`
--
ALTER TABLE `points_virtualpoint`
  ADD PRIMARY KEY (`id`),
  ADD KEY `points_virtualpoint_transaction_id_2e0cf6a2_fk_booking_b` (`transaction_id`),
  ADD KEY `points_virtualpoint_user_id_bd44ee9a_fk_booking_customer_user_id` (`user_id`),
  ADD KEY `points_virtualpoint_booking_id_420ccf89_fk_booking_m` (`booking_id`);

--
-- Indexes for table `rental_bankdetail`
--
ALTER TABLE `rental_bankdetail`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_bankdetail_company_id_fdab5a27_fk_rental_rentalcompany_id` (`company_id`),
  ADD KEY `rental_bankdetail_bankCountry_id_3713f305` (`bankCountry_id`);

--
-- Indexes for table `rental_rentalcompany`
--
ALTER TABLE `rental_rentalcompany`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_rentalcompany_owner_id_8d4858dc_fk_account_user_id` (`owner_id`);

--
-- Indexes for table `rental_rentalcompanyaddress`
--
ALTER TABLE `rental_rentalcompanyaddress`
  ADD PRIMARY KEY (`company_id`),
  ADD KEY `rental_rentalcompanyaddress_city_id_46ec8358_fk_hotel_city_id` (`city_id`),
  ADD KEY `rental_rentalcompany_country_id_f7118efa_fk_hotel_cou` (`country_id`),
  ADD KEY `rental_rentalcompanyaddress_state_id_7b6d085c_fk_hotel_state_id` (`state_id`);

--
-- Indexes for table `rental_rentalcompanyaddress_landmarks`
--
ALTER TABLE `rental_rentalcompanyaddress_landmarks`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rental_rentalcompanyaddr_rentalcompanyaddress_id__33cc2cf3_uniq` (`rentalcompanyaddress_id`,`landmark_id`),
  ADD KEY `rental_rentalcompany_landmark_id_b0ed581c_fk_hotel_lan` (`landmark_id`);

--
-- Indexes for table `rental_rentaloffers`
--
ALTER TABLE `rental_rentaloffers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_rentaloffers_creator_id_b52603d5_fk_account_o` (`creator_id`);

--
-- Indexes for table `rental_rentalsfacilities`
--
ALTER TABLE `rental_rentalsfacilities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rental_spotlight`
--
ALTER TABLE `rental_spotlight`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_spotlight_vehicle_inventory_id_b4b8ad8f_fk_rental_ve` (`vehicle_inventory_id`);

--
-- Indexes for table `rental_vehiclebrand`
--
ALTER TABLE `rental_vehiclebrand`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_vehiclebrand_category_id_1e25ec68_fk_rental_ve` (`category_id`);

--
-- Indexes for table `rental_vehiclecategory`
--
ALTER TABLE `rental_vehiclecategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rental_vehicledetail`
--
ALTER TABLE `rental_vehicledetail`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_vehicledetail_vehicle_category_id_4c2c5512_fk_rental_ve` (`vehicle_category_id`),
  ADD KEY `rental_vehicledetail_rental_company_id_7b7d3bbe_fk_rental_re` (`rental_company_id`),
  ADD KEY `rental_vehicledetail_vehicle_brand_id_2c9dcc56_fk_rental_ve` (`vehicle_brand_id`);

--
-- Indexes for table `rental_vehicleinventory`
--
ALTER TABLE `rental_vehicleinventory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_vehicleinvent_rental_company_id_a88b6584_fk_rental_re` (`rental_company_id`),
  ADD KEY `rental_vehicleinvent_vehicle_detail_id_6038d2b2_fk_rental_ve` (`vehicle_detail_id`),
  ADD KEY `rental_vehicleinvent_vehicle_location_id_5f947f95_fk_hotel_cit` (`vehicle_location_id`),
  ADD KEY `rental_vehicleinvent_vehicle_brand_id_cb8097de_fk_rental_ve` (`vehicle_brand_id`),
  ADD KEY `rental_vehicleinvent_vehicle_category_id_31e33812_fk_rental_ve` (`vehicle_category_id`);

--
-- Indexes for table `rental_vehicleinventorygallery`
--
ALTER TABLE `rental_vehicleinventorygallery`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_vehicleinvent_rentalInventory_id_be84a732_fk_rental_ve` (`rentalInventory_id`);

--
-- Indexes for table `rental_vehicleinventory_vehiclefacilities`
--
ALTER TABLE `rental_vehicleinventory_vehiclefacilities`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_vehicleinvent_vehicleFacilities_id_8055db51_fk_rental_re` (`vehicleFacilities_id`),
  ADD KEY `rental_vehicleinvent_vehicleinventory_id_de1be848_fk_rental_ve` (`vehicleinventory_id`);

--
-- Indexes for table `rental_vehicleoffers`
--
ALTER TABLE `rental_vehicleoffers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rental_vehicleoffers_offer_id_b28f4c38_fk_rental_rentaloffers_id` (`offer_id`),
  ADD KEY `rental_vehicleoffers_vehicle_inventory_id_7869840f_fk_rental_ve` (`vehicle_inventory_id`);

--
-- Indexes for table `restaurant_restaurantcategory`
--
ALTER TABLE `restaurant_restaurantcategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `restaurant_restaurantcompany`
--
ALTER TABLE `restaurant_restaurantcompany`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurant_restauran_category_id_fcf91d63_fk_restauran` (`category_id`),
  ADD KEY `restaurant_restauran_owner_id_d5f57151_fk_account_u` (`owner_id`);

--
-- Indexes for table `restaurant_restaurantcompanyaddress`
--
ALTER TABLE `restaurant_restaurantcompanyaddress`
  ADD PRIMARY KEY (`company_id`),
  ADD KEY `restaurant_restauran_city_id_ef7902e6_fk_hotel_cit` (`city_id`),
  ADD KEY `restaurant_restauran_country_id_12e896c0_fk_hotel_cou` (`country_id`),
  ADD KEY `restaurant_restauran_state_id_89b9ce13_fk_hotel_sta` (`state_id`);

--
-- Indexes for table `restaurant_restaurantcompanyaddress_landmarks`
--
ALTER TABLE `restaurant_restaurantcompanyaddress_landmarks`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `restaurant_restaurantcom_restaurantcompanyaddress_b387d229_uniq` (`restaurantcompanyaddress_id`,`landmark_id`),
  ADD KEY `restaurant_restauran_landmark_id_7ced5ec5_fk_hotel_lan` (`landmark_id`);

--
-- Indexes for table `restaurant_restaurantfacilities`
--
ALTER TABLE `restaurant_restaurantfacilities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `restaurant_restaurantfacilitys`
--
ALTER TABLE `restaurant_restaurantfacilitys`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurant_restauran_restaurantcompany_id_9cc1ed95_fk_restauran` (`restaurantcompany_id`),
  ADD KEY `restaurant_restauran_restaurantfacility_i_5bcec428_fk_restauran` (`restaurantfacility_id`);

--
-- Indexes for table `restaurant_restaurantgallery`
--
ALTER TABLE `restaurant_restaurantgallery`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurant_restauran_restaurant_company_i_8c27f140_fk_restauran` (`restaurant_company_id`);

--
-- Indexes for table `restaurant_restaurantinventory`
--
ALTER TABLE `restaurant_restaurantinventory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurant_restauran_company_id_6ae67df2_fk_restauran` (`company_id`),
  ADD KEY `restaurant_restauran_table_category_id_5220d4b1_fk_restauran` (`table_category_id`);

--
-- Indexes for table `restaurant_restaurantmenu`
--
ALTER TABLE `restaurant_restaurantmenu`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurant_restauran_restaurant_id_aa68b3b1_fk_restauran` (`restaurant_id`);

--
-- Indexes for table `restaurant_restaurantoffers`
--
ALTER TABLE `restaurant_restaurantoffers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurant_restauran_creator_id_955ab8ca_fk_account_o` (`creator_id`);

--
-- Indexes for table `restaurant_restaurantspecial`
--
ALTER TABLE `restaurant_restaurantspecial`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurant_restauran_restaurant_id_1bc4d4fb_fk_restauran` (`restaurant_id`);

--
-- Indexes for table `restaurant_restauranttablecategory`
--
ALTER TABLE `restaurant_restauranttablecategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `restaurant_spotlight`
--
ALTER TABLE `restaurant_spotlight`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurant_spotlight_restaurant_company_i_40bef62a_fk_restauran` (`restaurant_company_id`);

--
-- Indexes for table `travel_tour_addonactivities`
--
ALTER TABLE `travel_tour_addonactivities`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_addonact_tour_package_id_ed957e58_fk_travel_to` (`tour_package_id`);

--
-- Indexes for table `travel_tour_addoncuisine`
--
ALTER TABLE `travel_tour_addoncuisine`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_addoncui_tour_package_id_3b40b3bb_fk_travel_to` (`tour_package_id`);

--
-- Indexes for table `travel_tour_addonhotel`
--
ALTER TABLE `travel_tour_addonhotel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_addonhot_tour_package_id_57ecf4bc_fk_travel_to` (`tour_package_id`);

--
-- Indexes for table `travel_tour_addontransport`
--
ALTER TABLE `travel_tour_addontransport`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_addontra_tour_package_id_ed99dde6_fk_travel_to` (`tour_package_id`);

--
-- Indexes for table `travel_tour_packageoffers`
--
ALTER TABLE `travel_tour_packageoffers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_packageo_tour_package_id_fdbc52c1_fk_travel_to` (`tour_package_id`),
  ADD KEY `travel_tour_packageo_offer_id_ba1ecff2_fk_travel_to` (`offer_id`);

--
-- Indexes for table `travel_tour_spotlight`
--
ALTER TABLE `travel_tour_spotlight`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_spotligh_tour_package_id_a8655305_fk_travel_to` (`tour_package_id`);

--
-- Indexes for table `travel_tour_tourcompanyaddress`
--
ALTER TABLE `travel_tour_tourcompanyaddress`
  ADD PRIMARY KEY (`company_id`),
  ADD KEY `travel_tour_tourcompanyaddress_city_id_b10f27c4_fk_hotel_city_id` (`city_id`),
  ADD KEY `travel_tour_tourcomp_country_id_800797f5_fk_hotel_cou` (`country_id`),
  ADD KEY `travel_tour_tourcomp_state_id_2e9becb3_fk_hotel_sta` (`state_id`);

--
-- Indexes for table `travel_tour_tourcompanyaddress_landmarks`
--
ALTER TABLE `travel_tour_tourcompanyaddress_landmarks`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `travel_tour_tourcompanya_tourcompanyaddress_id_la_a041d470_uniq` (`tourcompanyaddress_id`,`landmark_id`),
  ADD KEY `travel_tour_tourcomp_landmark_id_dc89e88f_fk_hotel_lan` (`landmark_id`);

--
-- Indexes for table `travel_tour_tourgallery`
--
ALTER TABLE `travel_tour_tourgallery`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_tourgall_travel_id_490a0dcf_fk_travel_to` (`travel_id`);

--
-- Indexes for table `travel_tour_tourpackage`
--
ALTER TABLE `travel_tour_tourpackage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_tourpack_company_id_37e8d4ba_fk_travel_to` (`company_id`),
  ADD KEY `travel_tour_tourpack_distination_city_id_1b445be7_fk_hotel_cit` (`distination_city_id`),
  ADD KEY `travel_tour_tourpackage_start_city_id_f813b84d_fk_hotel_city_id` (`start_city_id`),
  ADD KEY `travel_tour_tourpackage_country_id_024369fe_fk_hotel_country_id` (`country_id`);

--
-- Indexes for table `travel_tour_tourpackagetheme`
--
ALTER TABLE `travel_tour_tourpackagetheme`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `travel_tour_tourpackagethememiddle`
--
ALTER TABLE `travel_tour_tourpackagethememiddle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_tourpack_tourPackage_id_03e2383e_fk_travel_to` (`tourPackage_id`),
  ADD KEY `travel_tour_tourpack_tourpackagetheme_id_cb242b40_fk_travel_to` (`tourpackagetheme_id`);

--
-- Indexes for table `travel_tour_tourpkgreview`
--
ALTER TABLE `travel_tour_tourpkgreview`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_tourpkgr_tour_pkg_id_ad3553ff_fk_travel_to` (`tour_pkg_id`),
  ADD KEY `travel_tour_tourpkgreview_user_id_33aa9e81_fk_account_user_id` (`user_id`);

--
-- Indexes for table `travel_tour_travelcompany`
--
ALTER TABLE `travel_tour_travelcompany`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_travelcompany_owner_id_ac2a7268_fk_account_user_id` (`owner_id`);

--
-- Indexes for table `travel_tour_travelexcluded`
--
ALTER TABLE `travel_tour_travelexcluded`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_travelex_tour_package_id_920f5668_fk_travel_to` (`tour_package_id`);

--
-- Indexes for table `travel_tour_travelfacilities`
--
ALTER TABLE `travel_tour_travelfacilities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `travel_tour_travelfacilitiesmiddle`
--
ALTER TABLE `travel_tour_travelfacilitiesmiddle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_travelfa_travel_tours_id_f3c221ed_fk_travel_to` (`travel_tours_id`),
  ADD KEY `travel_tour_travelfa_travelsfacilities_id_5c8623ae_fk_travel_to` (`travelsfacilities_id`);

--
-- Indexes for table `travel_tour_travelinclude`
--
ALTER TABLE `travel_tour_travelinclude`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_travelin_tour_package_id_e7f59b40_fk_travel_to` (`tour_package_id`);

--
-- Indexes for table `travel_tour_travelitenary`
--
ALTER TABLE `travel_tour_travelitenary`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_travelit_tour_package_id_82dabf7e_fk_travel_to` (`tour_package_id`);

--
-- Indexes for table `travel_tour_traveloffers`
--
ALTER TABLE `travel_tour_traveloffers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `travel_tour_travelof_creator_id_c5af273e_fk_account_o` (`creator_id`);

--
-- Indexes for table `travel_tour_travelstaff`
--
ALTER TABLE `travel_tour_travelstaff`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `contact` (`contact`),
  ADD KEY `travel_tour_travelst_owner_id_id_566d1dce_fk_travel_to` (`owner_id_id`),
  ADD KEY `travel_tour_travelst_travel_id_be58ef86_fk_travel_to` (`travel_id`);

--
-- Indexes for table `travel_tour_travel_tourowner`
--
ALTER TABLE `travel_tour_travel_tourowner`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `users_address`
--
ALTER TABLE `users_address`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_address_user_id_4c106ba4_fk_users_users_user_id` (`user_id`);

--
-- Indexes for table `users_users`
--
ALTER TABLE `users_users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_account_type`
--
ALTER TABLE `account_account_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `account_bankdetail`
--
ALTER TABLE `account_bankdetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `account_faq`
--
ALTER TABLE `account_faq`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `account_language`
--
ALTER TABLE `account_language`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `account_passwordreset`
--
ALTER TABLE `account_passwordreset`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `account_user`
--
ALTER TABLE `account_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;
--
-- AUTO_INCREMENT for table `account_user_account_type`
--
ALTER TABLE `account_user_account_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
--
-- AUTO_INCREMENT for table `account_user_groups`
--
ALTER TABLE `account_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `account_user_user_permissions`
--
ALTER TABLE `account_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=457;
--
-- AUTO_INCREMENT for table `blog_blog`
--
ALTER TABLE `blog_blog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `booking_bookingtable`
--
ALTER TABLE `booking_bookingtable`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_businesscashbonus`
--
ALTER TABLE `booking_businesscashbonus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_businesspartners`
--
ALTER TABLE `booking_businesspartners`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_guestdetail`
--
ALTER TABLE `booking_guestdetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_guestdocdetail`
--
ALTER TABLE `booking_guestdocdetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `booking_hotelbookinglog`
--
ALTER TABLE `booking_hotelbookinglog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_modulebooking`
--
ALTER TABLE `booking_modulebooking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_pointslog`
--
ALTER TABLE `booking_pointslog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_pointsonsale`
--
ALTER TABLE `booking_pointsonsale`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_refereeandreferred`
--
ALTER TABLE `booking_refereeandreferred`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_reward`
--
ALTER TABLE `booking_reward`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `booking_teamleader`
--
ALTER TABLE `booking_teamleader`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=115;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=382;
--
-- AUTO_INCREMENT for table `hotel_bedtype`
--
ALTER TABLE `hotel_bedtype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `hotel_cancellation_policy`
--
ALTER TABLE `hotel_cancellation_policy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `hotel_city`
--
ALTER TABLE `hotel_city`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=132;
--
-- AUTO_INCREMENT for table `hotel_country`
--
ALTER TABLE `hotel_country`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=741;
--
-- AUTO_INCREMENT for table `hotel_favourites`
--
ALTER TABLE `hotel_favourites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `hotel_hoteladdress_landmarks`
--
ALTER TABLE `hotel_hoteladdress_landmarks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=183;
--
-- AUTO_INCREMENT for table `hotel_hotelamenities`
--
ALTER TABLE `hotel_hotelamenities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `hotel_hotelbooking`
--
ALTER TABLE `hotel_hotelbooking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `hotel_hotelfacilities`
--
ALTER TABLE `hotel_hotelfacilities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `hotel_hotelfacilitiesmiddle`
--
ALTER TABLE `hotel_hotelfacilitiesmiddle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=256;
--
-- AUTO_INCREMENT for table `hotel_hotelfacilitiesmiddlenew`
--
ALTER TABLE `hotel_hotelfacilitiesmiddlenew`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `hotel_hotelgallery`
--
ALTER TABLE `hotel_hotelgallery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;
--
-- AUTO_INCREMENT for table `hotel_hotelinventory`
--
ALTER TABLE `hotel_hotelinventory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;
--
-- AUTO_INCREMENT for table `hotel_hotelinventory_amenities`
--
ALTER TABLE `hotel_hotelinventory_amenities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=811;
--
-- AUTO_INCREMENT for table `hotel_hotelinventory_roomfeatures`
--
ALTER TABLE `hotel_hotelinventory_roomfeatures`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=425;
--
-- AUTO_INCREMENT for table `hotel_hotelinventory_roomtype`
--
ALTER TABLE `hotel_hotelinventory_roomtype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=213;
--
-- AUTO_INCREMENT for table `hotel_hotellanguagemiddle`
--
ALTER TABLE `hotel_hotellanguagemiddle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
--
-- AUTO_INCREMENT for table `hotel_hotellog`
--
ALTER TABLE `hotel_hotellog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `hotel_hotelreview`
--
ALTER TABLE `hotel_hotelreview`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `hotel_hotelroomfeature`
--
ALTER TABLE `hotel_hotelroomfeature`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `hotel_hotelroomtype`
--
ALTER TABLE `hotel_hotelroomtype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `hotel_hotels`
--
ALTER TABLE `hotel_hotels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
--
-- AUTO_INCREMENT for table `hotel_hotelsnew`
--
ALTER TABLE `hotel_hotelsnew`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `hotel_inventorygallery`
--
ALTER TABLE `hotel_inventorygallery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=234;
--
-- AUTO_INCREMENT for table `hotel_inventoryoffers`
--
ALTER TABLE `hotel_inventoryoffers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `hotel_inventoryupdate`
--
ALTER TABLE `hotel_inventoryupdate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `hotel_inventory_bed_type`
--
ALTER TABLE `hotel_inventory_bed_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;
--
-- AUTO_INCREMENT for table `hotel_landmark`
--
ALTER TABLE `hotel_landmark`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;
--
-- AUTO_INCREMENT for table `hotel_offers`
--
ALTER TABLE `hotel_offers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `hotel_spotlight`
--
ALTER TABLE `hotel_spotlight`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `hotel_state`
--
ALTER TABLE `hotel_state`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;
--
-- AUTO_INCREMENT for table `points_creditpoint`
--
ALTER TABLE `points_creditpoint`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `points_membership_plan`
--
ALTER TABLE `points_membership_plan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `points_pointsetting`
--
ALTER TABLE `points_pointsetting`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `points_rewardpoint`
--
ALTER TABLE `points_rewardpoint`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `points_virtualpoint`
--
ALTER TABLE `points_virtualpoint`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `rental_bankdetail`
--
ALTER TABLE `rental_bankdetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `rental_rentalcompany`
--
ALTER TABLE `rental_rentalcompany`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `rental_rentalcompanyaddress_landmarks`
--
ALTER TABLE `rental_rentalcompanyaddress_landmarks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `rental_rentaloffers`
--
ALTER TABLE `rental_rentaloffers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `rental_rentalsfacilities`
--
ALTER TABLE `rental_rentalsfacilities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `rental_spotlight`
--
ALTER TABLE `rental_spotlight`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `rental_vehiclebrand`
--
ALTER TABLE `rental_vehiclebrand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `rental_vehiclecategory`
--
ALTER TABLE `rental_vehiclecategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `rental_vehicledetail`
--
ALTER TABLE `rental_vehicledetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `rental_vehicleinventory`
--
ALTER TABLE `rental_vehicleinventory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `rental_vehicleinventorygallery`
--
ALTER TABLE `rental_vehicleinventorygallery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `rental_vehicleinventory_vehiclefacilities`
--
ALTER TABLE `rental_vehicleinventory_vehiclefacilities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `rental_vehicleoffers`
--
ALTER TABLE `rental_vehicleoffers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `restaurant_restaurantcategory`
--
ALTER TABLE `restaurant_restaurantcategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `restaurant_restaurantcompany`
--
ALTER TABLE `restaurant_restaurantcompany`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `restaurant_restaurantcompanyaddress_landmarks`
--
ALTER TABLE `restaurant_restaurantcompanyaddress_landmarks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `restaurant_restaurantfacilities`
--
ALTER TABLE `restaurant_restaurantfacilities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `restaurant_restaurantfacilitys`
--
ALTER TABLE `restaurant_restaurantfacilitys`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `restaurant_restaurantgallery`
--
ALTER TABLE `restaurant_restaurantgallery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `restaurant_restaurantinventory`
--
ALTER TABLE `restaurant_restaurantinventory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `restaurant_restaurantmenu`
--
ALTER TABLE `restaurant_restaurantmenu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `restaurant_restaurantoffers`
--
ALTER TABLE `restaurant_restaurantoffers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `restaurant_restaurantspecial`
--
ALTER TABLE `restaurant_restaurantspecial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `restaurant_restauranttablecategory`
--
ALTER TABLE `restaurant_restauranttablecategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `restaurant_spotlight`
--
ALTER TABLE `restaurant_spotlight`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `travel_tour_addonactivities`
--
ALTER TABLE `travel_tour_addonactivities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `travel_tour_addoncuisine`
--
ALTER TABLE `travel_tour_addoncuisine`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `travel_tour_addonhotel`
--
ALTER TABLE `travel_tour_addonhotel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
--
-- AUTO_INCREMENT for table `travel_tour_addontransport`
--
ALTER TABLE `travel_tour_addontransport`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `travel_tour_packageoffers`
--
ALTER TABLE `travel_tour_packageoffers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `travel_tour_spotlight`
--
ALTER TABLE `travel_tour_spotlight`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `travel_tour_tourcompanyaddress_landmarks`
--
ALTER TABLE `travel_tour_tourcompanyaddress_landmarks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `travel_tour_tourgallery`
--
ALTER TABLE `travel_tour_tourgallery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `travel_tour_tourpackage`
--
ALTER TABLE `travel_tour_tourpackage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `travel_tour_tourpackagetheme`
--
ALTER TABLE `travel_tour_tourpackagetheme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `travel_tour_tourpackagethememiddle`
--
ALTER TABLE `travel_tour_tourpackagethememiddle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT for table `travel_tour_tourpkgreview`
--
ALTER TABLE `travel_tour_tourpkgreview`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `travel_tour_travelcompany`
--
ALTER TABLE `travel_tour_travelcompany`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `travel_tour_travelexcluded`
--
ALTER TABLE `travel_tour_travelexcluded`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT for table `travel_tour_travelfacilities`
--
ALTER TABLE `travel_tour_travelfacilities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `travel_tour_travelfacilitiesmiddle`
--
ALTER TABLE `travel_tour_travelfacilitiesmiddle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
--
-- AUTO_INCREMENT for table `travel_tour_travelinclude`
--
ALTER TABLE `travel_tour_travelinclude`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `travel_tour_travelitenary`
--
ALTER TABLE `travel_tour_travelitenary`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `travel_tour_traveloffers`
--
ALTER TABLE `travel_tour_traveloffers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `users_address`
--
ALTER TABLE `users_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_bankdetail`
--
ALTER TABLE `account_bankdetail`
  ADD CONSTRAINT `account_bankdetail_bankCountry_id_ef0a2402_fk_hotel_country_id` FOREIGN KEY (`bankCountry_id`) REFERENCES `hotel_country` (`id`),
  ADD CONSTRAINT `account_bankdetail_hotel_id_2b92b967_fk_hotel_hotels_id` FOREIGN KEY (`hotel_id`) REFERENCES `hotel_hotels` (`id`);

--
-- Constraints for table `account_passwordreset`
--
ALTER TABLE `account_passwordreset`
  ADD CONSTRAINT `account_passwordreset_user_id_8d2f98f2_fk_account_user_id` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`id`);

--
-- Constraints for table `booking_bookingtable`
--
ALTER TABLE `booking_bookingtable`
  ADD CONSTRAINT `booking_bookingtable_customer_id_6d50345f_fk_booking_c` FOREIGN KEY (`customer_id`) REFERENCES `booking_customer` (`user_id`);

--
-- Constraints for table `booking_businesscashbonus`
--
ALTER TABLE `booking_businesscashbonus`
  ADD CONSTRAINT `booking_businesscash_booking_id_d58bb0c2_fk_booking_m` FOREIGN KEY (`booking_id`) REFERENCES `booking_modulebooking` (`id`),
  ADD CONSTRAINT `booking_businesscash_transaction_id_819255eb_fk_booking_b` FOREIGN KEY (`transaction_id`) REFERENCES `booking_bookingtable` (`id`),
  ADD CONSTRAINT `booking_businesscash_user_id_bc8ec509_fk_booking_c` FOREIGN KEY (`user_id`) REFERENCES `booking_customer` (`user_id`);

--
-- Constraints for table `booking_customer`
--
ALTER TABLE `booking_customer`
  ADD CONSTRAINT `booking_customer_country_id_73bfa8d1_fk_hotel_country_id` FOREIGN KEY (`country_id`) REFERENCES `hotel_country` (`id`),
  ADD CONSTRAINT `booking_customer_memplan_id_831d8b97_fk_points_me` FOREIGN KEY (`memplan_id`) REFERENCES `points_membership_plan` (`id`),
  ADD CONSTRAINT `booking_customer_partnerplan_id_ad442ab0_fk_booking_b` FOREIGN KEY (`partnerplan_id`) REFERENCES `booking_businesspartners` (`id`),
  ADD CONSTRAINT `booking_customer_user_id_a3808e93_fk_account_user_id` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`id`);

--
-- Constraints for table `booking_guestdetail`
--
ALTER TABLE `booking_guestdetail`
  ADD CONSTRAINT `booking_guestdetail_booking_id_9dff880c_fk_booking_b` FOREIGN KEY (`booking_id`) REFERENCES `booking_bookingtable` (`id`),
  ADD CONSTRAINT `booking_guestdetail_customer_id_7de78b0e_fk_booking_c` FOREIGN KEY (`customer_id`) REFERENCES `booking_customer` (`user_id`);

--
-- Constraints for table `booking_guestdocdetail`
--
ALTER TABLE `booking_guestdocdetail`
  ADD CONSTRAINT `booking_guestdocdeta_guest_detail_id_caa887bb_fk_booking_g` FOREIGN KEY (`guest_detail_id`) REFERENCES `booking_guestdetail` (`id`);

--
-- Constraints for table `booking_hotelbookinglog`
--
ALTER TABLE `booking_hotelbookinglog`
  ADD CONSTRAINT `booking_hotelbooking_booking_id_d94252cb_fk_booking_b` FOREIGN KEY (`booking_id`) REFERENCES `booking_bookingtable` (`id`),
  ADD CONSTRAINT `booking_hotelbooking_staff_id_d5995c2f_fk_account_s` FOREIGN KEY (`staff_id`) REFERENCES `account_staffprofile` (`user_id`);

--
-- Constraints for table `booking_modulebooking`
--
ALTER TABLE `booking_modulebooking`
  ADD CONSTRAINT `booking_modulebookin_booking_id_e693ebcf_fk_booking_b` FOREIGN KEY (`booking_id`) REFERENCES `booking_bookingtable` (`id`);

--
-- Constraints for table `booking_pointslog`
--
ALTER TABLE `booking_pointslog`
  ADD CONSTRAINT `booking_pointslog_customer_id_fcfe2496_fk_booking_c` FOREIGN KEY (`customer_id`) REFERENCES `booking_customer` (`user_id`);

--
-- Constraints for table `booking_refereeandreferred`
--
ALTER TABLE `booking_refereeandreferred`
  ADD CONSTRAINT `booking_refereeandre_by_id_bfa705f3_fk_booking_c` FOREIGN KEY (`by_id`) REFERENCES `booking_customer` (`user_id`),
  ADD CONSTRAINT `booking_refereeandre_partnership_id_f112a0ce_fk_booking_b` FOREIGN KEY (`partnership_id`) REFERENCES `booking_businesspartners` (`id`),
  ADD CONSTRAINT `booking_refereeandre_to_id_f11eccd5_fk_booking_c` FOREIGN KEY (`to_id`) REFERENCES `booking_customer` (`user_id`);

--
-- Constraints for table `booking_reward`
--
ALTER TABLE `booking_reward`
  ADD CONSTRAINT `booking_reward_booking_id_fa1179f1_fk_booking_bookingtable_id` FOREIGN KEY (`booking_id`) REFERENCES `booking_bookingtable` (`id`),
  ADD CONSTRAINT `booking_reward_customer_id_c924b6d3_fk_booking_customer_user_id` FOREIGN KEY (`customer_id`) REFERENCES `booking_customer` (`user_id`);

--
-- Constraints for table `hotel_favourites`
--
ALTER TABLE `hotel_favourites`
  ADD CONSTRAINT `hotel_favourites_user_id_9619e1b5_fk_account_user_id` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`id`);

--
-- Constraints for table `hotel_inventoryupdate`
--
ALTER TABLE `hotel_inventoryupdate`
  ADD CONSTRAINT `hotel_inventoryupdat_inventory_id_a8e2753c_fk_hotel_hot` FOREIGN KEY (`inventory_id`) REFERENCES `hotel_hotelinventory` (`id`),
  ADD CONSTRAINT `hotel_inventoryupdate_hotel_id_8d9b6a3b_fk_hotel_hotels_id` FOREIGN KEY (`hotel_id`) REFERENCES `hotel_hotels` (`id`);

--
-- Constraints for table `points_creditpoint`
--
ALTER TABLE `points_creditpoint`
  ADD CONSTRAINT `points_creditpoint_booking_id_9059397f_fk_booking_m` FOREIGN KEY (`booking_id`) REFERENCES `booking_modulebooking` (`id`),
  ADD CONSTRAINT `points_creditpoint_transaction_id_0c78ac5b_fk_booking_b` FOREIGN KEY (`transaction_id`) REFERENCES `booking_bookingtable` (`id`),
  ADD CONSTRAINT `points_creditpoint_user_id_bbdaba18_fk_booking_customer_user_id` FOREIGN KEY (`user_id`) REFERENCES `booking_customer` (`user_id`);

--
-- Constraints for table `points_rewardpoint`
--
ALTER TABLE `points_rewardpoint`
  ADD CONSTRAINT `points_rewardpoint_booking_id_27153d34_fk_booking_m` FOREIGN KEY (`booking_id`) REFERENCES `booking_modulebooking` (`id`),
  ADD CONSTRAINT `points_rewardpoint_transaction_id_d7671e2a_fk_booking_b` FOREIGN KEY (`transaction_id`) REFERENCES `booking_bookingtable` (`id`),
  ADD CONSTRAINT `points_rewardpoint_user_id_4c0eb96c_fk_booking_customer_user_id` FOREIGN KEY (`user_id`) REFERENCES `booking_customer` (`user_id`);

--
-- Constraints for table `points_virtualpoint`
--
ALTER TABLE `points_virtualpoint`
  ADD CONSTRAINT `points_virtualpoint_booking_id_420ccf89_fk_booking_m` FOREIGN KEY (`booking_id`) REFERENCES `booking_modulebooking` (`id`),
  ADD CONSTRAINT `points_virtualpoint_transaction_id_2e0cf6a2_fk_booking_b` FOREIGN KEY (`transaction_id`) REFERENCES `booking_bookingtable` (`id`),
  ADD CONSTRAINT `points_virtualpoint_user_id_bd44ee9a_fk_booking_customer_user_id` FOREIGN KEY (`user_id`) REFERENCES `booking_customer` (`user_id`);

--
-- Constraints for table `rental_bankdetail`
--
ALTER TABLE `rental_bankdetail`
  ADD CONSTRAINT `rental_bankdetail_bankCountry_id_3713f305_fk_hotel_country_id` FOREIGN KEY (`bankCountry_id`) REFERENCES `hotel_country` (`id`),
  ADD CONSTRAINT `rental_bankdetail_company_id_fdab5a27_fk_rental_rentalcompany_id` FOREIGN KEY (`company_id`) REFERENCES `rental_rentalcompany` (`id`);

--
-- Constraints for table `rental_vehiclebrand`
--
ALTER TABLE `rental_vehiclebrand`
  ADD CONSTRAINT `rental_vehiclebrand_category_id_1e25ec68_fk_rental_ve` FOREIGN KEY (`category_id`) REFERENCES `rental_vehiclecategory` (`id`);

--
-- Constraints for table `rental_vehicledetail`
--
ALTER TABLE `rental_vehicledetail`
  ADD CONSTRAINT `rental_vehicledetail_vehicle_brand_id_2c9dcc56_fk_rental_ve` FOREIGN KEY (`vehicle_brand_id`) REFERENCES `rental_vehiclebrand` (`id`);

--
-- Constraints for table `rental_vehicleinventory`
--
ALTER TABLE `rental_vehicleinventory`
  ADD CONSTRAINT `rental_vehicleinvent_vehicle_brand_id_cb8097de_fk_rental_ve` FOREIGN KEY (`vehicle_brand_id`) REFERENCES `rental_vehiclebrand` (`id`),
  ADD CONSTRAINT `rental_vehicleinvent_vehicle_category_id_31e33812_fk_rental_ve` FOREIGN KEY (`vehicle_category_id`) REFERENCES `rental_vehiclecategory` (`id`);

--
-- Constraints for table `travel_tour_tourpackage`
--
ALTER TABLE `travel_tour_tourpackage`
  ADD CONSTRAINT `travel_tour_tourpackage_country_id_024369fe_fk_hotel_country_id` FOREIGN KEY (`country_id`) REFERENCES `hotel_country` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
