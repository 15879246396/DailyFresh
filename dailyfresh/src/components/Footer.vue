<template>
  <div class="footer">
    <div class="foot_link">
      <a href="#">关于我们</a>
      <span>|</span>
      <a href="#">联系我们</a>
      <span>|</span>
      <a href="#">招聘人才</a>
      <span>|</span>
      <a href="#">友情链接</a>
    </div>
    <p>CopyRight © 2016 北京天天生鲜信息技术有限公司 All Rights Reserved</p>
    <p>电话：010-****888    京ICP备*******8号</p>
    <div class="msg">Welcome！&nbsp;&nbsp;&nbsp;{{this.$route.params.username}}</div>
  </div>
</template>

<script>
  import {showMsg} from "../assets/js/app";

  export default {
    mounted() {
      if (this.$route.params.newLogin){
        showMsg(4000)
      }
    }

  }
</script>
