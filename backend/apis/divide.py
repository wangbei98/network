import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource,reqparse

class DivideAPI(Resource):
	'''
	操作步骤七（telnet完成）：将Router fa0/0划分为两个子接口
	'''
	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('ip',type=string,help='错误的ip',default='192.168.5.5')
		parse.add_argument('username',type=string,help='错误的username',default='root')
		parse.add_argument('password',type=string,help='错误的password',default='123456')
		args = parse.parse_args()
		# 获取当前文件夹id
		ip = args.get('ip')
		username = args.get('username')
		password = args.get('password')
		token = '操作步骤七（telnet完成）：将Router fa0/0划分为两个子接口'
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response
