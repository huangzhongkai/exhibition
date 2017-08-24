<template>
  <div>
    <div class="production_detail">
      <div class="top_image" :style="{height: isEnlarge? 'auto' : '150px'}">
        <img id="image" width="100%" :src="exhibit.image_path">
      </div>
      <!--<span @click="save()" class="save">保存</span>-->
      <div class="enlarge_icon" @click="enlarge_image(isEnlarge)">
        <i :class="{'icon-zoom-in':!isEnlarge, 'icon-zoom-out':isEnlarge}"></i>
      </div>
      <div class="production_info">
        <div class="info_left">
          <div>
            {{exhibit.name}}
          </div>
          <div>
            {{exhibit.author}}
          </div>
        </div>
      </div>
      <!--<audio_reading class='audio_reading' :name="exhibit.audio_name" ref="audio_reading"></audio_reading>-->
      <!--<audio :src="exhibit.audio_src" ref="audio"></audio>-->

      <div title="作品解读" class="reading_top">
        <span class="left">作品解读</span>
        <span class="right" @click="more_reading()">查看更多</span>
      </div>
      <div class="reading_info" v-if="isShow(index)"  v-for="(reading, index) in exhibit.audio_readings">
        <div class="avatar">
          <img class="avatar_image_background" src="/static/exhibition/head1.jpeg"/>
          <img class="avatar_image_play" @click="show_audio(index)" :src="play_icon"/>
        </div>
        <div class="reading_video">
          <audio :src="reading.audio_src" ref="my_audio" class="my_video"></audio>
        </div>
        <div class="reading_content">
          <div class="title">{{reading.reading_title}}</div>
          <div class="description">{{reading.reading_content}}</div>
        </div>
      </div>

      <div class="reading_info" v-if="isShow(index)" v-for="(reading, index) in exhibit.image_text_readings">
        <div class="avatar">
          <img class="avatar_image_background" :src="reading.image_path"/>
        </div>
        <div @click="show_image_text_readings(reading.id)" class="reading_content">
          <div class="title">{{reading.reading_title}}</div>
          <div class="description">{{reading.reading_content}}</div>
        </div>
      </div>
      <div class="reading_info"v-if="isShow(index)"  v-for="(reading, index) in exhibit.video_readings">
        <div class="avatar">
          <img class="avatar_image_background" src="/static/exhibition/head1.jpeg"/>
          <img class="avatar_image_play" @click="show_video(index)" src="/static/exhibit/play.svg"/>
        </div>
        <div class="reading_video">
          <video :src="reading.video_src" ref="my_video" class="my_video"></video>
        </div>
        <div @click="show_video_readings(reading.id)" class="reading_content">
          <div class="title">{{reading.reading_title}}</div>
          <div class="description">{{reading.reading_content}}</div>
        </div>
      </div>
    </div>

    <div class="ratings">
      <span class="left">评论</span>
      <div class="right">
        <span  @click="add_rating(0)">写评论</span>
        <span  @click="image_rating(1)">可圈可点</span>
      </div>

    </div>
    <div class="rating-wrapper">
      <ul>
        <li v-for="(rating,index) in exhibit.ratings" class="rating-item">
          <div class="avatar">
            <img width="28" height="28" :src="rating.avatar">
          </div>
          <div class="content">
            <h1 class="name">{{rating.username}}</h1>
            <p class="time">{{rating.rateTime}}</p>
            <p class="text">{{rating.text}}</p>
            <div>
              <img v-show="flag[index]" @click="show_rating(index)" class="flag" src="/static/exhibit/rating.png"/>
            </div>
            <div v-show="image_ratings[index]" class="js-result">
              <img @click="zoomout()" :width="w" :height="h" :src="rating.rate_image">
            </div>
          </div>
        </li>
      </ul>
    </div>
    <div class="bottom-box">
      <div class="tab">
        <div class="tab-item">
          <span>
            <span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>
            <span style="margin-left: 1px">可圈可点</span>
          </span>
        </div>
        <div class="tab-item">
          <span>
            <span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>
            <span @click="add_rating(0)" style="margin-left: 1px">评论</span>
          </span>
        </div>
        <div class="tab-item">
          <span>
            <span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>
            <span style="margin-left: 1px">收藏</span>
          </span>
        </div>
      </div>
    </div>


    <more_reading :exhibit_id="param.id" ref="more_reading">
    </more_reading>

    <ratings :exhibit_id="param.id" ref="edit_ratings">
    </ratings>
    <div style="height: 48px"></div>
  </div>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
  import audio_reading from '../../audio/audio_reading.vue'
  import more_reading from '../more_reading/more_reading.vue'
  import {formatDate} from '../../../common/js/date';
  import ratings from '../ratings/ratings.vue'
  import wx from 'weixin-js-sdk'
  import jQuery from 'jquery'
  import Cropper from 'cropperjs'

  import global_ from '../../Global.vue'

  let host = global_.host;

  export default {
    components: {
      audio_reading,
      more_reading,
      ratings
    },
    data () {
      return {
        input:'你好',
        flag:[],
        image_ratings:[],
        w:'128px',
        h:'128px',
        wh:false,
        result:'',
        cropper: {},
        play_icon:'/static/exhibition/play.svg',
        isPlaying: false,
        config:{},
        exhibit:{},
        isEnlarge: true,
        param: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })()
        },
      };
    },
    created() {
      console.log(this.param.id);
      this.$http.get('http://'+ host +'/exhibits/'+ this.param.id +'/').then(response => {

        this.exhibit = response.body;
        for(let i=0; i<this.exhibit.ratings.length; i++){
          this.exhibit.ratings[i]['text'] = this.utf8ToUtf16(this.exhibit.ratings[i]['text']);
          this.image_ratings.push(false);
          if(this.exhibit.ratings[i].type === 1){
            this.flag.push(true);
          }else{
            this.flag.push(false);
          }

        }
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
          _this.$http.get('http://qb4dwjh.hk1.mofasuidao.cn/motified_signature/?' +
            'url='+ encodeURIComponent(location.href.split('#')[0])).then(response => {
            window.location.reload();
          },response => {
          });
        });

      },response => {
      });

    },
