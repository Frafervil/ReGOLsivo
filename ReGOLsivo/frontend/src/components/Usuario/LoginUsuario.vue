<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Iniciar sesión</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                        <form @submit="onSubmit">

                        <div class="form-group row">
                            <label for="NombreDeUsuario" class="col-sm-2 col-form-label">Nombre de usuario</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Nombre de usuario" name="Nombre de usuario" class="form-control" v-model.trim="form.NombreDeUsuario">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="Contraseña" class="col-sm-2 col-form-label">Contraseña</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Contraseña" name="Contraseña" class="form-control" v-model.trim="form.Contraseña">
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
            usuarioId: this.$route.params.usuarioId,
            form: {
                Nombre: '',
                Apellidos: '',
                Email: ''
            }
        }
    },
    methods: {
        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/usuarios/${this.usuarioId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.Nombre = response.data.Nombre
                this.form.Apellidos = response.data.Apellidos
                this.form.Email = response.data.Email

                swal("¡Usuario actualizado con éxito!", "", "success")
            })
            .catch((error) => {
                console.log(error)
            })

        },

        getUsuario (){
            const path = `http://localhost:8000/api/v1.0/usuarios/${this.usuarioId}/`

            axios.get(path).then((response) =>{

                this.form.Nombre = response.data.Nombre
                this.form.Apellidos = response.data.Apellidos
                this.form.Email = response.data.Email

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

<style lang="css" scoped>
</style>