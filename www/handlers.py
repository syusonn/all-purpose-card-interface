#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'syuson'

'url handlers'

import re,time,json,logging,hashlib,base64,asyncio

from aiohttp import web

from coroweb import get,post
from apis import APIError,APIValueError,APIResourceNotFoundError,APIPermissionError,Page

from models import User,Comment,Blog,next_id

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

@get('/')
async def index(request,*,page='1'):
	page_index = get_page_index(page)
	

