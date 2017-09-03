/**
 * Created by huangzhongkai on 2017/6/29.
 */
import Vue from 'vue'
import App from '../../components/exhibit/exhibit_detail/exhibit_detail.vue'

import VUeResource from 'vue-resource'
import Vuex from 'vuex'
import "../../common/stylus/index.styl"
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap.min"
import "cropperjs/dist/cropper.css"


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
