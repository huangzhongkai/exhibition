<template>
  <div>
    <div class="exhibition" ref="exhibition">
      <!--<ul style="height: 1000px;">-->
        <li @click="show_exhibition(exhibition.id)" v-for="(exhibition, index) in exhibitions" class="my_exhibition">
          <div class="top_image">
            <img width="100%" v-bind:src="exhibition.image_path">
          </div>
          <div class="exhibition_info">
            <div class="info_left">
              <div>
                {{ exhibition.name}}
              </div>
              <div>
                展览时间：{{ exhibition.exhibition_date}}
              </div>
              <div>
                展览地点：{{ exhibition.exhibition_site}}
              </div>
            </div>
            <div class="info_right">
              <div>
                展策人:{{ exhibition.exhibition_curator}}
              </div>
            </div>
          </div>
        </li>
      <!--</ul>-->
    </div>
  </div>
</template>

<script>
  import {urlParse} from '../../common/js/util';
//  import BScroll from 'better-scroll';

  import global_ from '../Global.vue'

  let host = global_.host;

  export default {
    data () {
      return {
        exhibitions:[],
        params: {
          artist: (() => {
            let queryParam = urlParse();
            return queryParam.artist;
          })()
        },
      }
    },
    created() {
      this.$http.get('http://'+ host +'/exhibitions/?artist='+this.params.artist).then(response => {
        this.exhibitions = response.body;
//        this.$nextTick(() => {
//          this._initScroll();
//        });
      },response => {
      });

    },
    mounted() {

    },
    methods:{
      show_exhibition(key) {
        window.open("http://"+ host +"/exhibition_html/?id=" + key);
//        window.location = "http://qb4dwjh.hk1.mofasuidao.cn/exhibition_html/?id=" + key ;
      },
//      _initScroll() {
//        this.exhibitionScroll = new BScroll(this.$refs.exhibition, {
//          click: true,
////          scrollX: true,
//        });
//      },
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .exhibition
    width: 100%
    background-color: #f5f5f9
    .my_exhibition
      border-color: darkgrey
      border-style: solid
      border-radius: 5px
      border-width:1px
      margin-top:5px
      .exhibition_info
        display:flex
        .info_left
          margin-left:2px
          margin-right:auto
          color: #7e8c8d
        .info_right
          margin-left:auto
          margin-right:2px
          color: #7e8c8d
</style>
