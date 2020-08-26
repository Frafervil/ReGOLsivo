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

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Guardar cambios</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'LandingAdministrador'}">Cancelar</b-button>
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
                last_name: ''
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

        getAdministradorId(){
            var decodedPayload = atob(this.$session.get('token').split('.')[1]);
            var payloadSplittedByComa = decodedPayload.split(',')[0];
            return payloadSplittedByComa.split(':')[1];
        },

        onSubmit(evt){
            evt.preventDefault()

            const administradorId = this.getAdministradorId();

            const path = `http://localhost:8000/api/v1.0/administradores/${administradorId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.email = response.data.email
                this.form.first_name = response.data.first_name
                this.form.last_name = response.data.last_name

                swal({
                    title: "¡Administrador actualizado con éxito!",
                    icon: "success",
                    button: "¡Genial!"}).then(function() {
                    window.location = "/landingAdministrador";
                });
            })
            .catch((error) => {
                console.log(error)
            })

        },

        logout(){
            this.$session.destroy();
            location.href = '/'
        },

        getAdministrador (){

            const administradorId = this.getAdministradorId();

            const path = `http://localhost:8000/api/v1.0/administradores/${administradorId}/`

            axios.get(path).then((response) =>{

                this.form.username = response.data.username
                this.form.password = response.data.password
                this.form.email = response.data.email
                this.form.first_name = response.data.first_name
                this.form.last_name = response.data.last_name

            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getAdministrador()
    }
}
</script>>