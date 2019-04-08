<template>
  <div>
    <div class="register_con">
      <div class="l_con fl">
        <a class="reg_logo"><img src="../assets/images/logo02.png"></a>
        <div class="reg_slogan">足不出户  ·  新鲜每一天</div>
        <div class="reg_banner"></div>
      </div>

      <div class="r_con fr">
        <div class="reg_title clearfix">
          <h1>用户注册</h1>
          <a href="/login">登录</a>
        </div>
        <div class="reg_form clearfix">
          <form @submit.prevent="onSubmit">
            <ul>
              <li>
                <label for="username">用户名:</label>
                <input type="text" v-model="username" id="user_name">
                <span class="error_tip">提示信息</span>
              </li>
              <li>
                <label for="pwd">密码:</label>
                <input type="password" v-model="pwd" id="pwd">
                <span class="error_tip">提示信息</span>
              </li>
              <li>
                <label for="cpwd">确认密码:</label>
                <input type="password" v-model="cpwd" id="cpwd">
                <span class="error_tip">提示信息</span>
              </li>
              <li>
                <label for="email">邮箱:</label>
                <input type="email" v-model="email" id="email">
                <span class="error_tip">提示信息</span>
              </li>
              <li class="agreement">
                <input type="checkbox" name="allow" id="allow" checked="checked">
                <label>同意”天天生鲜用户使用协议“</label>
                <span class="error_tip2">提示信息</span>
              </li>
              <li class="reg_sub">
                <input type="submit" value="注 册">
              </li>
            </ul>
          </form>
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
        cpwd: '',
        email: '',
      }
    },
    methods: {
      onSubmit(){
        let params = {
          username: this.username,
          password: this.pwd,
          email: this.email,
        };
        Bmob.User.register(params).then(res => {
          alert('注册成功')
          this.$router.push('/login')
        }).catch(err => {
          console.log(err)
        })
      }
    }
  }
</script>
