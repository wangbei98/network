<template>
  <div id="userLayout">
    <el-main class="container">
      <div class="top">
        <div class="header">
          <a href="/">
            <img src="~@/assets/logo.svg" class="logo" alt="logo">
            <span class="title">Telnet 操作平台</span>
          </a>
        </div>
      </div>

      <div class="login-container">
        <el-form label-position="left" inline-message="true" autoComplete="on" :model="loginForm" ref="loginForm">
          <el-form-item label="用户名：">
            <el-input name="username" type="text" value="admin" autoComplete="on" placeholder="username" />
          </el-form-item>
          <el-form-item label="密码：">
            <el-input name="password" :type="pwdType" @keyup.enter.native="handleLogin" value="admin" autoComplete="on"
              placeholder="password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-checkbox class="auto-login" v-model="checked">自动登录</el-checkbox>
            <el-button type="text" class="show-tuitor" @click="showTuitor = true">查看教程</el-button>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" class="login-button" :loading="loading" @click.native.prevent="handleLogin">
              登 录
            </el-button>
          </el-form-item>
        </el-form>
      </div>


      <div class="footer">
        <div class="links">
          帮助ㅤㅤ隐私ㅤㅤ条款
        </div>
        <div class="copyright">
          Copyright © 2020  All rights reserved
        </div>
      </div>
    </el-main>
    <el-dialog
      title="实验背景"
      :visible.sync="showTuitor"
      fullscreen="true"
      center="true"
      width="60%">
      <span>
        <p>ㅤㅤ目前，很多中小型企业内部网络都是通过交换机互联而成，为了实现广播域的分割和广播包传播范围的控制，划分 Vlan 已成为网络架构中不可缺少的操作，通过划分 Vlan可以使得同一台交换机下的不同 Vlan 里的端口下连接的设备不能直接互相访问，这样有效的隔离了网络。虽然划分 Vlan 有效的地控制了广播包的传播范围，但是对于某些既希望隔离网络，也希望有些不同的 Vlan 能够通信的企业来讲， Vlan 间路由就成为必要的技术，常常在中小型企业网中部署。为了完成 Vlan 间路由的实验， 必须事先掌握 Vlan 的划分，VTP 同步，把接口划分进相应的 Vlan 等交换机的基本操作，以及一个相对比较新的概念子接口。</p>
        <p>ㅤㅤ不同的Vlan 相互隔离广播域，因此，传统的以太网 ARP 方式的通信机制在这里是不可用的， 需要在网络中添加三层设备，这里的三层设备可以是路由器，也可以是 Cisco 三层交换机（例如 Cisco 3550 Cisco3560 ）。本次实验的目的，是让处于不同Vlan 下的主机能够通信，因此 用路由器充当上述的三层设备，需要用到的知识点有：</p>
        <p>ㅤㅤ1. Vlan 的划分</p>
        <p>ㅤㅤ2. VTP 同步</p>
        <p>ㅤㅤ3. 将接口划分进 Vlan</p>
        <p>ㅤㅤ4. Trunk 链路的封装类型</p>
        <p>ㅤㅤ5. 子接口的配置</p>
        <p>ㅤㅤ实验拓扑如下：</p>
        <div class="img-area">
          <img class="img-topo" src="../assets/topo.png">
        </div>
        <p>ㅤㅤ其中，PC3为telnet远程连接终端，PC1和PC2为实验终端。</p>
        <p>ㅤㅤ在进行实验前，请按照上图拓扑连好物理线，并配置PC1的IP地址为192.168.10.2，网关为192.168.10.1；PC2的IP地址为192.168.20.2，网关为192.168.20.1；PC3的IP地址为192.168.5.2，网关为192.168.5.1；Router0 Fa0/0端口IP为192.168.5.1；配置交换机Switch0 虚拟VLAN1，IP为192.168.5.5；配置路由器和交换机的特权模式密码为123456，并设置无认证登陆。</p>
      </span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="showTuitor = false">完 成</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>

export default {
  name: 'UserLayout',
  data () {
    return {
      loginForm: {},
      loading: false,
      pwdType: 'password',
      checked:'',
      showTuitor:false
    }
  },
  methods:{
    handleLogin(){
        this.$router.push("/topo")
    }
  },
  mounted () {
    document.body.classList.add('userLayout')
  },
  beforeDestroy () {
    document.body.classList.remove('userLayout')
  },
}
</script>

<style scoped>
    .container {
      font-family: "Microsoft YaHei","微软雅黑";
      width: 100%;
      min-height: 100%;
      background-color: #FFFFFF;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1600 900'%3E%3Cpolygon fill='%2340a7cc' points='957 450 539 900 1396 900'/%3E%3Cpolygon fill='%23c6dbe1' points='957 450 872.9 900 1396 900'/%3E%3Cpolygon fill='%2350a7c5' points='-60 900 398 662 816 900'/%3E%3Cpolygon fill='%23c0d7da' points='337 900 398 662 816 900'/%3E%3Cpolygon fill='%235fa6be' points='1203 546 1552 900 876 900'/%3E%3Cpolygon fill='%23bad3d4' points='1203 546 1552 900 1162 900'/%3E%3Cpolygon fill='%236fa6b8' points='641 695 886 900 367 900'/%3E%3Cpolygon fill='%23b3cfcd' points='587 900 641 695 886 900'/%3E%3Cpolygon fill='%237ea5b1' points='1710 900 1401 632 1096 900'/%3E%3Cpolygon fill='%23adcbc7' points='1710 900 1401 632 1365 900'/%3E%3Cpolygon fill='%238ea5aa' points='1210 900 971 687 725 900'/%3E%3Cpolygon fill='%23a7c7c0' points='943 900 1210 900 971 687'/%3E%3C/svg%3E");
      background-attachment: fixed;
      background-size: cover;
      padding: 110px 0 144px;
      position:fixed
    }

    .top {
      text-align: center;
    }
    .header {
      height: 44px;
      line-height: 44px;
    }

    .logo {
      height: 44px;
      vertical-align: top;
      margin-right: 16px;
      border-style: none;
    }

    .title {
      font-size: 30px;
      color: rgba(0, 0, 0, .85);
      font-family: "Microsoft YaHei","微软雅黑";
      font-weight: 600;
      position: relative;
      top: 2px;
    }

    .footer {
      position: absolute;
      width: 100%;
      bottom: 0;
      padding: 0 16px;
      margin: 48px 0 24px;
      text-align: center;
    }
    .links {
      margin-bottom: 8px;
      font-size: 14px;
    }
    .copyright {
      color: rgba(0, 0, 0, 0.45);
      font-size: 14px;
    }
    .login-container{
      top: 25%;
      position: absolute;
      text-align: center;
      left: 40%;
      width: 20%;
    margin-left: auto;
    margin-right: auto;
    }
    .tuitor-container{
      top: 20%;
      position: absolute;
      text-align: center;
      left: 70%;
      width: 20%;
      height: 50%;
      margin-left: auto;
      margin-right: auto;
      background-color: aqua;
    }
    .login-button{
      width:100%;
      background-color:rgb(35, 187, 207);
      margin-top: 10px
    }
    .auto-login{
      margin-top: 10px;
      float: left;
    }
    .show-tuitor{
      margin-top: 10px;
      float: right;
    }
    .el-css-input{
      width: 80%;
    }
    .img-area{
      margin-left: 1%;
      background-color: rgb(255, 255, 255);
      padding: 1% 1% 1% 1%;
    }
    .img-topo{
      max-width: 90%;
      max-height: 90%;
    }
</style>