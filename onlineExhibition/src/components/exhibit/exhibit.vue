<template>
  <div class="production">
    <div class="left_product">
      <div v-for="exhibit in exhibits" class="exhibit_block">
        <img @click="show_exhibit(exhibit.id)" width="100%"  v-bind:src="exhibit.image_path">
        <div class="exhibit_name">
          {{exhibit.name}}
        </div>
        <div class="exhibit_author">
          {{exhibit.author}}
        </div>
      </div>
    </div>
    <div class="right_product">
      <div v-for="exhibit in exhibits_right" class="exhibit_block">
        <img @click="show_exhibit(exhibit.id)" width="100%" v-bind:src="exhibit.image_path">
        <div class="exhibit_name">
          {{exhibit.name}}
        </div>
        <div class="exhibit_author">
          {{exhibit.author}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {urlParse} from '../../common/js/util';

  import global_ from '../Global.vue'

  let host = global_.host;

  export default {
    data () {
      return {
        production:[],
        exhibits:[],
        exhibits_right:[],
        params: {
          artist: (() => {
            let queryParam = urlParse();
            return queryParam.artist;
          })()
        },
      }
    },
    props: {
    },
    created() {
      this.$http.get('http://'+ host +'/exhibits/?artist='+ this.params.artist).then(response => {
        this.exhibits = [];
        this.exhibits_right = [];
        if(response.body.length%2 === 0){
          for(let i=0;i<response.body.length/2;i++){
            this.exhibits[i]=response.body[i];
            this.exhibits_right[i]=response.body[i+response.body.length/2];
          }
        }else{
          let l = response.body.length -1;
          for(let i=0;i<l/2;i++){
            this.exhibits[i]=response.body[i];
            this.exhibits_right[i]=response.body[i+l/2];
          }
          this.exhibits_right[l/2] = response.body[response.body.length -1];
        }
      },response => {
      });
    },
    methods: {
      show_exhibit (key) {
        window.open('http://'+ host +'/exhibit_html/?id=' + key);
//        window.location = 'http://qb4dwjh.hk1.mofasuidao.cn/exhibit_html/?id=' + key;
      },
    }
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .production
    display: flex
    width: 100%
    margin-top: 5px
    .left_product
      margin-left: 5px
      margin-right: 5px
      flex: 1
      width:50%
      .exhibit_block
        margin-top:2px
        border-color: antiquewhite
        border-style: solid
        border-radius: 5px
        background-color: antiquewhite
    .right_product
      margin-left: 5px
      margin-right: 5px
      flex: 1
      width:50%
      .exhibit_block
        margin-top:2px
        border-color: antiquewhite
        border-style: solid
        border-radius: 5px
        background-color: antiquewhite
</style>
