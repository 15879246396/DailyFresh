<template>
  <div class="right_content clearfix">
    <h3 class="common_title2">收货地址</h3>
    <div class="site_con">
      <dl v-if="getUserInfo">
        <dt>当前地址：</dt>
        <dd>{{myAddress}} （{{myAddressee}} 收） {{myPhone}}</dd>
      </dl>
      <dl v-else>
        <dt>请添加收货地址</dt>
        <dd></dd>
      </dl>
    </div>
    <h3 class="common_title2">编辑地址</h3>
    <div class="site_con">
      <form @submit.prevent="onSubmit">
        <div class="form_group">
          <label for="addressee">收件人：</label>
          <input type="text" v-model="addressee">
        </div>
        <div class="form_group form_group2">
          <label for="address">详细地址：</label>
          <textarea class="site_area" v-model="address"></textarea>
        </div>
        <div class="form_group">
          <label for="postCode">邮编：</label>
          <input type="text" v-model="postCode">
        </div>
        <div class="form_group">
          <label for="phone">手机：</label>
          <input type="text" v-model="phone">
        </div>

        <input type="submit" name="" value="提交" class="info_submit">
      </form>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        addressee: '',
        address: '',
        postCode: '',
        phone: '',
        myAddressee: null,
        myAddress: null,
        myPhone: null,
      }
    },
    methods: {
      onSubmit(){
        if (this.addressee && this.address && this.phone) {
          const query = Bmob.Query('UserInfo');
          query.equalTo("user", "==", this.$store.getters.getUserId);
          query.find().then(res => {
            if (res.length == 0) {
              const pointer = Bmob.Pointer('_User')
              const poiID = pointer.set(this.$store.getters.getUserId)
              query.set('addressee', this.addressee)
              query.set('address', this.address)
              query.set('postCode', this.postCode)
              query.set('phone', this.phone)
              query.set('user', poiID)
              query.save().then(res => {
                console.log(res)
                this.$store.commit('setUserInfo', this.addressee, this.address, this.phone)
              })
            } else {
              query.get(res[0].objectId).then(res => {
                res.set('addressee', this.addressee)
                res.set('address', this.address)
                res.set('postCode', this.postCode)
                res.set('phone', this.phone)
                this.myAddressee = this.addressee
                this.myAddress = this.address
                this.myPhone = this.phone
                res.save().then(
                  this.$store.commit('setUserInfo', this.addressee, this.address, this.phone)
                )
              })
            }
          })
        } else {
          alert('请填入完整信息！')
        }
      }
    },
    computed: {
      getUserInfo(){
        const query = Bmob.Query('UserInfo')
        query.equalTo("user", "==", this.$store.getters.getUserId);
        query.find().then(res => {
          if (res.length) {
            this.myAddressee = res[0].addressee
            this.myAddress = res[0].address
            this.myPhone = res[0].phone
            this.$store.commit('setUserInfo', res[0].addressee, res[0].address, res[0].phone)
          }
        });
        if (this.myAddressee) {
          return true
        } else {
          return false
        }
      }
    }
  }
</script>
