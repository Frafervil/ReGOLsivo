<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Editar pronóstico</h2>
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

                       <div class="rows">
                            <div class="col text-left">
                            <b-button v-if="form.usuario == usuario" :disabled="partido.dia < diaActual || (partido.dia == diaActual && partido.hora < horaActual)" type="submit" variant="primary">Editar</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'PronosticadorUsuario'}">Cancelar</b-button>
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
            pronosticoId: this.$route.params.pronosticoId,
            form: {
                resultado: '',
                acertado: '',
                usuario: '',
                partido: ''
            },
            partido: {
                nombreLocal: '',
                nombreVisitante: '',
                resultado: '',
                dia: '',
                hora: '',
                pronosticoSistema: '',
                premio: '',
                dificultad: ''
            },
            errors: [],
            usuario: this.getUsuarioId(),
            diaActual: this.getDiaActual(),
            horaActual: this.getHoraActual()
        }
    },
    methods: {

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

            const path = `http://localhost:8000/api/v1.0/pronosticos/${this.pronosticoId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.resultado = response.data.resultado
                this.form.acertado = response.data.acertado
                this.form.usuario = response.data.usuario
                this.form.partido = response.data.partido

                swal({
                    title: "¡Pronóstico actualizado con éxito!",
                    icon: "success",
                    }).then(function() {
                    window.location = "/pronosticadorUsuario";
                    });
            })
            .catch((error) => {
                this.errors = [];
                if(this.form.resultado == ''){
                    this.errors.push('El resultado es obligatorio');
                }
                console.log(error)
                swal("¡El pronóstico no ha sido actualizado!", "", "error")
            })

        },

        getPartido(){
            const partidoId = this.form.partido

            const path = `http://localhost:8000/api/v1.0/partidos/${partidoId}/`

            axios.get(path).then((response) =>{

                this.partido.nombreLocal = response.data.nombreLocal
                this.partido.nombreVisitante = response.data.nombreVisitante
                this.partido.resultado = response.data.resultado
                this.partido.dia = response.data.dia
                this.partido.hora = response.data.hora
                this.partido.pronosticoSistema = response.data.pronosticoSistema
                this.partido.premio = response.data.premio
                this.partido.dificultad = response.data.dificultad

            })
            .catch((error) => {
                console.log(error)
                swal("¡Fallo al obtener partido!", "", "error")
            })
        },

        getPronostico (){
            const path = `http://localhost:8000/api/v1.0/pronosticos/${this.pronosticoId}/`

            axios.get(path).then((response) =>{

                this.form.resultado = response.data.resultado
                this.form.acertado = response.data.acertado
                this.form.usuario = response.data.usuario
                this.form.partido = response.data.partido

            }).then(() => {
                this.getPartido()
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getPronostico()
    }
}
</script>>