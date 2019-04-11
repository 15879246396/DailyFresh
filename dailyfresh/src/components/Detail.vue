<template>
  <div>
    <h1>{{this.$route.params.id}}</h1>
    <div class="breadcrumb">
      <a href="#">全部分类</a>
      <span>></span>
      <a href="#">{{goodsType}}</a>
      <span>></span>
      <a href="#">商品详情</a>
    </div>

    <div class="goods_detail_con clearfix">
      <div class="goods_detail_pic fl"><img :src="goodsDetail.image.url"></div>

      <div class="goods_detail_list fr">
        <h3>{{goodsDetail.name}}</h3>
        <p>&nbsp;{{goodsDetail.desc}}</p>
        <div class="prize_bar">
          <span class="show_pirze">¥<em>{{goodsDetail.price.toFixed(2)}}</em></span>
          <span class="show_unit">单  位：{{goodsDetail.unite}}</span>
        </div>
        <div class="goods_num clearfix">
          <div class="num_name fl">数 量：</div>
          <div class="num_add fl">
            <input type="text" class="num_show fl" v-model="quantity">
            <a href="javascript:;" class="add fr" @click="quantity>99?quantity=100:quantity++">+</a>
            <a href="javascript:;" class="minus fr" @click="quantity<2?quantity=1:quantity--">-</a>
          </div>
        </div>
        <div class="total">总价：<em>{{getTotal}}元</em></div>
        <div class="operate_btn">
          <a href="javascript:;" class="buy_btn" @click="Pay">立即购买</a>
          <a href="javascript:;" class="add_cart fly" id="add_cart" @click="addCart">加入购物车</a>
        </div>
      </div>
    </div>

    <div class="main_wrap clearfix">
      <div class="l_wrap fl clearfix">
        <div class="new_goods">
          <h3>新品推荐</h3>
          <ul>
            <li>
              <a href="#"><img src="/src/assets/images/goods/goods001.jpg"></a>
              <h4><a href="#">进口柠檬</a></h4>
              <div class="prize">￥3.90</div>
            </li>
            <li>
              <a href="#"><img src="/src/assets/images/goods/goods002.jpg"></a>
              <h4><a href="#">玫瑰香葡萄</a></h4>
              <div class="prize">￥16.80</div>
            </li>
          </ul>
        </div>
      </div>

      <div class="r_wrap fr clearfix">
        <ul class="detail_tab clearfix">
          <li class="active">商品介绍</li>
          <li>评论</li>
        </ul>

        <div class="tab_content">
          <dl>
            <dt>商品详情：</dt>
            <dd>草莓采摘园位于北京大兴区 庞各庄镇四各庄村 ，每年1月-6月面向北京以及周围城市提供新鲜草莓采摘和精品礼盒装草莓，草莓品种多样丰富，个大香甜。所有草莓均严格按照有机标准培育，不使用任何化肥和农药。草莓在采摘期间免洗可以直接食用。欢迎喜欢草莓的市民前来采摘，也欢迎各大单位选购精品有机草莓礼盒，有机草莓礼盒是亲朋馈赠、福利送礼的最佳选择。 </dd>
          </dl>
        </div>

      </div>
    </div>
    <div class="msg">已成功加入购物车！</div>
  </div>
</template>
<script>
  import {fly} from "../assets/js/app";

  export default {
    data () {
      return {
        goodsDetail: {
          image: {url: null},
          price: 0,
        },
        goodsType: null,
        quantity: 1,
        total: null,
      }
    },
    created() {
      if (!this.$route.query.id) {
        this.$router.push('/')
      }
      const query = Bmob.Query('GoodsSKU');
      query.get(this.$route.query.id).then(res => {
        const query = Bmob.Query('GoodsType');
        query.get(res.type.objectId).then(res => {
          this.goodsType = res.name
        });
        this.goodsDetail = res;
      }).catch(err => {
        this.$router.push('/')
      });

    },
    methods: {
      addCart(e){
        const query = Bmob.Query('Cart');
        query.equalTo("user", "==", this.$store.getters.getUserId);
        query.equalTo("goods", "==", this.goodsDetail.objectId);
        query.equalTo("order_status", "==", 0)
        query.find().then(res => {
          if (res.length) {
            Bmob.Query('Cart').get(res[0].objectId).then(res => {
              res.set('quantity', res.quantity+this.quantity)
              res.save()
            })
          } else {
            const query = Bmob.Query('Cart');
            const userID = Bmob.Pointer('_User').set(this.$store.getters.getUserId);
            const goodsID = Bmob.Pointer('GoodsSKU').set(this.goodsDetail.objectId);
            query.set("user",userID )
            query.set("goods", goodsID)
            query.set("quantity", this.quantity)
            query.set("order_status", 0)
            query.save()
            this.$store.dispatch('addCart')
          }
        })
        fly(e)
      },
      Pay(){
        const payCart = [this.goodsDetail]
        payCart[0].quantity = this.quantity;
        payCart[0].user = this.$store.getters.getUserId;
        this.$router.push({name:'placeOrderLink', params: {payCart: payCart}})
      }
    },
    computed: {
      getTotal(){
        const total = this.goodsDetail.price * this.quantity;
        return total.toFixed(2)
      }
    }
  }
</script>
