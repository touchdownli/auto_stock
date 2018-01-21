#CREATE DATABASE `auto_stock` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `auto_stock`;
#drop table mock_trans;
CREATE TABLE `mock_trans` (
  `id` int(32) NOT NULL auto_increment COMMENT '',
  `code` varchar(128) NOT NULL COMMENT '',
  `trans_type` varchar(8) NOT NULL COMMENT '',
  `price` float NOT NULL COMMENT '',
  `count` int(16) NOT NULL COMMENT '',
  `trans_date` date NOT NULL comment '',
  PRIMARY KEY (`id`)
) ENGINE = MyISAM DEFAULT CHARSET = utf8;