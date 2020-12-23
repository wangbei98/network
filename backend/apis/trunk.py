import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource,reqparse

class TrunkAPI(Resource):
	'''
	操作步骤六（telnet完成）：配置Switch1 fa0/1为Trunk接口，与Router1互连
	'''
	def get(self):
		token = '操作步骤六（telnet完成）：配置Switch1 fa0/1为Trunk接口，与Router1互连'
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response
