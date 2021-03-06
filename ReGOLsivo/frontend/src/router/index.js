import Vue from 'vue'
import Router from 'vue-router'
import LandingPage from '@/components/LandingPage'
import LandingUsuario from '@/components/LandingUsuario'
import LandingAdministrador from '@/components/LandingAdministrador'
import Auth from '@/components/Auth'
import Bienvenido from '@/components/Bienvenido'
import TerminosYCondiciones from '@/components/TerminosYCondiciones'
import TerminosYCondicionesUsuario from '@/components/TerminosYCondicionesUsuario'

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
import ShowPartidoAdministrador from '@/components/Partido/ShowPartidoAdministrador'
import Pronosticador from '@/components/Partido/Pronosticador'
import PronosticadorUsuario from '@/components/Partido/PronosticadorUsuario'
import Resultados from '@/components/Partido/Resultados'

import EditPronostico from '@/components/Pronostico/EditPronostico'
import DeletePronostico from '@/components/Pronostico/DeletePronostico'
import CreatePronostico from '@/components/Pronostico/CreatePronostico'
import ShowPronostico from '@/components/Pronostico/ShowPronostico'

import EditComentario from '@/components/Comentario/EditComentario'
import DeleteComentario from '@/components/Comentario/DeleteComentario'
import DeleteComentarioAdministrador from '@/components/Comentario/DeleteComentarioAdministrador'
import CreateComentario from '@/components/Comentario/CreateComentario'
import CreateComentarioRespuesta from '@/components/Comentario/CreateComentarioRespuesta'
import DarMeGusta from '@/components/Comentario/DarMeGusta'

import EditConfiguracion from '@/components/Configuracion/EditConfiguracion'

import ListLogro from '@/components/Logro/ListLogro'

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
      path: '/landingAdministrador',
      name: 'LandingAdministrador',
      component: LandingAdministrador
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/bienvenido',
      name: 'Bienvenido',
      component: Bienvenido
    },
    {
      path: '/terminosYCondiciones',
      name: 'TerminosYCondiciones',
      component: TerminosYCondiciones
    },
    {
      path: '/terminosYCondicionesUsuario',
      name: 'TerminosYCondicionesUsuario',
      component: TerminosYCondicionesUsuario
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
      path: '/usuarios/edit',
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
      path: '/partidos/:partidoId/showPartidoAdministrador',
      name: 'ShowPartidoAdministrador',
      component: ShowPartidoAdministrador
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
      path: '/pronosticos/:pronosticoId/:partidoId/show',
      name: 'ShowPronostico',
      component: ShowPronostico
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
      path: '/comentarios/:comentarioId/delete',
      name: 'DeleteComentarioAdministrador',
      component: DeleteComentarioAdministrador
    },
    {
      path: '/comentarios/create',
      name: 'CreateComentario',
      component: CreateComentario
    },
    {
      path: '/comentarios/:partidoId/:comentarioId/createComentarioRespuesta',
      name: 'CreateComentarioRespuesta',
      component: CreateComentarioRespuesta
    },
    {
      path: '/comentarios/:comentarioId/darMeGusta',
      name: 'DarMeGusta',
      component: DarMeGusta
    },
    {
      path: '/configuraciones/:configuracionId/edit',
      name: 'EditConfiguracion',
      component: EditConfiguracion
    },
    {
      path: '/logros',
      name: 'ListLogro',
      component: ListLogro
    }
  ],
  mode: 'history'
})
