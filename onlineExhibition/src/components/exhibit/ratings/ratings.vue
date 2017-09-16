<template>
  <transition name="move">
  <div v-show="showFlag" class="edit_ratings" >
    <div class="top">
      <span>{{title}}</span>
    </div>
    <div class="back" @click="hide">
      <i class="icon-arrow_lift"></i>
    </div>
    <button class="send btn btn-default" @click="upload()">发布</button>
    <div class="content" ref="content">
      <div>
        <textarea autofocus="autofocus" v-model="ratings" ref="ratings" class="ratings_input" placeholder="写评论..."/>
      </div>
    </div>
  </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import BScroll from 'better-scroll';
  import Cropper from 'cropperjs'

  import global_ from '../../Global.vue'

  let host = global_.host;

  export default {
    props: {
      exhibit_id:0
    },
    data () {
      return {
        parent_id:-1,
        title:'发评论',
        img_length:'',
        cropper: {},
        flag:false,
        rating_image:'',
        edit_rating_length:'',
        type: false,
        ratings:'',
        showFlag: false,
      }
    },
    created () {
    },
    methods: {
      utf16ToUtf8(str){
        let patt=/[\ud800-\udbff][\udc00-\udfff]/g; // 检测utf16字符正则
        return str.replace(patt,''
//          function(char){
//          let H, L, code;
//          if (char.length===2) {
//            H = char.charCodeAt(0); // 取出高位
//            L = char.charCodeAt(1); // 取出低位
//            code = (H - 0xD800) * 0x400 + 0x10000 + L - 0xDC00; // 转换算法
//            return '&#' + code + ';';
//          } else {
//            return char;
//          }
//        }
        );
      },
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
        if(this.ratings === ''){
          return ;
        }
        this.showFlag = false;
        let rating = {};
        rating['rateTime'] = Date.parse(new Date())/1000;
        rating['text'] = this.utf16ToUtf8(this.ratings);
        rating['parent_id'] = this.parent_id;
          this.$http.post('http://'+ host +'/exhibit_ratings/'+ this.exhibit_id+'/',rating, {emulateJSON:true} ).then(response => {
            if(response.body === 'error'){
              window.location = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx522cca3d4b048aa9&redirect_uri=http%3A//'+ encodeURIComponent(host) +'/home_html/&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
            }else{
              this.showFlag = false;
              document.body.style.height = '';
              document.body.style.overflow = '';
              window.location.reload();
            }
          },response => {
          });
      },
      show(content,parent_id) {
        this.title = content;
        this.parent_id = parent_id;
        this.showFlag = true;
      },
      hide() {
        this.showFlag = false;
        document.body.style.height = '';
        document.body.style.overflow = '';
      },
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
      transform: translate3d(0, 100%, 0)
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
    .send
      position: absolute
      top: 5px
      right: 2px
      font-size: 14px
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
        overflow-y:hidden
        overflow-x:hidden
        width: 100%
        height: 150px
        border-color: transparent
        /*border-top: 2px*/
        /*border-bottom: 2px*/
        /*border-style: solid*/
        /*background-color: antiquewhite*/
        padding-top: 10px
        line-height: 20px
        overflow: auto
      .commit
        text-align: center
        vertical-align: middle
        margin-top: 10px
</style>
