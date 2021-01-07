<template>
  <div >
    <el-container>
      <!-- 页眉 -->
      <el-header class="header-container">
        <h1 class="title">单臂路由-25组</h1>
      </el-header>
    </el-container>
    <el-main style="text-align:center" class="my-container">
          <el-row class="step-sty">
            <el-steps class="step-area" :active="active" align-center finish-status="success">
              <el-step title="操作步骤1" description="配置Switch划分VLAN10和VLAN20"></el-step>
              <el-step title="验证步骤1" description="Switch验证show vlan brief，正确划分"></el-step>
              <el-step title="操作步骤2" description="配置Switch fa0/1为Trunk接口，与Router互连"></el-step>
              <el-step title="操作步骤3" description="将Router fa0/0划分为两个子接口"></el-step>
              <el-step title="验证步骤2" description="验证Router可以ping通PC1和PC2，证明可以相互ping通"></el-step>
              <el-step title="验证步骤3" description="验证router路由表"></el-step>
            </el-steps>
            <el-row class="tuitor-area">
               {{tuitor}}
            </el-row>
          </el-row>
        <el-row class="middle-area">
          <div class="img-area">
            <br><img class="img-topo" src="../assets/topo.png">
          </div>
          <div class="ter-area">Terminal
            <el-input
              id="textarea_id"
              type="textarea"
              :rows="14"
              readonly="true"
              class="res-area"
              v-model="res">
            </el-input>
          </div>
        </el-row>
        <el-row class="button-area">
          <el-button @click="before" :disabled="isdis_before" :loading="buttonLoadingBefore" class="button-sty">{{button_before_name}}</el-button>
          <el-button @click="next" :disabled="isdis" :loading="buttonLoading" class="button-sty">{{button_next_name}}</el-button>
        </el-row>
        <el-row class="msg-area">
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
        <div class="footer">
          <div class="links">
            帮助ㅤㅤ隐私ㅤㅤ条款
          </div>
          <div class="copyright">
            Copyright © 2020  All rights reserved
          </div>
        </div>
      </el-main>
    </div>
</template>

<script>
import telnetApi from '@/api/telnet.js'
// import Stomp from 'stompjs'

