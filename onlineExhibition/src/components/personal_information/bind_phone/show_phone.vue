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
        <span>为了保证账号安全，请验证身份，验证成功后进行下一步操作</span>
        <div class="my_phone">
          <span class="number">{{person.phone_number}}</span>
        </div>
        <br>
        <div class="my_code input-group input-group-lg">
          <input v-model="auth_code" type="text" class="form-control" placeholder="输入验证码" aria-describedby="basic-addon2">
          <span class="input-group-btn">
            <button id="send_check_code" @click="sendMsg()" class="btn btn-primary" type="button">{{operation}}</button>
          </span>
        </div>
        <div class="my_commit">
          <button @click="commit()" type="button" class="btn btn-default" >验证身份</button>
        </div>
      </div>

      <div class="alert"></div>

      <bind_phone title="绑定新手机号" ref="bind_phone">
      </bind_phone>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
  import global_ from '../../Global.vue'
  import bind_phone from './bind_phone.vue'

  let host = global_.host;
  let count = 60;

  export default {
    components: {
      bind_phone,
    },
    data () {
      return {
        person:{},
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
        let params = {'phone_number':this.phone_number, 'auth_code': this.auth_code, 'wx_user_id': this.param.id};
        this.$http.post('http://'+ host +'/check_phone_commit/', params, {emulateJSON:true}).then(response => {
          if(response.body.code === 200){
            $('.alert').html('验证成功，请绑定新手机号').addClass('alert-success').show().delay(1500).fadeOut();
            this.$refs.bind_phone.show();
          }else if(response.body.code === -1){
            $('.alert').html('验证码错误').addClass('alert-warning').show().delay(1500).fadeOut();
          }
        },response => {
        });
      },
      time() {
        this.$store.state.check_timeout = this.$store.state.check_timeout -1;
        this.operation = this.$store.state.check_timeout +'s后可重发';
        if(this.$store.state.check_timeout === count-1){
          $('#send_check_code').removeClass('btn-primary').addClass('btn-default');
        }
        if(this.$store.state.check_timeout === 0){
          clearInterval(this.time_return_code);
          this.$store.state.check_timeout =count;
          this.operation = '发送验证码';
          $('#send_check_code').removeClass('btn-default').addClass('btn-primary');
        }
      },
      show() {
        $("title").html("验证手机号");
        this.showFlag = true;
      },
      hide() {
        this.showFlag = false;
      },
      sendMsg() {
        if(this.$store.state.check_timeout === count){
          let params = {'phone_number':this.phone_number, 'wx_user_id': this.param.id};
          this.$http.post('http://'+ host +'/send_auth_code/?type=check',params, {emulateJSON:true}).then(response => {
            if(response.body.code === 200){
              this.time_return_code = setInterval(this.time, 1000);
              $('.alert').html('验证码发送成功').addClass('alert-success').show().delay(2000).fadeOut();
            }else if(response.body.code === -1){
              $('.alert').html('验证码发送失败').addClass('alert-warning').show().delay(2000).fadeOut();
            }else if(response.body.code === -2){
              $('.alert').html('已绑定该手机号').addClass('alert-warning').show().delay(2000).fadeOut();
            }else if(response.body.code === -3){
              $('.alert').html('请输入正确的手机号码').addClass('alert-warning').show().delay(2000).fadeOut();
            }
          },response => {
          });
        }
      }
    },
    created() {
      this.$http.get('http://' + host + '/information/?id=' + this.param.id ).then(response => {
        this.person = response.body;
        this.phone_number = this.person.phone_number;
      }, response => {
      });
      if(this.$store.state.check_timeout != count && this.$store.state.check_timeout != 0){
        this.operation = this.$store.state.check_timeout +'s后可重发';
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
        margin-top: 40px
        margin-left: 20px
        margin-right: 20px
        .number
          font-size: 32px
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
