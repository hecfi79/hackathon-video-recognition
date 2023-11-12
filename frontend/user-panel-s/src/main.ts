/* eslint-disable vue/multi-word-component-names */
import Vue from 'vue'
import App from './app/App.vue'
import Router from 'vue-router'
import initRoutes from '@/app/app.routes'
import VueApexCharts from 'vue-apexcharts'

Vue.use(VueApexCharts)

Vue.component('apexchart', VueApexCharts)

Vue.use(Router)

export const router = new Router({
  linkActiveClass: 'is-active',
  routes: initRoutes,
  scrollBehavior: () => ({ x: 0, y: 0 })
})

Vue.config.productionTip = false
Vue.prototype.$eventBus = new Vue()

const app = new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app')

export default app
export { app }
