<template>
  <transition name="fade">
    <div class="mini-music">
      <!--<div class="music-img">-->
        <!--<img @click="showPlay" ref="img" v-bind:src="audio.musicImgSrc || (musicData[0]&&musicData[0].musicImgSrc) || defaultImg" alt="microzz.com">-->
      <!--</div>-->
      <div class="music-name">
        <div class="music-top">
          <div class="title">{{name}}</div>
          <div class="music-control">
            <i @click="play()" v-bind:class="[isPlaying ? pauseIcon : playIcon]"></i>
          </div>
        </div>

        <div class="progress">

          <div @click="changeTime($event)" @touchmove="touchMove($event)" @touchend="touchEnd($event)" ref="progressBar" class="progress-bar">
            <div class="now" ref="now" :style="{width: (now / nativeAudio.duration).toFixed(3)*100 + '%'}"></div>
          </div>
          <div>
            <span class="start" ref="start">{{transformTime(now)}}</span>
            <span class="end" ref="haha">{{totalTime}}</span>
          </div>

        </div>
      </div>

    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  export default {
    props: {
      name:''
    },
    mounted() {
      this.nativeAudio = document.querySelector('audio');

      this.nativeAudio.addEventListener('canplay', () => {
        this.totalTime = this.transformTime(this.nativeAudio.duration);
        console.log(this.$refs.haha.innerHTML);
        setInterval(() => {
          this.now = this.nativeAudio.currentTime;
        }, 1000);
      });
    },
    updated () {
      if(this.$refs.now.style.width === '100%'){
        this.$refs.now.style.width =0;
      }
      if(this.$refs.start.innerText === this.totalTime){
        this.now = 0;
      }
    },
    computed: {
      isPlaying() {
        return this.$store.state.isPlaying;
      },
      audio() {
        return this.$store.state.audio;
      },
      DOM() {
        return this.$store.state.DOM;
      },

    },
    data() {
      return {
        playIcon: 'play-icon',
        pauseIcon: 'pause-icon',
        now: 0,
        nativeAudio: {},
        totalTime: '00:00',
      }
    },
    methods: {
      play() {
        this.$store.commit('play', !this.isPlaying);
        !this.isPlaying ? this.DOM.audio.pause() : this.DOM.audio.play();
      },
      changeTime(event) {
        let progressBar = this.$refs.progressBar;
        let coordStart = progressBar.getBoundingClientRect().left;
        let coordEnd = event.pageX;
        this.nativeAudio.currentTime = (coordEnd - coordStart) / progressBar.offsetWidth * this.nativeAudio.duration;
        this.now = this.nativeAudio.currentTime;
        this.nativeAudio.play();
        this.$store.commit('play', true);
      },
      touchMove(event) {
        let progressBar = this.$refs.progressBar;
        let coordStart = progressBar.getBoundingClientRect().left;
        let coordEnd = event.touches[0].pageX;
        this.$refs.now.style.width = ((coordEnd - coordStart) / progressBar.offsetWidth).toFixed(3) * 100 + '%';
      },
      touchEnd(event) {
        this.nativeAudio.currentTime = this.$refs.now.style.width.replace('%', '')/100 * this.nativeAudio.duration;
        this.now = this.nativeAudio.currentTime;
        this.nativeAudio.play();
        this.$store.commit('play', true);
      },
      transformTime(seconds) {
        let m, s;
        m = Math.floor(seconds / 60);
        m = m.toString().length == 1 ? ('0' + m) : m;
        s = Math.floor(seconds - 60 * m);
        s = s.toString().length == 1 ? ('0' + s) : s;
        return m + ':' + s;
      },
      reset_progress_bar(){
        this.$refs.now.style.width = 0;
      }

    }
  }

</script>

<style lang="stylus" rel="stylesheet/stylus">
  .mini-music
    margin: 5px 5px 5px 5px
    width: 97%
    height: 120px
    border-color: aliceblue
    border: 2px
    border-style: solid
    border-radius: 5px
    background-color: #7e8c8d
    .music-top
      display: flex
      .title
        padding-left: 10px
        padding-top: 30px
      .music-control
        margin-left:auto
        margin-right:1px
        i
          padding-right: 10px;
          width: 45px;
          height: 45px;
          margin-top: 13px;
          display: inline-block;
          cursor: pointer;
          border-radius: 22px;
        .play-icon
          background: url(./play.svg) no-repeat;
          background-size: contain;
        .pause-icon
          background: url(./pause.svg) no-repeat;
          background-size: contain;

    .progress
      width: 100%;
      top: 10px;
      left: 0;
      span.start
        position: absolute;
        left: 6px;
        // padding-right: 5px;
      span.end
        position: absolute;
        right: 6px;
        // padding-left: 5px;
      .progress-bar
        position: relative;
        margin-left: 5px
        width: 98%;
        height: 5px;
        display: inline-block;
        background-color: rgba(255, 255, 255, .5);
        vertical-align: 2px;
        border-radius: 3px;
        cursor: pointer;
        .now
          position: absolute;
          left: 0;
          display: inline-block;
          max-width: 100%;
          // width: 70%;
          height: 5px;
          background-color: #31c27c;
        .now::after
          content: "";
          position: absolute;
          left: 100%;
          width: 2px;
          height: 6px;
          background-color: white;

</style>
