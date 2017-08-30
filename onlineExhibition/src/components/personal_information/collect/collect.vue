<template>
  <transition name="move">
    <div v-show="showFlag" class="collect">
      <div class="top">
        收藏
      </div>
      <div class="back" @click="hide">
        <i class="icon-arrow_lift"></i>
      </div>
      <div class="collect_content" ref="content">
        <ul :style="{height: max_length}">

          <div class='h' :ref="exhibit.flag" v-for="(exhibit,index) in exhibits" v-if="exhibit !==null">
            <ul :style="{width: scroll_width}">
              <div  class="collect_info" :style="{width: max_width}">
                <div @click.once="show_exhibit(exhibit.id)" class="avatar">
                  <img class="avatar_image_background" :src="exhibit.image_path"/>
                </div>
                <div @click.once="show_exhibit(exhibit.id)" class="content">
                  <div class="title">作品:{{exhibit.name}}</div>
                  <div class="description">作者:{{exhibit.author}}</div>
                </div>
                <div class="delete">
                  <i @click.once="delete_collect(index,exhibit.id, 0)" class=" text fa fa-trash fa-2x" aria-hidden="true"></i>
                  <!--<span @click.once="delete_collect(index,exhibit.id, 0)" class="text">删除</span>-->
                </div>
              </div>
            </ul>
          </div>

          <div class='h' :ref="exhibition.flag" v-for="(exhibition,index) in exhibitions" v-if="exhibition !==null">
            <ul class="a" :style="{width: scroll_width}">
              <div  class="collect_info" :style="{width: max_width}">
                <div @click.once="show_exhibit(exhibition.id)" class="avatar">
                  <img class="avatar_image_background" :src="exhibition.image_path"/>
                </div>
                <div @click.once="show_exhibit(exhibition.id)" class="content">
                  <div class="title">展览:{{exhibition.name}}</div>
                  <div class="description">展策人:{{exhibition.exhibition_curator}}</div>
                  <!--<div class="description">展览时间:{{exhibition.exhibition_date}}</div>-->
                  <!--<div class="description">展览地点:{{exhibition.exhibition_site}}</div>-->
                </div>
                <div class="delete">
                  <i @click.once="delete_collect(index,exhibition.id, 1)" class=" text fa fa-trash fa-2x" aria-hidden="true"></i>
                  <!--<span @click.once="delete_collect(index,exhibition.id, 1)" class="text">删除</span>-->
                </div>
              </div>

            </ul>
          </div>

          <!--<div class="exhibition" :ref="exhibition.flag" v-for="exhibition in exhibitions">-->
            <!--&lt;!&ndash;<ul style="height: 1000px;">&ndash;&gt;-->
            <!--<li @click="show_exhibition(exhibition.id)"  class="my_exhibition" :style="{width: max_width}">-->
              <!--<div @click="show_exhibition(exhibition.id)" class="top_image">-->
                <!--<img width="100%" height="200px" :src="exhibition.image_path">-->
              <!--</div>-->
              <!--<div @click="show_exhibition(exhibition.id)" class="exhibition_info">-->
                <!--<div class="info_left">-->
                  <!--<div>-->
                    <!--{{exhibition.name}}-->
                  <!--</div>-->
                  <!--<div>-->
                    <!--展览时间： {{exhibition.exhibition_date}}-->
                  <!--</div>-->
                  <!--<div>-->
                    <!--展览地点： {{exhibition.exhibition_site}}-->
                  <!--</div>-->
                <!--</div>-->
                <!--<div class="info_right">-->
                  <!--<div>-->
                    <!--展策人: {{exhibition.exhibition_curator}}-->
                  <!--</div>-->
                <!--</div>-->
              <!--</div>-->
              <!--<div class="delete">-->
                <!--<span @click.once="delete_collect()" class="text">删除</span>-->
              <!--</div>-->
            <!--</li>-->
          <!--</div>-->
        </ul>
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
    data () {
      return {
        user_id:'',
        showFlag: false,
        max_length:'',
        max_width:'',
        scroll_width:'',
        exhibits:[],
        exhibitions:[],
        param: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })()
        },
      };
    },
    methods: {
      delete_collect:function(index,id,type){
        if(type === 0){
          this.exhibits.splice(index,1,null);
        }else{
          this.exhibitions.splice(index,1,null);
        }
        this.$http.delete('http://' + host + '/collect/' + id + '/'+ "?type=" + type).then(response => {
//          if(response.body === 'error'){
//            window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ encodeURIComponent(host) +'/artist_html/%3Fartist%3D0&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
//          }
        }, response => {
        });
      },
      show_exhibition (key) {
        window.open("http://"+ host +"/exhibition_html/?id=" + key);
      },
      show_exhibit (key) {
        window.open("http://"+ host +"/exhibit_html/?id=" + key);
      },
      show() {
        this.showFlag = true;
      },
      hide() {
        this.showFlag = false;
        document.body.style.height = '';
        document.body.style.overflow = '';
      },
      _initScroll() {
        this.exhibitionScroll = new BScroll(this.$refs.content, {
          click: true,
        });
        for(let i=0; i<this.exhibits.length; i++){
          let flag = 'flag'+ this.exhibits[i].id.toString();
          new BScroll(this.$refs[flag][0], {
            scrollX:true,
            click: true,
          });
        };
        for(let i=0; i<this.exhibitions.length; i++){
          let flag = '_flag'+ this.exhibitions[i].id.toString();
          new BScroll(this.$refs[flag][0], {
            scrollX:true,
            click: true,
          });
        }
      },
    },
    created() {
      if(this.param.id != undefined){
        this.$http.get('http://'+ host +'/collect/'+ this.param.id + '/').then(response => {
          this.exhibits = response.body.exhibits;
          this.exhibitions = response.body.exhibitions;
          this.max_length = (this.exhibits.length + this.exhibitions.length) *120 - screen.height
          this.max_length = this.max_length.toString() + 'px';
          this.$nextTick(() => {
            this._initScroll();
          });
        },response => {
        });
      };

      this.max_width = screen.width + 64;
      this.scroll_width = 64;
      this.max_width = this.max_width.toString() + 'px';
      this.scroll_width = this.scroll_width.toString() + 'px';
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../../common/stylus/mixin.styl";

  .collect
    position: absolute
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
    .collect_content
      width:100%
      position: absolute
      top: 50px
      bottom: 0px
      height: 600px
      .h
        height: 80px
        margin: 5px 0px 5px 5px
        .collect_info
          position: relative
          height: 80px
          border: 1px
          border-style: solid
          border-right: transparent
          border-radius: 5px 0 0 5px
          background-color: white
          .avatar
            position: absolute
            top: 0px
            left: 4px
            margin: 5px 5px 5px 5px
            vertical-align: top
            display: inline-block
            width: 64px
            height: 64px
            .avatar_image_background
              border-radius: 5px
              width: 64px
              height: 64px
          .content
            position: absolute
            top: 0px
            left: 64px
            margin: 5px 5px 5px 5px
            margin-left: 8px
            .title
              margin: 2px 0 2px 2px
              color: darkgrey
              line-height: 20px
            .description
              margin: 2px 0 2px 2px
              height :40px
              margin-top: 20px
              font-size: 14px
              color: darkgrey
              line-height: 20px
              overflow: hidden
              text-overflow: ellipsis
          .delete
            position: absolute
            right: 0
            display: inline-block
            border-color: darkgrey
            border: 1px
            border-style: solid
            border-left: transparent
            border-top: transparent
            border-bottom: transparent
            text-align: center
            width: 64px
            height: 80px
            .text
              font-size: 24px
              line-height: 80px


</style>

