<template>
  <div>
    <div class="list_model" v-for="(type, index) in homeList" :key="type.objectId">
      <div class="list_title clearfix">
        <h3 class="fl" :id="'model0'+index">{{type.name}}</h3>
        <div class="subtitle fl">
          <span>|</span>
          <a href="#">鲜芒</a>
          <a href="#">加州提子</a>
          <a href="#">亚马逊牛油果</a>
        </div>
        <a href="#" class="goods_more fr" id="fruit_more">查看更多 ></a>
      </div>

      <div class="goods_con clearfix">
        <div class="goods_banner fl"><img :src="type.image.url"></div>
        <ul class="goods_list fl">
          <li v-for="goods in type.goods" :key="goods.objectId">
            <h4><a href="#">{{goods.name}}</a></h4>
            <a href="#" @click.prevent="goodsDetail(goods.objectId)"><img :src="goods.image.url"></a>
            <div class="prize">¥ {{goods.price.toFixed(2)}}</div>
          </li>
        </ul>
      </div>
    </div>
    <div class="msg">Welcome！&nbsp;&nbsp;&nbsp;{{this.$route.params.username}}</div>

  </div>
</template>


<script>
  import {showMsg} from "../assets/js/app";

  export default {
    data () {
      return {
        homeList: [],
      }
    },
    methods: {
      goodsDetail(id){
        this.$router.push({name: 'detailLink', query: {id: id}})
      },
    },
    created() {

    },
    mounted() {
      this.axios.get('/getHomeList').then(res => {
        this.homeList = res.data
        if (this.$route.params.newLogin){
          showMsg(4000)
        }
      }).catch(err => {
        console.log(err)
      });

    },

  }
</script>
