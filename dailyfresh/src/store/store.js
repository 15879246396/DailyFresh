import Vue from 'vue'
import Vuex from 'vuex'

import * as actions from './actions'
import * as getters from './getters'
import * as mutations from './mutations'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    // 设置属性
    isLogin: false,
    username: null,
    userId: null,
    userAddressee: null,
    userPhone: null,
    userAddress: null,
    adminId: null,
    cartCount: 0,
    newLogin: false
  },
  getters,
  mutations,
  actions,
});
