<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Detalles del partido</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                        <form @submit="onSubmit">

                        <div class="form-group row">
                            <label for="nombreLocal" class="col-sm-2 col-form-label">Local</label>    
                            <div class="col-sm-6">
                             <input type="text" name="nombreLocal" class="form-control" readonly v-model.trim="form.nombreLocal">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="nombreVisitante" class="col-sm-2 col-form-label">Visitante</label>    
                            <div class="col-sm-6">
                             <input type="text" name="nombreVisitante" class="form-control" readonly v-model.trim="form.nombreVisitante">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="resultado" class="col-sm-2 col-form-label">Resultado</label>    
                            <div class="col-sm-6">
                             <input type="text" name="resultado" class="form-control" readonly v-model.trim="form.resultado">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="dia" class="col-sm-2 col-form-label">Día</label>    
                            <div class="col-sm-6">
                             <input type="date" name="dia" class="form-control" readonly v-model.trim="form.dia">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="hora" class="col-sm-2 col-form-label">Hora</label>    
                            <div class="col-sm-6">
                             <input type="time" name="hora" class="form-control" readonly v-model.trim="form.hora">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="pronosticoSistema" class="col-sm-2 col-form-label">Pronóstico del sistema</label>    
                            <div class="col-sm-6">
                             <input type="text" name="pronosticoSistema" class="form-control" readonly v-model.trim="form.pronosticoSistema">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="premio" class="col-sm-2 col-form-label">Premio</label>    
                            <div class="col-sm-6">
                             <input type="number" name="premio" class="form-control" readonly v-model.trim="form.premio">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="dificultad" class="col-sm-2 col-form-label">Dificultad</label>    
                            <div class="col-sm-6">
                             <input type="text" name="dificultad" class="form-control" readonly v-model.trim="form.dificultad">
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button :disabled="form.dia < diaActual || (form.dia == diaActual && form.hora < horaActual) || noEsElUnico" size="sm" variant="info" :to="{ name:'CreatePronostico', params: {partidoId: this.partidoId} }"> <!--  && form.hora < horaActual -->
                            Pronosticar
                            </b-button>    
                            <b-button size="sm" variant="primary" :to="{ name:'CreateComentario', params: {partidoId: this.partidoId}}">
                            Comentar
                            </b-button>
                            <b-button size="sm" type="submit" class="btn-large-space" :to="{ name: 'PronosticadorUsuario'}">Atrás</b-button>
                            </div>
                        </div>

                        </form>
                        <br>
                        <h2>Comentarios</h2>
                        <br>
                        <div class="comentariosDelPartido">
                            <b-table striped hover
                                :items="comentariosDelPartido" 
                                :fields="fields"
                                :sort-by.sync="sortBy" 
                                :sort-desc.sync="sortDesc">
                                <template v-slot:cell(action)="data">
                                    <b-button size="sm" variant="primary" :to="{ name:'CreateComentarioRespuesta', params: {comentarioId: data.item.id} }">
                                        Responder
                                    </b-button>
                                    <b-button size="sm" variant="success" :to="{ name:'DarMeGusta', params: {comentarioId: data.item.id} }">
                                        Me gusta
                                    </b-button>
                                    <b-button v-if="data.item.autor == usuarioId" size="sm" variant="primary" :to="{ name:'EditComentario', params: {comentarioId: data.item.id} }">
                                        Editar
                                    </b-button>
                                    <b-button v-if="data.item.autor == usuarioId" size="sm" variant="danger" :to="{ name:'DeleteComentario', params: {comentarioId: data.item.id} }">
                                        Eliminar
                                    </b-button>
                                </template>
                            </b-table>
                        </div>  


                       </form> 
                    </div>   
                </div>
            </div> 
        </div>       
    </div>  
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'
import router from "../../router";
import { DateTime } from "luxon";

