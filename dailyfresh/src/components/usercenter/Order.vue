<template>
  <div class="right_content clearfix">
    <h3 class="common_title2">全部订单</h3>
    <div v-for="item in waitingPay" :key="item.order_no">
      <ul class="order_list_th w978 clearfix">
        <li class="col01">{{item.createdAt}}</li>
        <li class="col02">订单号：{{item.order_no}}</li>
        <li class="col02 stress">未支付</li>
      </ul>

      <table class="order_list_table w980">
        <tbody>
        <tr>
          <td width="55%">
            <ul class="order_goods_list clearfix" v-for="goods in item.goods" :key="goods.objectId">
              <li class="col01"><img :src="goods.image.url"></li>
              <li class="col02">{{goods.name}}<em>11.80元/500g</em></li>
              <li class="col03">{{goods.quantity}}</li>
              <li class="col04">{{(goods.price).toFixed(2)}}元</li>
            </ul>
          </td>
          <td width="15%">{{(item.tatol).toFixed(2)}}元</td>
          <td width="15%">待付款</td>
          <td width="15%"><a href="#" class="oper_btn">去付款</a></td>
        </tr>
        </tbody>
      </table>
    </div>

    <div>
      <ul class="order_list_th w978 clearfix">
        <li class="col01">2016-8-21 17:36:24</li>
        <li class="col02">订单号：56872934</li>
        <li class="col02 stress">已支付</li>
      </ul>
      <table class="order_list_table w980">
        <tbody>
        <tr>
          <td width="55%">
            <ul class="order_goods_list clearfix">
              <li class="col01"><img src="/src/assets/images/goods02.jpg"></li>
              <li class="col02">嘎啦苹果嘎啦苹果<em>11.80元/500g</em></li>
              <li class="col03">1</li>
              <li class="col04">11.80元</li>
            </ul>
            <ul class="order_goods_list clearfix">
              <li class="col01"><img src="/src/assets/images/goods02.jpg"></li>
              <li class="col02">嘎啦苹果嘎啦苹果<em>11.80元/500g</em></li>
              <li class="col03">1</li>
              <li class="col04">11.80元</li>
            </ul>
          </td>
          <td width="15%">33.60元</td>
          <td width="15%">已付款</td>
          <td width="15%"><a href="#" class="oper_btn">查看物流</a></td>
        </tr>
        </tbody>
      </table>
    </div>

    <div class="pagenation">
      <a href="#">&lt;上一页</a>
      <a href="#" class="active">1</a>
      <a href="#">2</a>
      <a href="#">3</a>
      <a href="#">4</a>
      <a href="#">5</a>
      <a href="#">下一页&gt;</a>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        waitingPay: [],
      }
    },
    methods: {
      getWaitingPay(){
        this.axios.post('/getWaitingPay', {'userId': this.$store.getters.getUserId, 'order_status': 1}).then(res => {
          this.waitingPay = res.data
          res.data.forEach(item => {

          })
          console.log(this.waitingPay)
        });
      },
    },
    mounted() {
      setTimeout(this.getWaitingPay, 100)
    },
  }
</script>
