#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'syuson'

'url handlers'

import re,time,json,logging,hashlib,base64,asyncio

from aiohttp import web

from coroweb import get,post
from apis import APIError,APIValueError,APIResourceNotFoundError,APIPermissionError,Page,operateResult

from models import Card,CardRecharge,AccountRecharge,CardRechargeCommit,UnitGj,BusinessPayOffline,next_id

# 页码
def get_page_index(page_str):
	p = 1
	try:
		p = int(page_str)
	except ValueError as e:
		pass
	if p < 1:
		p = 1
	return p

@get('/card/cardinfo')
async def api_card_info(request,*,card_no=None):
	cardList = await Card.findAll(where='card_no =?',args=[card_no])
	if len(cardList) == 0 :
		return operateResult.get_result(msg='db not card_no:%s data' % card_no)
	elif len(cardList) == 1:
		return operateResult.get_result(type=operateResult.__SUCCESS__,msg='query success',data=cardList[0])
	else:
		return operateResult.get_result(msg='invalid cardno')
	
		

