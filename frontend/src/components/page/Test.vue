<template>
  <div>
    <p>test</p>
    <el-button @click='getTestData'>从后端获取数据</el-button>
    <p>{{testData}}</p>
  </div>
</template>

<script>
  export default{
    name:'test',
    computed:{
      testData(){
        return this.$store.state.testData
      }
    },
    methods:{
      getTestData(){
        this.$store.dispatch('getTestData')
      }
    }
  }
</script>

<style>
</style>