<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Perfil</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                        <form @submit="onSubmit">

                        <div class="form-group row">
                            <label for="username" class="col-sm-2 col-form-label">Nombre de usuario</label>    
                            <div class="col-sm-6">
                             <input type="text" name="username" class="form-control" readonly v-model.trim="form.username">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="first_name" class="col-sm-2 col-form-label">Nombre</label>    
                            <div class="col-sm-6">
                             <input type="text" name="first_name" class="form-control" v-model.trim="form.first_name">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="last_name" class="col-sm-2 col-form-label">Apellidos</label>    
                            <div class="col-sm-6">
                             <input type="text" name="last_name" class="form-control" v-model.trim="form.last_name">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="email" class="col-sm-2 col-form-label">Email</label>    
                            <div class="col-sm-6">
                             <input type="email" name="email" class="form-control" v-model.trim="form.email">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="karma" class="col-sm-2 col-form-label">Karma</label>    
                            <div class="col-sm-6">
                             <input type="number" name="karma" class="form-control" readonly v-model.trim="form.karma">
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Guardar cambios</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'LandingUsuario'}">Cancelar</b-button>
                            <b-button v-on:click="logout" variant="danger">Cerrar sesión</b-button>
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
            form: {
                username: '',
                password: '',
                email: '',
                first_name: '',
                last_name: '',
                karma: ''
            }
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

            const usuarioId = this.getUsuarioId();

            const path = `http://localhost:8000/api/v1.0/usuarios/${usuarioId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.email = response.data.email
                this.form.first_name = response.data.first_name
                this.form.last_name = response.data.last_name

                swal({
                    title: "¡Usuario actualizado con éxito!",
                    icon: "success",
                    button: "¡Genial!"}).then(function() {
                    window.location = "/landingUsuario";
                    });
            })
            .catch((error) => {
                console.log(error)
            })

        },

        logout(){
            this.$session.destroy();
            router.push("/");
        },

        getUsuario (){
            const usuarioId = this.getUsuarioId();

            const path = `http://localhost:8000/api/v1.0/usuarios/${usuarioId}/`

            axios.get(path).then((response) =>{

                this.form.username = response.data.username
                this.form.password = response.data.password
                this.form.email = response.data.email
                this.form.first_name = response.data.first_name
                this.form.last_name = response.data.last_name
                this.form.karma = response.data.karma

            })
            .catch((error) => {
                console.log(error)
            })
        }
    },

    created() {
        this.getUsuario()
    }
}
</script>>