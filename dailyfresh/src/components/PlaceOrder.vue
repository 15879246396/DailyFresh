<template>
  <div>
    <h3 class="common_title">确认收货地址</h3>

    <div class="common_list_con clearfix">
      <dl v-if="getUserInfo()">
        <dt>寄送到：</dt>
        <dd>{{myAddress}} （{{myAddressee}} 收） {{myPhone}}</dd>
      </dl>
      <dl v-else>
        <dt>请添加收货地址</dt>
        <dd>&nbsp;</dd>
      </dl>
      <a href="/address" class="edit_site">编辑收货地址</a>

    </div>

    <h3 class="common_title">支付方式</h3>
    <div class="common_list_con clearfix">
      <div class="pay_style_con clearfix">
        <input type="radio" name="pay_style" checked>
        <label class="cash">货到付款</label>
        <input type="radio" name="pay_style">
        <label class="weixin">微信支付</label>
        <input type="radio" name="pay_style">
        <label class="zhifubao"></label>
        <input type="radio" name="pay_style">
        <label class="bank">银行卡支付</label>
      </div>
    </div>

    <h3 class="common_title">商品列表</h3>

    <div class="common_list_con clearfix">
      <ul class="goods_list_th clearfix">
        <li class="col01">商品名称</li>
        <li class="col02">商品单位</li>
        <li class="col03">商品价格</li>
        <li class="col04">数量</li>
        <li class="col05">小计</li>
      </ul>
      <ul class="goods_list_td clearfix" v-for="(item, index) in payCart" :key="item.objectId">
        <li class="col01">{{index+1}}</li>
        <li class="col02"><img :src="item.image.url"></li>
        <li class="col03">{{item.name}}</li>
        <li class="col04">{{item.unite}}</li>
        <li class="col05">{{item.price}}元</li>
        <li class="col06">{{item.quantity}}</li>
        <li class="col07">{{(item.price*item.quantity).toFixed(2)}}元</li>
      </ul>
    </div>

    <h3 class="common_title">总金额结算</h3>

    <div class="common_list_con clearfix">
      <div class="settle_con">
        <div class="total_goods_count">共<em>{{payCart.length}}</em>件商品，总金额<b>{{getPrice}}元</b></div>
        <div class="transit">运费：<b>10元</b></div>
        <div class="total_pay">实付款：<b>{{(parseFloat(getPrice)+10).toFixed(2)}}元</b></div>
      </div>
    </div>

    <div class="order_submit clearfix">
      <a href="javascript:;" id="order_btn" @click="placeOrder">提交订单</a>
    </div>
    <div class="msg">请添加收货信息！</div>
  </div>
</template>

<script>
  import {showMsg} from "../assets/js/app";

  export default {
    data () {
      return {
        myAddressee: null,
        myAddress: null,
        myPhone: null,
        payCart: this.$route.params.payCart,
      }
    },
    methods: {
      getUserInfo(){
        const query = Bmob.Query('UserInfo')
        query.equalTo("user", "==", this.$store.getters.getUserId);
        query.find().then(res => {
          if (res.length) {
            this.myAddressee = res[0].addressee
            this.myAddress = res[0].address
            this.myPhone = res[0].phone
          }
        });
        if (this.myAddressee) {
          return true
        } else {
          return false
        }
      },
      placeOrder(){
        if (this.myAddressee && this.myAddress) {
        this.axios.post('/placeOrder', {'payCart': this.payCart}).then(res => {
          if (res.status==200) {
            console.log(res)
            this.$router.push('/user_order')
          }
        })} else {
          showMsg()
        }
      },
    },
    computed: {
      getPrice(){
        let price = 0;
        this.payCart.forEach(item => {
          if (item.status) {
            price += item.price * item.quantity
          }
        })
        return price.toFixed(2)
      }
    },
    created() {
      if (!this.$route.params.payCart) {
        this.$router.push('/')
      }
    }
  }
</script>
