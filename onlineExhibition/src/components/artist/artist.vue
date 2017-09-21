<template>
  <div>
    <v-header :header="artist" ref="header"></v-header>
    <div class="tab">
      <div class="tab-item" @click="count()">
        <router-link to="/exhibit" >作品</router-link>
      </div>
      <div class="tab-item" @click="count()">
        <router-link to="/exhibition">展览</router-link>
      </div>
      <div class="tab-item" @click="count()">
        <router-link to="/introduction">简介</router-link>
      </div>
      <div class="tab-item" @click="count()">
        <router-link to="/achievement">成就</router-link>
      </div>
    </div>
    <router-view></router-view>
    <div class="bottom-box">
      <div class="tab">
        <div class="tab-item">
          <span>
            <i class="fa fa-reply fa-1x" aria-hidden="true"></i>
            <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
            <span @click="back()" style="margin-left: 1px">返回</span>
          </span>
        </div>
        <div class="tab-item">
          <span>
            <i class="fa fa-home fa-1x" aria-hidden="true"></i>
            <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
            <span @click="home()" style="margin-left: 1px">首页</span>
          </span>
        </div>
      </div>
    </div>
    <div style="height: 48px"></div>
  </div>
</template>

<script type="text/ecmascript-6">
  import header from "./../header/header.vue"
  import {urlParse} from '../../common/js/util';
  import wx from 'weixin-js-sdk'

  import global_ from './../Global.vue'
  import 'font-awesome-webpack'

  let host = global_.host;

  export default {
    data (){
      return {
        counter:-1,
        config:{},
        artist:{},
        header: {
          artist: (() => {
            let queryParam = urlParse();
            return queryParam.artist;
          })()
        },
      };
    },
    created() {
      this.$http.get('http://'+ host +'/artist/?id='+ this.header.artist).then(response => {
        if(response.body === 'error'){
          window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ encodeURIComponent(host) +'/home_html/&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
        }
        this.artist = response.body;
        this.$refs.header.update(this.artist.isAttention);

        this.$http.get('http://'+ host +'/get_signature/?' +
          '&url='+ encodeURIComponent(location.href.split('#')[0])).then(response => {
          this.config = response.body;
          let _this = this;
          wx.config({
            debug: false, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
            appId: this.config.appid, // 必填，公众号的唯一标识
            timestamp: this.config.timestamp, // 必填，生成签名的时间戳
            nonceStr: this.config.noncestr, // 必填，生成签名的随机串
            signature: this.config.signature,// 必填，签名，见附录1
            jsApiList: [
              'onMenuShareAppMessage',
              'onMenuShareTimeline',
              'onMenuShareQQ',
              'onMenuShareWeibo',
              'onMenuShareQZone'
            ] // 必填，需要使用的JS接口列表，所有JS接口列表见附录2
          });
          wx.ready(function(){
            wx.onMenuShareAppMessage({
              title: _this.artist.share.title, // 分享标题
              desc: _this.artist.share.description, // 分享描述
              link: location.href, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
              imgUrl: _this.artist.share.url, // 分享图标
              type: '', // 分享类型,music、video或link，不填默认为link
              dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
              success: function () {
                // 用户确认分享后执行的回调函数
              },
              cancel: function () {
                // 用户取消分享后执行的回调函数
              }
            });
            wx.onMenuShareTimeline({
              title: _this.artist.share.title, // 分享标题
              link: location.href, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
              imgUrl: _this.artist.share.url, // 分享图标
              success: function () {
              },
              cancel: function () {
              }
            });
            wx.onMenuShareQQ({
              title: _this.artist.share.title, // 分享标题
              desc: _this.artist.share.description, // 分享描述
              link: location.href, // 分享链接
              imgUrl: _this.artist.share.url, // 分享图标
              success: function () {
              },
              cancel: function () {
              }
            });
            wx.onMenuShareQZone({
              title: _this.artist.share.title, // 分享标题
              desc: _this.artist.share.description, // 分享描述
              link: location.href, // 分享链接
              imgUrl: _this.artist.share.url, // 分享图标
              success: function () {
                // 用户确认分享后执行的回调函数
              },
              cancel: function () {
                // 用户取消分享后执行的回调函数
              }
            });
          });

//          wx.error(function(res){
//            _this.$http.get('http://10.50.101.66:8887/motified_signature/?' +
//              'url='+ encodeURIComponent(location.href.split('#')[0])).then(response => {
//              window.location.reload();
//            },response => {
//            });
//          });

        },response => {
        });

      },response => {
      });


    },
    methods: {
      count(){
        this.counter -= 1;
      },
      back(){
        window.history.go(this.counter);
      },
      home(){
        window.open('http://'+ host +'/home_html/');
      }
    },
    components: {
      'v-header':header
    },
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/mixin.styl";
  .tab
    display: flex
    width: 100%
    height: 40px
    line-height: 40px
    border-1px(rgba(7, 17, 27, 0.1))
  .tab-item
    flex: 1
    text-align: center
    & > a
      display: block
      font-size: 14px
      color: rgb(77, 85, 93)
      &.active
        /*border-bottom:2px solid red*/
        background-color: darkgrey;
        border-radius:5px;
        text-decoration: underline
        color: rgb(240, 20, 20)
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

