<template>
  <div class="header">
    <div class="content_wrapper">
      <div class="avatar">
        <img width="64" height="64" v-bind:src="header.avatar">
      </div>
      <div class="name">
        {{header.name}}
      </div>
    </div>
    <div class="attention-wrapper">
      <div class="attention">
        <button @click="addOne()" v-bind:class="[attention_condition ? 'add_attention' : 'not_attention']"></button>
      </div>
      <div class="content_attention">
        <span>{{header.attention_count}}人关注</span>
      </div>
    </div>
    <div class="background">
      <img v-bind:src="header.avatar" width="100%" height="100%"/>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">

  import global_ from '../Global.vue'

  let host = global_.host;

  export default {
    props: {
      header: {
        type: Object
      }
    },
    data () {
      return {
        attention_condition: false,
      }
    },
    methods: {
        addOne() {
          if(this.attention_condition === true){
            this.attention_condition = false;
            this.header.attention_count -=1;
            this.$http.delete('http://'+ host +'/attention/?artist_id='+ this.header.id).then(response => {

            },response => {
              this.attention_condition = true;
              this.header.attention_count +=1;
            });
          }else{
            this.attention_condition = true;
            this.header.attention_count +=1;
            this.$http.post('http://'+ host +'/attention/?artist_id=' + this.header.id).then(response => {

            },response => {
              this.attention_condition = false;
              this.header.attention_count -=1;
            });
          }
        },
        update(isAttention){
          if(isAttention === 'true'){
            this.attention_condition = true;
          }else{
            this.attention_condition = false;
          }
        }
    }
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/mixin.styl";
  .header
    margin: 0px
    position: relative
    overflow: hidden
    .content_wrapper
      margin: 5px
      text-align:center
      img
        border-color: darkgrey
        border-style: solid
        border-radius: 5px
        border-width:1px
    .attention-wrapper
      margin: 5px
      text-align:center
      .add_attention
        margin: 5px
        border-color: #7e8c8d
        border-radius: 10px
        color: black
      .not_attention
        margin: 5px
        border-color: #7e8c8d
        border-radius: 10px
        color: black
      .add_attention::after
        size: 16px
        content: "已关注";
      .not_attention::after
        size: 16px
        content: "+关注";
    .background
      position: absolute
      top: 0
      left: 0
      width: 100%
      height: 100%
      z-index: -1
      filter: blur(10px)
</style>
