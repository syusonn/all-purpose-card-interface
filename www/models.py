#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'syuson'

import time,uuid
from orm import Model,StringField,BooleanField,IntegerField,TinyIntField,FloatFeild,TextField,DateTimeField,DateField,DecimalFeild

# 32位随机主键值
def next_id():
	return str(uuid.uuid4()).replace('-','')

# 卡信息表
class Card(Model):
	__table__ = 'tb_card'

	card_no = StringField(primary_key=True,ddl='varchar(30)')
	card_type = StringField(ddl='varchar(2)')
	onlline_trade_serial = IntegerField()
	offline_trade_serial = IntegerField()
	card_balance = IntegerField()
	account_balance = IntegerField()
	card_state = TinyIntField()
	issue_time = DateField()
	expire_time = DateField()
	begin_time = DateField()
	original_card_no = StringField(ddl='varchar(30)')
	holder_id = StringField(ddl='varchar(32)')
	recharge_time = DateTimeField()
	consume_time = DateTimeField()
	amount = IntegerField()
	card_kind = TinyIntField()
	issuer_code = StringField(ddl='varchar(8)')
	month_begin_time = StringField(ddl='varchar(20)')
	month_expire_time = StringField(ddl='varchar(20)')
	month_remaining_number = IntegerField()

# 卡充值流水表
class CardRecharge(object):
	__table__ = 'tb_card_recharge'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(32)')
	operator_id = StringField(ddl='varchar(32)')
	card_no = StringField(ddl='varchar(30)')
	online_trade_serial = TinyIntField()
	old_online_trade_serial = IntegerField()
	cancel_flag = TinyIntField()
	reverse_flag = TinyIntField()
	amount = IntegerField()
	card_balance = IntegerField()
	operate_time = DateTimeField()
	cancel_time = DateTimeField()
	reverse_time = DateField()
	state = IntegerField()
	clearing_at = DateField()
	card_type = StringField(ddl='varchar(32)')
	settlement_status = TinyIntField()
	settlemen_timet = DateField()

# 卡账户充值流水表
class AccountRecharge(Model):
	__table__ = 'tb_account_recharge'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(32)')
	operator_id = StringField(ddl='varchar(32)')
	card_no = StringField(ddl='varchar(30)')
	cancel_flag = TinyIntField()
	amount = IntegerField()
	account_balance = IntegerField()
	operate_time = DateTimeField()
	cancel_time = DateTimeField()
	settlement_status = IntegerField()
	settlemen_timet = DateField()


# 卡实充业务流水表
class CardRechargeCommit(Model):
	__table__ = 'tb_card_recharge_commit'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(32)')
	operator_id = StringField(ddl='varchar(32)')
	card_no = StringField(ddl='varchar(30)')
	trade_no = IntegerField()
	old_trade_no = IntegerField()
	reverse_flag = TinyIntField()
	amount = IntegerField()
	account_balance = IntegerField()
	card_balance = IntegerField()
	operate_time = DateTimeField()
	reverse_time = DateField()
	state = IntegerField()
	clearing_at = DateField()
	card_type = StringField(ddl='varchar(32)')
	transactionSerialNo = StringField(ddl='varchar(50)')

# 单元基础表
class UnitGj(Model):
	__table__ = 'tb_unit_gj'

	unit_id = StringField(primary_key=True,default=next_id,ddl='varchar(32)')
	unit_name = StringField(ddl='varchar(255)')
	parent_id = StringField(ddl='varchar(32)')
	city_code = StringField(ddl='varchar(255)')
	query_password = StringField(ddl='varchar(255)')
	supervisor = StringField(ddl='varchar(255)')
	link_phone = StringField(ddl='varchar(255)')
	address = StringField(ddl='varchar(255)')
	owner = StringField(ddl='varchar(255)')
	root_id = IntegerField()

# 脱机消费流水表
class BusinessPayOffline(Model):
	__table__ = 'tb_business_pay_offline'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(32)')
	psam_code = StringField(ddl='varchar(16)')
	terminal_trade_serial = StringField(ddl='varchar(26)')
	devCode = StringField(ddl='varchar(20)')
	trade_serial = IntegerField()
	devserial = StringField(ddl='varchar(20)')
	card_issuer_code = StringField(ddl='varchar(45)')
	tradetype = TinyIntField()
	card_type = StringField(ddl='varchar(32)')
	record_type = TinyIntField()
	citycode = IntegerField()
	orgCode = StringField(ddl='varchar(20)')
	appType = TinyIntField()
	card_number = StringField(ddl='varchar(30)')
	card_serial = StringField(ddl='varchar(45)')
	dtBegin = DateTimeField()
	dtEnd = DateTimeField()
	name = StringField(ddl='varchar(20)')
	IDCode = TinyIntField()
	IDNumber = StringField(ddl='varchar(45)')
	tradeStation = StringField(ddl='varchar(20)')
	trade_time = DateTimeField()
	trade_amount = IntegerField()
	real_paid_sum = IntegerField()
	remaining_sum = IntegerField()
	tradeStatus = TinyIntField()
	driver_number = StringField(ddl='varchar(20)')
	line_group_code = StringField(ddl='varchar(45)')
	line_code = StringField(ddl='varchar(45)')
	bus_code = StringField(ddl='varchar(45)')
	direction = TinyIntField()
	card_city_code = StringField(ddl='varchar(45)')
	paid_city_code = StringField(ddl='varchar(45)')
	tac_code = StringField(ddl='varchar(8)')
	tac_flag = IntegerField()
	area_code = StringField(ddl='varchar(45)')
	vocation_code = StringField(ddl='varchar(45)')
	mac = StringField(ddl='varchar(8)')
	state = IntegerField()
	collected_at = DateTimeField()
	inbound_at = DateTimeField()
	prepsam_code = StringField(ddl='varchar(16)')
	preterminal_trade_serial = StringField(ddl='varchar(26)')
	prerecord_type = TinyIntField()
	precitycode = IntegerField()
	preorgCode = StringField(ddl='varchar(20)')
	pretradeStation = StringField(ddl='varchar(20)')
	pretrade_time = DateTimeField()
	pretrade_amount = IntegerField()
	preremaining_sum = IntegerField()
	pretradeStatus = TinyIntField()
	predriver_number = StringField(ddl='varchar(20)')
	preline_code = StringField(ddl='varchar(45)')
	prebus_code = StringField(ddl='varchar(6)')
	predirection = StringField(ddl='varchar(4)')
	attribution = IntegerField()
	cardRandom = StringField(ddl='varchar(8)')
	terminal_code = StringField(ddl='varchar(12)')
	cardKind = IntegerField()
	consume_type = IntegerField()
	monthly_ticket_cost = IntegerField()
	monthly_ticket_total = IntegerField()
	preconsume_type = IntegerField()
	premonthly_ticket_cost = IntegerField()
	premonthly_ticket_total = IntegerField()
	operator_code = StringField(ddl='varchar(32)')
	geohash = StringField(ddl='varchar(12)')
	latitude = DecimalFeild()
	longitude = DecimalFeild()
