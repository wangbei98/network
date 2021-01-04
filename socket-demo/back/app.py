# -*- coding: utf-8 -*-
from flask import Flask
from flask import request,jsonify  
from flask_cors import CORS  
from flask_socketio import SocketIO,send,emit  
import urllib.parse  
import time
import json


app = Flask(__name__)  

# 以下两行：实例化socketio对象，并设置跨域
CORS(app,cors_allowed_origins="*")  
socketio = SocketIO(app,cors_allowed_origins='*')  


# 通过socketio和前端通信
# 过程：
#   1. 前端通过socket向后端socket发送请求
#   2. 这段代码接收到socket请求后，给前端回复
@socketio.on('message',namespace='/chat')  
def handle_message(message):  
    message = urllib.parse.unquote(message)
    ret = "前端发来消息：" + message + "；后端再把这条消息发给前端"  
    print(ret)  
    send(ret,broadcast=True)  
    # 下面的for循环，用来测试：收到前端socket请求后，后端陆陆续续给前端回复
    # 测试后端主动往前端发请求
    for x in range(10):
      msg = "后端主动发送信息：" + str(x)
      send(msg,broadcast=True)
      time.sleep(0.1)
    test()

# socket连接，不用改！！！
@socketio.on('connect', namespace='/chat')  
def test_connect():  
    emit('my response', {'data': 'Connected'})  

@socketio.on('disconnect', namespace='/chat')  
# socket断开，不用改！！！
def test_disconnect():  
    print('Client disconnected')  


# 在其他函数中用socket通信
# 由此证明，在其他函数中调用send，也可以给前端回复
# 此函数在27行被调用
def test():
  for x in range(10):
    msg = "在其他函数中用socket往前端发送数据：" + str(x)
    send(msg,broadcast=True)
    time.sleep(0.1)


# 工具类：不重要
class ReturnJ(object):
    def __init__(self):
        #由于存在setattr,此处必须采用这种方式赋值
        self.__dict__['res'] = {
            'code': 200,
            'msg': '请求成功!'
        }
 
    def toJson(self):
        return json.dumps(self.res, ensure_ascii=False)
 
    def __setattr__(self, key, val):
            self.res[key] = val


# 测试api接口
# 由此证明，前端可以调用api接口，来获取后端源源不断的响应
@app.route('/api/testCall')
def testCall():
  print("后端收到了前端通过API的调用行为")
  data = {}
  ret = ReturnJ()
  ret.data = data
  for x in range(10):
    # 下面这行代码是最重要！！！
    # 'response_data' 是操作类型，可以不用改
    # '/chat' 是命名空间，可以修改，但要和前端一致
    socketio.emit('response_data',{'msg': x},
                    namespace='/chat')
    time.sleep(0.1)
  return ret.toJson()

if __name__ == '__main__':  
    socketio.run(app,debug=True,port=5000)