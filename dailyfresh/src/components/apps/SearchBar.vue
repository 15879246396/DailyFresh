<template>
  <div class="search_bar clearfix">
    <a href="/" class="logo fl"><img src="../../assets/images/logo.png"></a>
    <div class="sub_page_name fl" v-if="this.$route.meta.title=='用户中心-天天生鲜'">|&nbsp;&nbsp;&nbsp;&nbsp;用户中心</div>
    <div class="sub_page_name fl" v-if="this.$route.meta.title=='购物车-天天生鲜'">|&nbsp;&nbsp;&nbsp;&nbsp;购物车</div>
    <div class="sub_page_name fl" v-if="this.$route.meta.title=='提交订单-天天生鲜'">|&nbsp;&nbsp;&nbsp;&nbsp;提交订单</div>
    <div class="search_con" :class="(this.$route.path=='/'||this.$route.path=='/detail')?'fl':'fr'">
      <input type="text" class="input_text fl" name="" placeholder="搜索商品">
      <input type="button" class="input_btn fr" name="" value="搜索">
    </div>
    <div class="guest_cart fr" v-show="this.$route.path=='/'||this.$route.path=='/detail'">
      <a href="/cart" class="cart_name fl">我的购物车</a>
      <div class="goods_count fl fly_end" id="show_count">{{getCartCount()}}</div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {

      }
    },
    methods: {
      getCartCount(){
        return this.$store.getters.getCartCount
      },
    },
  }
</script>
