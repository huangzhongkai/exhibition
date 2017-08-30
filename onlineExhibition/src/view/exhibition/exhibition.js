// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from '../../components/exhibition/exhibition_detail/exhibition_detail.vue'
import VueRouter from 'vue-router'
import VUeResource from 'vue-resource'
import Vuex from 'vuex'
import "../../common/stylus/index.styl"
import "bootstrap/dist/css/bootstrap.css"


Vue.config.productionTip = false

Vue.use(VUeResource)
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
  store,
  template: '<App/>',
  components: { App }
})
