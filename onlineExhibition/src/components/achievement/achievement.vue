<template>
  <div class="achievement">
    <p v-for="item in achievement" class="my_section">
      {{item}}
    </p>
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
    padding-top: 5px
    line-height: 20px
    .my_section
      text-indent: 2em
      width: 100%
      background-color: #f5f5f9
      margin-top: 5px
</style>
