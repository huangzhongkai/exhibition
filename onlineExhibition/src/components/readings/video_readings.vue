<template>
  <div>
    <video @click="play()" class="video_play"
           :src="reading.video_src"
           ref="video"
           :poster="reading.poster">
    </video>
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
        isPlaying:true,
        introduction:'',
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
    methods:{
      play() {
        this.isPlaying = !this.isPlaying;
        this.isPlaying ? this.$refs.video.play() : this.$refs.video.pause();
      }
    },
    created() {
      if(this.params.type === 'exhibit'){
        this.$http.get('http://'+ host +'/exhibit_vedio_readings/?id='+ this.params.id).then(response => {
          this.reading = response.body;
        },response => {
        });
      }else if(this.params.type === 'exhibition'){
        this.$http.get('http://'+ host +'/exhibition_vedio_readings/?id='+ this.params.id).then(response => {
          this.reading = response.body;
        },response => {
        });
      };
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .video_play
    playsinlin:true
    display: inline-block
    width: 100%
    height: 200px
  .reading
    position: relative
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
