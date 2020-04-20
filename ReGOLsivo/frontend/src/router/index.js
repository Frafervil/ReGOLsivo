import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListUsuario from '@/components/Usuario/ListUsuario'
import CreateUsuario from '@/components/Usuario/CreateUsuario'
import EditUsuario from '@/components/Usuario/EditUsuario'
import DeleteUsuario from '@/components/Usuario/DeleteUsuario'
import RegistrarUsuario from '@/components/Usuario/RegistrarUsuario'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/registroUsuario',
      name: 'RegistrarUsuario',
      component: RegistrarUsuario
    },
    {
      path: '/usuarios',
      name: 'ListUsuario',
      component: ListUsuario
    },
    {
      path: '/usuarios/create',
      name: 'CreateUsuario',
      component: CreateUsuario
    },
    {
      path: '/usuarios/:usuarioId/edit',
      name: 'EditUsuario',
      component: EditUsuario
    },
    {
      path: '/usuarios/:usuarioId/delete',
      name: 'DeleteUsuario',
      component: DeleteUsuario
    }
  ],
  mode: 'history'
})
