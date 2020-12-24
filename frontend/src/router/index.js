import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

import Home from '../components/page/Home.vue'
import NotFound from '../components/page/NotFound.vue'
import Test from '../components/page/Test.vue'
import GetMessage from '../components/page/GetMessage.vue'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    },
    {
      path: '/getMessage',
      name: 'GetMessage',
      component: GetMessage
    },
    {
      path: '*',
      component: NotFound ,
    }
  ]
})
