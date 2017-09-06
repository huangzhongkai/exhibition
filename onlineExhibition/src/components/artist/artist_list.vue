<template>
  <div>
    <div class="production">
      <div class="left_product">
        <div v-for="artist in artists" class="exhibit_block">
          <img @click="show_artist(artist.id)" width="100%"  v-bind:src="artist.head_path">
          <div class="exhibit_name">
            {{artist.name}}
          </div>
          <div class="exhibit_author">
            作品数量:{{artist.production_number}}
          </div>
        </div>
      </div>
      <div class="right_product">
        <div v-for="artist in artists_right" class="exhibit_block">
          <img @click="show_artist(artist.id)" width="100%" v-bind:src="artist.head_path">
          <div class="exhibit_name">
            {{artist.name}}
          </div>
          <div class="exhibit_author">
            作品数量:{{artist.production_number}}
          </div>
        </div>
      </div>
    </div>
    <div style="display: none;" class="load-more-gif" id="loading">loading...</div>
  </div>
</template>

<script type="text/ecmascript-6">
  import {urlParse} from '../../common/js/util';

  import global_ from '../Global.vue'

  let host = global_.host;

  export default {
    data () {
      return {
        artists:[],
        artists_right:[],
        is_more_rating:true,
        get_count:8,
        get_offset:0,
      }
    },
    props: {
    },
    created() {
      this.$http.get('http://'+ host +'/artists/?get_count=' + this.get_count
        + '&get_offset=' + this.get_offset ).then(response => {
        this.artists = [];
        this.artists_right = [];
        if(response.body.length%2 === 0){
          for(let i=0;i<response.body.length/2;i++){
            this.artists[i]=response.body[i];
            this.artists_right[i]=response.body[i+response.body.length/2];
          }
        }else{
          let l = response.body.length -1;
          for(let i=0;i<l/2;i++){
            this.artists[i]=response.body[i];
            this.artists_right[i]=response.body[i+l/2];
          }
          this.artists[l/2] = response.body[response.body.length -1];
        }

        _this.get_offset +=response.body.length;
      },response => {
      });


      let _this = this;
      $(window).scroll(function () {
        console.log('aaaaa');
        let scrpllTop = $(this).scrollTop();
        let scroolHeight = $(document).height();
        let windowHeight = $(this).height();
        if(_this.is_more_rating === true){
          if(scrpllTop + windowHeight === scroolHeight){
            $("#loading").css('display','block');
            _this.$http.get('http://'+ host +'/artists/?get_count=' + _this.get_count
              + '&get_offset=' + _this.get_offset ).then(response => {

              if(response.body.length%2 === 0){
                for(let i=0;i<response.body.length/2;i++){
                  _this.artists.push(response.body[i]);
                  _this.artists_right.push(response.body[i+response.body.length/2]);
                }
              }else{
                let l = response.body.length -1;
                for(let i=0;i<l/2;i++){
                  _this.artists.push(response.body[i]);
                  _this.artists_right.push(response.body[i+l/2]);
                }
                _this.artists.push(response.body[response.body.length -1]);
              }

              if(response.body.length < _this.get_count){
                $("#loading").html('没有更多艺术家了');
                _this.is_more_rating = false;
                _this.get_offset +=response.body.length;
              }else{
                _this.get_offset +=_this.get_count;
              }
            },response => {
            });

          }
        }
      })
    },
    methods: {
      show_artist (key) {
        window.open('http://'+ host +'/artist_html/?artist=' + key);
      },
    }
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .production
    display: flex
    width: 100%
    .left_product
      margin-left: 5px
      margin-right: 5px
      flex: 1
      width:50%
      .exhibit_block
        margin-top:10px
        border-color: darkgrey
        border-style: solid
        border-radius: 5px
        border-width:1px
        background-color: white
        .exhibit_author
          color: darkgrey
    .right_product
      margin-left: 5px
      margin-right: 5px
      flex: 1
      width:50%
      .exhibit_block
        margin-top:10px
        border-color: darkgrey
        border-style: solid
        border-radius: 5px
        border-width:1px
        background-color: white
        .exhibit_author
          color: darkgrey
  .load-more-gif
    width: 100%
    height: 44px
    text-align: center
    line-height: 44px
    background: #fff
    border-top: none
    color: #48B884
</style>
