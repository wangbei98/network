<template>
  <div>
    <p>test</p>
    <el-button @click='getMessage'>从后端的文件获取数据</el-button>
    <p>{{message}}</p>
  </div>
</template>

<script>
  export default{
    name:'test',
    computed:{
      message(){
        return this.$store.state.message
      }
    },
    methods:{
      getMessage(){
        this.$store.dispatch('getMessage')
      }
    }
  }
</script>

<style>
</style>