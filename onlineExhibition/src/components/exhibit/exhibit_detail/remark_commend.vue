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
          <div class="tab-item">
          <span>
            <i class="fa fa-commenting-o fa-1x" aria-hidden="true"></i>
            <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
            <span @click="add_rating()" style="margin-left: 1px">评论</span>
          </span>
          </div>
        </div>
      </div>
      <div class="remark" ref="content">
        <div>
          <div :class="is_select">
            <!--<div class="top">-->
              <!--可圈可点-->
            <!--</div>-->
            <!--<div class="back" @click="hide">-->
              <!--<i class="icon-arrow_lift"></i>-->
            <!--</div>-->
          </div>

          <div class="content_show" >
              <div class="top_image">
                <img class="image" width="100%" height="100%" :src="reading.image_path">

                <div id="search" class="search">
                  <i class="fa fa-search fa-3x" aria-hidden="true"></i>
                  <div id="moveid" class="div" :style="{'left':show_left, 'top': show_top}">
                    <img :src="reading.image_path" :style="{'margin-left':margin_left, 'margin-top': margin_top}"/>
                  </div>
                </div>
                <!--<i id="rating" class="rating fa fa-commenting-o fa-3x" aria-hidden="true" data-toggle="modal" data-target="#myModal"></i>-->
              </div>
          </div>
          <div style="height: 53px"></div>
          <div class="alert_"></div>
        </div>
      </div>

      <ratings :exhibit_id="params.id" ref="edit_ratings">
      </ratings>
    </div>
  </transition>
</template>

<script>
  import {urlParse} from '../../../common/js/util';
  import wx from 'weixin-js-sdk'
  import BScroll from 'better-scroll';
  import global_ from '../../Global.vue'
  import 'font-awesome-webpack'
  import ratings from '../ratings/ratings.vue'

  let host = global_.host;

  export default {
    components: {
      ratings,
    },
    props: {
      exhibit_id:0
    },
    data () {
      return {
        show_left:'38px',
        show_top:'5px',
        title:'',
        img_origin_width:'',
        img_origin_height:'',
        margin_left:'',
        margin_top:'',
        is_scroll:'',
        is_select:'show',
        is_click:'content_show',
        showFlag: false,
        config:{},
        readings:[],
        reading:{},
        params: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })(),
        },
      }
    },
    methods: {
      add_rating () {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        let left = this.margin_left;
        let top = this.margin_top;
        let remark = {'left': left, 'top': top};
        this.$refs.edit_ratings.show_remark(remark);
      },
      utf16ToUtf8(str){
        let patt=/[\ud800-\udbff][\udc00-\udfff]/g; // 检测utf16字符正则
        return str.replace(patt,'');
      },
//      enlarge(){
//        if( this.is_select === 'show'){
////          this.is_select = 'hidden';
//          this.is_click  = 'content_show'
//          $("#rating").css("display", "block")
//        }else{
//          this.is_select = 'show'
//          this.is_click  = 'content_hidden'
//          $("#rating").css("display", "none")
//        }
//
//      },
      show() {
        this.title = $('title').html();
        $('title').html('可圈可点');
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
      _initScroll() {
        this.scroll = new BScroll(this.$refs.content, {
          click: true,
        });
      },
    },
    created() {
      this.$http.get('http://'+ host +'/exhibit/?id='+ this.exhibit_id).then(response => {
        this.reading = response.body;
        let img = new Image();
        let _this = this;
        img.src = this.reading.image_path;
        img.onload = function() {
          _this.img_origin_width = img.width;
          _this.img_origin_height = img.height;
          _this.img_length = img.height/(img.width/screen.width);

          _this.$nextTick(() =>{
            let _x_start,_y_start,_x_move,_y_move,_x_end,_y_end,left_start,top_start;
            document.getElementById("search").addEventListener("touchstart",function(e)
            {
              $("body").on("touchmove",function(event){
                event.preventDefault;
              }, false)
//              $("#rating").css("display", "none");
              _x_start=e.touches[0].pageX;
              _y_start=e.touches[0].pageY;
              left_start=$("#search").css("left");
              top_start=$("#search").css("top");
              console.log( _x_start, left_start);
            })
            document.getElementById("search").addEventListener("touchmove",function(e)
            {
              _x_move=e.touches[0].pageX;
              _y_move=e.touches[0].pageY;
              // console.log("move",_x_move)
              if((parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start) >=-1 &&
                parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start) <=((screen.width/_this.img_origin_width * _this.img_origin_height )-35))){
                $("#search").css("top",parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start)+"px");
                _this.margin_top = (parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start))/(screen.width/_this.img_origin_width);
                if(_this.margin_top > _this.img_origin_height -128){
                  _this.margin_top = _this.img_origin_height -128;
                }
                _this.margin_top = '-' + _this.margin_top.toString() + 'px';

              }
              if((parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start) >=-5 &&
                parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start) <=(screen.width) - 35)){
                $("#search").css("left",parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start)+"px");
                _this.margin_left = (parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start))/screen.width * _this.img_origin_width;
                if(_this.margin_left > _this.img_origin_width -128){
                  _this.margin_left = _this.img_origin_width -128;
                }
                _this.margin_left = '-' + _this.margin_left.toString() + 'px';
              }

              if(parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start) <= screen.width - 148){
                _this.show_left = '38px';
              }
              if(parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start) >= screen.width - 148){
                _this.show_left = '-128px';
              }
              if(parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start) >= screen.height - 208){
                _this.show_top = '-128px'
              }
              if(parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start) <= screen.height - 208){
                _this.show_top = '5px'
              }
            })
            document.getElementById("search").addEventListener("touchend",function(e)
            {
              let _x_end=e.changedTouches[0].pageX;
              let _y_end=e.changedTouches[0].pageY;
//              $("#rating").css("display", "block");
              $("body").off("touchmove");
            })
          })
        }
      },response => {
      });

