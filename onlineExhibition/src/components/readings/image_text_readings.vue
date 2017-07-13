<template>
  <div>
    <div class="top_image">
      <img width="100%" :src="reading.image_path">
    </div>
    <div class="image_text_readings">
      {{reading.reading_content}}
    </div>
    <span style="float: right;">
      —— 张大千
    </span>
  </div>
</template>

<script>
  import {urlParse} from '../../common/js/util';

  export default {
    data () {
      return {
        readings:[],
        reading:{},
        params: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })(),
          type: (() => {
            let queryParam = urlParse();
            return queryParam.type;
          })()
        },
      }
    },
    created() {
      if(this.params.type === 'exhibit'){
        this.$http.get('http://10.50.101.66:8887/exhibit_image_text_readings/'+ this.params.id).then(response => {
          this.reading = response.body;
        },response => {
        });
      }else if(this.params.type === 'exhibition'){
        this.$http.get('http://10.50.101.66:8887/exhibition_image_text_readings/'+ this.params.id).then(response => {
          this.reading = response.body;
        },response => {
        });
      }
    },
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .image_text_readings
    position: relative
    margin: 2px 2px 2px 2px
    height: 200px
    border-color: antiquewhite
    border: 2px
    border-style: solid
    border-radius: 5px
    background-color: antiquewhite
    padding-top: 10px
    overflow: auto
    line-height: 20px
</style>
