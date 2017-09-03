<template>
  <transition name="move">
    <div v-show="showFlag" class="remark">
      <div :class="is_select">
        <div class="top">
          可圈可点
        </div>
        <div class="back" @click="hide">
          <i class="icon-arrow_lift"></i>
        </div>
      </div>

      <div :class="is_click" ref="content">
        <ul :style="{height: max_length}">
          <div class="top_image">
            <img class="image" @click="enlarge()" width="100%" height="100%" :src="reading.image_path">
            <div id="moveid" class="div">
              <img :src="reading.image_path" :style="{'margin-left':margin_left, 'margin-top': margin_top}"/>
            </div>
            <div id="search" class="search">
              <i class="fa fa-search fa-3x" aria-hidden="true"></i>
            </div>
            <i id="rating" class="rating fa fa-commenting-o fa-3x" aria-hidden="true" data-toggle="modal" data-target="#myModal"></i>
          </div>
        </ul>
      </div>

      <div class="alert"></div>
    </div>
  </transition>
</template>

<script>
  import {urlParse} from '../../../common/js/util';
  import wx from 'weixin-js-sdk'
  import BScroll from 'better-scroll';
  import global_ from '../../Global.vue'
  import 'font-awesome-webpack'

  let host = global_.host;

  export default {
    props: {
      exhibit_id:0
    },
    data () {
      return {
        img_origin_width:'',
        img_origin_height:'',
        margin_left:'',
        margin_top:'',
        max_length:'',
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
      utf16ToUtf8(str){
        let patt=/[\ud800-\udbff][\udc00-\udfff]/g; // 检测utf16字符正则
        return str.replace(patt,'');
      },
      enlarge(){
        if( this.is_select === 'show'){
          this.is_select = 'hidden';
          this.is_click  = 'content_hidden'
        }else{
          this.is_select = 'show'
          this.is_click  = 'content_show'
        }

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
        new BScroll(this.$refs.content, {
          click: true,
        });
      },
    },
    created() {
      this.$http.get('http://'+ host +'/exhibits/'+ this.exhibit_id +'/').then(response => {
        this.reading = response.body;
        let img = new Image();
        let _this = this;
        img.src = this.reading.image_path;
        img.onload = function() {
          _this.img_origin_width = img.width,
          _this.img_origin_height = img.height
          console.log(_this.img_origin_width, _this.img_origin_height);
          _this.img_length = img.height/(img.width/screen.width);
          _this.max_length = img.height/(img.width/screen.width) - screen.height + 65 ;
          _this.max_length = _this.max_length.toString() + 'px';
          _this.$nextTick(() => {
            _this._initScroll();
          });

          _this.$nextTick(() =>{
            let _x_start,_y_start,_x_move,_y_move,_x_end,_y_end,left_start,top_start;
            document.getElementById("search").addEventListener("touchstart",function(e)
            {
              $("#rating").css("display", "none");
              _x_start=e.touches[0].pageX;
              _y_start=e.touches[0].pageY;
              // console.log("start",_x_start)
              left_start=$("#search").css("left");
              top_start=$("#search").css("top");
            })
            document.getElementById("search").addEventListener("touchmove",function(e)
            {
              _x_move=e.touches[0].pageX;
              _y_move=e.touches[0].pageY;
              // console.log("move",_x_move)
              if(parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start) >=0 &&
                parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start) >=0 &&
                parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start) <=(screen.width-40) &&
                parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start) <=((screen.width/_this.img_origin_width * _this.img_origin_height)-40)){
                $("#search").css("left",parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start)+"px");
                $("#search").css("top",parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start)+"px");
                console.log('x=', parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start));
                console.log('y=',parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start));
                _this.margin_left = parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start)/screen.width * _this.img_origin_width;
                if(_this.margin_left > _this.img_origin_width -128){
                  _this.margin_left = _this.img_origin_width -128;
                }
                _this.margin_left = '-' + _this.margin_left.toString() + 'px';
                _this.margin_top = parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start)/(screen.width/_this.img_origin_width);
                if(_this.margin_top > _this.img_origin_height -128){
                  _this.margin_top = _this.img_origin_height -128;
                }
                _this.margin_top = '-' + _this.margin_top.toString() + 'px';

                console.log(_this.margin_left,_this.margin_top);
              }
            })
            document.getElementById("search").addEventListener("touchend",function(e)
            {
              let _x_end=e.changedTouches[0].pageX;
              let _y_end=e.changedTouches[0].pageY;
              $("#rating").css("display", "block");
              // console.log("end",_x_end)
            })
          })
        }
      },response => {
      });
      this.$nextTick(() =>{
        let _x_start,_y_start,_x_move,_y_move,_x_end,_y_end,left_start,top_start;
        document.getElementById("moveid").addEventListener("touchstart",function(e)
        {

          _x_start=e.touches[0].pageX;
          _y_start=e.touches[0].pageY;
          // console.log("start",_x_start)
          left_start=$("#moveid").css("left");
          top_start=$("#moveid").css("top");

        })
        document.getElementById("moveid").addEventListener("touchmove",function(e)
        {
          _x_move=e.touches[0].pageX;
          _y_move=e.touches[0].pageY;
          // console.log("move",_x_move)
          if(parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start) >=0 &&
            parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start) >=0 &&
            parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start) <=(screen.width-128) &&
            parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start) <=(screen.height-128)){
            $("#moveid").css("left",parseFloat(_x_move)-parseFloat(_x_start)+parseFloat(left_start)+"px");
            $("#moveid").css("top",parseFloat(_y_move)-parseFloat(_y_start)+parseFloat(top_start)+"px");
          }
        })
        document.getElementById("moveid").addEventListener("touchend",function(e)
        {
          let _x_end=e.changedTouches[0].pageX;
          let _y_end=e.changedTouches[0].pageY;
          // console.log("end",_x_end)
        })
      })

     let _this = this;
      $("#send").click(function(){
        let content = _this.utf16ToUtf8($("#content")[0].value);
        let left = _this.margin_left;
        let top = _this.margin_top;
        if(left == '' || top == ''){
          $('.alert').html('请拖动放大图标选择放大区域').addClass('alert-warning').show().delay(2000).fadeOut();
        }else{
          let remark = {'content':content,'left': left, 'top': top};
          _this.$http.post('http://'+ host +'/exhibit_remark/'+ _this.exhibit_id+'/',remark, {emulateJSON:true} ).then(response => {
            $("#myModal").modal('hide');
            $('.alert').html('评论成功').addClass('alert-warning').show().delay(2000).fadeOut(function () {
              window.location.reload();
            });

          },response => {
            $("#myModal").modal('hide');
          });
        }
      });

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
    .hidden
      display: none
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
    .content_show
      width: 100%
      overflow: hidden
      position: absolute
      top: 42px
      bottom: 0
      .div
        display: none
      .search
        display: none
    .content_hidden
      width: 100%
      overflow: hidden
      position: absolute
      top: 0
      bottom: 0
      .div
        position: absolute
        top: 64px
        left: 64px
        width: 128px
        height: 128px
        z-index: 30
        border-color: aliceblue
        border: 1px
        border-style: solid
        border-radius: 5px
        overflow: hidden
      .search
        position: absolute
        top: 64px
        left: 64px
        z-index: 30
      .rating
        position: absolute
        z-index: 20
        top: 0px
        left: 0px
    .alert
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

</style>

