from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from apis.testapi import TestAPI
from apis.divide import DivideAPI
from apis.iproute import IprouteAPI
from apis.ping import PingAPI
from apis.trunk import TrunkAPI
from apis.vlan import VlanAPI
from apis.get_test_message import GetTestMessageFromFileAPI

app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")
# app.debug = True

api = Api(app)

# 请求跨域
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


api.add_resource(TestAPI, '/api/test', endpoint='test')
api.add_resource(DivideAPI, '/api/divide', endpoint='divide')
api.add_resource(IprouteAPI, '/api/iproute', endpoint='iproute')
api.add_resource(PingAPI, '/api/ping', endpoint='ping')
api.add_resource(TrunkAPI, '/api/trunk', endpoint='trunk')
api.add_resource(VlanAPI, '/api/vlan', endpoint='vlan')
api.add_resource(GetTestMessageFromFileAPI, '/api/get_test_message', endpoint='get_test_message')