import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource,reqparse

class IprouteAPI(Resource):
	'''
	验证步骤六（telnet完成）：验证router路由表。
	'''
	def get(self):
		token = '验证步骤六（telnet完成）：验证router路由表。'
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response
