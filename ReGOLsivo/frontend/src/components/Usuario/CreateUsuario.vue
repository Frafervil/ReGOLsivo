<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Registro de usuario</h2>
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
                            <label for="username" class="col-sm-2 col-form-label">Nombre de usuario</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="jsanchez23" name="username" class="form-control" v-model.trim="form.username">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="password" class="col-sm-2 col-form-label">Contraseña</label>    
                            <div class="col-sm-6">
                             <input type="password" name="password" class="form-control" v-model.trim="form.password">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="email" class="col-sm-2 col-form-label">Email</label>    
                            <div class="col-sm-6">
                             <input type="email" placeholder="j.s.herrera@gmail.com" name="email" class="form-control" v-model.trim="form.email">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="first_name" class="col-sm-2 col-form-label">Nombre</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Javier" name="first_name" class="form-control" v-model.trim="form.first_name">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="last_name" class="col-sm-2 col-form-label">Apellidos</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Sánchez Herrera" name="last_name" class="form-control" v-model.trim="form.last_name">
                            </div>
                        </div>

                        <div class="form-group form-check">
                            <b-button type="button" class="btn btn-link" variant="link" :to="{ name: 'TerminosYCondiciones'}">Términos y condiciones</b-button>
                            <br>
                            <input type="checkbox" class="form-check-input" id="checkTerminosYCondiciones" @click="validar">
                            <label class="form-check-label" for="checkTerminosYCondiciones">Aceptar</label>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                                <b-button :disabled="!valid" type="submit" variant="primary">Registrarse</b-button>
                                <b-button type="submit" class="btn-large-space" :to="{ name: 'LandingPage'}">Cancelar</b-button>
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

export default {

    data() {
        return {
            form: {
                username: '',
                password: '',
                email: '',
                first_name: '',
                last_name: ''
            },
            errors: [],
            valid: false
        }
    },
    methods: {

        validar(){
            if(this.valid == false){
                this.valid = true;
            } else {
                this.valid = false;
            }
        },

        onSubmit(evt){

            evt.preventDefault()

            const path = 'http://localhost:8000/api/v1.0/usuarios/'

            axios.post(path, this.form).then((response) =>{

                this.form.username = response.data.username
                this.form.password = response.data.password
                this.form.email = response.data.email
                this.form.first_name = response.data.first_name
                this.form.last_name = response.data.last_name

                swal({
                    title: "¡Felicidades!",
                    text: "¡Te has registrado correctamente!",
                    icon: "success",
                    button: "¡Vamos!"}).then(function() {
                    window.location = "/bienvenido";
                    });
            })
            .catch((error) => {
                this.errors = [];
                if(this.form.username == ''){
                    this.errors.push('El nombre de usuario es obligatorio');
                }
                if(this.form.username.length <= 3){
                    this.errors.push('El nombre de usuario debe tener más de 3 caracteres de longitud');
                }
                if(this.form.password == ''){
                    this.errors.push('La contraseña es obligatoria');
                }
                if(this.form.password.length <= 7){
                    this.errors.push('La contraseña debe tener más de 7 caracteres de longitud');
                }
                if(this.form.email == ''){
                    this.errors.push('El email es obligatorio');
                }
                if(this.form.first_name == ''){
                    this.errors.push('El nombre es obligatorio');
                }
                if(this.form.last_name == ''){
                    this.errors.push('Los apellidos son obligatorios');
                }
                swal("¡No te has registrado correctamente!", "", "error")
            })

        },
    },
    created() {
    }
}
</script>>

<style lang="css" scoped>
</style>