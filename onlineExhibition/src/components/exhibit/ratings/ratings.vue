<template>
  <div>
    <div class="top">
      【朝奉图】
    </div>
    <div>
      <textarea v-model="ratings" ref="ratings" class="ratings_input" placeholder="留言将由作者删选显示"/>
    </div>
    <div class="commit">
      <button  @click="commit" type="button" class="btn btn-primary">提交</button>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data () {
      return {
        ratings:''
      }
    },
    methods: {
      commit(){
        console.log(this.ratings);
        console.log(Date.parse(new Date()));9
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .top
    text-align: center
    padding: 10px 0 10px 0
  .ratings_input
    width: 100%
    height: 150px
    border-color: darkgrey
    border-top: 2px
    border-bottom: 2px
    border-style: solid
    background-color: antiquewhite
    padding-top: 10px
    line-height: 20px
    overflow: auto
  .commit
    text-align: center
    vertical-align: middle
    margin-top: 10px
</style>
