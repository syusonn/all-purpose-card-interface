#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'syuson'

'''
JSON API definition
'''

import json,logging,inspect,functools,json
import datetime

# 自定义响应结果类
class operateResult(object):
	"""docstring for operate_result"""
	__SUCCESS__ = 10000
	__FAILED__ = 99999

	# 自定义响应结果方法
	def get_result(type=__FAILED__,msg=None,data=None):
		return dict(type=type,msg=msg,data = json.dumps(data,cls=CJsonEncoder))

# 自定义时间格式化类
class CJsonEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, datetime.date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj)  

class APIError(Exception):
	"""
	the base APIError which contains error(required), data(optional) and message(optional)
	"""
	def __init__(self, error,data='',message=''):
		super(APIError, self).__init__(message)
		self.error = error
		self.data = data
		self.message = message

class APIValueError(APIError):
	"""
    Indicate the input value has error or invalid. The data specifies the error field of input form.
	"""
	def __init__(self, field,message=''):
		super(APIValueError, self).__init__('value:invalid', field, message)
		
class APIResourceNotFoundError(APIError):
	"""
	Indicate the resource was not found. The data specifies the resource name.
	"""
	def __init__(self, field,message=''):
		super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)

class APIPermissionError(APIError):
	"""
	Indicate the api has no permission.
	"""
	def __init__(self, message=''):
		super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)
		self.arg = arg
		
class Page(object):
	"""docstring for Page"""
	def __init__(self, item_count,page_index=1,page_size=3):
		'''
        Init Pagination by item_count, page_index and page_size.
        >>> p1 = Page(100, 1)
        >>> p1.page_count
        10
        >>> p1.offset
        0
        >>> p1.limit
        10
        >>> p2 = Page(90, 9, 10)
        >>> p2.page_count
        9
        >>> p2.offset
        80
        >>> p2.limit
        10
        >>> p3 = Page(91, 10, 10)
        >>> p3.page_count
        10
        >>> p3.offset
        90
        >>> p3.limit
        10
        '''
		self.item_count = item_count
		self.page_size = page_size
		self.page_count = item_count // page_size + ( 1 if item_count % page_size > 0 else 0)
		if (item_count ==0) or (page_index > self.page_count):
			self.offset = 0
			self.limit = 0
			self.page_index = 1
		else:
			self.page_index = page_index
			self.offset = self.page_size * (page_index -1) 
			self.limit = self.page_size
		self.has_next = self.page_index < self.page_count
		self.has_previous = self.page_index > 1
		print('item_count: %s, page_count: %s, page_index: %s, page_size: %s, offset: %s, limit: %s' % (self.item_count, self.page_count, self.page_index, self.page_size, self.offset, self.limit))

	def __str__(self):
		return 'item_count: %s, page_count: %s, page_index: %s, page_size: %s, offset: %s, limit: %s' % (self.item_count, self.page_count, self.page_index, self.page_size, self.offset, self.limit)

	__repr__ = __str__	
