<template>
  <div>
    <div class="list_model" v-for="(type, index) in homeList" :key="type.objectId">
      <div class="list_title clearfix">
        <h3 class="fl" :id="'model0'+index">{{type.name}}</h3>
        <div class="subtitle fl">
          <span>|</span>
          <a href="#">鲜芒</a>
          <a href="#">加州提子</a>
          <a href="#">亚马逊牛油果</a>
        </div>
        <a href="#" class="goods_more fr" id="fruit_more">查看更多 ></a>
      </div>

      <div class="goods_con clearfix">
        <div class="goods_banner fl"><img :src="type.image.url"></div>
        <ul class="goods_list fl">
          <li v-for="goods in type.goods" :key="goods.objectId">
            <h4><a href="#">{{goods.name}}</a></h4>
            <a href="#" @click.prevent="goodsDetail(goods.objectId)"><img :src="goods.image.url"></a>
            <div class="prize">¥ {{goods.price.toFixed(2)}}</div>
          </li>
          <!--<li>-->
            <!--<h4><a href="#">葡萄</a></h4>-->
            <!--<a href="#"><img src="../assets/images/goods/goods002.jpg"></a>-->
            <!--<div class="prize">¥ 5.50</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">柠檬</a></h4>-->
            <!--<a href="#"><img src="../assets/images/goods/goods001.jpg"></a>-->
            <!--<div class="prize">¥ 3.90</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">奇异果</a></h4>-->
            <!--<a href="#"><img src="../assets/images/goods/goods012.jpg"></a>-->
            <!--<div class="prize">¥ 25.80</div>-->
          <!--</li>-->
        </ul>
      </div>
    </div>

    <!--<div class="list_model">-->
      <!--<div class="list_title clearfix">-->
        <!--<h3 class="fl" id="model02">海鲜水产</h3>-->
        <!--<div class="subtitle fl">-->
          <!--<span>|</span>-->
          <!--<a href="#">河虾</a>-->
          <!--<a href="#">扇贝</a>-->
        <!--</div>-->
        <!--<a href="#" class="goods_more fr">查看更多 ></a>-->
      <!--</div>-->

      <!--<div class="goods_con clearfix">-->
        <!--<div class="goods_banner fl"><img src="images/banner02.jpg"></div>-->
        <!--<ul class="goods_list fl">-->
          <!--<li>-->
            <!--<h4><a href="#">青岛野生海捕大青虾</a></h4>-->
            <!--<a href="#"><img src="images/goods/goods018.jpg"></a>-->
            <!--<div class="prize">¥ 48.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">扇贝</a></h4>-->
            <!--<a href="#"><img src="images/goods/goods019.jpg"></a>-->
            <!--<div class="prize">¥ 46.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">冷冻秋刀鱼</a></h4>-->
            <!--<a href="#"><img src="images/goods/goods020.jpg"></a>-->
            <!--<div class="prize">¥ 19.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">基围虾</a></h4>-->
            <!--<a href="#"><img src="images/goods/goods021.jpg"></a>-->
            <!--<div class="prize">¥ 25.00</div>-->
          <!--</li>-->
        <!--</ul>-->
      <!--</div>-->
    <!--</div>-->

    <!--<div class="list_model">-->
      <!--<div class="list_title clearfix">-->
        <!--<h3 class="fl" id="model03">猪牛羊肉</h3>-->
        <!--<div class="subtitle fl">-->
          <!--<span>|</span>-->
          <!--<a href="#">鲜芒</a>-->
          <!--<a href="#">加州提子</a>-->
          <!--<a href="#">亚马逊牛油果</a>-->
        <!--</div>-->
        <!--<a href="#" class="goods_more fr">查看更多 ></a>-->
      <!--</div>-->

      <!--<div class="goods_con clearfix">-->
        <!--<div class="goods_banner fl"><img src="images/banner03.jpg"></div>-->
        <!--<ul class="goods_list fl">-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄维多利亚葡萄维多利亚葡萄维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
        <!--</ul>-->
      <!--</div>-->
    <!--</div>-->

    <!--<div class="list_model">-->
      <!--<div class="list_title clearfix">-->
        <!--<h3 class="fl" id="model04">禽类蛋品</h3>-->
        <!--<div class="subtitle fl">-->
          <!--<span>|</span>-->
          <!--<a href="#">鲜芒</a>-->
          <!--<a href="#">加州提子</a>-->
          <!--<a href="#">亚马逊牛油果</a>-->
        <!--</div>-->
        <!--<a href="#" class="goods_more fr">查看更多 ></a>-->
      <!--</div>-->

      <!--<div class="goods_con clearfix">-->
        <!--<div class="goods_banner fl"><img src="images/banner04.jpg"></div>-->
        <!--<ul class="goods_list fl">-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄维多利亚葡萄维多利亚葡萄维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
        <!--</ul>-->
      <!--</div>-->
    <!--</div>-->

    <!--<div class="list_model">-->
      <!--<div class="list_title clearfix">-->
        <!--<h3 class="fl" id="model05">新鲜蔬菜</h3>-->
        <!--<div class="subtitle fl">-->
          <!--<span>|</span>-->
          <!--<a href="#">鲜芒</a>-->
          <!--<a href="#">加州提子</a>-->
          <!--<a href="#">亚马逊牛油果</a>-->
        <!--</div>-->
        <!--<a href="#" class="goods_more fr">查看更多 ></a>-->
      <!--</div>-->

      <!--<div class="goods_con clearfix">-->
        <!--<div class="goods_banner fl"><img src="images/banner05.jpg"></div>-->
        <!--<ul class="goods_list fl">-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄维多利亚葡萄维多利亚葡萄维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
        <!--</ul>-->
      <!--</div>-->
    <!--</div>-->

    <!--<div class="list_model">-->
      <!--<div class="list_title clearfix">-->
        <!--<h3 class="fl" id="model06">速冻食品</h3>-->
        <!--<div class="subtitle fl">-->
          <!--<span>|</span>-->
          <!--<a href="#">鲜芒</a>-->
          <!--<a href="#">加州提子</a>-->
          <!--<a href="#">亚马逊牛油果</a>-->
        <!--</div>-->
        <!--<a href="#" class="goods_more fr">查看更多 ></a>-->
      <!--</div>-->

      <!--<div class="goods_con clearfix">-->
        <!--<div class="goods_banner fl"><img src="images/banner06.jpg"></div>-->
        <!--<ul class="goods_list fl">-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄维多利亚葡萄维多利亚葡萄维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<h4><a href="#">维多利亚葡萄</a></h4>-->
            <!--<a href="#"><img src="images/goods.jpg"></a>-->
            <!--<div class="prize">¥ 38.00</div>-->
          <!--</li>-->
        <!--</ul>-->
      <!--</div>-->
    <!--</div>-->
  </div>
</template>


<script>
  export default {
    data () {
      return {
        homeList: []
      }
    },
    methods: {
      goodsDetail(id){
        this.$router.push({name: 'detailLink', query: {id: id}})
      }
    },
  created() {
    this.axios.get('/getHomeList').then(res => {
      this.homeList = res.data
    }).catch(err => {
      console.log(err)
    })
  }
  }
</script>
