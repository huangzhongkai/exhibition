<template>
  <div class="header">
    <div class="content_wrapper">
      <div class="avatar">
        <img v-bind:src="header.avatar">
      </div>
      <div class="name">
        {{header.name}}
      </div>
    </div>
    <div class="attention-wrapper">
      <div class="attention btn-group" role="group">
        <button @click="addOne()" id="attention" type="button" class=" not_attention btn btn-block" ></button>
        <!--<span @click="addOne()" v-bind:class="[attention_condition ? 'add_attention' : 'not_attention']"></span>-->
      </div>
      <div class="content_attention">
        <span style="font-size: 10pt">{{header.attention_count}}人关注</span>
      </div>
    </div>
    <div style="background-color: #f5f5f9; height: 5px"></div>
    <!--<div class="background">-->
      <!--<img v-bind:src="header.avatar" width="100%" height="100%"/>-->
    <!--</div>-->
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
          if(this.attention_condition === true){
            $('#attention').removeClass("not_attention").addClass("add_attention");
          }else{
            $('#attention').removeClass("add_attention").addClass("not_attention");
          }
        },
        update(isAttention){
          if(isAttention === 'true'){
            this.attention_condition = true;
          }else{
            this.attention_condition = false;
          }

          if(this.attention_condition === true){
            $('#attention').removeClass("not_attention").addClass("add_attention");
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
      margin-top: 16pt
      text-align:center
      img
        width: 91pt
        height: 91pt
        border-color: darkgrey
        border-style: solid
        border-radius: 5px
        border-width:1px
      .name
        margin-top: 12pt
    .attention-wrapper
      margin-top: 1px
      margin-bottom: 2px
      text-align:center
      .add_attention
        width: 75pt
        border-color: #7e8c8d
        border-radius: 5px
        background-color #666666
      .not_attention
        width: 75pt
        border-color: #7e8c8d
        border-radius: 5px
        background-color #666666
      .add_attention::after
        font-size: 12px
        content: "已关注";
      .not_attention::after
        font-size: 12px
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
