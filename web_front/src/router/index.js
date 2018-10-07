import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/E-main'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'E-main',
      component: HelloWorld
    }
  ]
})
