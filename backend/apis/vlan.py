# coding=utf-8
import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource,reqparse
from apis.basic_operation import excute

class VlanAPI(Resource):
	'''
	操作步骤五（telnet完成）：配置Switch1划分VLAN10和VLAN20
	'''
	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('ip',type=str,help='错误的ip',default='192.168.5.5')
		parse.add_argument('username',type=str,help='错误的username',default='root')
		parse.add_argument('password',type=str,help='错误的password',default='123456')
		args = parse.parse_args()
		# 获取当前文件夹id
		ip = args.get('ip')
		username = args.get('username')
		password = args.get('password')
		
		# 这里调用（操作/验证）脚本

		# 配置Switch1划分VLAN10和VLAN20

		excute(ip, username, password, './scripts/Split_Vlan.txt')

		# 以下为实例代码
		token = 'opearte step 5 : telnet complete：configurate Switch1 divide as VLAN10 and VLAN20'
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response

	'''
	验证步骤四（telnet完成）：Switch1验证show vlan brief，正确划分
	'''
	def get(self):
		
		# 这里调用（操作/验证）脚本

		# 以下为实例代码
		token = 'validate step 4 : telnet complete:Switch1: validate show vlan brief '
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response