export default {

    mounted() {
        this.checkLoggedIn();
    },

    data() {
        return {
            sortBy: 'momento',
            sortDesc: false,
            partidoId: this.$route.params.partidoId,
            form: {
                nombreLocal: '',
                nombreVisitante: '',
                resultado: '',
                dia: '',
                hora: '',
                pronosticoSistema: '',
                premio: '',
                dificultad: ''
            },
        
            fields: [
                { key: 'id', label: 'Número de comentario' },
                { key: 'momento', formatter: "formatMomento", label: 'Momento', sortable: true},
                { key: 'texto', label: 'Texto' },
                { key: 'meGustas', label: 'Número de "me gustas"', sortable: true},
                { key: 'autor', formatter: "nombreDeUsuario", label: 'Autor' },
                { key: 'comentarioRespuesta', label: 'Responde al comentario:' },
                { key: 'action', label: '' }
            ],
            comentarios: [],
            usuarios: [],
            usuarioId: this.getUsuarioId(),
            diaActual: this.getDiaActual(),
            horaActual: this.getHoraActual(),
            usuario: {
                username: '',
                password: '',
                email: '',
                first_name: '',
                last_name: '',
                karma: ''
            },
            pronosticos: []
        }
    },
    methods: {

        formatMomento(value) {
            const formattedDate = DateTime.fromISO(value).toLocaleString(DateTime.DATETIME_SHORT);
            return formattedDate;
        },

        getUsuarios(){
            const path = 'http://localhost:8000/api/v1.0/usuarios/'

            axios.get(path).then((response) => {

                this.usuarios = response.data

             })
            .catch((error) => {
                console.log(error)
            })
        },

        nombreDeUsuario(usuarioId){

            const usuario = this.usuarios.find(u => u.id === usuarioId);
            return usuario ? `${usuario.username}` : 'Cargando...';

        },

        checkLoggedIn() {
         this.$session.start();
        if (!this.$session.has("token")) {
            router.push("/auth");
            }
        },

        getUsuarioId(){
            var decodedPayload = atob(this.$session.get('token').split('.')[1]);
            var payloadSplittedByComa = decodedPayload.split(',')[0];
            return payloadSplittedByComa.split(':')[1];
        },

        getDiaActual(){
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0');
            var yyyy = today.getFullYear();

            return yyyy + '-' + mm + '-' + dd;
        },

        getHoraActual(){
            var today = new Date();
            return today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

        },

        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

            axios.get(path).then((response) =>{

                this.form.nombreLocal = response.data.nombreLocal
                this.form.nombreVisitante = response.data.nombreVisitante
                this.form.resultado = response.data.resultado
                this.form.dia = response.data.dia
                this.form.hora = response.data.hora
                this.form.pronosticoSistema = response.data.pronosticoSistema
                this.form.premio = response.data.premio
                this.form.dificultad = response.data.dificultad

            })
            .catch((error) => {
                console.log(error)
            })

        },

        getUsuario(){
            const path = `http://localhost:8000/api/v1.0/usuarios/${this.usuarioId}/`

            axios.get(path).then((response) =>{

                this.usuario.username = response.data.username
                this.usuario.password = response.data.password
                this.usuario.email = response.data.email
                this.usuario.first_name = response.data.first_name
                this.usuario.last_name = response.data.last_name
                this.usuario.karma = response.data.karma

            })
            .catch((error) => {
                console.log(error)
                swal("¡Fallo al obtener usuario!", "", "error")
            })
        },

        getPartido(){
            const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

            axios.get(path).then((response) =>{

                this.form.nombreLocal = response.data.nombreLocal
                this.form.nombreVisitante = response.data.nombreVisitante
                this.form.resultado = response.data.resultado
                this.form.dia = response.data.dia
                this.form.hora = response.data.hora
                this.form.pronosticoSistema = response.data.pronosticoSistema
                this.form.premio = response.data.premio
                this.form.dificultad = response.data.dificultad

            })
            .catch((error) => {
                console.log(error)
            })
        },

    getComentarios(){
      const path = 'http://localhost:8000/api/v1.0/comentarios/'

      axios.get(path).then((response) => {
        this.comentarios = response.data
      })
      .catch((error) => {
        console.log(error)
      })
     },

     getPronosticos(){
      const path = 'http://localhost:8000/api/v1.0/pronosticos/'
      
      axios.get(path).then((response) => {
        this.pronosticos = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },

    },

    computed: {
      comentariosDelPartido: function (){
        return this.comentarios.filter((comentario) => comentario.partido == this.partidoId);
      },

      pronosticosDelUsuarioYDelPartido: function (){
        return this.pronosticos.filter((pronostico) => pronostico.usuario == this.usuarioId && pronostico.partido == this.partidoId);
      },

      noEsElUnico: function (){
        if(this.pronosticosDelUsuarioYDelPartido.length == 0){
            return false;
        } else {
            return true;
        }
      }

    },

    created() {
        this.getPartido(),
        this.getComentarios(),
        this.getUsuarios(),
        this.getUsuario(),
        this.getPronosticos()
    }
}
</script>>

<style lang="css" scoped>
</style>