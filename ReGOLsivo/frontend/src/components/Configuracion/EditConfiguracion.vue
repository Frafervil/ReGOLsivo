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
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'LandingAdministrador'}">Cancelar</b-button>
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

            const path = `http://localhost:8000/api/v1.0/configuraciones/1/`

            axios.put(path, this.form).then((response) =>{

                this.form.valorComentariosPositivos = response.data.valorComentariosPositivos
                this.form.premioComentariosPositivos = response.data.premioComentariosPositivos

                swal({
                    title: "¡Configuración actualizada con éxito!",
                    icon: "success",
                    button: "¡Genial!"}).then(function() {
                    window.location = "/landingAdministrador";
                });
            })
            .catch((error) => {
                console.log(error)
            })

        },

        getConfiguracion (){
            const path = `http://localhost:8000/api/v1.0/configuraciones/1/`

            axios.get(path).then((response) =>{

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