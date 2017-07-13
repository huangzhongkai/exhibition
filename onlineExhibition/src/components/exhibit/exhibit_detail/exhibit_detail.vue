<template>
  <div>
    <div class="production_detail">
      <div class="top_image" :style="{height: isEnlarge? 'auto' : '150px'}">
        <img width="100%" :src="exhibit.image_path">
      </div>
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
      <audio_reading class='audio_reading' :name="exhibit.audio_name" ref="audio_reading"></audio_reading>
      <audio :src="exhibit.audio_src" ref="audio"></audio>

      <div class="reading_top">
        <span class="left">作品解读</span>
        <span class="right" @click="more_reading()">查看更多</span>
      </div>
      <div class="reading_info" v-if="isShow(index)" v-for="(reading, index) in exhibit.image_text_readings">
        <div class="avatar">
          <img :src="reading.image_path"/>
        </div>
        <div @click="show_image_text_readings(reading.id)" class="reading_content">
          <div class="title">{{reading.reading_title}}</div>
          <div class="description">{{reading.reading_content}}</div>
        </div>
      </div>
      <div class="reading_info" v-if="isShow(index)" v-for="(reading, index) in exhibit.audio_readings">
        <div class="avatar">
          <img @click="show_video(index)" :src="reading.play_icon"/>
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
      <span class="right" @click="add_rating()">写评论</span>
    </div>
    <div class="rating-wrapper">
      <ul>
        <li v-for="rating in exhibit.ratings" class="rating-item">
          <div class="avatar">
            <img width="28" height="28" :src="rating.avatar">
          </div>
          <div class="content">
            <h1 class="name">{{rating.username}}</h1>
            <p class="text">{{rating.text}}</p>
            <div class="time">
              {{rating.rateTime}}
            </div>
          </div>
        </li>
      </ul>
    </div>

    <more_reading :exhibit_id="param.id" ref="more_reading">
    </more_reading>

    <ratings :exhibition_id="param.id" ref="edit_ratings">
    </ratings>
  </div>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
  import audio_reading from '../../audio/audio_reading.vue'
  import more_reading from '../more_reading/more_reading.vue'
  import {formatDate} from '../../../common/js/date';
  import ratings from '../ratings/ratings.vue'

  export default {
    components: {
      audio_reading,
      more_reading,
      ratings
    },
    data () {
      return {
        exhibit:{},
        isEnlarge: false,
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
      this.$http.get('http://10.50.101.66:8887/exhibits/'+ this.param.id +'/').then(response => {

        this.exhibit = response.body;
      },response => {
      });

    },
    mounted() {
      this.$store.commit('findDOM', {name: 'audio', dom: this.$refs.audio});
      this.$refs.audio.addEventListener('ended', () => {
        this.$store.state.isPlaying = false;
      });
      this.$refs.audio.addEventListener('error', () => { console.log(' play error') });
    },
    computed: {
      audio() {
        return this.$store.state.audio;
      },
    },
    methods: {
      show_video (index) {
        this.$refs.my_video[index].play();
        if(this.$store.state.isPlaying === true){
          this.$refs.audio_reading.play();
        }
      },
      enlarge_image (bool) {
        this.isEnlarge = !bool;
      },
      more_reading () {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.more_reading.show();
      },
      show_image_text_readings(key) {
        window.open("http://10.50.101.66:8080/readings/image_text_readings.html?id=" + key +'&type=exhibit');
      },
      show_video_readings(key) {
        window.open("http://10.50.101.66:8080/readings/video_readings.html?id=" + key +'&type=exhibit');
      },
      add_rating () {
//        window.open("http://10.50.101.66:8080/ratings/ratings.html");
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.edit_ratings.show();
      },
      isShow (index) {
        if(index <=1){
          return true;
        }else{
          return false;
        }
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
      background-color: #7e8c8d
      .reading_video
        top: 0
        left: 0
        position: absolute
        margin: 5px 5px 5px 5px
        vertical-align: top
        display: inline-block
        width: 64px
        height: 64px
        z-index: 1
        .my_video
          border-radius: 5px
          display: inline-block
          width: 100%
          height: 100%
      .avatar
        z-index: 2
        position: relative
        margin: 5px 5px 5px 5px
        vertical-align: top
        display: inline-block
        img
          border-radius: 5px
          width: 64px
          height: 64px
          background: url(/static/exhibit/bamboo.jpeg) no-repeat;
          background-size: 64px 64px;
      .reading_content
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
          margin-bottom: 8px
          line-height: 18px
          color: rgb(7, 17, 27)
          font-size: 12px
        .time
          position: absolute
          top: 0
          right: 0
          line-height: 12px
          font-size: 10px
          color: rgb(147, 153, 159)
</style>

