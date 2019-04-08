<template>
  <div>
    <div class="total_count">全部商品<em>{{getCartItems.length}}</em>件</div>
    <ul class="cart_list_th clearfix">
      <li class="col01">商品名称</li>
      <li class="col02">商品单位</li>
      <li class="col03">商品价格</li>
      <li class="col04">数量</li>
      <li class="col05">小计</li>
      <li class="col06">操作</li>
    </ul>
    <transition-group name="slide-fade">
    <ul class="cart_list_td clearfix" v-for="item in getCartItems" :key="item.name">
      <li class="col01"><input type="checkbox" v-model="item.status" checked></li>
      <li class="col02"><img :src="item.picture"></li>
      <li class="col03">{{item.name}}<br><em>{{item.price}}元/{{item.unit}}</em></li>
      <li class="col04">{{item.unit}}</li>
      <li class="col05">{{item.price}}元</li>
      <li class="col06">
        <div class="num_add">
          <a href="javascript:;" @click.prevent="addQuantity(item)" class="add fl">+</a>
          <input type="text" class="num_show fl" v-model="item.quantity">
          <a href="javascript:;" @click.prevent="subQuantity(item)" class="minus fl">-</a>
        </div>
      </li>
      <li class="col07">25.80元</li>
      <li class="col08"><a href="javascript:;" @click.prevent="removeCart(item)">删除</a></li>
    </ul>
    </transition-group>

    <ul class="settlements">
      <li class="col01"><input type="checkbox" v-model="allChecked" checked @click="checked"></li>
      <li class="col02">全选</li>
      <li class="col03">合计(不含运费)：<span>¥</span><em>{{getPrice}}</em><br>共计<b>{{getCount}}</b>件商品</li>
      <li class="col04"><a href="place_order.html">去结算</a></li>
    </ul>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        allChecked: true,
        getCartItems: [
          {
            name: '奇异果',
            price: '25.80',
            unit: '500g',
            picture: '/src/assets/images/goods/goods012.jpg',
            quantity: '1',
            status: true,
          },
          {
            name: '大兴大棚草莓',
            price: '16.80',
            unit: '500g',
            picture: '/src/assets/images/goods/goods003.jpg',
            quantity: '1',
            status: true,
          },
        ]
      }
    },
    computed: {
      getCount(){
        let count = 0
        this.getCartItems.forEach(item => {
          if (item.status) {
            count ++
          }
        })
        if (count == this.getCartItems.length) {
          this.allChecked = true
        } else {
          this.allChecked = false
        }
        return count
      },
      getPrice(){
        let price = 0
        this.getCartItems.forEach(item => {
          if (item.status) {
            price += item.price * item.quantity
          }
        })
        return price.toFixed(2)
      }
    },
    methods: {
      checked(){
        if (!this.allChecked) {
          this.getCartItems.forEach(item => {
            item.status = true
          })
        } else {
          this.getCartItems.forEach(item => {
            item.status = false
          })
        }
      },
      addQuantity(item){
        item.quantity ++
        item.status = true
      },
      subQuantity(item){
        item.quantity --
        if (item.quantity < 1) {
          item.quantity = 0
          item.status = false
        }
      },
      removeCart(item){
        this.getCartItems.splice(this.getCartItems.indexOf(item), 1)
      },
    }
  }
</script>
<style>
  /* 可以设置不同的进入和离开动画 */
  /* 设置持续时间和动画函数 */
  .slide-fade-enter-active {
    transition: all .3s ease;
  }
  .slide-fade-leave-active {
    transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }
  .slide-fade-enter, .slide-fade-leave-to
    /* .slide-fade-leave-active 用于 2.1.8 以下版本 */ {
    transform: translateX(10px);
    opacity: 0;
  }
</style>
