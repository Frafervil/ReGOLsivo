<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Editar configuración</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                        <form @submit="onSubmit">

                        <div class="form-group row">
                            <label for="mensajeBienvenida" class="col-sm-2 col-form-label">Mensaje de bienvenida</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Mensaje de bienvenida" name="mensajeBienvenida" class="form-control" v-model.trim="form.mensajeBienvenida">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="linkLogo" class="col-sm-2 col-form-label">Enlace del logo</label>    
                            <div class="col-sm-6">
                             <input type="url" placeholder="Enlace del logo" name="linkLogo" class="form-control" v-model.trim="form.linkLogo">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="valorComentariosPositivos" class="col-sm-2 col-form-label">Valor de los comentarios positivos</label>    
                            <div class="col-sm-6">
                             <input type="number" min="0" placeholder="0" name="valorComentariosPositivos" class="form-control" v-model.trim="form.valorComentariosPositivos">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="premioComentariosPositivos" class="col-sm-2 col-form-label">Premio de los comentarios positivos</label>    
                            <div class="col-sm-6">
                             <input type="number" min="0" placeholder="0" name="premioComentariosPositivos" class="form-control" v-model.trim="form.premioComentariosPositivos">
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Editar</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'ListConfiguracion'}">Cancelar</b-button>
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
            configuracionId: this.$route.params.configuracionId,
            form: {
                mensajeBienvenida: '',
                linkLogo: '',
                valorComentariosPositivos: '',
                premioComentariosPositivos: ''
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

            const path = `http://localhost:8000/api/v1.0/configuraciones/${this.configuracionId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.mensajeBienvenida = response.data.mensajeBienvenida
                this.form.linkLogo = response.data.linkLogo
                this.form.valorComentariosPositivos = response.data.valorComentariosPositivos
                this.form.premioComentariosPositivos = response.data.premioComentariosPositivos

                swal("¡Configuración actualizado con éxito!", "", "success")
            })
            .catch((error) => {
                console.log(error)
            })

        },

        getConfiguracion (){
            const path = `http://localhost:8000/api/v1.0/configuraciones/${this.configuracionId}/`

            axios.get(path).then((response) =>{

                this.form.mensajeBienvenida = response.data.mensajeBienvenida
                this.form.linkLogo = response.data.linkLogo
                this.form.valorComentariosPositivos = response.data.valorComentariosPositivos
                this.form.premioComentariosPositivos = response.data.premioComentariosPositivos

            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getConfiguracion()
    }
}
</script>>

<style lang="css" scoped>
</style>