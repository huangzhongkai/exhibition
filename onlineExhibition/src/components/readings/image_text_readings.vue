<template>
  <div>
    <div class="top_image">
      <img width="100%" :src="reading.image_path">
    </div>
    <!--<div class="image_text_readings" v-for="item in reading.reading_content">-->
      <!--{{item}}-->
    <!--</div>-->
    <div class="reading">
      <div v-for="item in reading.reading_content" class="my_section">
        {{item}}
      </div>
    </div>
    <span style="float: right;">
      —— 张大千
    </span>
  </div>
</template>

<script>
  import {urlParse} from '../../common/js/util';
  import wx from 'weixin-js-sdk'
  import global_ from '../Global.vue'

  let host = global_.host;

  export default {
    data () {
      return {
        config:{},
        readings:[],
        reading:{},
        params: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })(),
          type: (() => {
            let queryParam = urlParse();
            return queryParam.type;
          })()
        },
      }
    },
    created() {
      if(this.params.type === 'exhibit'){
        this.$http.get('http://'+ host +'/exhibit_image_text_readings/'+ this.params.id +'/').then(response => {
          this.reading = response.body;
        },response => {
        });
      }else if(this.params.type === 'exhibition'){
        this.$http.get('http://'+ host +'/exhibition_image_text_readings/'+ this.params.id + '/').then(response => {
          this.reading = response.body;
        },response => {
        });
      };

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
          _this.$http.get('http://qb4dwjh.hk1.mofasuidao.cn/motified_signature/?' +
            'url='+ encodeURIComponent(location.href.split('#')[0])).then(response => {
            window.location.reload();
          },response => {
          });
        });

      },response => {
      });
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .reading
    margin: 5px 5px 5px 5px
    height: 200px
    border-color: antiquewhite
    border: 2px
    border-style: solid
    border-radius: 5px
    background-color: antiquewhite
    padding-top: 10px
    line-height: 20px
    overflow: auto
    .my_section
      margin: 10px
</style>
