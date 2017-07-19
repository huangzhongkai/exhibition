<template>
  <transition name="move">
    <div v-show="showFlag" class="more_enjoyable">
      <div class="top">
        写意作品
      </div>
      <div class="back" @click="hide">
        <i class="icon-arrow_lift"></i>
      </div>
      <div class="more_enjoyable_content" ref="more_content">
        <ul :style="{height: max_length}" style="display: flex">
          <div class="left_product">
            <div v-for="enjoyable in exhibits" class="exhibit_block">
              <img @click="show_exhibit(enjoyable.id)" width="100%"  v-bind:src="enjoyable.image_path">
              <div class="exhibit_name">
                {{enjoyable.name}}
              </div>
              <div class="exhibit_author">
                {{enjoyable.author}}
              </div>
            </div>
          </div>
          <div class="right_product">
            <div v-for="enjoyable in exhibits_right" class="exhibit_block">
              <img @click="show_exhibit(enjoyable.id)" width="100%" v-bind:src="enjoyable.image_path">
              <div class="exhibit_name">
                {{enjoyable.name}}
              </div>
              <div class="exhibit_author">
                {{enjoyable.author}}
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
        exhibit:{},
        exhibits:[],
        exhibits_right:[],
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
        window.open("http://10.50.101.66:8080/exhibit/exhibit.html?id=" + key);
      },
      _initScroll() {
        this.exhibitionScroll = new BScroll(this.$refs.more_content, {
          click: true,
        });
      }
    },
    created() {
      if(this.exhibition_id != undefined){
        this.$http.get('http://10.50.101.66:8887/exhibits/?exhibition='+ this.exhibition_id +'&type=enjoyable').then(response => {
          this.exhibits = [];
          this.exhibits_right = [];
          if(response.body.length%2 === 0){
            for(let i=0;i<response.body.length/2;i++){
              this.exhibits[i]=response.body[i];
              this.exhibits_right[i]=response.body[i+response.body.length/2];
            }
          }else{
            let l = response.body.length -1;
            for(let i=0;i<l/2;i++){
              this.exhibits[i]=response.body[i];
              this.exhibits_right[i]=response.body[i+l/2];
            }
            this.exhibits_right[l/2] = response.body[response.body.length -1];
          }

          this.exhibit = response.body;
          this.max_length = (this.exhibit.length + this.exhibit.length) *100 - screen.height
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

  .more_enjoyable
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
    .more_enjoyable_content
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
