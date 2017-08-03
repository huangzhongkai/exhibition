<template>
  <transition name="move">
  <div v-show="showFlag" class="edit_ratings" >
    <div class="top">
      <span>【朝奉图】</span>
    </div>
    <div class="back" @click="hide">
      <i class="icon-arrow_lift"></i>
    </div>
    <div class="content" ref="content">
      <ul :style="max_length">
        <div v-show="type">
          <img id="img" :src="rating_image" ref="rating_image">
          <!--<div>-->
            <!--<img @click="show_rating()" class="flag" src="/static/exhibit/rating.png"/>-->
          <!--</div>-->
        </div>
        <div>
          <textarea @click="ratings_input()" v-model="ratings" ref="ratings" class="ratings_input" placeholder="留言将由作者删选显示"/>
        </div>
        <div class="commit">
          <div  @click="upload()"  class="btn btn-primary">提交</div>
        </div>
      </ul>
    </div>
  </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import BScroll from 'better-scroll';
  import Cropper from 'cropperjs'

  let host = 'qb4dwjh.hk1.mofasuidao.cn';

  export default {
    props: {
      exhibit_id:0
    },
    data () {
      return {
        img_length:'',
        cropper: {},
        flag:false,
        rating_image:'',
        edit_rating_length:'',
        max_length:'',
        type: false,
        ratings:'',
        showFlag: false,
      }
    },
    created () {
      this.$http.get('http://'+ host +'/exhibits/'+ this.exhibit_id + '/').then(response => {
        this.rating_image = response.body['image_path'];
        var img = new Image();
        let _this = this;
        img.src = this.rating_image;
        img.onload = function() {
          _this.img_length = img.height/(img.width/screen.width);
          _this.max_length = img.height/(img.width/screen.width) + 350 - screen.height
          _this.max_length = 'height:'+ _this.max_length.toString() + 'px';
          _this.$nextTick(() => {
            _this.rating_initScroll();
          });
        }
//        this.edit_rating_length = 500 + 200;
//        this.edit_rating_length = this.edit_rating_length.toString().split('.')[0] + 'px';

      },response => {
      });

    },
    methods: {
      convertBase64UrlToBlob(urlData){
        var bytes=window.atob(urlData.split(',')[1]);        //去掉url的头，并转换为byte
        //处理异常,将ascii码小于0的转换为大于0
        var ab = new ArrayBuffer(bytes.length);
        var ia = new Uint8Array(ab);
        for (var i = 0; i < bytes.length; i++) {
          ia[i] = bytes.charCodeAt(i);
        }
        return new Blob( [ab] , {type : 'image/png'});
      },
      upload(){
        this.showFlag = false;
        let rating = {};
        rating['rateTime'] = Date.parse(new Date())/1000;
        rating['text'] = this.ratings;
        if(this.type === true){
          var croppedCanvas;
          croppedCanvas = this.cropper.getCroppedCanvas({
          });
          this.result = croppedCanvas.toDataURL();
          let _this = this;

          var formData = new FormData();
          formData.append('imageblob',this.convertBase64UrlToBlob(croppedCanvas.toDataURL()));
          formData.append('text',rating['text']);
          this.$http.post('http://'+ host +'/exhibit_ratings/'+ this.exhibit_id+'/?type=1',formData ).then(response => {
            if(response.body === 'error'){
              window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//qb4dwjh.hk1.mofasuidao.cn/artist_html/%3Fartist%3D0&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
            }else{
              document.body.style.height = '';
              document.body.style.overflow = '';
              window.location.reload();
            }
          },response => {
            alert('request error');
          });

//          this.cropper.getCroppedCanvas().toBlob(function (blob) {
//            alert('aaa');
//            var formData = new FormData();
//            formData.append('imageblob',blob);
//            formData.append('text',rating['text']);
//            alert('bbb');
//
//            _this.$http.post('http://'+ host +'/exhibit_ratings/'+ _this.exhibit_id+'/?type=1',formData ).then(response => {
//              _this.showFlag = false;
//              document.body.style.height = '';
//              document.body.style.overflow = '';
//              window.location.reload();
//            },response => {
//            });
//          });
        }else{
          this.$http.post('http://'+ host +'/exhibit_ratings/'+ this.exhibit_id+'/?type=0',rating, {emulateJSON:true} ).then(response => {
            this.showFlag = false;
            document.body.style.height = '';
            document.body.style.overflow = '';
            window.location.reload();
          },response => {
          });
        }
      },
//      show_rating () {
//        this.flag = !this.flag;
//        if(this.flag === true){
//          var image = document.getElementById('img');
//          this.cropper = new Cropper(image, {
//            aspectRatio: 1 / 1,
//            autoCropArea:0.5,
//            dragMode: 'none',
//            zoomable:false,
//            crop: function(e) {
//
//            },
//            ready: function () {
//            }
//          });
//        }else{
//          this.cropper.destroy();
//        }
//
//      },
      show(type) {
        if(type === 1){
          this.type = true;

          var image = document.getElementById('img');
          this.cropper = new Cropper(image, {
            aspectRatio: 1 / 1,
            autoCropArea:0.5,
            dragMode: 'none',
            zoomable:false,
            crop: function(e) {

            },
            ready: function () {
            }
          });

        }else if(type === 0){
          this.type = false;
        }
        this.showFlag = true;
      },
      hide() {
        this.showFlag = false;
        document.body.style.height = '';
        document.body.style.overflow = '';
      },
      rating_initScroll() {
        this.ratingScroll = new BScroll(this.$refs.content, {
          click: true,
        });
      },
      ratings_input() {
        this.max_length = 'height:' + (this.img_length + screen.height).toString() + 'px';
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .edit_ratings
    position: fixed
    left: 0
    top: 0
    z-index: 30
    width: 100%
    height : 100%
    background: #fff
    overflow: hidden
    transform: translate3d(0, 0, 0)
    &.move-enter-active, &.move-leave-active
      transition: all 0.2s linear
    &.move-enter, &.move-leave-active
      transform: translate3d(100%, 0, 0)
    .top
      text-align: center
      font-size: 15px
      padding: 10px 0 10px 0
    .back
      position: absolute
      top: 0px
      left: 0px
      .icon-arrow_lift
        display: block
        padding: 10px
        font-size: 20px
        color: black
    .content
      width: 100%
      overflow: hidden
      top: 50px
      bottom: 0px
      height :100%
      img
        max-width: 100%
      .flag
        position: absolute
        top: 0
        right: 0
        width: 32px
        height: 32px
        line-height: 12px
        font-size: 10px
        color: rgb(147, 153, 159)
      .ratings_input
        width: 100%
        height: 150px
        border-color: darkgrey
        border-top: 2px
        border-bottom: 2px
        border-style: solid
        background-color: antiquewhite
        padding-top: 10px
        line-height: 20px
        overflow: auto
      .commit
        text-align: center
        vertical-align: middle
        margin-top: 10px
</style>
