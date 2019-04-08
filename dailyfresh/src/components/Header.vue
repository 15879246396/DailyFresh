<template>
  <div class="header_con">
    <div class="header">
      <div class="welcome fl">欢迎来到天天生鲜!</div>
      <div class="fr">
        <div class="login_info fl login_btn" v-if="this.$store.getters.getIsLogin">
          欢迎您：<em>{{this.$store.getters.getUserName}}</em>
          <span>|</span>
          <a href="#" @click.prevent="loginOut">退出</a>
        </div>
        <div class="login_btn fl" v-else>
          <a href="/login">登录</a>
          <span>|</span>
          <a href="/register">注册</a>
        </div>
        <div class="user_link fl">
          <span>|</span>
          <a href="/user_center">用户中心</a>
          <span>|</span>
          <a href="/cart">我的购物车</a>
          <span>|</span>
          <a href="/user_order">我的订单</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    methods: {
      loginOut(){
        Bmob.User.logout()
        this.$store.dispatch('setUser')
        this.$router.push('/')
      }
    }
  }
</script>
