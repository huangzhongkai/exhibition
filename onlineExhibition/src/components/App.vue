<template>
  <div>
    <v-header :header="header"></v-header>
    <div class="tab">
      <div class="tab-item">
        <router-link to="/exhibit" >作品</router-link>
      </div>
      <div class="tab-item">
        <router-link to="/exhibition">展览</router-link>
      </div>
      <div class="tab-item">
        <router-link to="/introduction">简介</router-link>
      </div>
      <div class="tab-item">
        <router-link to="/achievement">成就</router-link>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script type="text/ecmascript-6">
  import header from "./header/header.vue"
  import {urlParse} from '../common/js/util';

  export default {
      data (){
        return {
          header: {
            artist: (() => {
              let queryParam = urlParse();
              return queryParam.artist;
            })()
          },
        };
      },
      created() {
        this.$http.get('http://10.50.101.66:8887/artists/'+ this.header.artist).then(response => {
          this.header = response.body;
        },response => {
        });
      },
      components: {
        'v-header':header
      },
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../common/stylus/mixin.styl";
  .tab
    display: flex
    width: 100%
    height: 40px
    line-height: 40px
    border-1px(rgba(7, 17, 27, 0.1))
  .tab-item
    flex: 1
    text-align: center
    & > a
      display: block
      font-size: 14px
      color: rgb(77, 85, 93)
      &.active
        color: rgb(240, 20, 20)

</style>
