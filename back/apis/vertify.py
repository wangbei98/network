import logging
import time
import telnetlib
import re

sleep_time = 1

#断线时，重新login再执行
#Ping的重试

#telnet登录函数
def login_host(host_ip,username,password,socketio):
    tn = telnetlib.Telnet()
    flag=False
    try:
        # self.tn = telnetlib.Telnet(host_ip,port=23)
        tn.open(host_ip,port=23)
    except:
        logging.warning('%s网络连接失败'%host_ip)
        str1 = host_ip + '网络连接失败\n'
        socketio.emit('response_data', {'msg': str1},
                      namespace='/chat')
        return tn,flag
    command_result = tn.read_very_eager().decode('ascii')
    if 'Login incorrect' not in command_result:
        logging.warning('%s登录成功'%host_ip)
        str1 = host_ip + '登录成功\n'
        socketio.emit('response_data', {'msg': str1},
                      namespace='/chat')
        flag=True
    else:
        logging.warning('%s登录失败，用户名或密码错误'%host_ip)
        str1 = host_ip + '登录失败，用户名或密码错误\n'
        socketio.emit('response_data', {'msg': str1},
                      namespace='/chat')
    return tn,flag

#验证
def validate_command(tn,command,pattern):
    tn.write(command.encode('ascii') + b'\n')
    time.sleep(sleep_time)
    command_result = tn.read_very_eager().decode('ascii')
    #print(command_result)
    is_match = re.search(pattern,command_result, flags=0)
    if is_match:
        #print("match")
        return True, command_result
    else:
        return False, command_result

def validate_ip_route(tn,command,patterns,socketio):
    tn.write(command.encode('ascii') + b'\n')
    time.sleep(sleep_time)
    command_result = tn.read_very_eager().decode('ascii')
    print(command_result)
    match1 = re.search(patterns[0], command_result, flags=0)
    match2 = re.search(patterns[1], command_result, flags=0)
    match3 = re.search(patterns[2], command_result, flags=0)
    if match1 and match2 and match3:
        #print("yes!!!!!!!!!!!!!!!")
        socketio.emit('response_data', {'msg': command_result},
                      namespace='/chat')
        return True,command_result
    else:
        str1 = '路由表不正确'
        socketio.emit('response_data', {'msg': str1},
                      namespace='/chat')
        return False,'Error'


# 退出telnet
def logout_host(tn):
    tn.write(b"exit\n")
    tn.close()

#验证vlan
def vertifyVlan(Switch_ip,username,password, socketio):
    vlanBriefPattern1 = "VLAN0010.*active.*Fa0/2"
    vlanBriefPattern2 = "VLAN0020.*active.*Fa0/3"
    commandVlan = "show vlan brief"
    #登录
    for i in range(5):
        tn, flag = login_host(Switch_ip, username, password,socketio)
        if flag==True:
            break
    if flag == True:
        commandenable="enable"
        tn.write(commandenable.encode('ascii') + b'\n')
        # 等待Password出现后输入密码，最多等待10秒
        tn.read_until(b'Password: ', timeout=10)
        time.sleep(sleep_time)
        tn.write(password.encode('ascii') + b'\n')
        #tn.write(password + b'\n')
        time.sleep(sleep_time)
        str1 = '>进入特权模式\n'
        socketio.emit('response_data', {'msg': str1},
                      namespace='/chat')
        bool1, res1 = validate_command(tn, commandVlan, vlanBriefPattern1)
        bool2, res2 = validate_command(tn, commandVlan, vlanBriefPattern2)
        if bool1 and bool2:
            str2 = 'vlan配置成功'
            socketio.emit('response_data', {'msg': str2},
                          namespace='/chat')
            socketio.emit('response_data', {'msg': res1},
                          namespace='/chat')
            ans = True
        else:
            str2 = 'vlan配置失败'
            socketio.emit('response_data', {'msg': str2},
                          namespace='/chat')
            socketio.emit('response_data', {'msg': res1},
                          namespace='/chat')
            ans = False
        logout_host(tn)
        str3 = '>登出\n'
        socketio.emit('response_data', {'msg': str3},
                      namespace='/chat')
        return ans,str2
    else:
        str4 = '>五次登陆全部失败，本次验证失败\n'
        socketio.emit('response_data', {'msg': str4},
                      namespace='/chat')
        return False,"登陆失败"

