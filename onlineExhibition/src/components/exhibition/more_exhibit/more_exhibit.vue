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
      <div  class="more_charactor" ref="more_content">
        <div class="production-content">
          <!--<div class="top">-->
             <!--{{title}}-->
          <!--</div>-->
          <!--<div class="back" @click="hide">-->
            <!--<i class="icon-arrow_lift"></i>-->
          <!--</div>-->
          <div class="more_charactor_content" >
              <div class="flex-show">
                <div class="left_product">
                  <div v-for="charactor in exhibits" class="exhibit_block">
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
                  <div v-for="charactor in exhibits_right" class="exhibit_block">
                    <img @click="show_exhibit(charactor.id)" width="100%" v-bind:src="charactor.image_path">
                    <div class="exhibit_name">
                      {{charactor.name}}
                    </div>
                    <div class="exhibit_author">
                      {{charactor.author}}
                    </div>
                  </div>
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
  import BScroll from 'better-scroll';

  import global_ from '../../Global.vue'

  let host = global_.host;

  export default {
    props: {
      exhibition_id:0,
      type:''
    },
    data () {
      return {
        title_bak:'',
        title:'',
        exhibits:[],
        exhibits_right:[],
        showFlag: false,
      };
    },
    methods: {
      show() {
        this.title_bak = $('title').html();
        $('title').html(this.title);
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
        $('title').html(this.title_bak);
        this.showFlag = false;
        document.body.style.height = '';
        document.body.style.overflow = '';
      },
      show_exhibit (key) {
        window.open("http://"+ host +"/exhibit_html/?id=" + key);
      },
      _initScroll() {
        this.scroll = new BScroll(this.$refs.more_content, {
          click: true,
        });
      }
    },
    created() {
      if(this.type === 'all'){
        this.title = '作品推荐';
      }else if(this.type === 'charactor'){
        this.title = '人物作品'
      }else if(this.type === 'enjoyable'){
        this.title = '写意作品'
      }
      if(this.exhibition_id != undefined){
        this.$http.get('http://'+ host +'/exhibits/?exhibition='+ this.exhibition_id + '&type=' + this.type).then(response => {
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
            this.exhibits[l/2] = response.body[response.body.length -1];
          }
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
        line-height: 40px
        font-size: 20px
        color: black
    .production-content
      overflow: hidden
      .more_charactor_content
        width: 100%
        overflow: hidden
        margin-top: 5px
        .flex-show
          display: flex
          .left_product
            margin-left: 5px
            margin-right: 5px
            flex: 1
            width:50%
            .exhibit_block
              border-color: darkgrey
              border-style: solid
              border-radius: 5px
              border-width:1px
              background-color: white
              margin-top:2px
          .right_product
            margin-left: 5px
            margin-right: 5px
            flex: 1
            width:50%
            .exhibit_block
              margin-top:2px
              border-color: darkgrey
              border-style: solid
              border-radius: 5px
              border-width:1px
              background-color: white
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