//    mounted() {
//      this.$store.commit('findDOM', {name: 'audio', dom: this.$refs.audio});
//      this.$refs.audio.addEventListener('ended', () => {
//        this.$store.state.isPlaying = false;
//      });
//      this.$refs.audio.addEventListener('error', () => { console.log(' play error') });
//    },
//    computed: {
//      audio() {
//        return this.$store.state.audio;
//      },
//    },
    methods: {
      utf8ToUtf16(str){
        let patt = /&#(\d+);/g;
        return str.replace(patt,function(char){
          let code = char.match(/(\d+)/g)[0];
          let H = Math.floor((parseInt(code)-0x10000) / 0x400)+0xD800 // 高位

          let L = (parseInt(code) - 0x10000) % 0x400 + 0xDC00 // 低位

          return unescape('%u'+ H.toString(16) + '%u' + L.toString(16))
        });

      },
      zoomout () {
        if(this.wh === true){
          this.w = '256px';
          this.h = '256px';
          this.wh = false;
        }else if(this.wh === false){
          this.w = '128px';
          this.h = '128px';
          this.wh = true;
        }
      },
      show_video (index) {
        this.$refs.my_video[index].play();
        if(this.$store.state.isPlaying === true){
          this.$refs.audio_reading.play();
        }
      },
//      save () {
//        var croppedCanvas;
//        croppedCanvas = this.cropper.getCroppedCanvas({
//        });
//        this.result = croppedCanvas.toDataURL();
//
//
//        let _this = this;
//        this.cropper.getCroppedCanvas().toBlob(function (blob) {
//          var formData = new FormData();
//          formData.append('imageblob',blob)
//          _this.$http.post('http://'+ host +'/exhibit_image_ratings/'+ _this.param.id+'/', formData ).then(response => {
//          },response => {
//          });
//        });
//
//      },
      enlarge_image (bool) {
        this.isEnlarge = !bool;
//        if(this.isEnlarge === true){
//          var image = document.getElementById('image');
//          this.cropper = new Cropper(image, {
//            aspectRatio: 1 / 1,
//            autoCropArea:0.5,
//            dragMode: 'none',
//            zoomable:false,
//            crop: function(e) {
//
//            },
//            ready: function () {
//            }
//          });
//        }else{
//          this.cropper.destroy();
//        }
      },
      more_reading () {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.more_reading.show();
      },
      show_image_text_readings(key) {
        window.open("http://"+ host +"/image_text_readings_html/?id=" + key +'&type=exhibit');
      },
//      show_video_readings(key) {
//        window.open("http://"+ host +"/video_readings_html/?id=" + key +'&type=exhibit');
//      },
      add_rating (type) {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.edit_ratings.show(type);
      },
      image_rating (type) {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.edit_ratings.show(type);
      },
      show_audio (index) {
        !this.isPlaying ? this.$refs.my_audio[index].play() : this.$refs.my_audio[index].pause();
        !this.isPlaying ? this.play_icon = '/static/exhibition/pause.svg' : this.play_icon = '/static/exhibition/play.svg'
        this.isPlaying = !this.isPlaying;

        this.$refs.my_audio[0].addEventListener('ended', () => {
          this.play_icon = '/static/exhibition/play.svg'
          this.isPlaying = false;
        });
      },
      isShow (index) {
        if(index < 1){
          return true;
        }else{
          return false;
        }
      },
      show_rating(index){
        this.$set(this.image_ratings, index, !this.image_ratings[index])
      }
    },
    filters: {
      formatDate(time) {
        let date = new Date(time);
        return formatDate(date, 'yyyy-MM-dd hh:mm');
      }
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../../common/stylus/mixin.styl"

  .production_detail
    width: 100%
    background: #fff
    .top_image
      height: 256px
      overflow: hidden
      img
        max-width: 100%
    .save
      position: absolute
      top: 0px
      right: 0px
    .enlarge_icon
      position: relative
      top: -18px
      float: right
    .production_info
      border-color: #000
      display:flex
      margin-top: 5px
      .info_left
        margin-left:2px
        margin-right:auto
        color: #7e8c8d
      .info_right
        margin-left:auto
        margin-right:2px
        color: #7e8c8d
    .reading_top
      margin-top: 5px
      margin-bottom: 5px
      display:flex
      .left
        margin-left: 2px
        margin-right: auto
      .right
        color: #7e8c8d
        margin-left: auto
        margin-right: 2px
    .reading_info
      position: relative
      margin: 5px 5px 5px 5px
      width: 97%
      height: 80px
      border-color: aliceblue
      border: 2px
      border-style: solid
      border-radius: 5px
      background-color: white
      .reading_video
        top: 0
        left: 0
        position: absolute
        margin: 5px 5px 5px 5px
        vertical-align: top
        display: inline-block
        width: 1px
        height: 1px
        z-index: 1
        .my_video
          display: inline-block
          width: 100%
          height: 100%
      .avatar
        z-index: 2
        position: relative
        margin: 5px 5px 5px 5px
        vertical-align: top
        display: inline-block
        width: 64px
        height: 64px
        .avatar_image_play
          border-radius: 5px
          width: 32px
          height: 32px
          position: relative
          top: -48px
          right : -16px
        .avatar_image_background
          border-radius: 5px
          width: 64px
          height: 64px
      .reading_content
        position: absolute
        margin: 5px 5px 5px 5px
        display: inline-block
        margin-left: 16px
        .title
          height :20px
          line-height: 20px
          display: inline-block
          margin: 2px 0 2px 0
          overflow: hidden
          text-overflow: ellipsis
        .description
          height :40px
          display: inline-block
          margin-bottom: 10px
          font-size: 14px
          color: darkgrey
          line-height: 20px
          overflow: hidden
          text-overflow: ellipsis
  .ratings
    margin-top: 20px
    margin-bottom: 5px
    display:flex
    .left
      margin-left: 2px
      margin-right: auto
    .right
      color: #7e8c8d
      margin-left: auto
      margin-right: 2px
  .rating-wrapper
    padding: 0 18px
    .rating-item
      display: flex
      padding: 18px 0
      border-1px(rgba(7, 17, 27, 0.1))
      .avatar
        flex: 0 0 28px
        width: 28px
        margin-right: 12px
        img
          border-radius: 50%
      .content
        position: relative
        flex: 1
        .name
          margin-top: 0px
          line-height: 12px
          font-size: 10px
          color: rgb(7, 17, 27)
        .text
          margin-top: 4px
          margin-bottom: 8px
          line-height: 12px
          color: rgb(7, 17, 27)
          font-size: 14px
        .time
          margin-top: 4px
          margin-bottom: 8px
          line-height: 12px
          color: rgb(7, 17, 27)
          font-size: 10px
        .flag
          position: absolute
          top: 0
          right: 0
          width: 16px
          height: 16px
          line-height: 12px
          font-size: 10px
          color: rgb(147, 153, 159)
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

