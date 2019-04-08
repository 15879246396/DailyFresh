import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import {routes} from './routes'
import VueTitle from 'vue-wechat-title'
import './assets/js/key'
import {store} from './store/store'
import axios from 'axios'
import VueAxios from 'vue-axios'


// 配置Bmob的axios
axios.defaults.headers['Content-Type'] = 'application/x-www-form-urlencoded'
// axios.defaults.headers['X-Bmob-Master-Key'] = 'df418e6d9ef0da9f47c9d80411b3e030'
//   'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
//   // 'X-Bmob-Master-Key': 'df418e6d9ef0da9f47c9d80411b3e030',
// };
axios.defaults.baseURL = 'https://pycloud.bmob.cn/afd05bb58d4d5e42/';

Vue.use(VueRouter);
Vue.use(VueTitle);
Vue.use(VueAxios, axios);

Vue.prototype.Bmob = Bmob;

const router = new VueRouter({
  routes,
  mode: 'history',
  scrollBehavior: function (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return {x: 0, y: 0}
    }
  }
});

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})

store.dispatch('setUser')
router.beforeEach((to, from, next) => {
  store.dispatch('setUser')
  next()
})
