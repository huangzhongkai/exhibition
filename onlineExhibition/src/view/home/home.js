/**
 * Created by huangzhongkai on 2017/6/26.
 */
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueResource from 'vue-resource'
import App from '../../components/home/home.vue'
import VueAwesomeSwiper from 'vue-awesome-swiper';
import "../../common/stylus/index.styl"


Vue.config.productionTip = false

Vue.use(VueResource)
Vue.use(VueAwesomeSwiper)




/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})
