// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from '../../components/artist/artist.vue'
import VueRouter from 'vue-router'
import VUeResource from 'vue-resource'
import achievement from "../../components/achievement/achievement.vue"
import exhibition from "../../components/exhibition/exhibition.vue"
import introduction from "../../components/introduction/introduction.vue"
import exhibit from "../../components/exhibit/exhibit.vue"
import Vuex from 'vuex'
import "../../common/stylus/index.styl"
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap.min"


Vue.config.productionTip = false



Vue.use(VueRouter)
Vue.use(VUeResource)

// var params = window.location.search.replace('?','').split('&');
// var artist = 'defaultAsrtist';
// for(var i=0; i<params.length; i++){
//   if(params[i].split('=')[0] ==='name'){
//     artist = params[i].split('=')[1];
//   }
// }

const routes = [
  { path: '/', redirect: '/exhibit' },
  { path: '/achievement', component: achievement },
  { path: '/exhibition', component: exhibition },
  { path: '/introduction', component: introduction },
  { path: '/exhibit', component: exhibit }
]


const router = new VueRouter({
  linkActiveClass: 'active',
  routes //（缩写）相当于 routes: routes
})

const app = new Vue({
  router
}).$mount('#app')


Vue.use(Vuex);


const store = new Vuex.Store({
  state: {
    isPlaying: false,
    DOM: {},
    audio: {
      name: '',
      src: 'http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/%E6%9D%8E%E7%8E%89%E5%88%9A-%E5%88%9A%E5%A5%BD%E9%81%87%E8%A7%81%E4%BD%A0.mp3',
      musicImgSrc: '',
    }
  },
  mutations: {
    play(state, flag) {
      state.isPlaying = flag;
    },
    findDOM(state, payload) {
      state.DOM[payload.name] = payload.dom;
    },
  },
  actions: {
    getData({ commit,state }) {
    }
  }
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
