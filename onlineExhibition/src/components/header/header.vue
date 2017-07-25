<template>
  <div class="header">
    <div class="content_wrapper">
      <div class="avatar">
        <img width="64" height="64" v-bind:src="header.avatar">
      </div>
      <div class="login" @click="login()">登录</div>
      <div class="name">
        {{header.name}}
      </div>
    </div>
    <div class="attention-wrapper">
      <div class="attention">
        <button v-on:click="addOne" v-bind:class="[attention_condition ? 'add_attention' : 'not_attention']"></button>
      </div>
      <div class="content_attention">
        <span>{{header.attention_count}}人关注</span>
      </div>
    </div>
    <div class="background">
      <img v-bind:src="header.avatar" width="100%" height="100%"/>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data () {
      return {
        attention_condition: false,
      }
    },
    props: {
      header: {
        type: Object
      }
    },
    methods: {
        login() {
          window.open('https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//kll2cwa.hk1.mofasuidao.cn/artist.html%3Fartist%3D0&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect')
        },
        addOne: function () {
//          if(this.attention_condition === true){
//            this.$http.delete('http://10.50.101.66:8887/attention/?artist='+ this.header.name).then(response => {
//                this.attention_condition = false;
//                this.header.attention_count -=1;
//            },response => {
//            });
//          }else{
//            this.$http.post('http://10.50.101.66:8887/attention/?artist=' + this.header.name).then(response => {
//              this.attention_condition = true;
//              this.header.attention_count +=1;
//            },response => {
//            });
//          }
        }
    }
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/mixin.styl";
  .header
    margin: 0px
    position: relative
    overflow: hidden
    .content_wrapper
      margin: 5px
      text-align:center
      .login
        position: absolute
        top: 10px
        left: 10px
    .attention-wrapper
      margin: 5px
      text-align:center
      .add_attention
        margin: 5px
        border-color: #7e8c8d
        border-radius: 10px
        color: black
      .not_attention
        margin: 5px
        border-color: #7e8c8d
        border-radius: 10px
        color: black
      .add_attention::after
        content: "已关注";
      .not_attention::after
        content: "+关注";
    .background
      position: absolute
      top: 0
      left: 0
      width: 100%
      height: 100%
      z-index: -1
      filter: blur(10px)
</style>
