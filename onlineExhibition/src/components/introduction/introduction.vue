<template>
  <div class="introduction">
   <div v-for="item in introduction" class="my_section">
     {{item}}
   </div>
  </div>
</template>

<script>
  import {urlParse} from '../../common/js/util';

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
      this.$http.get('http://10.50.101.66:8887/introduction?artist='+ this.params.artist).then(response => {
        this.introduction = response.body;
      },response => {
      });
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .introduction
    position: relative
    margin: 5px 5px 5px 5px
    height: 200px
    border-color: antiquewhite
    border: 2px
    border-style: solid
    border-radius: 5px
    background-color: antiquewhite
    padding-top: 10px
    overflow: auto
    .my_section
      margin: 10px
</style>
