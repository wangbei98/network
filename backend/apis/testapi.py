#encoding=utf-8
import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource

class TestAPI(Resource):
	def get(self):
		token = 'this is a test string'
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response