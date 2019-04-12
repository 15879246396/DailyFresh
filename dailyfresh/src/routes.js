import Home from './components/Home'
import Login from './components/Login'
import Register from './components/Register'
import UserCenter from './components/UserCenter'
import Cart from './components/Cart'
import CMS from './components/cms/CMS'
import CMSLogin from './components/cms/CMSLogin'
import Detail from './components/Detail'
import PlaceOrder from './components/PlaceOrder'
import List from './components/List'

import Header from './components/Header'
import Search from './components/apps/SearchBar'
import Nav from './components/apps/NavBar'
import RotationChart from './components/apps/RotationChart'
import UserInfo from './components/usercenter/UserInfo'
import Order from './components/usercenter/Order'
import DeliveryAddress from './components/usercenter/DeliveryAddress'

import {store} from './store/store'


export const routes = [
  {path: '/', name: 'homeLink', components: {
    default: Home,
    'header': Header,
    'search': Search,
    'nav': Nav,
    'rotationChart': RotationChart,
    }, meta: {
      title: '天天生鲜-首页'
    },
  },
  {path: '/login', name: 'loginLink', component: Login, meta: {title: '登录-天天生鲜'}},
  {path: '/register', name: 'registerLink', component: Register, meta: {title: '注册-天天生鲜'}},
  {path: '/user_center', name: 'userCenterLink', redirect: '/user_info', meta: {title: '用户中心-天天生鲜'},
    components: {
      default: UserCenter,
      'header': Header,
      'search': Search,
    },
    children: [
      {path: '/user_info', name: 'userInfoLink', component: UserInfo, meta: {title: '用户中心-天天生鲜'}},
      {path: '/user_order', name: 'orderLink', component: Order, meta: {title: '用户中心-天天生鲜'}},
      {path: '/address', name: 'addressLink', component: DeliveryAddress, meta: {title: '用户中心-天天生鲜'}},
    ]},
  {path: '/cart', name: 'cartLink', components: {
      default: Cart,
      'header': Header,
      'search': Search,
    }, meta: {
      title: '购物车-天天生鲜'
    }},
  {path: '/cms', name: 'cmsLink', component: CMS, meta: {title: 'cms-天天生鲜'},},
  {path: '/cms_login', name: 'cmsLoginLink', component: CMSLogin, meta: {title: 'cms登录-天天生鲜'}},
  {path: '/detail', name: 'detailLink', meta: {title: '商品详情-天天生鲜'},
    components: {
      default: Detail,
      'header': Header,
      'search': Search,
      'nav': Nav,
    }},
  {path: '/place_order', name: 'placeOrderLink', meta: {title: '提交订单-天天生鲜'},
    components: {
      default: PlaceOrder,
      'header': Header,
      'search': Search,
    }},
  {path: '/list', name: 'listLink', meta: {title: '商品列表-天天生鲜'},
    components: {
      default: List,
      'header': Header,
      'search': Search,
      'nav': Nav,
    }
  },
];
