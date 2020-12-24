#encoding=utf-8
import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource,reqparse

class IprouteAPI(Resource):
	'''
	验证步骤六（telnet完成）：验证router路由表。
	'''
	def get(self):

		# 这里调用（操作/验证）脚本

		# 以下为实例代码
		token = '验证步骤六（telnet完成）：验证router路由表。'
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response