export default {
  name: 'Topo',
  data () {
    return {
      id:'',
      active: 0,
      isdis:false,
      isdis_before:true,
      button_next_name:"执行步骤",
      button_before_name:"上一步",
      successmsg:'',
      errormsg:'',
      successShow:false,
      errorShow:false,
      switch:{},
      router:{},
      buttonLoading:false,
      buttonLoadingBefore:false,
      // client: Stomp.client("ws://127.0.0.1:65081/stomp"),
      res:'',
      tuitor:'操作步骤1：此步骤为交换机划分VLAN10和VLAN20，并且将交换机的Fa0/2和Fa0/3端口分别划分到VLAN10和VLAN20，即将PC1和PC2分别划分到VLAN10和VLAN20。此时PC1和PC2处在不同子网不能相互ping通。',
    }
  },
  mounted() {
      this.$socket.emit('login', 25);       //触发socket连接
  },
  sockets: {
    connect() {
     this.id = this.$socket.id;
     this.$socket.emit('login', 25);      //监听connect事件
    },
    message(data) {                                 //监听message事件，方法是后台定义和提供的
      console.log('responseCallback msg=>' + data)
      this.res += data.msg
      const textarea = document.getElementById('textarea_id');
      textarea.scrollTop = textarea.scrollHeight;
    },
    response_data(data){
    	console.log('返回:'+data);
      this.res += data.msg
      const textarea = document.getElementById('textarea_id');
      textarea.scrollTop = textarea.scrollHeight;
    }
},
  methods: {
    // clickButton: function(val){                       //添加按钮事件向服务端发送数据
    //   this.$socket.emit('emit_method', val);
    // },
    next() {
      this.successmsg=''
      this.errormsg=''
      this.successShow=false;
      this.errorShow=false;
      this.doTelnet(this.active)
      this.res=''
    },
    before(){
      this.successmsg=''
      this.errormsg=''
      this.successShow=false;
      this.errorShow=false;
      this.doLast(this.active)
      this.res=''
    },
    doLast(active){
      switch(active){
      case 1:
        this.active--;
        this.tuitor="操作步骤1：此步骤为交换机划分VLAN10和VLAN20，并且将交换机的Fa0/2和Fa0/3端口分别划分到VLAN10和VLAN20，即将PC1和PC2分别划分到VLAN10和VLAN20。此时PC1和PC2处在不同子网不能相互ping通。"
        this.button_next_name="执行步骤"
        break;
      case 2:
        this.active--;
        this.tuitor="验证步骤1：在交换机上使用show vlan brief 命令，查看对应接口是否在正确的VLAN中。结果应有VLAN10和VLAN20，状态为Active，端口分别为Fa0/2与Fa0/3。"
        this.button_next_name="执行步骤"
        break;
      case 3:
        this.active--;
        this.tuitor="操作步骤2：Trunk接口区别于Access接口：Access接口只能加入一个VLAN，传递加入这个VLAN的流量；Trunk接口属于所有VLAN（1-4094），可以传递所有VLAN的流量，经过Trunk接口传出去的流量，会加上VLAN tag加以区分。"
        this.button_next_name="执行步骤"
        break;
      case 4:
        this.active--;
        this.tuitor="操作步骤3：此步骤将Router0的Fa0/0端口划分为两个子接口，分别对应VLAN10 和VLAN20，作为它们的网关。"
        this.button_next_name="执行步骤"
        break;
      case 5:
        this.active--;
        this.tuitor="验证步骤2：在VLAN间路由配置成功以后，PC1和PC2应该是可以相互ping通的。因为PC1和PC2的网关均为Router0的Fa0/0端口，所以可以通过Router0间接验证PC之间的连通性。在Router0上尝试ping 192.168.10.2和192.168.20.2均成功，证明VLAN间通信成功。如果不成功，请对照检查配置与物理连线。"
        this.button_next_name="执行步骤"
        break;
      case 6:
        this.active--;
        this.isdis=false;
        this.tuitor="验证步骤3：在Router0上查看路由表，192.168.10.0和192.169.20.0两个网段均应当在路由表中。如果没有，请对照检查配置与物理连线。"
        this.button_next_name="执行步骤"
        break;
      }
    },
    doTelnet(active){
      this.buttonLoading=true;
      this.isdis_before = true;
      switch(active){
        case 0:telnetApi.makevlan(this.switch).then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
            this.active++;
            this.tuitor="验证步骤1：在交换机上使用show vlan brief 命令，查看对应接口是否在正确的VLAN中。结果应有VLAN10和VLAN20，状态为Active，端口分别为Fa0/2与Fa0/3。"
            this.button_next_name="执行步骤"
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.button_next_name='重试'
          }
          this.buttonLoading=false;
          this.isdis_before = false;
        }); break;
        case 1:telnetApi.vlan().then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
            this.tuitor="操作步骤2：Trunk接口区别于Access接口：Access接口只能加入一个VLAN，传递加入这个VLAN的流量；Trunk接口属于所有VLAN（1-4094），可以传递所有VLAN的流量，经过Trunk接口传出去的流量，会加上VLAN tag加以区分。"
            this.button_next_name="执行步骤"
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.button_next_name='重试'
          }
          this.buttonLoading=false;
          this.isdis_before = false;
        }); break;
        case 2:telnetApi.trunk().then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
            this.tuitor="操作步骤3：此步骤将Router0的Fa0/0端口划分为两个子接口，分别对应VLAN10 和VLAN20，作为它们的网关。"
            this.button_next_name="执行步骤"
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.button_next_name='重试'
          }
          this.buttonLoading=false;
          this.isdis_before = false;
        }); break;
        case 3:telnetApi.divide(this.router).then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
            this.tuitor="验证步骤2：在VLAN间路由配置成功以后，PC1和PC2应该是可以相互ping通的。因为PC1和PC2的网关均为Router0的Fa0/0端口，所以可以通过Router0间接验证PC之间的连通性。在Router0上尝试ping 192.168.10.2和192.168.20.2均成功，证明VLAN间通信成功。如果不成功，请对照检查配置与物理连线。"
            this.button_next_name="执行步骤"
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.button_next_name='重试'
          }
          this.buttonLoading=false;
          this.isdis_before = false;
        }); break;
        case 4:telnetApi.ping().then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
             this.active++;
            this.tuitor="验证步骤3：在Router0上查看路由表，192.168.10.0和192.169.20.0两个网段均应当在路由表中。如果没有，请对照检查配置与物理连线。"
            this.button_next_name="执行步骤"
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.button_next_name='重试'
          }
          this.buttonLoading=false;
          this.isdis_before = false;
        }); break;
        case 5:telnetApi.iproute().then(resp=>{
          if(resp.data.flag){
            this.successmsg=resp.data.message
            this.successShow=true;
            this.active++;
            this.tuitor=""
            this.isdis=true;
            this.button_next_name="已完成"
            this.open();
          }else{
            this.errormsg=resp.data.message
            this.errorShow=true;
            this.button_next_name='重试'
          }
          this.buttonLoading=false;
          this.isdis_before = false;
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
    // connect(){
    //   var clientid = util.uuid()
    //   var headers = {
    //     'client-id': clientid
    //   }
    //   this.client.connect(headers, this.onConnected, this.onFailed)
    // },
    // onConnected: function (frame) {
    //   console.log('Connected: ' + frame)
    //   var topic = '/topic/AllCustomer'
    //   this.client.subscribe(topic, this.responseCallback, this.onFailed)
    // },
    // onFailed: function (frame) {
    //   console.log('Failed: ' + frame)
    // },
    // responseCallback: function (frame) {
    //   console.log('responseCallback msg=>' + frame.body)
    //   this.res += frame.body
    // },
  },
  // created () {
  //   this.connect();
  // },
}
</script>

