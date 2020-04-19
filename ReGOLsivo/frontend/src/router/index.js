import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListUsuario from '@/components/Aplicacion/ListUsuario'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/usuarios',
      name: 'ListUsuario',
      component: ListUsuario
    }
  ],
  mode: 'history'
})
