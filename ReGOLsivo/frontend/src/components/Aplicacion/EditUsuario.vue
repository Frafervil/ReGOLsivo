<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Editar usuario</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                        <form @submit="onSubmit">

                        <div class="form-group row">
                            <label for="Nombre" class="col-sm-2 col-form-label">Nombre</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Nombre" name="Nombre" class="form-control" v-model.trim="form.Nombre">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="Apellidos" class="col-sm-2 col-form-label">Apellidos</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Apellidos" name="Apellido" class="form-control" v-model.trim="form.Apellidos">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="Email" class="col-sm-2 col-form-label">Email</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Email" name="Email" class="form-control" v-model.trim="form.Email">
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Editar</b-button>
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