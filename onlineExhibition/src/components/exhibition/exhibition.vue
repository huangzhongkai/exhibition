<template>
  <div>
    <div class="exhibition" ref="exhibition">
      <ul style="height: 1000px;">
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
      </ul>
    </div>
  </div>
</template>

<script>
  import {urlParse} from '../../common/js/util';
  import BScroll from 'better-scroll';

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
      this.$http.get('http://10.50.101.66:8887/exhibitions/?artist='+this.params.artist).then(response => {
        this.exhibitions = response.body;
        this.$nextTick(() => {
          this._initScroll();
        });
      },response => {
      });

    },
    mounted() {

    },
    methods:{
      show_exhibition(key) {
          console.log(key);
        window.open("http://10.50.101.66:8080/exhibition/exhibition.html?id=" + key);
      },
      _initScroll() {
        this.exhibitionScroll = new BScroll(this.$refs.exhibition, {
          click: true,
//          scrollX: true,
        });
      },
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .exhibition
    width: 100%
    overflow: hidden
    position: absolute
    top: 189px
    bottom: 0px
    .my_exhibition
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
</style>
