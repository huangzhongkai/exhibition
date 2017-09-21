<template>
  <transition name="move">
    <div v-show="showFlag">
      <div class="bottom-box">
        <div class="tab">
          <div class="tab-item">
              <span @click="hide()">
                <i class="fa fa-reply fa-1x" aria-hidden="true"></i>
                <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
                <span style="margin-left: 1px">返回</span>
              </span>
          </div>
        </div>
      </div>
      <div class="more_reading" ref="more_reading_content">
        <div class="production-content">
          <!--<div class="top">-->
            <!--展览解读-->
          <!--</div>-->
          <!--<div class="back" @click="hide()">-->
            <!--<i class="icon-arrow_lift"></i>-->
          <!--</div>-->
          <div class="more_content" >
            <div class="more_reading_info" v-for="(reading, index) in exhibition.audio_readings">
              <div class="avatar">
                <img class="avatar_image_background" src="/static/exhibition/head1.jpeg"/>
                <img class="avatar_image_play" @click="show_audio(index)" :src="play_icon[index]"/>
              </div>
              <div class="reading_video">
                <audio :src="reading.audio_src" ref="my_audio" class="my_video"></audio>
              </div>
              <div class="more_reading_content">
                <div class="title">{{reading.reading_title}}</div>
                <div class="description">{{reading.reading_content}}</div>
              </div>
            </div>
            <div class="more_reading_info" v-for="reading in exhibition.image_text_readings">
              <div class="avatar">
                <img class="avatar_image_background" :src="reading.image_path"/>
              </div>
              <div @click="show_image_text_readings(reading.id)" class="more_reading_content">
                <div class="title">{{reading.reading_title}}</div>
                <div class="description">{{reading.reading_content}}</div>
              </div>
            </div>
            <div class="more_reading_info" v-for="(reading, index) in exhibition.video_readings">
              <div class="avatar">
                <img class="avatar_image_background" src="/static/exhibition/head1.jpeg"/>
                <img class="avatar_image_play" @click="show_video(index)" src="/static/exhibition/play.svg"/>
              </div>
              <div class="reading_video">
                <video :src="reading.video_src" ref="my_video" class="my_video"></video>
              </div>
              <div class="more_reading_content">
                <div class="title">{{reading.reading_title}}</div>
                <div class="description">{{reading.reading_content}}</div>
              </div>
            </div>
          </div>
          <div style="height: 53px"></div>
        </div>
      </div>
    </div>
    </transition>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
  import audio_reading from '../../audio/audio_reading.vue'
  import BScroll from 'better-scroll';

  import global_ from '../../Global.vue'

  let host = global_.host;

  export default {
    props: {
      exhibition_id:0
    },
    data () {
      return {
        title:'',
        play_icon:[],
        isPlaying: [],
        exhibitions:[],
        exhibition:{},
        showFlag: false,
      };
    },
    methods: {
      show() {
        this.title = $('title').html();
        $('title').html('作品解读');
        this.showFlag = true;
        this.$nextTick(() => {
          if (!this.scroll) {
            this._initScroll();
          } else {
            this.scroll.refresh();
          }
        });
      },
      hide() {
        $('title').html(this.title);
        this.showFlag = false;
        document.body.style.height = '';
        document.body.style.overflow = '';
      },
      show_video (index) {
        this.$refs.my_video[index].play();
        if(this.$store.state.isPlaying === true){
          this.$refs.audio_reading.play();
        }
      },
      show_audio (index) {
        !this.isPlaying[index] ? this.$refs.my_audio[index].play() : this.$refs.my_audio[index].pause();
        !this.isPlaying[index] ? this.$set(this.play_icon, index, '/static/exhibition/pause.svg')  :
          this.$set(this.play_icon, index, '/static/exhibition/play.svg')
        this.isPlaying[index] = !this.isPlaying[index];

        this.$refs.my_audio[index].addEventListener('ended', () => {
          this.$set(this.play_icon, index, '/static/exhibition/play.svg')
          this.isPlaying[index] = false;
        });
      },
      _initScroll() {
        this.scroll = new BScroll(this.$refs.more_reading_content, {
          click: true,
        });
      },
      show_image_text_readings(key) {
        window.open("http://"+ host +"/image_text_readings_html/?id=" + key +'&type=exhibition');
      },
      show_video_readings(key) {
        window.open("http://"+ host +"/video_readings_html/?id=" + key +'&type=exhibition');
      },
    },
    created() {
      if(this.exhibition_id != undefined){
        this.$http.get('http://'+ host +'/exhibition_readings/?id='+ this.exhibition_id).then(response => {
          this.exhibition = response.body;
          for(let i=0; i<this.exhibition.audio_readings.length; i++){
            this.play_icon.push('/static/exhibition/play.svg');
            this.isPlaying.push(false);
          }
        },response => {
        });
      }
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../../common/stylus/mixin.styl";

  .more_reading
    position: fixed
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
      position: relative
      border-1px(rgba(7, 17, 27, 0.1))
      height: 40px
      line-height: 40px
      text-align: center
    .back
      position: absolute
      top: 0px
      left: 0px
      .icon-arrow_lift
        display: block
        font-size: 20px
        line-height: 40px
        color: black
    .more_content
      width: 100%
      overflow: hidden
      bottom: 0px
      .more_reading_info
        margin: 2px 5px 0px 5px
        width: 97%
        height: 80px
        border-color: aliceblue
        border: 1px
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
      .more_reading_content
        position: absolute
        margin: 5px 5px 5px 5px
        display: inline-block
        margin-left: 16px
        .title
          display: inline-block
          margin: 2px 0 8px 0
        .description
          height :40px
          display: inline-block
          margin-bottom: 10px
          font-size: 14px
          color: darkgrey
          line-height: 20px
          overflow: hidden
          text-overflow: ellipsis
  .bottom-box
    position: fixed
    left: 0
    bottom: 0
    z-index: 50
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
