<template>
  <div>
    <div class="header">
      <img class="avatar" :src="person.avatar"/>
      <div><br/></div>
      <span class="nickname">{{person.name}}</span>
    </div>
    <!--<div class="info">-->
      <!--<span class="swaper">个人资料</span>-->
      <!--<i class="fa fa-angle-right fa-2x fa-pull-right " aria-hidden="true"></i>-->
    <!--</div>-->
    <div class="interval"></div>
    <div @click="show_collect()" class="info">
      <i class="star fa fa-star-o fa-1x" aria-hidden="true"></i>
      <span class="swaper">收藏</span>
      <i class="angle fa fa-angle-right fa-2x fa-pull-right" aria-hidden="true"></i>
    </div>
    <div @click="bind_phone()" class="info">
      <i class="star fa fa-mobile fa-1x" aria-hidden="true"></i>
      <span class="swaper">绑定手机号</span>
      <i class="angle fa fa-angle-right fa-2x fa-pull-right" aria-hidden="true"></i>
      <span class="phone_number">{{person.phone_number}}</span>
    </div>
    <div class="bottom-box">
      <div class="tab">
        <div class="tab-item">
            <span>
              <i class="fa fa-reply fa-1x" aria-hidden="true"></i>
              <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
              <span @click="back()" style="margin-left: 1px">返回</span>
            </span>
        </div>
      </div>
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
      this.$http.get('http://' + host + '/information/?id=' + this.param.id).then(response => {
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
          this.$refs.bind_phone.show('绑定手机号');
        }
      },
      back(){
        window.history.back();
      },
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/mixin.styl";
  .header
    width: 100%
    height: 163pt
    background-image: url("background.jpeg")
    text-align: center
    .avatar
      margin-top:23pt
      width: 75pt
      height: 75pt
      border-radius: 50%
    .nickname
      margin-top:16pt
      color: white
      font-size: 18pt
  .interval
    height: 5pt
    background-color: #f5f5f9
  .info
    width: 100%
    height: 40pt
    line-height:40pt
    border-bottom: 1px
    border-style: solid
    border-color: darkgrey
    .phone_number
      float:right
    i
      color: #8c8c8c
    .star
      margin-left: 19pt
      margin-right: 21pt
    .angle
      margin-top: 10pt
      margin-right: 14pt
  .bottom-box
    position: fixed
    left: 0
    bottom: 0
    z-index: 20
    width: 100%
    height: 48px
    background-color: white
    border-top:1px solid gainsboro
    .tab
      display: flex
      width: 100%
      height: 48px
      line-height: 40px
      border-color: white
      border-1px(rgba(7, 17, 27, 0.1))
      .tab-item
        flex: 1
        margin-top: 2px
        margin-bottom: 2px
        text-align: center

</style>
