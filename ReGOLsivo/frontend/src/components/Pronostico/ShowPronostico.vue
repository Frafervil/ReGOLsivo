<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Pulsa el botón azul para comprobar el pronóstico</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                       <form @submit="onSubmit">
                       <div class="rows">
                            <div class="col text-left">
                            <b-button @click="comprobarPronostico" type="submit" variant="primary">Comprobar</b-button>
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
            partidoId: this.$route.params.partidoId,
            form: {
                resultado: '',
                acertado: '',
                usuario: '',
                partido: ''
            },
            errors: [],
            usuarioId: this.getUsuarioId(),
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
            usuario: {
                username: '',
                password: '',
                email: '',
                first_name: '',
                last_name: '',
                karma: ''
            },
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

        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/pronosticos/${this.pronosticoId}/`

            axios.put(path, this.form);

                swal({
                    title: "¡Pronóstico comprobado con éxito!",
                    icon: "success",
                    }).then(function() {
                    window.location = "/pronosticadorUsuario";
                })
                
            .catch((error) => {
                console.log(error)
                swal("¡El pronóstico no existe!", "", "error")
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
            })
        },

        comprobarPronostico(){
            if(this.form.resultado == this.partido.resultado && this.form.acertado == false){
                this.usuario.karma = parseInt(this.usuario.karma) + parseInt(this.partido.premio);
                this.sumarKarma();
                this.form.acertado = true;
                this.acertarPronostico();
            }
        },

        sumarKarma(){
            const path = `http://localhost:8000/api/v1.0/usuarios/${this.usuarioId}/`

            axios.put(path, this.usuario)

            .catch((error) => {
                console.log(error)
                swal("¡Fallo al sumar karma!", "", "error")
            })
        },

        acertarPronostico(){
            const path = `http://localhost:8000/api/v1.0/pronosticos/${this.pronosticoId}/`

            axios.put(path, this.form)

            .catch((error) => {
                console.log(error)
                swal("¡Fallo al acertar pronóstico!", "", "error")
            })
        },

        getPronostico(){
            const path = `http://localhost:8000/api/v1.0/pronosticos/${this.pronosticoId}/`

            axios.get(path).then((response) =>{

                this.form.resultado = response.data.resultado
                this.form.acertado = response.data.acertado
                this.form.usuario = response.data.usuario
                this.form.partido = response.data.partido

            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getPronostico(),
        this.getPartido(),
        this.getUsuario()
    }
}
</script>>

<style lang="css" scoped>
</style>