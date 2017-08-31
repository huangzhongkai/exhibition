<template>
  <transition name="move">
    <div v-show="showFlag" class="bind">
      <div class="top">
        绑定手机号
      </div>
      <div class="back" @click="hide">
        <i class="icon-arrow_lift"></i>
      </div>
      <div class="content">
        <div class="my_phone input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon1">手机</span>
          <input v-model="phone_number" type="text" class="form-control" placeholder="" aria-describedby="sizing-addon1">
        </div>
        <br>
        <div class="my_code input-group input-group-lg">
          <input v-model="auth_code" type="text" class="form-control" placeholder="输入验证码" aria-describedby="basic-addon2">
          <span @click="sendMsg()" class="input-group-addon" id="basic-addon2">{{operation}}</span>
        </div>
        <div class="my_commit">
          <button @click="commit()" type="button" class="btn btn-default" >提交</button>
        </div>
      </div>

      <div class="alert"></div>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
  import global_ from '../../Global.vue'

  let host = global_.host;

  export default {
    data () {
      return {
        phone_number:'',
        auth_code:'',
        showFlag: false,
        operation:'发送验证码',
        time_return_code:'',
        param: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })()
        },
      };
    },
    methods: {
      commit(){
        let params = {'phone_number':this.phone_number, 'auth_code': this.auth_code, 'wx_user_id': 13};
        this.$http.post('http://'+ host +'/bing_phone_commit/', params, {emulateJSON:true}).then(response => {
          if(response.body.code === 200){
            window.location.reload();
          }else if(response.body.code === -1){
            $('.alert').html('验证码错误').addClass('alert-warning').show().delay(1500).fadeOut();
          }
        },response => {
        });
      },
      time() {
        this.$store.state.timeout = this.$store.state.timeout -1;
        this.operation = '重新发送' + this.$store.state.timeout + 's';
        if(this.$store.state.timeout === 0){
          clearInterval(this.time_return_code);
          this.$store.state.timeout =21;
          this.operation = '发送验证码'
        }
      },
      show() {
        this.showFlag = true;
      },
      hide() {
        this.showFlag = false;
      },
      sendMsg() {
        if(this.$store.state.timeout === 21){
          this.time_return_code = setInterval(this.time, 1000);
          let params = {'phone_number':this.phone_number, 'wx_user_id': 13};
          this.$http.post('http://'+ host +'/send_auth_code/',params, {emulateJSON:true}).then(response => {
            if(response.body.code === 200){
              $('.alert').html('验证码发送成功').addClass('alert-success').show().delay(1500).fadeOut();
            }else{
              $('.alert').html('验证码发送失败').addClass('alert-warning').show().delay(1500).fadeOut();
            }
          },response => {
          });
        }
      }
    },
    created() {
      console.log(this.$store.state.timeout);
      if(this.$store.state.timeout != 21 && this.$store.state.timeout != 0){
        this.operation = '重新发送' + this.$store.state.timeout +'s';
        this.time_return_code = setInterval(this.time, 1000)
      }else{
        this.operation = '发送验证码'
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../../common/stylus/mixin.styl";
  .bind
    position: absolute
    left: 0
    top: 0
    z-index: 30
    width: 100%
    height: 100%
    background: #fff
    overflow: hidden
    transform: translate3d(0, 0, 0)
    &.move-enter-active, &.move-leave-active
      transition: all 0.2s linear
    &.move-enter, &.move-leave-active
      transform: translate3d(100%, 0, 0)
    .top
      border-1px(rgba(7, 17, 27, 0.1))
      margin-top:10px
      height: 32px
      text-align: center
    .back
      position: absolute
      top: 0px
      left: 0px
      .icon-arrow_lift
        display: block
        padding: 10px
        font-size: 20px
        color: black
    .content
      width:100%
      position: absolute
      top: 50px
      bottom: 0px
      .my_phone
        margin-top: 60px
        margin-left: 20px
        margin-right: 20px
      .my_code
        margin-top: 20px
        margin-left: 20px
        margin-right: 20px
      .my_commit
        margin-top: 30px
        text-align: center
    .alert
      display: none
      position: fixed
      top: 50%
      left: 50%
      min-width: 200px
      margin-left: -100px
      z-index: 99999
      padding: 15px
      border: 1px solid transparent
      border-radius: 4px
      text-align: center
    .alert-success
      color: #3c763d
      background-color: #dff0d8
      border-color: #d6e9c6
    .alert-warning
      color: #f01414
      background-color: #fcf8e3
      border-color: #faebcc
</style>
