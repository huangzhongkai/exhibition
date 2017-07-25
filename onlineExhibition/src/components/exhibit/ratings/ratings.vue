<template>
  <transition name="move">
  <div v-show="showFlag" class="edit_ratings">
    <div class="top">
      <span>【朝奉图】</span>
    </div>
    <div class="back" @click="hide">
      <i class="icon-arrow_lift"></i>
    </div>
    <div>
      <textarea v-model="ratings" ref="ratings" class="ratings_input" placeholder="留言将由作者删选显示"/>
    </div>
    <div class="commit">
      <button  @click="commit" type="button" class="btn btn-primary">提交</button>
    </div>
  </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  export default {
    props: {
      exhibition_id:0
    },
    data () {
      return {
        ratings:'',
        showFlag: false,
      }
    },
    methods: {
      commit(){
        let rating = {};
        rating['username'] = '赵六';
        rating['rateTime'] = Date.parse(new Date())/1000;
        rating['text'] = this.ratings;
        rating['avatar'] = 'http://static.galileo.xiaojukeji.com/static/tms/default_header.png';
        this.$http.post('http://qb4dwjh.hk1.mofasuidao.cn/exhibit_ratings/'+ this.exhibition_id+'/',rating,{emulateJSON:true} ).then(response => {
          this.showFlag = false;
          document.body.style.height = '';
          document.body.style.overflow = '';
          window.location.reload();
        },response => {
        });
      },
      show() {
        this.showFlag = true;
      },
      hide() {
        this.showFlag = false;
        document.body.style.height = '';
        document.body.style.overflow = '';
      },
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .edit_ratings
    position: fixed
    left: 0
    top: 0
    z-index: 30
    width: 100%
    height: 100%
    background: #fff
    overflow: hidden
    transform: translate3d(0, 0, 0)
    &.move-enter-active, &.move-leave-active
      transition: all 0.2s linear
    &.move-enter, &.move-leave-active
      transform: translate3d(100%, 0, 0)
    .top
      text-align: center
      font-size: 15px
      padding: 10px 0 10px 0
    .back
      position: absolute
      top: 0px
      left: 0px
      .icon-arrow_lift
        display: block
        padding: 10px
        font-size: 20px
        color: black
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
