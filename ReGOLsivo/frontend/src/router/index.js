import Vue from 'vue'
import Router from 'vue-router'
import LandingPage from '@/components/LandingPage'

import ListUsuario from '@/components/Usuario/ListUsuario'
import CreateUsuario from '@/components/Usuario/CreateUsuario'
import EditUsuario from '@/components/Usuario/EditUsuario'
import DeleteUsuario from '@/components/Usuario/DeleteUsuario'

import ListAdministrador from '@/components/Administrador/ListAdministrador'
import EditAdministrador from '@/components/Administrador/EditAdministrador'

import ListPartido from '@/components/Partido/ListPartido'
import EditPartido from '@/components/Partido/EditPartido'

import ListPronostico from '@/components/Pronostico/ListPronostico'

import ListComentario from '@/components/Comentario/ListComentario'
import EditComentario from '@/components/Comentario/EditComentario'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'LandingPage',
      component: LandingPage
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
    },
    {
      path: '/administradores',
      name: 'ListAdministrador',
      component: ListAdministrador
    },
    {
      path: '/administradores/:administradorId/edit',
      name: 'EditAdministrador',
      component: EditAdministrador
    },
    {
      path: '/partidos',
      name: 'ListPartido',
      component: ListPartido
    },
    {
      path: '/partidos/:partidoId/edit',
      name: 'EditPartido',
      component: EditPartido
    },
    {
      path: '/pronosticos',
      name: 'ListPronostico',
      component: ListPronostico
    },
    {
      path: '/comentarios',
      name: 'ListComentario',
      component: ListComentario
    },
    {
      path: '/comentarios/:comentarioId/edit',
      name: 'EditComentario',
      component: EditComentario
    }
  ],
  mode: 'history'
})
