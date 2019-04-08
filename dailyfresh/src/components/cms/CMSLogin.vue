<template>
  <div id="wrap-login">
    <div class="container">
      <div class="bimoe-wrap">
        <div class="bimoe-inner">
          <h3 class="bimoe-form-title">
            登录<span class="bimoe-switch pull-right">系统管理</span>
          </h3>
          <form class="bimoe-form" @submit.prevent="onSubmit">
            <div class="bimoe-form-group">
              <label>
                <i class="fas fa-envelope"></i>
                <input type="text" id="email" class="bimoe-form-input require" v-model="user" placeholder="用户名或邮箱" data-label="邮箱">
              </label>
            </div>
            <div class="bimoe-form-group">
              <label>
                <i class="fas fa-lock"></i>
                <input type="password" id="passwd" class="bimoe-form-input require" v-model="pwd" placeholder="登录密码" data-label="密码">
              </label>
            </div>
            <div class="checkbox">
              <label class="bimoe-checkbox">

              </label>
            </div>
            <div class="last">
              <input class="btn btn-login btn-block btn-lg" type="submit" id="login" value="登录">
            </div>
          </form>
        </div>
      </div>
    </div>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css">
    <link rel="stylesheet" href="https://ssr.koonb.cn/theme/assets/home/css/style.css">
    <link rel="stylesheet" href="https://ssr.koonb.cn/theme/assets/home/css/bimoe.css">
    <link rel="stylesheet" href="https://ssr.koonb.cn/theme/assets/layui/layui.css">
  </div>
</template>

<script>
  export default {
    data () {
      return {
        user: '',
        pwd: '',
      }
    },
    methods: {
      onSubmit(){
        if (this.user && this.pwd) {
          Bmob.User.login(this.user, this.pwd).then(res => {
            const query = Bmob.Query('_User')
            query.get(res.objectId).then(res => {
              if (res['is_admin']) {
                this.$store.commit('setAdmin', res.objectId)
                this.$router.push('/cms')
              } else {
                alert('用户名或密码错误!')
              }
            })
          }).catch(err =>alert('用户名或密码错误!'))
        }
      }
    }
  }
</script>

