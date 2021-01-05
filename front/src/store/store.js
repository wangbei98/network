import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:5000/api'

Vue.use(Vuex);

export const store = new Vuex.Store({
  state:{
    testData : '',
    message : ''
  },
  getters:{

  },
  mutations:{
    getTestData(state,testData){
      state.testData = testData
    }
  },
  actions:{
    getTestData(context){
      axios.get('/testCall')
      .then(response => {
        let testData = response.data.data.token
        context.commit('getTestData',testData)
      })
      .catch(err => {
        console.log(err)
      })
    },
    funcName(context){
 // get后面写的是api地址
 // 比如后端api是 localhost:5000/api/testCall, 这里就写 /testCall
  axios.get('/vlan')
  .then(response => {
   // 下面的代码入关紧要，我们只需要调用api，后续服务器通过socket回复给前端，暂时可能不需要处理调用api后返回的response
    console.log(response)
  })
  .catch(err => {
   // 错误处理，暂时不考虑
    console.log(err)
  })
}

  }
})
