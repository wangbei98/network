webpackJsonp([1],{"+/NM":function(t,e){},NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s=n("7+uW"),a={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("router-view")],1)},staticRenderFns:[]};var o=n("VU/8")({name:"App"},a,!1,function(t){n("+/NM")},null,null).exports,r=n("/ocq"),c={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("p",[this._v("主页")])])}]},i=n("VU/8")(null,c,!1,null,null,null).exports,u={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("p",[this._v("404 - Not Found")])])}]},l=n("VU/8")(null,u,!1,null,null,null).exports,f={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("p",[t._v("test")]),t._v(" "),n("el-button",{on:{click:t.getTestData}},[t._v("从后端获取数据")]),t._v(" "),n("p",[t._v(t._s(t.testData))])],1)},staticRenderFns:[]};var p=n("VU/8")({name:"test",computed:{testData:function(){return this.$store.state.testData}},methods:{getTestData:function(){this.$store.dispatch("getTestData")}}},f,!1,function(t){n("TqRg")},null,null).exports,m={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("p",[t._v("test")]),t._v(" "),n("el-button",{on:{click:t.getMessage}},[t._v("从后端的文件获取数据")]),t._v(" "),n("p",[t._v(t._s(t.message))])],1)},staticRenderFns:[]};var d=n("VU/8")({name:"test",computed:{message:function(){return this.$store.state.message}},methods:{getMessage:function(){this.$store.dispatch("getMessage")}}},m,!1,function(t){n("fODW")},null,null).exports;s.default.use(r.a);var g=new r.a({mode:"history",routes:[{path:"/",name:"Home",component:i},{path:"/test",name:"Test",component:p},{path:"/getMessage",name:"GetMessage",component:d},{path:"*",component:l}]}),h=n("NYxO"),v=n("mtWM"),_=n.n(v);_.a.defaults.baseURL="http://127.0.0.1:5000/api",s.default.use(h.a);var D=new h.a.Store({state:{testData:"",message:""},getters:{},mutations:{getTestData:function(t,e){t.testData=e},getMessage:function(t,e){t.message=e}},actions:{getTestData:function(t){_.a.get("/test").then(function(e){var n=e.data.data.token;t.commit("getTestData",n)}).catch(function(t){console.log(t)})},getMessage:function(t){_.a.get("/get_test_message").then(function(e){var n=e.data.data.message;t.commit("getMessage",n)}).catch(function(t){console.log(t)})}}}),M=n("zL8q"),$=n.n(M);n("tvR6");s.default.config.productionTip=!1,s.default.use($.a),new s.default({el:"#app",router:g,store:D,components:{App:o},template:"<App/>"})},TqRg:function(t,e){},fODW:function(t,e){},tvR6:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.eed7e2aa84fc45fc9bdc.js.map