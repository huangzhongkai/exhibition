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
        introduction:'',
        params: {
          id: (() => {
            let queryParam = urlParse();
            return queryParam.id;
          })()
        },
      }
    },
    created() {
      this.$http.get('http://10.50.101.66:8887/image_text_readings/'+ this.params.id).then(response => {
        this.reading = response.body;
      },response => {
      });
      this.introduction = '张大千（Chang Dai-Chien），男，四川内江人，祖籍广东省番禺，1899年5月10日出生于四川省内江市中区城郊安良里的\
      一个书香门第的家庭，中国泼墨画家，书法家。20 世纪50年代，张大千游历世界，获得巨大的国际声誉，被西方艺坛赞为“东方之笔”。\\n[1]\
      他与二哥张善子昆仲创立“大风堂派”，是二十世纪中国画坛最具传奇色彩的泼墨画工。特别在山水画方面卓有成就。后旅居海外，画风工写结合，\
      重彩、水墨融为一体，尤其是泼墨与泼彩，开创了新的艺术风格，因其诗、书、画与齐白石、溥心畲齐名，故又并称为“南张北齐”和“南张北溥”，\
      名号多如牛毛。与黄君璧、溥心畲以“渡海三家”齐名。二十多岁便蓄著一把大胡子，成为张大千日后的特有标志。他曾与齐白石、徐悲鸿、黄君璧、\
      黄宾虹、溥儒、郎静山等及西班牙抽象派画家毕加索交游切磋。'
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
