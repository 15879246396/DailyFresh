<template>
  <div class="navbar_con">
    <div class="navbar clearfix">
      <div v-if="this.$route.path=='/list'" class="subnav_con fl">
        <h1>全部商品分类</h1>
        <span></span>
        <ul class="subnav">
          <li v-for="item in goodsTypes" :key="item.objectId">
            <a :href="'/list?name='+item.name" :class="item.class">{{item.name}}</a>
          </li>
          <!--<li><a href="#" class="fruit">新鲜水果</a></li>-->
          <!--<li><a href="#" class="seafood">海鲜水产</a></li>-->
          <!--<li><a href="#" class="meet">猪牛羊肉</a></li>-->
          <!--<li><a href="#" class="egg">禽类蛋品</a></li>-->
          <!--<li><a href="#" class="vegetables">新鲜蔬菜</a></li>-->
          <!--<li><a href="#" class="ice">速冻食品</a></li>-->
        </ul>
      </div>
      <h1 v-else class="fl">全部商品分类</h1>

      <ul class="navlist fl">
        <li><a href="">首页</a></li>
        <li class="interval">|</li>
        <li><a href="">手机生鲜</a></li>
        <li class="interval">|</li>
        <li><a href="">抽奖</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        goodsTypes: []
      }
    },
    created() {
      this.axios.get('/getHomeList').then(res => {
        this.goodsTypes = res.data
      })
    }
  }
</script>
