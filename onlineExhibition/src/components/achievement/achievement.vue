<template>
  <div class="achievement">
    <div v-for="item in achievement" class="my_section">
      {{item}}
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
        achievement:[],
        params: {
          artist: (() => {
            let queryParam = urlParse();
            return queryParam.artist;
          })()
        },
      }
    },
    created() {
      this.$http.get('http://'+ host +'/achievement/?artist='+ this.params.artist).then(response => {
        this.achievement = response.body;
      },response => {
      });
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">

  .achievement
    position: relative
    margin: 5px 5px 5px 5px
    height: 200px
    /*border-color: antiquewhite*/
    /*border: 2px*/
    /*border-style: solid*/
    /*border-radius: 5px*/
    /*background-color: antiquewhite*/
    padding-top: 10px
    line-height: 20px
    /*overflow: auto*/
    .my_section
      margin: 10px
</style>
