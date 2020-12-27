# coding=utf-8
import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource,reqparse

from apis.basic_operation import excute


class TrunkAPI(Resource):
	'''
	操作步骤六（telnet完成）：配置Switch1 fa0/1为Trunk接口，与Router1互连
	'''
	def get(self):
		
		# 这里调用（操作/验证）脚本
		# 配置Switch1 fa0/1 为Trunk接口，与Router1互连
		excute(ip, username, password, './scripts/Trunk.txt')
		# 以下为实例代码
		token = 'opearte step 6 : telnet complete： configurate Switch1 fa0/1 as Trunk,link with Router1'
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response
