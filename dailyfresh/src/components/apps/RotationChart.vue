<template>
  <div class="center_con clearfix">
    <ul class="subnav fl">
      <li v-for="(item, index) in goodsTypes" :key="item.objectId">
        <a :href="'#model0'+index" :class="item.class">{{item.name}}</a>
      </li>
      <!--<li><a href="#model02" class="seafood">海鲜水产</a></li>-->
      <!--<li><a href="#model03" class="meet">猪牛羊肉</a></li>-->
      <!--<li><a href="#model04" class="egg">禽类蛋品</a></li>-->
      <!--<li><a href="#model05" class="vegetables">新鲜蔬菜</a></li>-->
      <!--<li><a href="#model06" class="ice">速冻食品</a></li>-->
    </ul>
    <div class="slide fl">
      <ul class="slide_pics">
        <li><img src="../../assets/images/slide.jpg" alt="幻灯片"></li>
        <li><img src="../../assets/images/slide02.jpg" alt="幻灯片"></li>
        <li><img src="../../assets/images/slide03.jpg" alt="幻灯片"></li>
        <li><img src="../../assets/images/slide04.jpg" alt="幻灯片"></li>
      </ul>
      <div class="prev"></div>
      <div class="next"></div>
      <ul class="points"></ul>
    </div>
    <div class="adv fl">
      <a href="#"><img src="../../assets/images/adv01.jpg"></a>
      <a href="#"><img src="../../assets/images/adv02.jpg"></a>
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
