import Vue from 'vue'
import Router from 'vue-router'
import LandingPage from '@/components/LandingPage'
import LandingUsuario from '@/components/LandingUsuario'
import Auth from '@/components/Auth'

import ListUsuario from '@/components/Usuario/ListUsuario'
import CreateUsuario from '@/components/Usuario/CreateUsuario'
import PerfilUsuario from '@/components/Usuario/PerfilUsuario'
import DeleteUsuario from '@/components/Usuario/DeleteUsuario'
import Clasificacion from '@/components/Usuario/Clasificacion'

import ListAdministrador from '@/components/Administrador/ListAdministrador'
import PerfilAdministrador from '@/components/Administrador/PerfilAdministrador'
import DeleteAdministrador from '@/components/Administrador/DeleteAdministrador'
import CreateAdministrador from '@/components/Administrador/CreateAdministrador'

import ListPartido from '@/components/Partido/ListPartido'
import EditPartido from '@/components/Partido/EditPartido'
import DeletePartido from '@/components/Partido/DeletePartido'
import CreatePartido from '@/components/Partido/CreatePartido'
import ShowPartido from '@/components/Partido/ShowPartido'
import Pronosticador from '@/components/Partido/Pronosticador'
import PronosticadorUsuario from '@/components/Partido/PronosticadorUsuario'
import Resultados from '@/components/Partido/Resultados'

import ListPronostico from '@/components/Pronostico/ListPronostico'
import EditPronostico from '@/components/Pronostico/EditPronostico'
import DeletePronostico from '@/components/Pronostico/DeletePronostico'
import CreatePronostico from '@/components/Pronostico/CreatePronostico'

import ListComentario from '@/components/Comentario/ListComentario'
import EditComentario from '@/components/Comentario/EditComentario'
import DeleteComentario from '@/components/Comentario/DeleteComentario'

import EditConfiguracion from '@/components/Configuracion/EditConfiguracion'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'LandingPage',
      component: LandingPage
    },
    {
      path: '/landingUsuario',
      name: 'LandingUsuario',
      component: LandingUsuario
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
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
      name: 'PerfilUsuario',
      component: PerfilUsuario
    },
    {
      path: '/usuarios/:usuarioId/delete',
      name: 'DeleteUsuario',
      component: DeleteUsuario
    },
    {
      path: '/clasificacion',
      name: 'Clasificacion',
      component: Clasificacion
    },
    {
      path: '/administradores',
      name: 'ListAdministrador',
      component: ListAdministrador
    },
    {
      path: '/administradores/:administradorId/edit',
      name: 'PerfilAdministrador',
      component: PerfilAdministrador
    },
    {
      path: '/administradores/:administradorId/delete',
      name: 'DeleteAdministrador',
      component: DeleteAdministrador
    },
    {
      path: '/administradores/create',
      name: 'CreateAdministrador',
      component: CreateAdministrador
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
      path: '/partidos/:partidoId/delete',
      name: 'DeletePartido',
      component: DeletePartido
    },
    {
      path: '/partidos/create',
      name: 'CreatePartido',
      component: CreatePartido
    },
    {
      path: '/partidos/:partidoId/show',
      name: 'ShowPartido',
      component: ShowPartido
    },
    {
      path: '/pronosticador',
      name: 'Pronosticador',
      component: Pronosticador
    },
    {
      path: '/pronosticadorUsuario',
      name: 'PronosticadorUsuario',
      component: PronosticadorUsuario
    },
    {
      path: '/resultados',
      name: 'Resultados',
      component: Resultados
    },
    {
      path: '/pronosticos',
      name: 'ListPronostico',
      component: ListPronostico
    },
    {
      path: '/pronosticos/:pronosticoId/edit',
      name: 'EditPronostico',
      component: EditPronostico
    },
    {
      path: '/pronosticos/:pronosticoId/delete',
      name: 'DeletePronostico',
      component: DeletePronostico
    },
    {
      path: '/pronosticos/:partidoId/create',
      name: 'CreatePronostico',
      component: CreatePronostico
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
    },
    {
      path: '/comentarios/:comentarioId/delete',
      name: 'DeleteComentario',
      component: DeleteComentario
    },
    {
      path: '/configuraciones/:configuracionId/edit',
      name: 'EditConfiguracion',
      component: EditConfiguracion
    }
  ],
  mode: 'history'
})
