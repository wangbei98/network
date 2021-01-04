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
    }
  }
})