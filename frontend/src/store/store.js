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
    },
    getMessage(state,message){
      state.message = message
    }
  },
  actions:{
    getTestData(context){
      axios.get('/test')
      .then(response => {
        let testData = response.data.data.token
        context.commit('getTestData',testData)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getMessage(context){
      axios.get('/get_test_message')
      .then(response => {
        let message = response.data.data.message
        context.commit('getMessage',message)
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
})