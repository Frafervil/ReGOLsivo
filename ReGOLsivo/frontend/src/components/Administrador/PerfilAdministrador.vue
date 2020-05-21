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

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Guardar cambios</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'ListAdministrador'}">Cancelar</b-button>
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
            administradorId: this.$route.params.administradorId,
            form: {
                nombre: '',
                apellidos: '',
                email: '',
                nombreDeUsuario: '',
                password: ''
            }
        }
    },
    methods: {
        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/administradores/${this.administradorId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.nombre = response.data.nombre
                this.form.apellidos = response.data.apellidos
                this.form.email = response.data.email
                this.form.nombreDeUsuario = response.data.nombreDeUsuario
                this.form.password = response.data.password

                swal("¡Administrador actualizado con éxito!", "", "success")
            })
            .catch((error) => {
                console.log(error)
            })

        },

        getAdministrador (){
            const path = `http://localhost:8000/api/v1.0/administradores/${this.administradorId}/`

            axios.get(path).then((response) =>{

                this.form.nombre = response.data.nombre
                this.form.apellidos = response.data.apellidos
                this.form.email = response.data.email
                this.form.nombreDeUsuario = response.data.nombreDeUsuario
                this.form.password = response.data.password

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

<style lang="css" scoped>
</style>