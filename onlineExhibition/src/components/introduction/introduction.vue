<template>
  <div class="introduction">
    <p v-for="item in introduction" class="my_section">
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
        introduction:[],
        params: {
          artist: (() => {
            let queryParam = urlParse();
            return queryParam.artist;
          })()
        },
      }
    },
    created() {
      this.$http.get('http://'+ host +'/introduction/?artist='+ this.params.artist).then(response => {
        this.introduction = response.body;
      },response => {
      });
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .introduction
    position: relative
    line-height: 20px
    padding-top: 5px
    .my_section
      text-indent: 2em
      width: 100%
      background-color: #f5f5f9
      margin-top: 10px
</style>
