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
        swiperOption1: {
          pagination: '.swiper-pagination',
          effect: 'coverflow',
          grabCursor: true,
          centeredSlides: true,
          slidesPerView: 2,
          coverflow: {
            rotate: 50,
            stretch: 0,
            depth: 400,
            modifier: 1,
            slideShadows: false
          },
          spaceBetween: -150,
          loop: true,
        },
        exhibitions:[],
        exhibition:{},
        c_height:'',
        i_height:'',
        exhibits:[]
      }
    },
    created(){
      this.$http.get('http://10.50.101.66:8887/exhibitions?artist=0').then(response => {
        this.exhibitions = response.body;
      },response => {
      });
      this.exhibits = [
        {
          'id':0,
          'image_path':'/static/exhibit/朝奉图.jpeg'
        },
        {
          'id':1,
          'image_path':'/static/exhibit/树.jpeg'
        },
        {
          'id':2,
          'image_path':'/static/exhibit/景.jpeg'
        },
        {
          'id':3,
          'image_path':'/static/exhibit/竹子.jpeg'
        }
      ]
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
