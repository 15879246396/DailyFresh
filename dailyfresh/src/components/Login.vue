<template>
  <div>
    <div class="login_top clearfix">
      <a href="/" class="login_logo"><img src="../assets/images/logo02.png"></a>
    </div>
    <div class="login_form_bg">
      <div class="login_form_wrap clearfix">
        <div class="login_banner fl"></div>
        <div class="slogan fl">日夜兼程 · 急速送达</div>
        <div class="login_form fr">
          <div class="login_title clearfix">
            <h1>用户登录</h1>
            <a href="/register">立即注册</a>
          </div>
          <div class="form_input">
            <form @submit.prevent="onSubmit">
              <input type="text" v-model="username" class="name_input" placeholder="请输入用户名或邮箱">
              <div class="user_error" v-show="show_1">用户不存在</div>
              <input type="password" v-model="pwd" class="pass_input" placeholder="请输入密码" v-on:click="show_2=false">
              <div class="pwd_error" v-show="show_2">密码错误</div>
              <div class="more_input clearfix">
                <input type="checkbox" name="">
                <label>记住用户名</label>
                <a href="#">忘记密码</a>
              </div>
              <input type="submit" name="" value="登录" class="input_submit">
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        username: '',
        pwd: '',
        show_2: false,
        show: false,
      }
    },
    methods: {
      onSubmit(){
        Bmob.User.login(this.username, this.pwd).then(res => {
          alert('登陆成功！')
          this.$router.push('/')
        }).catch(err => {
          if (err.code == 101) {
            this.show_2 = true
          }
        })
      }
    },
    computed: {
      show_1: {
        get(){
          if (this.username.length > 4) {
            const query = Bmob.Query('_User');
            const query1 = query.equalTo('username', '==', this.username);
            const query2 = query.equalTo('email', '==', this.username);
            query.or(query1, query2);
            query.find().then(res => {
              if (res.length > 0) {
                this.show = false
              } else {
                this.show = true
              }
            })
            return this.show
          } else {
            return false
          }
        }
      }
    }
  }
</script>
