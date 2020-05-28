<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Crear usuario</h2>
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

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Crear</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'ListUsuario'}">Cancelar</b-button>
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
                karma: 0
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

        onSubmit(evt){
            evt.preventDefault()

            const path = 'http://localhost:8000/api/v1.0/usuarios/'

            const auth = {
                headers: {Authorization:'JWT ' + this.$session.get('token')} 
            }

            axios.post(path, this.form, auth).then((response) =>{

                this.form.username = response.data.username
                this.form.password = response.data.password
                this.form.email = response.data.email
                this.form.first_name = response.data.first_name
                this.form.last_name = response.data.last_name

                swal("¡Usuario creado con éxito!", "", "success")
            })
            .catch((error) => {
                swal("¡El usuario no ha sido creado!", "", "error")
            })

        },
    },
    created() {
    }
}
</script>>

<style lang="css" scoped>
</style>