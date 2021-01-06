<template>
  <div>
  <el-container>
    <!-- 页眉 -->
    <el-header class="header-container">
      <h1 class="title">单臂路由-25组</h1>
    </el-header>
  </el-container>
  <div style="text-align:center">
      <el-row>
        <br>
        <br>
        <br>
        <el-col>
          <el-steps :active="active" align-center finish-status="success">
            <el-step title="操作步骤1" description="配置Switch划分VLAN10和VLAN20"></el-step>
            <el-step title="验证步骤1" description="Switch验证show vlan brief，正确划分"></el-step>
            <el-step title="操作步骤2" description="配置Switch fa0/1为Trunk接口，与Router互连"></el-step>
            <el-step title="操作步骤3" description="将Router fa0/0划分为两个子接口"></el-step>
            <el-step title="验证步骤2" description="验证Router可以ping通PC1和PC2，证明可以相互ping通"></el-step>
            <el-step title="验证步骤3" description="验证router路由表"></el-step>
          </el-steps>
        </el-col>
      </el-row>
        <br>
        <br>
        <br>
      <el-row style="height:30px">
          <el-alert
            :title="successmsg"
            type="success"
            v-show="successShow"
            show-icon center>
          </el-alert>
          <el-alert
            :title="errormsg"
            type="error"
            v-show="errorShow"
            show-icon center>
          </el-alert>
      </el-row>
        <br>
        <br>
      <hr>
        <br>
      <el-row>
        <el-col :span="200" style="width:50%"><img src="../assets/topo.jpg"></el-col>
        <el-col :span=10000 style="width:48%">Termina
          <el-input
            type="textarea"
            :rows="10"
            readonly="true"
            class="res-area"
            v-model="res">
          </el-input>
        </el-col>
      </el-row>
      <hr>
      <br>
      <el-row>
         <el-button style="height:5%;width:10%; background-color: rgb(161, 207, 35);color:#FFF" @click="next" :disabled="isdis" :loading="buttonLoading">{{buttonname}}</el-button>
      </el-row>
      <br>
    </div>
    </div>
</template>

<script>
import telnetApi from '../api/telnet.js'
import Stomp from 'stompjs'

export default {
  name: 'Topo',
  data () {
    return {
      active: 0,
      isdis:false,
      buttonname:"下一步",
      successmsg:'',
      errormsg:'',
      successShow:false,
      errorShow:false,
      switch:{},
      router:{},
      buttonLoading:false,
      client: Stomp.client("ws://127.0.0.1:65081/stomp"),
      res:'asfffffffffffffffasfffffffffffffffff'
    }
  },
  methods: {
    next() {
      this.successmsg=''
      this.errormsg=''
      this.successShow=false;
      this.errorShow=false;
      this.buttonLoading=true;
      if (this.active > 4){
        this.isdis=true;
        this.buttonname="已完成"
        this.active++;
        this.open();
      }else{
        this.doTelnet(this.active)
      }
      this.buttonLoading=false;
    },
    doTelnet(active){
      switch(active){
        case 0:telnetApi.makevlan(this.switch).then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.buttonname='重试'
          }
        }); break;
        case 1:telnetApi.vlan().then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.buttonname='重试'
          }
        }); break;
        case 2:telnetApi.trunk().then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.buttonname='重试'
          }
        }); break;
        case 3:telnetApi.divide(this.router).then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.buttonname='重试'
          }
        }); break;
        case 4:telnetApi.ping().then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.buttonname='重试'
          }
        }); break;
        case 5:telnetApi.iproute().then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.buttonname='重试'
          }
        });
      }
    },
    open() {
      this.$alert('所有Telnet步骤已完成，网络配置成功', '配置成功', {
        confirmButtonText: '确定',
        callback: action => {
        }
      })
    },
    connect(){
      var clientid = util.uuid()
      var headers = {
        'client-id': clientid
      }
      this.client.connect(headers, this.onConnected, this.onFailed)
    },
    onConnected: function (frame) {
      console.log('Connected: ' + frame)
      var topic = '/topic/AllCustomer'
      this.client.subscribe(topic, this.responseCallback, this.onFailed)
    },
    onFailed: function (frame) {
      console.log('Failed: ' + frame)
    },
    responseCallback: function (frame) {
      console.log('responseCallback msg=>' + frame.body)
      this.res += frame.body
    },
  },
  created () {
    this.connect();
  },
}
</script>

<style scoped>

.aside {
  background-color: #F2F6FC;
  border-right: 2px solid #F2F6FC;
  height: 100%;
}
.library-item {
  color: #606266;
}
.library-item img {
  width: 30px;
  height: 30px;
  margin-right: 10px;
}
.board-container {
  padding: 0;
  position: relative;
}
.button-container {
  position: absolute;
  right: 16px;
  top: 10px;
}
.board {
  background-color: #FFF;
  height: 99%;
  width: 100%;
}
.header-container {
  background-color: rgb(35, 187, 207);
}
.title {
  margin: 0;
  line-height: 60px;
  color: #FFF;
}
.address {
  color: rgb(35, 187, 207);
  line-height: 60px;
}
.res-area {
  color: rgb(35, 187, 207);
}
</style>
