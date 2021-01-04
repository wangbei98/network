// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import {store} from './store/store.js'

Vue.config.productionTip = false

import VueSocketio from 'vue-socket.io';  

Vue.use(VueSocketio,'http://127.0.0.1:5000/chat');

// 引入 element ui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
