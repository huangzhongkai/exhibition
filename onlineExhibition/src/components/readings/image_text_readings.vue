<template>
  <div>
    <div class="title">
      【{{reading.title}}】
    </div>
    <div class="top_image">
      <img width="100%" :src="reading.image_path">
    </div>
    <div class="reading">
      <div v-for="item in reading.reading_content" v-if="item != '' " class="my_section">
        <p style="text-indent: 2em">
          {{item}}。
        </p>
      </div>
    </div>
    <div class="bottom-box">
      <div class="tab">
        <div class="tab-item">
          <span>
            <i class="fa fa-reply fa-1x" aria-hidden="true"></i>
            <!--<span><img src="/static/exhibit/rating.png" width="20px" height="20px"/></span>-->
            <span @click="back()" style="margin-left: 1px">返回</span>
          </span>
        </div>
      </div>
    </div>
    <div style="height: 48px"></div>
  </div>
</template>

<script>
  import {urlParse} from '../../common/js/util';
  import wx from 'weixin-js-sdk'
  import global_ from '../Global.vue'
  import 'font-awesome-webpack'

  let host = global_.host;

  export default {
    data () {
      return {
        config:{},
        readings:[],
        reading:{},
        params: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })(),
          type: (() => {
            let queryParam = urlParse();
            return queryParam.type;
          })()
        },
      }
    },
    created() {
      if(this.params.type === 'exhibit'){
        this.$http.get('http://'+ host +'/exhibit_image_text_readings/'+ this.params.id +'/').then(response => {
          this.reading = response.body;
        },response => {
        });
      }else if(this.params.type === 'exhibition'){
        this.$http.get('http://'+ host +'/exhibition_image_text_readings/'+ this.params.id + '/').then(response => {
          this.reading = response.body;
        },response => {
        });
      };
    },
    methods: {
      back(){
        window.history.back();
      },
    }
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/mixin.styl"
  .title
    margin-top: 20px
    margin-bottom: 10px
    text-align: center
    font-size: 24px
  .top_image
    margin: 0 10px 5px 10px
  .reading
    margin: 5px 5px 5px 5px
    padding-top: 10px
    line-height: 20px
    /*overflow: auto*/
    .my_section
      margin: 10px
  .bottom-box
    position: fixed
    left: 0
    bottom: 0
    z-index: 20
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
