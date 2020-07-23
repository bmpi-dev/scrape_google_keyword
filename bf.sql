/*
 Navicat Premium Data Transfer

 Source Server         : localhost_mysql
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : bf

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 23/07/2020 20:23:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for google_serp_202007
-- ----------------------------
DROP TABLE IF EXISTS `google_serp_202007`;
CREATE TABLE `google_serp_202007` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `keyword_id` bigint DEFAULT NULL,
  `keyword` varchar(500) DEFAULT NULL,
  `rank` bigint DEFAULT NULL,
  `link` varchar(500) DEFAULT NULL,
  `snippet` varchar(500) DEFAULT NULL,
  `title` varchar(500) DEFAULT NULL,
  `visible_link` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31428 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for keyword
-- ----------------------------
DROP TABLE IF EXISTS `keyword`;
CREATE TABLE `keyword` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `keyword` varchar(200) NOT NULL,
  `country` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL COMMENT '0-tag, 1-store',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=37585 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for keyword_copy
-- ----------------------------
DROP TABLE IF EXISTS `keyword_copy`;
CREATE TABLE `keyword_copy` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `keyword` varchar(200) NOT NULL,
  `country` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL COMMENT '0-tag, 1-store',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=39126 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

