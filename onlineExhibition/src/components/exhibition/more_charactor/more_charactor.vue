<template>
  <transition name="move">
    <div v-show="showFlag" class="more_charactor">
      <div class="top">
         人物作品
      </div>
      <div class="back" @click="hide">
        <i class="icon-arrow_lift"></i>
      </div>
      <div class="more_charactor_content" ref="more_content">
        <ul :style="{height: max_length}" style="display: flex">
          <div class="left_product">
            <div v-for="charactor in exhibition.charactors" class="exhibit_block">
              <img @click="show_exhibit(charactor.id)" width="100%"  v-bind:src="charactor.image_path">
              <div class="exhibit_name">
                {{charactor.name}}
              </div>
              <div class="exhibit_author">
                {{charactor.author}}
              </div>
            </div>
          </div>
          <div class="right_product">
            <div v-for="charactor in exhibition.charactors" class="exhibit_block">
              <img @click="show_exhibit(charactor.id)" width="100%" v-bind:src="charactor.image_path">
              <div class="exhibit_name">
                {{charactor.name}}
              </div>
              <div class="exhibit_author">
                {{charactor.author}}
              </div>
            </div>
          </div>
        </ul>
      </div>

    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../../common/js/util';
  import BScroll from 'better-scroll';

  export default {
    props: {
      exhibition_id:0
    },
    data () {
      return {
        exhibitions:[],
        exhibition:{},
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
      show_exhibit (key) {
        window.open("http://10.50.101.66:8080/production/production.html?id=" + key);
      },
      _initScroll() {
        this.exhibitionScroll = new BScroll(this.$refs.more_content, {
          click: true,
        });
      }
    },
    created() {
      if(this.exhibition_id != undefined){
        this.$http.get('http://10.50.101.66:8887/exhibition_readings/'+ this.exhibition_id).then(response => {
          this.exhibition = response.body;
          this.max_length = (this.exhibition.image_text_readings.length + this.exhibition.audio_readings.length) *100 - screen.height
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

  .more_charactor
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
    .more_charactor_content
      width: 100%
      overflow: hidden
      position: absolute
      top: 50px
      bottom: 0px
      height: 600px
      display: flex
      margin-top: 5px
      .left_product
        margin-left: 5px
        margin-right: 5px
        flex: 1
        width:50%
        .exhibit_block
          margin-top:2px
          border-color: antiquewhite
          border-style: solid
          border-radius: 5px
          background-color: antiquewhite
      .right_product
        margin-left: 5px
        margin-right: 5px
        flex: 1
        width:50%
        .exhibit_block
          margin-top:2px
          border-color: antiquewhite
          border-style: solid
          border-radius: 5px
          background-color: antiquewhite

</style>
