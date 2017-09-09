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

    <div class="ratings">
      <span class="left">评论</span>
      <div class="right">
        <!--<span  @click="add_rating(0)">写评论</span>-->
        <!--<span  @click="image_rating(1)">可圈可点</span>-->
      </div>

    </div>
    <div class="rating-wrapper">
      <ul>
        <li v-for="(rating,index) in exhibition.ratings" class="rating-item">
          <div class="avatar">
            <img @click="show_information(rating.wx_id)" width="28" height="28" :src="rating.avatar">
          </div>
          <div class="content" @click="add_rating(0,'回复',rating.id)">
            <h1 class="name">{{rating.username}}</h1>
            <p class="time">{{rating.rateTime}}</p>
            <p class="text">{{rating.text}}</p>
          </div>
        </li>
      </ul>
    </div>
    <div style="display: none;" class="load-more-gif" id="loading">loading...</div>
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
            <i class="fa fa-commenting-o fa-1x" aria-hidden="true"></i>
            <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
            <span @click="add_rating(0,'发评论',-1)" style="margin-left: 1px">评论</span>
          </span>
        </div>
        <div class="tab-item">
          <span>
            <i :class="collect_icon" aria-hidden="true"></i>
            <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
            <span @click="collect(1)" style="margin-left: 1px">{{collect_flag}}</span>
          </span>
        </div>
      </div>
    </div>

    <more_reading :exhibition_id="param.id" ref="more_reading">
    </more_reading>

    <more_exhibit :exhibition_id="param.id" type="charactor" ref="more_charactor">
    </more_exhibit>

    <more_exhibit :exhibition_id="param.id" type="enjoyable" ref="more_enjoyable">
    </more_exhibit>

    <ratings :exhibition_id="param.id" ref="edit_ratings">
    </ratings>
    <div style="height: 72px"></div>
    <div class="alert"></div>
  </div>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
