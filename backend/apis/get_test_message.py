import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource
'''
此API用来演示前端从后端的文件中读取数据
'''
class GetTestMessageFromFileAPI(Resource):
	def get(self):
		with open("files/prints.txt") as f:
			message = f.read()
			response = make_response(jsonify(code=0,data={'message':message},message='OK'))
			return response