<template>
  <div>
    <div class="production_detail">
      <div class="top_image">
        <img id="image" width="100%" :src="exhibit.image_path">
      </div>
      <div class="exhibit_info">
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

      <div class="reading_top">
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
          <video ref="my_video" class="my_video">
            <source :src="reading.video_src" type="video/mp4">
          </video>
        </div>
        <div @click="show_video_readings(reading.id)" class="reading_content">
          <div class="title">{{reading.reading_title}}</div>
          <div class="description">{{reading.reading_content}}</div>
        </div>
      </div>
    </div>

    <div class="ratings">
      <span class="left">评论</span>
    </div>
    <div class="rating-wrapper">
      <ul>
        <li v-for="(rating,index) in exhibit.ratings" class="rating-item">
          <div class="avatar">
            <img @click="show_information(rating.wx_id)" width="28" height="28" :src="rating.avatar">
          </div>
          <div class="content">
            <h1 @click="add_rating('回复'+ rating.username,rating.id)" class="name">{{rating.username}}</h1>
            <p @click="add_rating('回复'+ rating.username,rating.id)" class="time">{{rating.rateTime}}</p>
            <p @click="add_rating('回复'+ rating.username,rating.id)" class="text">{{rating.text}}</p>
            <div v-show="image_ratings[index]" class="js-result">
              <img :src="exhibit.image_path" :style="{'width': e_width, 'margin-left':rating.x_coordinate, 'margin-top': rating.y_coordinate}"/>
              <!--<img @click="zoomout()" :width="w" :height="h" :src="rating.rate_image">-->
            </div>
          </div>
          <div class="flags">
            <img v-show="flag[index]" @click="show_rating(index)" class="flag" src="/static/exhibit/rating.png"/>
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
            <i class="fa fa-hand-o-up fa-1x" aria-hidden="true"></i>
            <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
            <span @click="remark_commend()" style="margin-left: 1px">可圈可点</span>
          </span>
        </div>
        <div class="tab-item">
          <span>
            <i class="fa fa-commenting-o fa-1x" aria-hidden="true"></i>
            <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
            <span @click="add_rating('发评论',-1)" style="margin-left: 1px">评论</span>
          </span>
        </div>
        <div class="tab-item">
          <span>
            <i :class="collect_icon" aria-hidden="true"></i>
            <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
            <span @click="collect(0)" style="margin-left: 1px">{{collect_flag}}</span>
          </span>
        </div>
      </div>
    </div>

    <div class="alert"></div>
    <more_reading :exhibit_id="param.id" ref="more_reading">
    </more_reading>

    <ratings :exhibit_id="param.id" ref="edit_ratings">
    </ratings>

    <remark_commend :exhibit_id="param.id" ref="remark_commend">
    </remark_commend>
    <div style="height: 48px"></div>
  </div>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
  import audio_reading from '../../audio/audio_reading.vue'
  import more_reading from '../more_reading/more_reading.vue'
  import remark_commend from './remark_commend.vue'
  import {formatDate} from '../../../common/js/date';
  import ratings from '../ratings/ratings.vue'
  import wx from 'weixin-js-sdk'
  import Cropper from 'cropperjs'
  import 'font-awesome-webpack'


  import global_ from '../../Global.vue'

  let host = global_.host;

  export default {
    components: {
      audio_reading,
      more_reading,
      ratings,
      remark_commend,
    },
    data () {
      return {
        e_width:'',
        is_more_rating:true,
        get_count:5,
        get_offset:5,
        collect_icon:'fa fa-star-o',
        collect_flag:'收藏',
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
        param: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })()
        },
      };
    },
    created() {
      this.e_width = screen.width * 128 / 40 + 'px';
      this.$http.get('http://'+ host +'/exhibit/?id='+ this.param.id).then(response => {
        if(response.body === 'error'){
          window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ encodeURIComponent(host) +'/home_html/&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
        }
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
        if(this.exhibit.collect_flag === true){
          this.collect_flag = '已收藏';
          this.collect_icon = 'fa fa-star';
        }

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
              title: _this.exhibit.share.title, // 分享标题
              desc: _this.exhibit.share.description, // 分享描述
              link: location.href, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
              imgUrl: _this.exhibit.share.url, // 分享图标
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
              title: _this.exhibit.share.title, // 分享标题
              link: location.href, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
              imgUrl: _this.exhibit.share.url, // 分享图标
              success: function () {
              },
              cancel: function () {
              }
            });
            wx.onMenuShareQQ({
              title: _this.exhibit.share.title, // 分享标题
              desc: _this.exhibit.share.description, // 分享描述
              link: location.href, // 分享链接
              imgUrl: _this.exhibit.share.url, // 分享图标
              success: function () {
              },
              cancel: function () {
              }
            });
            wx.onMenuShareQZone({
              title: _this.exhibit.share.title, // 分享标题
              desc: _this.exhibit.share.description, // 分享描述
              link: location.href, // 分享链接
              imgUrl: _this.exhibit.share.url, // 分享图标
              success: function () {
                // 用户确认分享后执行的回调函数
              },
              cancel: function () {
                // 用户取消分享后执行的回调函数
              }
            });
          });

