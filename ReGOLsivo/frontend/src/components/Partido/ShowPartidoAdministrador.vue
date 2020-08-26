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
                        <form>

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
                             <input type="number" name="pronosticoSistema" class="form-control" readonly v-model.trim="form.pronosticoSistema">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="probabilidadVictoriaLocal" class="col-sm-2 col-form-label">Probabilidad de victoria del equipo local (%)</label>    
                            <div class="col-sm-6">
                             <input type="number" name="probabilidadVictoriaLocal" class="form-control" readonly v-model.trim="form.probabilidadVictoriaLocal">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="probabilidadEmpate" class="col-sm-2 col-form-label">Probabilidad de empate (%)</label>    
                            <div class="col-sm-6">
                             <input type="number" name="probabilidadEmpate" class="form-control" readonly v-model.trim="form.probabilidadEmpate">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="probabilidadVictoriaVisitante" class="col-sm-2 col-form-label">Probabilidad de victoria del equipo visitante (%)</label>    
                            <div class="col-sm-6">
                             <input type="number" name="probabilidadVictoriaVisitante" class="form-control" readonly v-model.trim="form.probabilidadVictoriaVisitante">
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

                        <div class="form-group row">
                            <label for="proporcion_de_puntos_del_equipo_local" class="col-sm-2 col-form-label">Proporción de puntos del equipo local</label>    
                            <div class="col-sm-6">
                             <input type="number" step="any" placeholder="0.614975317" name="proporcion_de_puntos_del_equipo_local" class="form-control" readonly v-model.trim="form.proporcion_de_puntos_del_equipo_local">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="proporcion_de_puntos_del_equipo_visitante" class="col-sm-2 col-form-label">Proporción de puntos del equipo visitante</label>    
                            <div class="col-sm-6">
                             <input type="number" step="any" placeholder="0.614975317" name="proporcion_de_puntos_del_equipo_visitante" class="form-control" readonly v-model.trim="form.proporcion_de_puntos_del_equipo_visitante">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="goles_por_partido_del_equipo_local" class="col-sm-2 col-form-label">Proporción de goles por partido del equipo local</label>    
                            <div class="col-sm-6">
                             <input type="number" step="any" placeholder="0.614975317" name="goles_por_partido_del_equipo_local" class="form-control" readonly v-model.trim="form.goles_por_partido_del_equipo_local">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="goles_por_partido_del_equipo_visitante" class="col-sm-2 col-form-label">Proporción de goles por partido del equipo visitante</label>    
                            <div class="col-sm-6">
                             <input type="number" step="any" placeholder="0.614975317" name="goles_por_partido_del_equipo_visitante" class="form-control" readonly v-model.trim="form.goles_por_partido_del_equipo_visitante">
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
                                    <b-button size="sm" variant="danger" :to="{ name:'DeleteComentarioAdministrador', params: {comentarioId: data.item.id} }">
                                        Eliminar
                                    </b-button>
                                </template>
                            </b-table>
                        </div>  

                        <div class="rows">
                            <div class="col text-left">   
                            <b-button size="sm" type="submit" class="btn-large-space" :to="{ name: 'Pronosticador'}">Atrás</b-button>
                            </div>
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
                probabilidadVictoriaLocal: '',
                probabilidadEmpate: '',
                probabilidadVictoriaVisitante: '',
                premio: '',
                dificultad: '',
                proporcion_de_puntos_del_equipo_local: '',
                proporcion_de_puntos_del_equipo_visitante: '',
                goles_por_partido_del_equipo_local: '',
                goles_por_partido_del_equipo_visitante: ''
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
            usuarios: []
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

        isOwner(item){
            return item === this.getUsuarioId();
        },

        getPartido (){
            const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

            axios.get(path).then((response) =>{

                this.form.nombreLocal = response.data.nombreLocal
                this.form.nombreVisitante = response.data.nombreVisitante
                this.form.resultado = response.data.resultado
                this.form.dia = response.data.dia
                this.form.hora = response.data.hora
                this.form.pronosticoSistema = response.data.pronosticoSistema
                this.form.probabilidadVictoriaLocal = response.data.probabilidadVictoriaLocal
                this.form.probabilidadEmpate = response.data.probabilidadEmpate
                this.form.probabilidadVictoriaVisitante = response.data.probabilidadVictoriaVisitante
                this.form.premio = response.data.premio
                this.form.dificultad = response.data.dificultad
                this.form.proporcion_de_puntos_del_equipo_local = response.data.proporcion_de_puntos_del_equipo_local
                this.form.proporcion_de_puntos_del_equipo_visitante = response.data.proporcion_de_puntos_del_equipo_visitante
                this.form.goles_por_partido_del_equipo_local = response.data.goles_por_partido_del_equipo_local
                this.form.goles_por_partido_del_equipo_visitante = response.data.goles_por_partido_del_equipo_visitante

            })
            .catch((error) => {
                console.log(error)
            })
        },

    getComentarios (){

      const path = 'http://localhost:8000/api/v1.0/comentarios/'
      axios.get(path).then((response) => {
        this.comentarios = response.data
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

    },

    created() {
        this.getPartido(),
        this.getComentarios(),
        this.getUsuarios()
    }
}
</script>>