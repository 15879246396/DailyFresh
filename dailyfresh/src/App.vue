<template>
  <div id="app">
    <body>
      <router-view name="header"></router-view>
      <router-view name="search"></router-view>
      <router-view name="nav"></router-view>
      <router-view name="rotationChart"></router-view>

      <router-view v-wechat-title="$route.meta.title"></router-view>

      <app-footer></app-footer>
    </body>
  </div>
</template>

<script>
import Footer from './components/Footer'
import RotationChart from './components/apps/RotationChart'

export default {
  components: {
    appFooter: Footer,
    appRotationChart: RotationChart,
  }
}
</script>

<style>

</style>
