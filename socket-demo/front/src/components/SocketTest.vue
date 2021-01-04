<template>
  <div>

    <div v-for="item in log_list"
    >
    {{item}}
  </div>

    <input v-model="msg" />

    <button @click="send">发送消息</button>

    <button @click="call">调用API接口</button>

    <button @click="aaaaa">IIIIIII</button>
</div>

</template>



<script>

export default {
  data () {
    return {
      msg: "",
      log_list:[]
    }
  },
  //注册组件标签
  components:{


  },
  sockets:{
    connect: function(){
      console.log('socket 连接成功')
    },
    message: function(val){
      	console.log('返回:'+val);
    	this.log_list.push(val);
    },
    response_data: function(val){
    	console.log('返回:'+val);
    	this.log_list.push(val);
    }
},
  mounted:function(){




},
  methods:{

    send(){
      this.$socket.emit('message',encodeURI("用户:"+this.msg));
    },
    call(){
    	console.log("测试：前端调用后端的api")
    	this.$store.dispatch('getTestData')
    },
    aaaaa(){
 console.log("这是一个print函数，随便输出点什么")
 // 下面调用store里面的函数来给后端发请求
 // 括号中的内容为 store.js 中对应的action函数
 this.$store.dispatch('funcName')
},
  }
}


</script>

<style>


</style>
