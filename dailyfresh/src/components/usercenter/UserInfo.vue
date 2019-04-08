<template>
  <div class="right_content clearfix">
    <div class="info_con clearfix">
      <h3 class="common_title2">基本信息</h3>
      <ul class="user_info_list">
        <li><span>用户名：</span>&nbsp;{{this.$store.getters.getUserName}}</li>
        <li><span>联系方式：</span>&nbsp;{{getUserInfo.phone}}</li>
        <li><span>联系地址：</span>&nbsp;{{getUserInfo.address}}</li>
      </ul>
    </div>

    <h3 class="common_title2">最近浏览</h3>
    <div class="has_view_list">
      <ul class="goods_type_list clearfix">
        <li>
          <a href="detail.html"><img src="/src/assets/images/goods/goods003.jpg"></a>
          <h4><a href="detail.html">大兴大棚草莓</a></h4>
          <div class="operate">
            <span class="prize">￥16.80</span>
            <span class="unit">16.80/500g</span>
            <a href="#" class="add_goods" title="加入购物车"></a>
          </div>
        </li>

        <li>
          <a href="#"><img src="/src/assets/images/goods/goods004.jpg"></a>
          <h4><a href="#">吐鲁番梨光杏</a></h4>
          <div class="operate">
            <span class="prize">￥5.50</span>
            <span class="unit">5.50/500g</span>
            <a href="#" class="add_goods" title="加入购物车"></a>
          </div>
        </li>

        <li>
          <a href="#"><img src="/src/assets/images/goods/goods005.jpg"></a>
          <h4><a href="#">黄肉桃</a></h4>
          <div class="operate">
            <span class="prize">￥10.00</span>
            <span class="unit">10.00/500g</span>
            <a href="#" class="add_goods" title="加入购物车"></a>
          </div>
        </li>

        <li>
          <a href="#"><img src="/src/assets/images/goods/goods006.jpg"></a>
          <h4><a href="#">进口西梅</a></h4>
          <div class="operate">
            <span class="prize">￥28.80</span>
            <span class="unit">28.8/500g</span>
            <a href="#" class="add_goods" title="加入购物车"></a>
          </div>
        </li>

        <li>
          <a href="#"><img src="/src/assets/images/goods/goods007.jpg"></a>
          <h4><a href="#">香梨</a></h4>
          <div class="operate">
            <span class="prize">￥6.45</span>
            <span class="unit">6.45/500g</span>
            <a href="#" class="add_goods" title="加入购物车"></a>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        phone: '',
        address: '',
      }
    },
    computed: {
      getUserInfo: {
        get(){
          const query = Bmob.Query('UserInfo')
          query.equalTo("user", "==", this.$store.getters.getUserId);
          query.find().then(res => {
            if (res.length) {
              this.address = res[0].address
              this.phone = res[0].phone
            }
          });
          return {'address': this.address, 'phone': this.phone}
        }
      }
    }
  }
</script>
