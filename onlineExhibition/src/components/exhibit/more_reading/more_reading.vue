<template>
  <transition name="move">
    <div v-show="showFlag" class="more_reading">
      <div class="top">
        展览解读
      </div>
      <div class="back" @click="hide">
        <i class="icon-arrow_lift"></i>
      </div>
      <div class="more_content" ref="more_reading_content">
        <ul :style="{height: max_length}">
          <div class="more_reading_info" v-for="reading in exhibit.image_text_readings">
            <div class="avatar">
              <img class="avatar_image_background" :src="reading.image_path"/>
            </div>
            <div @click="show_image_text_readings(reading.id)" class="more_reading_content">
              <div class="title">{{reading.reading_title}}</div>
              <div class="description">{{reading.reading_content}}</div>
            </div>
          </div>
          <div class="more_reading_info" v-for="(reading, index) in exhibit.audio_readings">
            <div class="avatar">
              <img class="avatar_image_background" src="/static/exhibition/head1.jpeg"/>
              <img class="avatar_image_play" @click="show_video(index)" :src="reading.play_icon"/>
            </div>
            <div class="reading_video">
              <video :src="reading.video_src" ref="my_video" class="my_video"></video>
            </div>
            <div @click="show_video_readings(reading.id)" class="more_reading_content">
              <div class="title">{{reading.reading_title}}</div>
              <div class="description">{{reading.reading_content}}</div>
            </div>
          </div>
        </ul>
      </div>

    </div>
    </transition>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
  import audio_reading from '../../audio/audio_reading.vue'
  import BScroll from 'better-scroll';

  export default {
    props: {
      exhibit_id:0
    },
    data () {
      return {
        exhibit:{},
        showFlag: false,
        max_length:''
      };
    },
    methods: {
      show() {
        this.showFlag = true;
      },
      hide() {
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
      _initScroll() {
        console.log(this.$refs.reading_content);
        this.exhibitionScroll = new BScroll(this.$refs.more_reading_content, {
          click: true,
        });
      },
      show_image_text_readings(key) {
        window.open("http://10.50.101.66:8080/readings/image_text_readings.html?id=" + key +'&type=exhibit');
      },
      show_video_readings(key) {
        window.open("http://10.50.101.66:8080/readings/video_readings.html?id=" + key +'&type=exhibit');
      },
    },
    created() {
      if(this.exhibit_id != undefined){
        this.$http.get('http://10.50.101.66:8887/exhibit_readings/'+ this.exhibit_id).then(response => {
          this.exhibit = response.body;
          this.max_length = (this.exhibit.image_text_readings.length + this.exhibit.audio_readings.length) *100 - screen.height
          this.max_length = this.max_length.toString() + 'px';
          this.$nextTick(() => {
            this._initScroll();
          });
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
    .more_content
      width: 100%
      overflow: hidden
      position: absolute
      top: 50px
      bottom: 0px
      height: 600px
      .more_reading_info
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
</style>
