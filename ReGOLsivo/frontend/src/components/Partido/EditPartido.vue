<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Editar partido</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                        <form @submit="onSubmit">

                        <p v-if="errors.length">
                            <b>Por favor, corrija el(los) siguiente(s) error(es):</b>
                            <ul>
                                <li v-for="error in errors">{{ error }}</li>
                            </ul>
                        </p>

                        <div class="form-group row">
                            <label for="nombreLocal" class="col-sm-2 col-form-label">Local</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Local" name="nombreLocal" class="form-control" v-model.trim="form.nombreLocal">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="nombreVisitante" class="col-sm-2 col-form-label">Visitante</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Visitante" name="nombreVisitante" class="form-control" v-model.trim="form.nombreVisitante">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="dia" class="col-sm-2 col-form-label">Día</label>    
                            <div class="col-sm-6">
                             <input type="date" name="dia" class="form-control" v-model.trim="form.dia">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="hora" class="col-sm-2 col-form-label">Hora</label>    
                            <div class="col-sm-6">
                             <input type="time" name="hora" class="form-control" v-model.trim="form.hora">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="resultado" class="col-sm-2 col-form-label">Resultado</label>    
                            <div class="col-sm-6">
                             <input type="radio" id="1" value="1" v-model.trim="form.resultado">
                             <label for="1">1</label>
                             <br>
                             <input type="radio" id="X" value="X" v-model.trim="form.resultado">
                             <label for="X">X</label>
                             <br>
                             <input type="radio" id="2" value="2" v-model.trim="form.resultado">
                             <label for="2">2</label>
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="premio" class="col-sm-2 col-form-label">Premio</label>    
                            <div class="col-sm-6">
                             <input type="number" min="0" placeholder="0" name="premio" class="form-control" v-model.trim="form.premio">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="proporcion_de_puntos_del_equipo_local" class="col-sm-2 col-form-label">Proporción de puntos del equipo local</label>    
                            <div class="col-sm-6">
                             <input type="number" step="any" placeholder="0.614975317" name="proporcion_de_puntos_del_equipo_local" class="form-control" v-model.trim="form.proporcion_de_puntos_del_equipo_local">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="proporcion_de_puntos_del_equipo_visitante" class="col-sm-2 col-form-label">Proporción de puntos del equipo visitante</label>    
                            <div class="col-sm-6">
                             <input type="number" step="any" placeholder="0.614975317" name="proporcion_de_puntos_del_equipo_visitante" class="form-control" v-model.trim="form.proporcion_de_puntos_del_equipo_visitante">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="goles_por_partido_del_equipo_local" class="col-sm-2 col-form-label">Proporción de goles por partido del equipo local</label>    
                            <div class="col-sm-6">
                             <input type="number" step="any" placeholder="0.614975317" name="goles_por_partido_del_equipo_local" class="form-control" v-model.trim="form.goles_por_partido_del_equipo_local">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="goles_por_partido_del_equipo_visitante" class="col-sm-2 col-form-label">Proporción de goles por partido del equipo visitante</label>    
                            <div class="col-sm-6">
                             <input type="number" step="any" placeholder="0.614975317" name="goles_por_partido_del_equipo_visitante" class="form-control" v-model.trim="form.goles_por_partido_del_equipo_visitante">
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Editar</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'Pronosticador'}">Cancelar</b-button>
                            </div>
                        </div>

                       </form>  


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

export default {

    mounted() {
        this.checkLoggedIn();
    },

    data() {
        return {
            partidoId: this.$route.params.partidoId,
            form: {
                nombreLocal: '',
                nombreVisitante: '',
                resultado: '',
                dia: '',
                hora: '',
                premio: '',
                dificultad: '',
                proporcion_de_puntos_del_equipo_local: '',
                proporcion_de_puntos_del_equipo_visitante: '',
                goles_por_partido_del_equipo_local: '',
                goles_por_partido_del_equipo_visitante: ''
            },
            errors: []
        }
    },
    methods: {

        checkLoggedIn() {
         this.$session.start();
        if (!this.$session.has("token")) {
            router.push("/auth");
            }
        },

        obtenerDificultad(){
            if(this.form.premio < 50)
                this.form.dificultad = 'Fácil'
            else if(this.form.premio >= 50 && this.form.premio < 100)
                this.form.dificultad = 'Intermedia' 
            else if(this.form.premio >= 100)
                this.form.dificultad = 'Difícil'   
        },

        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.nombreLocal = response.data.nombreLocal
                this.form.nombreVisitante = response.data.nombreVisitante
                this.form.dia = response.data.dia
                this.form.hora = response.data.hora
                this.form.resultado = response.data.resultado
                this.form.premio = response.data.premio
                this.form.dificultad = response.data.dificultad
                this.form.proporcion_de_puntos_del_equipo_local = response.data.proporcion_de_puntos_del_equipo_local
                this.form.proporcion_de_puntos_del_equipo_visitante = response.data.proporcion_de_puntos_del_equipo_visitante
                this.form.goles_por_partido_del_equipo_local = response.data.goles_por_partido_del_equipo_local
                this.form.goles_por_partido_del_equipo_visitante = response.data.goles_por_partido_del_equipo_visitante

                swal({
                    title: "¡Partido actualizado con éxito!",
                    icon: "success",
                    button: "Ok"}).then(function() {
                    window.location = "/pronosticador";
                    });
            },this.obtenerDificultad())
            .catch((error) => {
                this.errors = [];
                if(this.form.nombreLocal == ''){
                    this.errors.push('El nombre del equipo local es obligatorio');
                }
                if(this.form.nombreVisitante == ''){
                    this.errors.push('El nombre del equipo visitante es obligatorio');
                }
                if(this.form.dia == ''){
                    this.errors.push('El día es obligatorio');
                }
                if(this.form.hora == ''){
                    this.errors.push('La hora es obligatoria');
                }
                if(this.form.resultado == ''){
                    this.errors.push('El resultado es obligatorio');
                }
                if(this.form.premio == ''){
                    this.errors.push('El premio es obligatorio');
                }
                if(this.form.proporcion_de_puntos_del_equipo_local == ''){
                    this.errors.push('La proporción de puntos del equipo local es obligatoria');
                }
                if(this.form.proporcion_de_puntos_del_equipo_visitante == ''){
                    this.errors.push('La proporción de puntos del equipo visitante es obligatoria');
                }
                if(this.form.goles_por_partido_del_equipo_local == ''){
                    this.errors.push('La proporción de goles por partido del equipo local es obligatoria');
                }
                if(this.form.goles_por_partido_del_equipo_visitante == ''){
                    this.errors.push('La proporción de goles por partido del equipo visitante es obligatoria');
                }
                console.log(error)
                swal("¡El partido no ha sido editado!", "", "error")
            })

        },

        getPartido (){
            const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

            axios.get(path).then((response) =>{

                this.form.nombreLocal = response.data.nombreLocal
                this.form.nombreVisitante = response.data.nombreVisitante
                this.form.dia = response.data.dia
                this.form.hora = response.data.hora
                this.form.resultado = response.data.resultado
                this.form.pronosticoSistema = response.data.pronosticoSistema
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
        }
    },
    created() {
        this.getPartido()
    }
}
</script>>