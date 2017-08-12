<template>
  <div>
    <div class="exhibition_detail">
      <div class="top_image">
        <img width="100%" :src="exhibition.image_path">
      </div>
      <div class="exhibition_info">
        <div class="info_left">
          <div>
            {{exhibition.name}}
          </div>
          <div>
            展览时间:{{exhibition.exhibition_date}}
          </div>
          <div>
            展览地点:{{exhibition.exhibition_site}}
          </div>
        </div>
        <div class="info_right">
          <div>
            展策人:{{exhibition.exhibition_curator}}
          </div>
        </div>
      </div>
      <!--<audio_reading :name="exhibition.audio_name" ref="audio_reading"></audio_reading>-->
      <!--<audio src="/static/exhibit/lyg.mp3" ref="audio"></audio>-->

      <div class="reading_top">
        <span class="left">展览解读</span>
        <span class="right" @click="more_reading()">查看更多</span>
      </div>

      <div class="reading_info" v-if="isShow(index)"  v-for="(reading, index) in exhibition.audio_readings">
        <div class="avatar">
          <img class="avatar_image_background" src="/static/exhibition/head1.jpeg"/>
          <img class="avatar_image_play" @click="show_audio(index)" :src="play_icon"/>
        </div>
        <div class="reading_audio">
          <audio :src="reading.audio_src" ref="my_audio" class="my_audio" id="my_audio"></audio>
        </div>
        <div class="reading_content">
          <div class="title">{{reading.reading_title}}</div>
          <div class="description">{{reading.reading_content}}</div>
        </div>
      </div>

      <div class="reading_info" v-if="isShow(index)" v-for="(reading, index) in exhibition.image_text_readings">
        <div class="avatar">
          <img class="avatar_image_background" :src="reading.image_path"/>
        </div>
        <div @click="show_image_text_readings(reading.id)" class="reading_content">
          <div class="title">{{reading.reading_title}}</div>
          <div class="description">{{reading.reading_content}}</div>
        </div>
      </div>
      <div class="reading_info"v-if="isShow(index)"  v-for="(reading, index) in exhibition.video_readings">
        <div class="avatar">
          <img class="avatar_image_background" src="/static/exhibition/head1.jpeg"/>
          <img class="avatar_image_play" @click="show_video(index)" src="/static/exhibition/play.svg"/>
        </div>
        <div class="reading_video">
          <video :src="reading.video_src" ref="my_video" class="my_video"></video>
        </div>
        <div @click="show_video_readings(reading.id)" class="reading_content">
          <div class="title">{{reading.reading_title}}</div>
          <div class="description">{{reading.reading_content}}</div>
        </div>
      </div>

      <div class="reading_top">
        <span class="left">人物作品</span>
        <span class="right" @click="more_charactor()">查看更多</span>
      </div>
      <div class="charactor">
        <img @click="show_charactor(charactor.id)" :src="charactor.image_path" v-for="charactor in exhibition.charactors"/>
      </div>

      <div class="reading_top">
        <span class="left">写意作品</span>
        <span class="right" @click="more_enjoyable()">查看更多</span>
      </div>
      <div class="enjoyable">
        <img @click="show_enjoyable(enjoyable.id)" :src="enjoyable.image_path" v-for="enjoyable in exhibition.enjoyables"/>
      </div>
    </div>
    <more_reading :exhibition_id="param.id" ref="more_reading">
    </more_reading>

    <more_charactor :exhibition_id="param.id" ref="more_charactor">
    </more_charactor>

    <more_enjoyable :exhibition_id="param.id" ref="more_enjoyable">
    </more_enjoyable>
  </div>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
//  import audio_reading from '../../audio/audio_reading.vue'
  import more_reading from "../more_reading/more_reading.vue"
  import more_charactor from "../more_charactor/more_charactor.vue"
  import more_enjoyable from "../more_enjoyable/more_enjoyable.vue"
  import wx from 'weixin-js-sdk'

  import global_ from '../Global.vue'

  let host = global_.host;

  export default {
    components: {
//      audio_reading,
      more_reading,
      more_charactor,
      more_enjoyable
    },
    data () {
      return {
        play_icon:'/static/exhibition/play.svg',
        isPlaying: false,
        config:{},
        select_show:{},
        my_video: false,
        exhibitions: [],
        exhibition: {},
        param: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })()
        },
      };
    },
    created() {
      if(this.param.id != undefined ){
        this.$http.get('http://'+ host +'/exhibitions/'+ this.param.id +'/').then(response => {
          this.exhibition = response.body;
        },response => {
        });
      }

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
    mounted() {
      //this.$store.commit('findDOM', {name: 'audio', dom: this.$refs.audio});

//      console.log(this.$refs.my_audio);
//      this.$refs.my_audio.addEventListener('ended', () => {
//        this.isPlaying = false;
//      });
    },
//    computed: {
//      audio() {
//        return this.$store.state.audio;
//      },
//    },
    methods: {
      more_reading () {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.more_reading.show();
      },
      more_charactor () {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.more_charactor.show();
      },
      more_enjoyable () {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.more_enjoyable.show();
      },
      show_video (index) {
        this.$refs.my_video[index].play();
        if(this.$store.state.isPlaying === true){
          this.$refs.audio_reading.play();
        }
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
      show_charactor(key) {
        window.open("http://"+ host +"/exhibit_html/?id=" + key);
      },
      show_enjoyable(key) {
        window.open("http://"+ host +"/exhibit_html/?id=" + key);
      },
      show_image_text_readings(key) {
        window.open("http://"+ host +"/image_text_readings_html/?id=" + key +'&type=exhibition');
      },
      show_video_readings(key) {
        window.open("http://"+ host +"/video_readings_html/?id=" + key +'&type=exhibition');
      },
      isShow (index) {
        if(index < 1){
          return true;
        }else{
          return false;
        }
      }
    }
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .exhibition_detail
    width: 100%
    background: #fff
    .exhibition_info
      border-color: #000
      display:flex
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
      background-color: #7e8c8d
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
      .reading_audio
        top: 0
        left: 0
        position: absolute
        margin: 5px 5px 5px 5px
        vertical-align: top
        display: inline-block
        width: 1px
        height: 1px
        z-index: 1
        .my_audio
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
    .charactor
      display: flex
      height: 180px
      width: 100%
      overflow: hidden
      img
        margin-left: 5px
        margin-right: 5px
        width:140px
    .enjoyable
      display: flex
      height: 180px
      width: 100%
      overflow: hidden
      img
        margin-left: 5px
        margin-right: 5px
        width:140px
</style>