<style scoped>
.my-container {
  font-family: "Microsoft YaHei","微软雅黑";
  width: 100%;
  height: 100%;
  background-color: rgb(240, 242, 245);
  background-image: url("../assets/background.svg");
  background-attachment: fixed;
  background-size: cover;
  position:fixed
}
.header-container {
  background-color: rgb(35, 187, 207);
}
.title {
  margin: 0;
  line-height: 60px;
  color: #FFF;
}
.footer {
  position: absolute;
  width: 98%;
  margin-top: 2%;
  margin-bottom: 5%;
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

.step-sty{
  background-color: rgb(255, 255, 255);
  margin-top: 1%;
  margin-left: 1%;
  margin-right: 1%;
}
.step-area{
  margin-top: 1.5%;
  margin-bottom: 1.5%;
}
.tuitor-area{
  height: 30px;
  text-align: left;
  margin-left: 5%;
  margin-right: 5%;
  margin-bottom: 2%;
  color: green;
  font-size: 15px
}
.middle-area{
  margin-top: 1%;
}
.img-area{
  width:48%;
  margin-left: 1%;
  float: left;
  background-color: rgb(255, 255, 255);
  padding: 1% 1% 1% 1%;
  height: 370px;
}
.img-topo{
  max-width: 90%;
  max-height: 90%;
}
.ter-area{
  width: 48%;
  margin-right: 1%;
  float: right;
  background-color: rgb(255, 255, 255);
  padding: 1% 1% 1% 1%;
  height: 370px;
}
/* .res-area {
} */
.button-area{
  margin-top: 2%;
  margin-left: 1%;
  margin-right: 1%;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: rgb(35, 187, 207)
}
.button-sty{
  width:20%;
  margin-top: 2%;
  background-color: rgb(147, 218, 54);
  color:#FFF ;
}
.msg-area{
  height: 30px;
  margin-left: 1%;
  margin-right: 1%;
  margin-top: 1%;
}
</style>