//  import audio_reading from '../../audio/audio_reading.vue'
  import more_reading from "../more_reading/more_reading.vue"
  import more_exhibit from "../more_exhibit/more_exhibit.vue"
  import wx from 'weixin-js-sdk'
  import ratings from '../ratings/ratings.vue'
  import 'font-awesome-webpack'
  import global_ from '../../Global.vue'

  let host = global_.host;

  export default {
    components: {
      ratings,
      more_reading,
      more_exhibit
    },
    data () {
      return {
        is_more_rating:true,
        get_count:5,
        get_offset:5,
        flag:[],
        image_ratings:[],
        collect_icon:'fa fa-star-o',
        collect_flag:'收藏',
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
          if(response.body === 'error'){
            window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ encodeURIComponent(host) +'/home_html/&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
          }
          this.exhibition = response.body;
          for(let i=0; i<this.exhibition.ratings.length; i++){
            this.exhibition.ratings[i]['text'] = this.utf8ToUtf16(this.exhibition.ratings[i]['text']);
            this.image_ratings.push(false);
            if(this.exhibition.ratings[i].type === 1){
              this.flag.push(true);
            }else{
              this.flag.push(false);
            }
          }
          if(this.exhibition.collect_flag === true){
            this.collect_flag = '已收藏';
            this.collect_icon = 'fa fa-star';
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
                title: _this.exhibition.share.title, // 分享标题
                desc: _this.exhibition.share.description, // 分享描述
                link: location.href, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
                imgUrl: _this.exhibition.share.url, // 分享图标
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
                title: _this.exhibition.share.title, // 分享标题
                link: location.href, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
                imgUrl: _this.exhibition.share.url, // 分享图标
                success: function () {
                },
                cancel: function () {
                }
              });
              wx.onMenuShareQQ({
                title: _this.exhibition.share.title, // 分享标题
                desc: _this.exhibition.share.description, // 分享描述
                link: location.href, // 分享链接
                imgUrl: _this.exhibition.share.url, // 分享图标
                success: function () {
                },
                cancel: function () {
                }
              });
              wx.onMenuShareQZone({
                title: _this.exhibition.share.title, // 分享标题
                desc: _this.exhibition.share.description, // 分享描述
                link: location.href, // 分享链接
                imgUrl: _this.exhibition.share.url, // 分享图标
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

        },response => {
        });
      }

      let _this = this;
      $(window).scroll(function () {
        let scrpllTop = $(this).scrollTop();
        let scroolHeight = $(document).height();
        let windowHeight = $(this).height();
        if(_this.is_more_rating === true){
          if(scrpllTop + windowHeight === scroolHeight){
            $("#loading").css('display','block');
            _this.$http.get('http://'+ host +'/exhibition_ratings/'+ _this.param.id+'/?get_count=' + _this.get_count
              + '&get_offset=' + _this.get_offset ).then(response => {
              for(let i=0; i<response.body.ratings.length; i++){
                _this.exhibition.ratings.push(response.body.ratings[i]);
              }
              if(response.body.ratings.length < _this.get_count){
                $("#loading").html('没有更多评论了');
                _this.is_more_rating = false;
                _this.get_offset +=response.body.ratings.length;
              }else{
                _this.get_offset +=_this.get_count;
              }
            },response => {
            });

          }
        }
      })
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
      back(){
        window.history.back();
      },
      collect(type){
        if(this.collect_flag === '收藏'){
          $('.alert').html('收藏成功').addClass('alert-success').show().delay(1500).fadeOut();
          this.$http.post('http://' + host + '/collect/' + this.param.id + '/'+ "?type=" + type).then(response => {
            if(response.body === 'error'){
              window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ encodeURIComponent(host) +'/artist_html/%3Fartist%3D0&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
            }else{
              this.collect_flag = '已收藏';
              this.collect_icon = 'fa fa-star';
            }
          }, response => {
          });
        }else if(this.collect_flag === '已收藏'){
          $('.alert').html('已收藏').addClass('alert-warning').show().delay(1500).fadeOut();
        }
      },
      show_information(id){
        let url = "http://"+ host +"/personal_information_html/?id=" + id;
        window.open(url);
      },
      utf8ToUtf16(str){
        let patt = /&#(\d+);/g;
        return str.replace(patt,function(char){
          let code = char.match(/(\d+)/g)[0];
          let H = Math.floor((parseInt(code)-0x10000) / 0x400)+0xD800 // 高位

          let L = (parseInt(code) - 0x10000) % 0x400 + 0xDC00 // 低位

          return unescape('%u'+ H.toString(16) + '%u' + L.toString(16))
        });

      },
      add_rating (type,content,parent_id) {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.edit_ratings.show(type,content,parent_id);
      },
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
  @import "../../../common/stylus/mixin.styl"
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
        border-color: darkgrey
        border-style: solid
        border-radius: 5px
        border-width:1px
        background-color: white
        margin-left: 5px
        margin-right: 5px
        width:140px
    .enjoyable
      display: flex
      height: 180px
      width: 100%
      overflow: hidden
      img
        border-color: darkgrey
        border-style: solid
        border-radius: 5px
        border-width:1px
        background-color: white
        margin-left: 5px
        margin-right: 5px
        width:140px
  .ratings
    margin-top: 20px
    margin-bottom: 5px
    margin-left: 5px
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
      padding: 12px 0
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
          line-height: 8px
          font-size: 14px
          color: rgb(7, 17, 27)
        .text
          margin-top: 4px
          margin-bottom: 8px
          line-height: 16px
          color: rgb(7, 17, 27)
          font-size: 12px
        .time
          margin-top: 4px
          margin-bottom: 8px
          line-height: 8px
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
    color: #8a6d3b
    background-color: #fcf8e3
    border-color: #faebcc
  .load-more-gif
    width: 100%
    height: 44px
    text-align: center
    line-height: 44px
    background: #fff
    border-top: none
    color: #48B884
</style>
