<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>¿Dar "me gusta"?</h2>
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
                            <b-button type="submit" variant="primary">Si</b-button>
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
            comentarioId: this.$route.params.comentarioId,
            form: {
                meGustas: ''
            },
            configuracion: {
                valorComentariosPositivos: '',
                premioComentariosPositivos: ''
            },
            usuarioId: this.getUsuarioId(),
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

            const path = `http://localhost:8000/api/v1.0/comentarios/${this.comentarioId}/`

            axios.get(path).then((response) =>{

                this.form.meGustas = this.form.meGustas + 1

            }).then(() => {
                 axios.put(path, this.form).then((response) =>{

                this.form.meGustas = this.form.meGustas + 1

                swal({
                    title: "¡Gracias por apoyar el comentario!",
                    icon: "success",
                    button: "Continuar"}).then(function() {
                    window.location = "/pronosticadorUsuario";
                    });
                })
            }, this.esPositivo())
            .catch((error) => {
                console.log(error)
            })

        },

        esPositivo(){
            if(this.form.meGustas == this.configuracion.valorComentariosPositivos - 1){
                this.usuario.karma = parseInt(this.usuario.karma) + parseInt(this.configuracion.premioComentariosPositivos);
                this.sumarKarma();
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

        getConfiguracion (){
            const path = `http://localhost:8000/api/v1.0/configuraciones/1/`

            axios.get(path).then((response) =>{

                this.configuracion.valorComentariosPositivos = response.data.valorComentariosPositivos
                this.configuracion.premioComentariosPositivos = response.data.premioComentariosPositivos

            })
            .catch((error) => {
                console.log(error)
            })
        },

        getComentario(){
            const path = `http://localhost:8000/api/v1.0/comentarios/${this.comentarioId}/`

            axios.get(path).then((response) =>{

                this.form.momento = response.data.momento
                this.form.texto = response.data.texto
                this.form.meGustas = response.data.meGustas
                this.form.autor = response.data.autor
                this.form.partido = response.data.partido

            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getComentario(),
        this.getConfiguracion(),
        this.getUsuario()
    }
}
</script>>

<style lang="css" scoped>
</style>