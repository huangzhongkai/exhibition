<template>
  <div>
    <swiper :options="swiperOption" ref="mySwiperA">
      <swiper-slide v-for="item in exhibitions" :key="item.id">
        <img @click="show_exhibition(item.id)" width="100%" :src="item.image_path" >
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>

    <div class="topbar">
      <span class="left">作品推荐</span>
      <span class="right" @click="more_charactor()">查看更多</span>
    </div>
    <div class="recommend">
      <div class="recommend-left" :style="{height:c_height}" ref="recommend_left">
        <img @click="show_exhibit(exhibits[0].id)" :src="exhibits[0].image_path" :style="{width:'100%' ,height:c_height}"/>
      </div>
      <div class="recommend-right" :style="{height:c_height}">
        <div class="recommend-right-top">
          <div class="recommend-right-top-left" :style="{height:i_height}">
            <img @click="show_exhibit(exhibits[1].id)" :src="exhibits[1].image_path" :style="{width:'100%' ,height:i_height}"/>
          </div>
          <div class="recommend-right-top-right" :style="{height:i_height}">
            <img @click="show_exhibit(exhibits[2].id)" :src="exhibits[2].image_path" :style="{width:'100%' ,height:i_height}"/>
          </div>
        </div>
        <div class="recommend-right-bottom">
          <div class="recommend-right-bottom-left" :style="{height:i_height}">
            <img @click="show_exhibit(exhibits[3].id)" :src="exhibits[3].image_path" :style="{width:'100%' ,height:i_height}"/>
          </div>
          <div class="recommend-right-bottom-right" :style="{height:i_height}">
            <img @click="show_exhibit(exhibits[1].id)" :src="exhibits[1].image_path" :style="{width:'100%' ,height:i_height}"/>
          </div>
        </div>
      </div>
    </div>

    <!--<div class="swiper-inner">-->
      <!--<swiper :options="swiperOption1" ref="mySwiper">-->
        <!--<swiper-slide>-->
          <!--<div class="swiper-content">-->
            <!--<img width="100%" height="200px" src="./body3.jpeg" >-->
            <!--<span>-->
              <!--陈小江极其盒子-->
            <!--</span>-->
            <!--<br/>-->
            <!--<span>-->
              <!--展览时间：2017年4月16至5月-->
            <!--</span>-->
          <!--</div>-->
        <!--</swiper-slide>-->
        <!--<swiper-slide>-->
          <!--<div class="swiper-content">-->
            <!--<img width="100%" height="200px" src="./body1.jpeg" >-->
            <!--<span>-->
              <!--陈小江极其盒子-->
            <!--</span>-->
            <!--<br/>-->
            <!--<span>-->
              <!--展览时间：2017年4月16至5月-->
            <!--</span>-->
          <!--</div>-->
        <!--</swiper-slide>-->
        <!--<swiper-slide>-->
          <!--<div class="swiper-content">-->
            <!--<img width="100%" height="200px" src="./body2.jpeg" >-->
            <!--<span>-->
              <!--陈小江极其盒子-->
            <!--</span>-->
            <!--<br/>-->
            <!--<span>-->
              <!--展览时间：2017年4月16至5月-->
            <!--</span>-->
          <!--</div>-->
        <!--</swiper-slide>-->
        <!--<div class="swiper-pagination" slot="pagination"></div>-->
      <!--</swiper>-->
    <!--</div>-->

    <div class="topbar">
      <span class="left">最新展览</span>
    </div>
    <div class="new_exhibition" v-for="item in exhibitions">
      <div class="top_image">
        <img @click="show_exhibition(item.id)" width="100%" :src="item.image_path">
      </div>
      <div class="exhibition_info">
        <div class="info_left">
          <div>
            展览:{{item.name}}
          </div>
          <div>
            展览时间:{{item.exhibition_date}}
          </div>
          <div>
            展览地点:{{item.exhibition_site}}
          </div>
        </div>
        <div class="info_right">
          <div>
            展策人:{{item.exhibition_curator}}
          </div>
        </div>
      </div>
    </div>

    <more_charactor :exhibition_id="0" ref="more_charactor">
    </more_charactor>
  </div>
</template>