//          wx.error(function(res){
//            _this.$http.get('http://qb4dwjh.hk1.mofasuidao.cn/motified_signature/?' +
//              'url='+ encodeURIComponent(location.href.split('#')[0])).then(response => {
//              window.location.reload();
//            },response => {
//            });
//          });

        },response => {
        });

      },response => {
      });

      let _this = this;
      $(window).scroll(function () {
        let scrpllTop = $(this).scrollTop();
        let scroolHeight = $(document).height();
        let windowHeight = $(this).height();
        if(_this.is_more_rating === true){
          if(scrpllTop + windowHeight === scroolHeight){
            _this.is_more_rating = false;
            $("#loading").css('display','block');
            _this.$http.get('http://'+ host +'/exhibit_ratings/?id='+ _this.param.id+'&get_count=' + _this.get_count
              + '&get_offset=' + _this.get_offset ).then(response => {
              for(let i=0; i<response.body.ratings.length; i++){
                _this.exhibit.ratings.push(response.body.ratings[i]);
                if(response.body.ratings[i].type === 1){
                  _this.flag.push(true);
                }else{
                  _this.flag.push(false);
                }

              }
              if(response.body.ratings.length < _this.get_count){
                $("#loading").html('没有更多评论了');
                _this.is_more_rating = false;
                _this.get_offset +=response.body.ratings.length;
              }else{
                _this.is_more_rating = true;
                _this.get_offset +=_this.get_count;
              }
            },response => {
            });

          }
        }
      })
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
      back(){
        window.history.back();
      },
      remark_commend () {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.remark_commend.show();
      },
      collect(type){
        if(this.collect_flag === '收藏'){
          $('.alert').html('收藏成功').addClass('alert-success').show().delay(1500).fadeOut();
          this.$http.post('http://' + host + '/collect/?id=' + this.param.id + "&type=" + type).then(response => {
            if(response.body === 'error'){
              window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ encodeURIComponent(host) +'/artist_html/%3Fartist%3D0&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
            }else{
              this.collect_flag = '已收藏';
              this.collect_icon = 'fa fa-star';
            }
          }, response => {
          });
        }else if(this.collect_flag === '已收藏'){
          this.$http.delete('http://' + host + '/collect/?id=' + this.param.id + "&type=" + type).then(response => {
            if(response.body === 'error'){
              window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ encodeURIComponent(host) +'/artist_html/%3Fartist%3D0&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
            }else{
              this.collect_flag = '收藏';
              this.collect_icon = 'fa fa-star-o';
            }
          }, response => {
          });
          $('.alert').html('已取消收藏').addClass('alert-warning').show().delay(1500).fadeOut();
        }
      },
      show_information(id){
//        window.open("http://"+ host +"/personal_information_html/?id=" + id);
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
        alert('aaaa');
        this.$refs.my_video[index].play();
//        if(this.$store.state.isPlaying === true){
//          this.$refs.audio_reading.play();
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
      add_rating (content,parent_id) {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.edit_ratings.show(content,parent_id);
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
    background: #fff
    margin-top: 5px
    margin-left: 5px
    margin-right 5px
    .top_image
      img
        max-width: 100%
    .exhibit_info
      border-color: #000
      display:flex
      .info_left
        margin-left:0px
        margin-right:auto
        color: #7e8c8d
    .reading_top
      margin-top: 5px
      margin-bottom: 5px
      margin-right: 0px
      display:flex
      .left
        margin-left: 0px
        margin-right: auto
      .right
        color: #7e8c8d
        margin-left: auto
        margin-right: 0px
    .reading_info
      position: relative
      margin: 5px 0px 5px 0px
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
    margin-left: 5px
    .left
      margin-left: 0px
      margin-right: auto
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
        margin-right: 30px
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
        .js-result
          width: 128px
          height: 128px
          border-color: aliceblue
          border: 1px
          border-style: solid
          border-radius: 5px
          overflow: hidden
      .flags
        margin-left :50px
        .flag
          position: absolute
          right: 10px
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

