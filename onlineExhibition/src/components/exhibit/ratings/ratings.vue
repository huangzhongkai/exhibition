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
      <div class="edit_ratings" >
        <!--<div class="top">-->
          <!--<span>{{title}}</span>-->
        <!--</div>-->
        <!--<div class="back" @click="hide">-->
          <!--<i class="icon-arrow_lift"></i>-->
        <!--</div>-->
        <!--<button class="send btn btn-default" @click="upload()">发布</button>-->
        <div class="content" ref="content">
          <div>
            <textarea autofocus="autofocus" v-model="ratings" ref="ratings" class="ratings_input" placeholder="写评论..."/>
          </div>
          <div class="my_commit">
            <button @click="upload()" type="button" class="btn btn-primary btn-block btn-lg" >提交</button>
          </div>
        </div>
        <div style="height: 53px"></div>
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
        remark: {},
        parent_id:-1,
        title:'',
        title_bak:'',
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
        if(this.type === false){
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
        }else{
          this.remark['content'] = this.utf16ToUtf8(this.ratings);
          this.$http.post('http://'+ host +'/exhibit_remark/'+ this.exhibit_id+'/',this.remark, {emulateJSON:true} ).then(response => {
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
        }

      },
      show(content,parent_id) {
        this.title = content;
        this.title_bak = $('title').html();
        $('title').html(this.title);
        this.parent_id = parent_id;
        this.showFlag = true;
      },
      show_remark(remark) {
        this.title_bak = $('title').html();
        $('title').html('圈点点评');
        this.showFlag = true;
        this.type = true;
        this.remark = remark;
      },
      hide() {
        $('title').html(this.title_bak);
        this.showFlag = false;
        document.body.style.height = '';
        document.body.style.overflow = '';
      },
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../../common/stylus/mixin.styl";
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
      .my_commit
        margin-left: 40px
        margin-right: 40px
        margin-top: 60px
        text-align: center
      .ratings_input
        overflow-y:hidden
        overflow-x:hidden
        width: 100%
        height: 150px
        font-size: 18px
        border-color: transparent
        padding-top: 10px
        line-height: 20px
        overflow: auto
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
