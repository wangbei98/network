#@Author:   Casserole fish
#@Time:    2020/12/27 21:00

import logging
import time
import telnetlib
import re


#打开文件
outf= open('./files/prints.txt','wb')

def login_host(host_ip,username,password):
    tn = telnetlib.Telnet()
    flag=False
    try:
        # self.tn = telnetlib.Telnet(host_ip,port=23)
        tn.open(host_ip,port=23)
    except:
        logging.warning('%s网络连接失败'%host_ip)
        str1 = host_ip + '网络连接失败\n'
        outf.write(str1.encode('utf-8'))
        return tn,flag
    command_result = tn.read_very_eager().decode('ascii')
    if 'Login incorrect' not in command_result:
        logging.warning('%s登录成功'%host_ip)
        str1 = host_ip + '登录成功\n'
        outf.write(str1.encode('utf-8'))
        flag=True
    else:
        logging.warning('%s登录失败，用户名或密码错误'%host_ip)
        str1 = host_ip + '登录失败，用户名或密码错误\n'
        outf.write(str1.encode('utf-8'))
    return tn,flag
# 此函数实现执行传过来的命令文件，并输出其执行结果
def execute_some_command(tn, conf,password):
    confp = open(conf, 'r')
    for command in confp.readlines():
        try:
            command = command.strip('\n')
            #enable命令 需要输入密码
            if command=='enable':
                # 执行命令
                tn.write(command.encode('ascii') + b'\n')
                # 等待Password出现后输入密码，最多等待10秒
                tn.read_until(b'Password: ', timeout=10)
                time.sleep(2)
                tn.write(password.encode('ascii') + b'\n')
                time.sleep(2)
            else:
                # 执行命令
                tn.write(command.encode('ascii') + b'\n')
                time.sleep(2)
            # 获取命令结果
            command_result = tn.read_very_eager().decode('ascii')
            logging.warning('命令执行结果：\n%s' % command_result)
            command_result=command_result+'\n'
            outf.write(command_result.encode('utf-8'))
        except:
            return False
    confp.close()
    return True

# 退出telnet
def logout_host(tn):
    tn.write(b"exit\n")
    tn.close()



def excute(host_ip,username,password,conf):
    #设置最大重试次数
    max_reconnect = 10
    #已经重试的次数
    has_reconnect=0
    #标志变量是否执行命令成功
    isSuccessExcute=False
    #如果执行出现异常，那么就重试
    while isSuccessExcute==False and has_reconnect<max_reconnect:
        tn,flag = login_host(host_ip,username,password)
        #登录成功后，才执行命令
        if flag==True:
            #返回执行是否成功
            isSuccessExcute=execute_some_command(tn, conf,password)
            #执行成功的话退出登录
            if isSuccessExcute==True:
                str1="命令已执行完毕\n"
                print(str1)
                outf.write(str1.encode('utf-8'))
                outf.close()
                logout_host(tn)
            #执行失败的话，重试次数+1
            else:
                has_reconnect = has_reconnect+1
                str1='正在尝试重连，已经重连次数为：'+str(has_reconnect)+'\n'
                print(str1)
                outf.write(str1.encode('utf-8'))
        else:
            break
    if isSuccessExcute==False:
        logging.warning('网络连接失败,请检查网络后稍后重试！！！' )
        str1 = '网络连接失败,请检查网络后稍后重试！！！\n'
        outf.write(str1.encode('utf-8'))
        outf.close()

