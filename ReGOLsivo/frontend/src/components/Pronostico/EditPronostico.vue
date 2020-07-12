<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Editar pronóstico</h2>
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
                            <label for="resultado" class="col-sm-2 col-form-label">Resultado</label>    
                            <div class="col-sm-6">
                             <input type="radio" id="1" value="1" v-model.trim="form.resultado">
                             <label for="1">1</label>
                             <br>
                             <input type="radio" id="X" value="X" v-model.trim="form.resultado">
                             <label for="X">X</label>
                             <br>
                             <input type="radio" id="2" value="2" v-model.trim="form.resultado">
                             <label for="2">2</label>
                            </div>
                        </div>

                       <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Editar</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'PronosticadorUsuario'}">Cancelar</b-button>
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
            pronosticoId: this.$route.params.pronosticoId,
            form: {
                resultado: '',
                acertado: '',
                usuario: '',
                partido: ''
            },
            errors: []
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

            const path = `http://localhost:8000/api/v1.0/pronosticos/${this.pronosticoId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.resultado = response.data.resultado
                this.form.acertado = response.data.acertado
                this.form.usuario = response.data.usuario
                this.form.partido = response.data.partido

                swal({
                    title: "¡Pronóstico actualizado con éxito!",
                    icon: "success",
                    }).then(function() {
                    window.location = "/pronosticadorUsuario";
                    });
            })
            .catch((error) => {
                this.errors = [];
                if(this.form.resultado == ''){
                    this.errors.push('El resultado es obligatorio');
                }
                console.log(error)
                swal("¡El pronóstico no ha sido actualizado!", "", "error")
            })

        },

        getPronostico (){
            const path = `http://localhost:8000/api/v1.0/pronosticos/${this.pronosticoId}/`

            axios.get(path).then((response) =>{

                this.form.resultado = response.data.resultado
                this.form.acertado = response.data.acertado
                this.form.usuario = response.data.usuario
                this.form.partido = response.data.partido

            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getPronostico()
    }
}
</script>>

<style lang="css" scoped>
</style>