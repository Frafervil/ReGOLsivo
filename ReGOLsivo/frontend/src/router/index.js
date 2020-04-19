import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListUsuario from '@/components/Aplicacion/ListUsuario'
import EditUsuario from '@/components/Aplicacion/EditUsuario'

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
    },
    {
      path: '/usuarios/edit',
      name: 'EditUsuario',
      component: EditUsuario
    }
  ],
  mode: 'history'
})
