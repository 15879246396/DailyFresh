<template>
  <div class="main_con clearfix">
    <div class="left_menu_con clearfix">
      <h3>用户中心</h3>
      <ul>
        <router-link tag="li" class="left_menu_li" :to="{name: 'userInfoLink'}">
          <a :class="{'active': this.$route.path=='/user_info'}">· 个人信息</a>
        </router-link>
        <router-link tag="li" class="left_menu_li" :to="{name: 'orderLink'}">
          <a :class="{'active': this.$route.path=='/user_order'}">· 全部订单</a>
        </router-link>
        <router-link tag="li" class="left_menu_li" :to="{name: 'addressLink'}">
          <a :class="{'active': this.$route.path=='/address'}">· 收货地址</a>
        </router-link>
      </ul>
    </div>
    <router-view></router-view>
  </div>
</template>
