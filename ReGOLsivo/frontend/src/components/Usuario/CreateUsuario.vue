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
                            <label for="nombre" class="col-sm-2 col-form-label">Nombre</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Nombre" name="nombre" class="form-control" v-model.trim="form.nombre">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="apellidos" class="col-sm-2 col-form-label">Apellidos</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Apellidos" name="apellidos" class="form-control" v-model.trim="form.apellidos">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="email" class="col-sm-2 col-form-label">Email</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Email" name="email" class="form-control" v-model.trim="form.email">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="cuentaDeUsuario" class="col-sm-2 col-form-label">Cuenta de usuario</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Cuenta de usuario" name="cuentaDeUsuario" class="form-control" v-model.trim="form.cuentaDeUsuario">
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
    data() {
        return {
            form: {
                nombre: '',
                apellidos: '',
                email: '',
                cuentaDeUsuario: ''
            }
        }
    },
    methods: {
        onSubmit(evt){
            evt.preventDefault()

            const path = 'http://localhost:8000/api/v1.0/usuarios/'

            axios.post(path, this.form).then((response) =>{

                this.form.nombre = response.data.nombre
                this.form.apellidos = response.data.apellidos
                this.form.email = response.data.email
                this.form.cuentaDeUsuario = response.data.cuentaDeUsuario

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