def vertifyPing(Router_ip, username, password, commandPing, socketio):
    pingPattern1 = ".*Success rate is 100.*"
    pingPattern2 = ".*Success rate is 75.*"
    pingPattern3 = ".*Success rate is 50.*"
    for i in range(5):
        tn, flag = login_host(Router_ip, username, password, socketio)
        if flag==True:
            break
    if flag == True:
        commandenable = "enable"
        tn.write(commandenable.encode('ascii') + b'\n')
        # 等待Password出现后输入密码，最多等待10秒
        tn.read_until(b'Password: ', timeout=10)
        time.sleep(sleep_time)
        tn.write(password.encode('ascii') + b'\n')
        #tn.write(password + b'\n')
        time.sleep(sleep_time)
        str1 = '>进入特权模式\n'
        socketio.emit('response_data', {'msg': str1},
                      namespace='/chat')
        # strtest = tn.read_until(b'Password: ', timeout=10)
        # socketio.emit('response_data', {'msg': strtest},
        #               namespace='/chat')
        bool1, res1 = validate_command(tn, commandPing, pingPattern1)
        bool2, res2 = validate_command(tn, commandPing, pingPattern2)
        bool3, res3 = validate_command(tn, commandPing, pingPattern3)
        if bool1 or bool2 or bool3:
            str2 = '路由器可以'+commandPing+'通'
            socketio.emit('response_data', {'msg': res1},
                          namespace='/chat')
            socketio.emit('response_data', {'msg': str2},
                          namespace='/chat')
            ans = True
        else:
            str2 = '路由器'+commandPing+'不通'
            socketio.emit('response_data', {'msg': res1},
                          namespace='/chat')
            socketio.emit('response_data', {'msg': str2},
                          namespace='/chat')
            ans = False
        logout_host(tn)
        str3 = '>登出\n'
        socketio.emit('response_data', {'msg': str3},
                      namespace='/chat')
        return ans,str2
    else:
        str4 = '>五次登陆全部失败，本次验证失败\n'
        socketio.emit('response_data', {'msg': str4},
                      namespace='/chat')
        return False, "登录失败"


def vertifyRouter(Router_ip, username, password, IP1, IP2, IP3, socketio):
    Router_ip = '192.168.5.1'
    # IP1 = "192.168.10.0"
    # IP2 = "192.168.20.0"
    # IP3 = "192.168.5.0"
    routePatterns = []
    routePatterns.append("C.*" + IP1 + "/24 is di")
    routePatterns.append("C.*" + IP2 + "/24 is di")
    routePatterns.append("C.*" + IP3 + "/24 is di")
    commandRoute = "show ip route"
    for i in range(5):
        tn, flag = login_host(Router_ip, username, password,socketio)
        if flag==True:
            break
    if flag == True:
        commandenable = "enable"
        tn.write(commandenable.encode('ascii') + b'\n')
        # 等待Password出现后输入密码，最多等待10秒
        tn.read_until(b'Password: ', timeout=10)
        time.sleep(sleep_time)
        tn.write(password.encode('ascii') + b'\n')
        time.sleep(sleep_time)
        str1 = '>进入特权模式\n'
        socketio.emit('response_data', {'msg': str1},
                      namespace='/chat')
        bool,res = validate_ip_route(tn, commandRoute, routePatterns,socketio)
        logout_host(tn)
        if bool:
            return bool,"路由表正确"
        else:
            return bool,"路由表不正确"
    else:
        str4 = '>五次登陆全部失败，本次验证失败\n'
        socketio.emit('response_data', {'msg': str4},
                      namespace='/chat')
        return False,"登录失败"


if __name__ == '__main__':

    Switch_ip ='192.168.5.5'
    Router_ip = '192.168.5.1'

    username = 'root'
    password = '123456'

    vertifyPing()

    #配置Switch1划分VLAN10和VLAN20

    #excute(Switch_ip ,username,password,'Split_Vlan.txt')
    #
    #配置Switch1 fa0/1 为Trunk接口，与Router1互连
    #excute(Switch_ip ,username,password,'Trunk.txt')
    #
    #将Router fa0/0划分为两个子接口
    #excute(Router_ip ,username,password,'Router.txt')