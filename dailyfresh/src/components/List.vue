<template>
  <div>
    <div class="breadcrumb">
      <a href="#">全部分类</a>
      <span>></span>
      <a href="#">{{goodsList.type}}</a>
    </div>

    <div class="main_wrap clearfix">
      <div class="l_wrap fl clearfix">
        <div class="new_goods">
          <h3>新品推荐</h3>
          <ul>
            <li>
              <a href="#"><img src="images/goods/goods001.jpg"></a>
              <h4><a href="#">进口柠檬</a></h4>
              <div class="prize">￥3.90</div>
            </li>
            <li>
              <a href="#"><img src="images/goods/goods002.jpg"></a>
              <h4><a href="#">玫瑰香葡萄</a></h4>
              <div class="prize">￥16.80</div>
            </li>
          </ul>
        </div>
      </div>

      <div class="r_wrap fr clearfix">
        <div class="sort_bar">
          <a href="#" class="active">默认</a>
          <a href="#">价格</a>
          <a href="#">人气</a>
        </div>

        <ul class="goods_type_list clearfix">
          <li v-for="goods in goodsList.goods" :key="goods.objectId">
            <a href="#" @click.prevent="goodsDetail(goods.objectId)"><img :src="goods.image.url"></a>
            <h4><a href="#" @click.prevent="goodsDetail(goods.objectId)">{{goods.name}}</a></h4>
            <div class="operate">
              <span class="prize">￥{{(goods.price).toFixed(2)}}</span>
              <span class="unit">{{(goods.price).toFixed(2)}}/{{goods.unite}}</span>
              <a href="#" class="add_goods" title="加入购物车"></a>
            </div>
          </li>

          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods004.jpg"></a>-->
            <!--<h4><a href="#">吐鲁番梨光杏</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥5.50</span>-->
              <!--<span class="unit">5.50/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->

          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods005.jpg"></a>-->
            <!--<h4><a href="#">黄肉桃</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥10.00</span>-->
              <!--<span class="unit">10.00/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->

          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods006.jpg"></a>-->
            <!--<h4><a href="#">进口西梅</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥28.80</span>-->
              <!--<span class="unit">28.8/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->

          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods007.jpg"></a>-->
            <!--<h4><a href="#">香梨</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥6.45</span>-->
              <!--<span class="unit">6.45/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->

          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods008.jpg"></a>-->
            <!--<h4><a href="#">栗子</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥9.50</span>-->
              <!--<span class="unit">9.50/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->

          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods009.jpg"></a>-->
            <!--<h4><a href="#">海南香蕉</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥3.30</span>-->
              <!--<span class="unit">3.30/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->

          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods010.jpg"></a>-->
            <!--<h4><a href="#">青苹果</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥5.00</span>-->
              <!--<span class="unit">5.00/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->

          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods011.jpg"></a>-->
            <!--<h4><a href="#">山莓</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥28.80</span>-->
              <!--<span class="unit">28.8/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->

          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods012.jpg"></a>-->
            <!--<h4><a href="#">奇异果</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥25.80</span>-->
              <!--<span class="unit">25.8/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods013.jpg"></a>-->
            <!--<h4><a href="#">蜜桔</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥4.80</span>-->
              <!--<span class="unit">4.8/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods014.jpg"></a>-->
            <!--<h4><a href="#">脐橙</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥3.50</span>-->
              <!--<span class="unit">3.50/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods001.jpg"></a>-->
            <!--<h4><a href="#">进口柠檬</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥3.90</span>-->
              <!--<span class="unit">3.90/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->
          <!--<li>-->
            <!--<a href="#"><img src="images/goods/goods002.jpg"></a>-->
            <!--<h4><a href="#">玫瑰香葡萄</a></h4>-->
            <!--<div class="operate">-->
              <!--<span class="prize">￥16.80</span>-->
              <!--<span class="unit">16.80/500g</span>-->
              <!--<a href="#" class="add_goods" title="加入购物车"></a>-->
            <!--</div>-->
          <!--</li>-->
        </ul>

        <div class="pagenation">
          <a :href="getUrl($route.query.page-1)">&lt;上一页</a>
          <a :href="getUrl(index)" :class="($route.query.page==index)?'active':''" v-for="(page, index) in goodsList.max_page" :key="index">{{index+1}}</a>
          <!--<a href="#">2</a>-->
          <!--<a href="#">3</a>-->
          <!--<a href="#">4</a>-->
          <!--<a href="#">5</a>-->
          <a :href="($route.query.page)?getUrl($route.query.page+1):getUrl(1)">下一页&gt;</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        goodsList: {},
      }
    },
    mounted() {
      this.axios.get('/getList', {params: this.$route.query}).then(res => {
        this.goodsList = res.data
      })
    },
    methods: {
      goodsDetail(id){
        this.$router.push({name: 'detailLink', query: {id: id}})
      },
      getUrl(index){
        if (index==NaN || index>=this.goodsList.max_page || index<0) {
          var url = 'javascript:;'
        } else {
          if ((this.$route.query.page && this.$route.query.page!=index) || (!this.$route.query.page && this.$route.query.page!=0)) {
            if (this.$route.query.name) {
              var url = '/list?name=' + this.$route.query.name + '&page=' + index
            } else {
              var url = '/list?page=' + index
            }
          } else {
            var url = 'javascript:;'
          }
        }
        return url
      },
    },
  }
</script>
