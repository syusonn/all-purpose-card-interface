-- schema.sql

/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50538
Source Host           : localhost:3306
Source Database       : cardcloud

Target Server Type    : MYSQL
Target Server Version : 50538
File Encoding         : 65001

Date: 2017-07-28 14:26:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_account_recharge
-- ----------------------------
DROP TABLE IF EXISTS `tb_account_recharge`;
CREATE TABLE `tb_account_recharge` (
  `id` varchar(32) NOT NULL,
  `operator_id` varchar(32) DEFAULT NULL,
  `card_no` varchar(30) DEFAULT NULL,
  `cancel_flag` tinyint(4) DEFAULT NULL,
  `amount` int(11) DEFAULT '0',
  `account_balance` int(11) DEFAULT '0',
  `operate_time` datetime DEFAULT NULL,
  `cancel_time` datetime DEFAULT NULL,
  `settlement_status` tinyint(4) DEFAULT NULL COMMENT '0：未结算； 1：已结算',
  `settlemen_timet` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_business_pay_offline
-- ----------------------------
DROP TABLE IF EXISTS `tb_business_pay_offline`;
CREATE TABLE `tb_business_pay_offline` (
  `id` varchar(32) NOT NULL,
  `psam_code` varchar(16) DEFAULT NULL,
  `terminal_trade_serial` varchar(26) DEFAULT NULL,
  `devCode` varchar(20) DEFAULT NULL,
  `trade_serial` int(11) DEFAULT NULL,
  `devserial` varchar(20) DEFAULT NULL,
  `card_issuer_code` varchar(45) DEFAULT NULL,
  `tradetype` tinyint(4) DEFAULT NULL,
  `card_type` varchar(32) DEFAULT NULL,
  `record_type` tinyint(4) DEFAULT NULL,
  `citycode` smallint(6) DEFAULT NULL,
  `orgCode` varchar(20) DEFAULT NULL,
  `appType` tinyint(4) DEFAULT NULL,
  `card_number` varchar(30) DEFAULT NULL,
  `card_serial` varchar(45) DEFAULT NULL,
  `dtBegin` datetime DEFAULT NULL,
  `dtEnd` datetime DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `IDCode` tinyint(4) DEFAULT NULL,
  `IDNumber` varchar(45) DEFAULT NULL,
  `tradeStation` varchar(20) DEFAULT NULL,
  `trade_time` datetime DEFAULT NULL,
  `trade_amount` int(11) DEFAULT NULL,
  `real_paid_sum` int(11) DEFAULT NULL,
  `remaining_sum` int(11) DEFAULT NULL,
  `tradeStatus` tinyint(4) DEFAULT NULL,
  `driver_number` varchar(20) DEFAULT NULL,
  `line_group_code` varchar(45) DEFAULT NULL,
  `line_code` varchar(45) DEFAULT NULL,
  `bus_code` varchar(45) DEFAULT NULL,
  `direction` tinyint(4) DEFAULT NULL,
  `card_city_code` varchar(45) DEFAULT NULL,
  `paid_city_code` varchar(45) DEFAULT NULL,
  `tac_code` varchar(8) DEFAULT NULL,
  `tac_flag` int(11) DEFAULT NULL,
  `area_code` varchar(45) DEFAULT NULL,
  `vocation_code` varchar(45) DEFAULT NULL,
  `mac` varchar(8) DEFAULT NULL,
  `state` int(11) DEFAULT NULL COMMENT '1:未处理；2：已处理；3作废 4：已过期 5:异常数据',
  `collected_at` datetime DEFAULT NULL,
  `inbound_at` datetime DEFAULT NULL,
  `prepsam_code` varchar(16) DEFAULT NULL,
  `preterminal_trade_serial` varchar(26) DEFAULT NULL,
  `prerecord_type` tinyint(4) DEFAULT NULL,
  `precitycode` smallint(6) DEFAULT NULL,
  `preorgCode` varchar(20) DEFAULT NULL,
  `pretradeStation` varchar(20) DEFAULT NULL,
  `pretrade_time` datetime DEFAULT NULL,
  `pretrade_amount` int(11) DEFAULT NULL,
  `preremaining_sum` int(11) DEFAULT NULL,
  `pretradeStatus` tinyint(4) DEFAULT NULL,
  `predriver_number` varchar(20) DEFAULT NULL,
  `preline_code` varchar(45) DEFAULT NULL,
  `prebus_code` varchar(6) DEFAULT NULL,
  `predirection` tinyint(4) DEFAULT NULL,
  `attribution` int(11) DEFAULT NULL,
  `cardRandom` varchar(8) DEFAULT NULL,
  `terminal_code` varchar(12) DEFAULT NULL,
  `cardKind` int(11) DEFAULT NULL COMMENT '1=CPU,2=M1',
  `consume_type` int(11) DEFAULT NULL COMMENT '1=钱，2=月票',
  `monthly_ticket_cost` int(11) DEFAULT NULL,
  `monthly_ticket_total` int(11) DEFAULT NULL,
  `preconsume_type` int(11) DEFAULT NULL COMMENT '1=钱，2=月票',
  `premonthly_ticket_cost` int(11) DEFAULT NULL,
  `premonthly_ticket_total` int(11) DEFAULT NULL,
  `operator_code` varchar(32) DEFAULT NULL,
  `geohash` varchar(12) DEFAULT NULL,
  `latitude` decimal(12,6) DEFAULT NULL,
  `longitude` decimal(12,6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_card
-- ----------------------------
DROP TABLE IF EXISTS `tb_card`;
CREATE TABLE `tb_card` (
  `card_no` varchar(30) NOT NULL,
  `card_type` varchar(2) DEFAULT NULL,
  `onlline_trade_serial` bigint(20) DEFAULT NULL,
  `offline_trade_serial` bigint(20) DEFAULT NULL,
  `card_balance` int(11) DEFAULT '0',
  `account_balance` int(11) DEFAULT '0',
  `card_state` tinyint(4) DEFAULT NULL COMMENT '0：正常；1：挂失；2：退卡；3：坏卡登记',
  `issue_time` date DEFAULT NULL,
  `expire_time` date DEFAULT NULL,
  `begin_time` date DEFAULT NULL,
  `original_card_no` varchar(30) DEFAULT NULL,
  `holder_id` varchar(32) DEFAULT NULL,
  `recharge_time` datetime DEFAULT NULL,
  `consume_time` datetime DEFAULT NULL,
  `amount` int(11) DEFAULT '0',
  `card_kind` tinyint(4) DEFAULT NULL,
  `issuer_code` varchar(8) DEFAULT NULL,
  `month_begin_time` varchar(20) DEFAULT NULL,
  `month_expire_time` varchar(20) DEFAULT NULL,
  `month_remaining_number` int(11) DEFAULT NULL,
  PRIMARY KEY (`card_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_card_recharge
-- ----------------------------
DROP TABLE IF EXISTS `tb_card_recharge`;
CREATE TABLE `tb_card_recharge` (
  `id` varchar(32) NOT NULL,
  `operator_id` varchar(32) DEFAULT NULL,
  `card_no` varchar(30) DEFAULT NULL,
  `online_trade_serial` tinyint(4) DEFAULT NULL,
  `old_online_trade_serial` int(11) DEFAULT NULL,
  `cancel_flag` tinyint(4) DEFAULT NULL COMMENT '0：未撤销；1：撤销完成',
  `reverse_flag` tinyint(4) DEFAULT NULL,
  `amount` int(11) DEFAULT '0',
  `card_balance` int(11) DEFAULT '0',
  `operate_time` datetime DEFAULT NULL,
  `cancel_time` datetime DEFAULT NULL,
  `reverse_time` date DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  `clearing_at` date DEFAULT NULL,
  `card_type` varchar(32) DEFAULT NULL,
  `settlement_status` tinyint(4) DEFAULT NULL COMMENT '0：未结算； 1：已结算',
  `settlemen_timet` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_card_recharge_commit
-- ----------------------------
DROP TABLE IF EXISTS `tb_card_recharge_commit`;
CREATE TABLE `tb_card_recharge_commit` (
  `id` varchar(32) NOT NULL,
  `operator_id` varchar(32) DEFAULT NULL,
  `card_no` varchar(30) DEFAULT NULL,
  `trade_no` int(11) DEFAULT NULL,
  `old_trade_no` int(11) DEFAULT NULL,
  `reverse_flag` tinyint(4) DEFAULT NULL COMMENT '0：未充正;1：完成充正',
  `amount` int(11) DEFAULT NULL,
  `account_balance` int(11) DEFAULT '0',
  `card_balance` int(11) DEFAULT '0',
  `operate_time` datetime DEFAULT NULL,
  `reverse_time` date DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  `clearing_at` date DEFAULT NULL,
  `card_type` varchar(32) DEFAULT NULL,
  `transactionSerialNo` varchar(50) DEFAULT NULL COMMENT '用于华通宝写卡失败时回滚',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_unit_gj
-- ----------------------------
DROP TABLE IF EXISTS `tb_unit_gj`;
CREATE TABLE `tb_unit_gj` (
  `unit_id` varchar(32) NOT NULL COMMENT '结算单元编码',
  `unit_name` varchar(255) DEFAULT NULL COMMENT '结算单元名称',
  `parent_id` varchar(32) DEFAULT NULL COMMENT '所属单元编码',
  `city_code` varchar(255) DEFAULT NULL COMMENT '结算单元编码(对应发卡方)',
  `query_password` varbinary(255) DEFAULT NULL COMMENT '查询密码',
  `supervisor` varchar(255) DEFAULT NULL COMMENT '管理者',
  `link_phone` varchar(255) DEFAULT NULL COMMENT '联系电话',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `owner` varchar(255) DEFAULT NULL COMMENT '所有者',
  `root_id` int(11) DEFAULT NULL COMMENT '根单元编码',
  PRIMARY KEY (`unit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