<script type="text/ecmascript-6">
  import { swiper, swiperSlide,} from 'vue-awesome-swiper'
  import more_charactor from "../exhibition/more_charactor/more_charactor.vue"
  import wx from 'weixin-js-sdk'

  export default{
    components: {
      swiper,
      swiperSlide,
      more_charactor
    },
    data(){
      return {
        swiperOption: {
          //notNextTick: true,
          pagination: '.swiper-pagination',
          slidesPerView: 1,
          paginationClickable: true,
          spaceBetween: 10,
          loop: true,
//          centeredSlides: true,
          autoplay: 3000,
          autoplayDisableOnInteraction: false,
          zoom: true,
//          onTransitionStart(swiper){
//            console.log(swiper)
//          }
        },
//        swiperOption1: {
//          pagination: '.swiper-pagination',
//          effect: 'coverflow',
//          grabCursor: true,
//          centeredSlides: true,
//          slidesPerView: 2,
//          coverflow: {
//            rotate: 50,
//            stretch: 0,
//            depth: 400,
//            modifier: 1,
//            slideShadows: false
//          },
//          spaceBetween: -150,
//          loop: true,
//        },
        exhibitions:[],
        exhibition:{},
        c_height:'',
        i_height:'',
        exhibits:[],
        config:{},
      }
    },
    created(){
      this.$http.get('http://qb4dwjh.hk1.mofasuidao.cn/exhibitions/?artist=0').then(response => {
        this.exhibitions = response.body;
      },response => {
      });

      this.$http.get('http://qb4dwjh.hk1.mofasuidao.cn/get_signature/?' +
        '&url='+ encodeURIComponent(location.href.split('#')[0])).then(response => {
        this.config = response.body;
        let _this = this;
        wx.config({
          debug: true, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
          appId: this.config.appid, // 必填，公众号的唯一标识
          timestamp: this.config.timestamp, // 必填，生成签名的时间戳
          nonceStr: this.config.noncestr, // 必填，生成签名的随机串
          signature: this.config.signature,// 必填，签名，见附录1
          jsApiList: [
            'onMenuShareAppMessage',
            'onMenuShareTimeline',
            'onMenuShareQQ',
            'onMenuShareWeibo',
            'onMenuShareQZone'
          ] // 必填，需要使用的JS接口列表，所有JS接口列表见附录2
        });

        wx.ready(function(){
          wx.onMenuShareAppMessage({
            title: '在线艺术品超市分享给朋友', // 分享标题
            desc: '在线艺术品超市，展厅,高大上的艺术家都在这里，加关注，不迷路', // 分享描述
            link: 'http://qb4dwjh.hk1.mofasuidao.cn/home_html/', // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
            imgUrl: 'http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/backround.jpg', // 分享图标
            type: '', // 分享类型,music、video或link，不填默认为link
            dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
            success: function () {
              // 用户确认分享后执行的回调函数
              alert('success');
            },
            cancel: function () {
              // 用户取消分享后执行的回调函数
              alert('fail');
            }
          });
          wx.onMenuShareTimeline({
            title: '在线艺术品超市分享到朋友圈', // 分享标题
            link: 'http://qb4dwjh.hk1.mofasuidao.cn/home_html/', // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
            imgUrl: 'http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/backround.jpg', // 分享图标
            success: function () {
            },
            cancel: function () {
            }
          });
          wx.onMenuShareQQ({
            title: '在线艺术品超市分享到qq', // 分享标题
            desc: '在线艺术品超市，展厅,高大上的艺术家都在这里，加关注，不迷路', // 分享描述
            link: 'http://qb4dwjh.hk1.mofasuidao.cn/home_html/', // 分享链接
            imgUrl: 'http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/backround.jpg', // 分享图标
            success: function () {
            },
            cancel: function () {
            }
          });
          wx.onMenuShareQZone({
            title: '在线艺术品超市分享到QZone', // 分享标题
            desc: '在线艺术品超市，展厅,高大上的艺术家都在这里，加关注，不迷路', // 分享描述
            link: 'http://qb4dwjh.hk1.mofasuidao.cn/home_html/', // 分享链接
            imgUrl: 'http://picturebank.oss-cn-qingdao.aliyuncs.com/onlineExhibition/backround.jpg', // 分享图标
            success: function () {
              // 用户确认分享后执行的回调函数
            },
            cancel: function () {
              // 用户取消分享后执行的回调函数
            }
          });
        });

        wx.error(function(res){
          _this.$http.get('http://qb4dwjh.hk1.mofasuidao.cn/motified_signature/?' +
            'url='+ encodeURIComponent(location.href.split('#')[0])).then(response => {
            window.location.reload();
          },response => {
          });
        });

      },response => {
      });

      this.exhibits = [
        {
          'id':0,
          'image_path':''
        },
        {
          'id':1,
          'image_path':''
        },
        {
          'id':2,
          'image_path':''
        },
        {
          'id':3,
          'image_path':''
        }
      ]
      this.$http.get('http://10.50.101.66:8887/exhibits/?artist=0').then(response => {
        this.exhibits = response.body;
      },response => {
      });
    },
    mounted() {
      console.log(this.$refs.recommend_left.style);
      this.c_height = (window.innerWidth/2+5) +'px';
      this.i_height = window.innerWidth/4 +'px';
    },
    methods: {
      show_exhibit(key) {
        window.open("http://10.50.101.66:8080/exhibit/exhibit.html?id=" + key);
      },
      show_exhibition(key) {
        window.open("http://10.50.101.66:8080/exhibition/exhibition.html?id=" + key);
      },
      more_charactor () {
        document.body.style.height = '100%';
        document.body.style.overflow = 'hidden';
        this.$refs.more_charactor.show();
      },
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .swiper-inner
    width: 100%;
    height: 240px;
    .swiper-content
      border-color: aliceblue
      border: 1.5px
      border-style: solid
      border-radius: 5px
      background-color: aliceblue
  .swiper-slide
    background-position: center;
    background-size: cover;
    width: 100%;
  .topbar
    margin-top: 5px
    margin-bottom: 5px
    display:flex
    .left
      margin-left: 2px
      margin-right: auto
    .right
      color: #7e8c8d
      margin-left: auto
      margin-right: 2px
  .exhibition_info
    border-color: #000
    display:flex
    .info_left
      margin-left:2px
      margin-right:auto
      color: #7e8c8d
    .info_right
      margin-left:auto
      margin-right:2px
      color: #7e8c8d
  .recommend
    display: flex
    width: 100%
    .recommend-left
      width:50%
      margin: 5px 5px 5px 5px
    .recommend-right
      width:50%
      margin: 5px 5px 5px 0px
      .recommend-right-top
        display: flex
        .recommend-right-top-left
          width: 50%
          margin-right: 5px
          margin-bottom: 5px
        .recommend-right-top-right
          width:50%
          margin-bottom: 5px
      .recommend-right-bottom
        display: flex
        .recommend-right-bottom-left
          width: 50%
          margin-right: 5px
        .recommend-right-bottom-right
          width:50%


</style>
