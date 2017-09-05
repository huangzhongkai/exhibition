<template>
  <div>
    <div class="header">
      <img class="avatar" :src="person.avatar"/>
      <br/>
      <span class="nickname">{{person.name}}</span>
    </div>
    <!--<div class="info">-->
      <!--<span class="swaper">个人资料</span>-->
      <!--<i class="fa fa-angle-right fa-2x fa-pull-right " aria-hidden="true"></i>-->
    <!--</div>-->
    <div @click="show_collect()" class="info">
      <span class="swaper">收藏</span>
      <i class="fa fa-angle-right fa-2x fa-pull-right" aria-hidden="true"></i>
    </div>
    <div @click="bind_phone()" class="info">
      <span class="swaper">绑定手机号</span>
      <i class="fa fa-angle-right fa-2x fa-pull-right" aria-hidden="true"></i>
      <span class="phone_number">{{person.phone_number}}</span>
    </div>

    <collect ref="collect">
    </collect>

    <bind_phone ref="bind_phone">
    </bind_phone>

    <show_phone ref="show_phone">
    </show_phone>
  </div>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../common/js/util'
  import 'font-awesome-webpack'
  import global_ from '../Global.vue'
  import collect from './collect/collect.vue'
  import bind_phone from './bind_phone/bind_phone.vue'
  import show_phone from './bind_phone/show_phone.vue'

  let host = global_.host;
  export default {
    components: {
      collect,
      bind_phone,
      show_phone
    },
    data () {
      return {
        person:{
        },
        avatar_url: host + "/personal_information/personal_information.html",
        param: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })()
        },
      }
    },
    created() {
      this.$http.get('http://' + host + '/information/' + this.param.id + '/').then(response => {
        this.person = response.body;
      }, response => {
      });
    },
    methods:{
      show_collect(id){
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.collect.show();
      },
      bind_phone(){
        if(this.person.phone_number != ''){
          this.$refs.show_phone.show();
        }else{
          this.$refs.bind_phone.show();
        }
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/mixin.styl";
  .header
    width: 100%
    height: 160px
    background-image: url("background.jpeg")
    text-align: center
    .avatar
      margin-top:30px
      width: 80px
      height: 80px
      border-radius: 50%
    .nickname
      margin-top:10px
      color: white
  .info
    width: 100%
    height: 40px
    line-height:40px
    border-bottom: 1px
    border-style: solid
    border-color: darkgrey
    .swaper
      margin-left: 8px
    .phone_number
      float:right
    i
      color: #8c8c8c

</style>