//     let _this = this;
//      $("#send").click(function(){
//        let content = _this.utf16ToUtf8($("#content")[0].value);
//        let left = _this.margin_left;
//        let top = _this.margin_top;
//        if(left == '' || top == ''){
//          $('.alert').html('请拖动放大图标选择放大区域').addClass('alert-warning').show().delay(2000).fadeOut();
//        }else{
//          let remark = {'content':content,'left': left, 'top': top};
//          _this.$http.post('http://'+ host +'/exhibit_remark/'+ _this.exhibit_id+'/',remark, {emulateJSON:true} ).then(response => {
//            if(response.body === 'error'){
//              window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ encodeURIComponent(host) +'/home_html/&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
//            }else{
//              $("#myModal").modal('hide');
//              $('.alert_').html('评论成功').addClass('alert-warning').show().delay(2000).fadeOut(function () {
//                window.location.reload();
//              });
//            }
//          },response => {
//            $("#myModal").modal('hide');
//          });
//        }
//      });

    }
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../../common/stylus/mixin.styl";
  .remark
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
      transform: translate3d(0, 0, 100%)
    .show
      display: block
      .top
        position: relative
        border-1px(rgba(7, 17, 27, 0.1))
        line-height: 42px
        height: 42px
        text-align: center
      .back
        position: absolute
        top: 0px
        left: 0px
        .icon-arrow_lift
          display: block
          line-height: 42px
          font-size: 20px
          color: black
    .hidden
      display: none
      .top
        position: relative
        border-1px(rgba(7, 17, 27, 0.1))
        line-height: 42px
        height: 42px
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
    .content_hidden
      width: 100%
      overflow: hidden
      bottom: 0
      .div
        display: none
      .search
        margin-left: -10px
        margin-top: -10px
        display: none
      .rating
        display: none
    .content_show
      width: 100%
      overflow: hidden
      bottom: 0
      .search
        position: absolute
        top: 20px
        left: 20px
        z-index: 30
        .div
          position: absolute
          width: 128px
          height: 128px
          z-index: 30
          border-color: aliceblue
          border: 1px
          border-style: solid
          border-radius: 5px
          overflow: hidden
      .rating
        position: absolute
        height: 40px
        z-index: 20
        top: 0px
        right: 0px
    .alert_
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

