<template>
  <div>
    <v-header :header="artist" ref="header"></v-header>
    <div class="tab">
      <div class="tab-item">
        <router-link to="/exhibit" >作品</router-link>
      </div>
      <div class="tab-item">
        <router-link to="/exhibition">展览</router-link>
      </div>
      <div class="tab-item">
        <router-link to="/introduction">简介</router-link>
      </div>
      <div class="tab-item">
        <router-link to="/achievement">成就</router-link>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script type="text/ecmascript-6">
  import header from "./header/header.vue"
  import {urlParse} from '../common/js/util';
  import wx from 'weixin-js-sdk'

  import global_ from './Global.vue'

  let host = global_.host;

  export default {
      data (){
        return {
          config:{},
          artist:{},
          header: {
            artist: (() => {
              let queryParam = urlParse();
              return queryParam.artist;
            })(),
            code: (() => {
              let queryParam = urlParse();
              return queryParam.code;
            })()
          },
        };
      },
      created() {
        this.$http.get('http://'+ host +'/artists/'+ this.header.artist + '/?code=' + this.header.code).then(response => {
          this.artist = response.body;
          this.$refs.header.update(this.artist.isAttention);
        },response => {
        });

        this.$http.get('http://'+ host +'/get_signature/?' +
          '&url='+ encodeURIComponent(location.href.split('#')[0])).then(response => {
          this.config = response.body;
          let _this = this;
          wx.config({
            debug: true, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
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
              title: '在线艺术品超市分享给朋友', // 分享标题
              desc: '在线艺术品超市，展厅,高大上的艺术家都在这里，加关注，不迷路', // 分享描述
              link: location.href, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
              imgUrl: 'http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/backround.jpg', // 分享图标
              type: '', // 分享类型,music、video或link，不填默认为link
              dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
              success: function () {
                // 用户确认分享后执行的回调函数
                alert('success');
              },
              cancel: function () {
                // 用户取消分享后执行的回调函数
                alert('fail');
              }
            });
            wx.onMenuShareTimeline({
              title: '在线艺术品超市分享到朋友圈', // 分享标题
              link: location.href, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
              imgUrl: 'http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/backround.jpg', // 分享图标
              success: function () {
              },
              cancel: function () {
              }
            });
            wx.onMenuShareQQ({
              title: '在线艺术品超市分享到qq', // 分享标题
              desc: '在线艺术品超市，展厅,高大上的艺术家都在这里，加关注，不迷路', // 分享描述
              link: location.href, // 分享链接
              imgUrl: 'http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/backround.jpg', // 分享图标
              success: function () {
              },
              cancel: function () {
              }
            });
            wx.onMenuShareQZone({
              title: '在线艺术品超市分享到QZone', // 分享标题
              desc: '在线艺术品超市，展厅,高大上的艺术家都在这里，加关注，不迷路', // 分享描述
              link: location.href, // 分享链接
              imgUrl: 'http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/backround.jpg', // 分享图标
              success: function () {
                // 用户确认分享后执行的回调函数
              },
              cancel: function () {
                // 用户取消分享后执行的回调函数
              }
            });
          });

          wx.error(function(res){
            _this.$http.get('http://10.50.101.66:8887/motified_signature/?' +
              'url='+ encodeURIComponent(location.href.split('#')[0])).then(response => {
              window.location.reload();
            },response => {
            });
          });

        },response => {
        });
        if(this.header.code === undefined){
          window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ host +'/artist_html/%3Fartist%3D0&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
        }
      },
      components: {
        'v-header':header
      },
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../common/stylus/mixin.styl";
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
        color: rgb(240, 20, 20)

</style>
