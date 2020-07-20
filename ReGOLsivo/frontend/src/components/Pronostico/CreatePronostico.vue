<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Crear pronóstico</h2>
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
                            <b-button type="submit" variant="primary">Crear</b-button>
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
            form: {
                resultado: '',
                usuario: this.getUsuarioId(),
                partido: this.$route.params.partidoId
            },
            logro: {
                nombre: '',
                usuarios: []
            },
            errors: [],
            pronosticos: []
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

            const path = `http://localhost:8000/api/v1.0/pronosticos/`

            const auth = {
                headers: {Authorization:'JWT ' + this.$session.get('token')} 
            }

            axios.post(path, this.form, auth).then((response) =>{

                this.form.resultado = response.data.resultado

                 swal({
                    title: "¡Pronóstico creado con éxito!",
                    text: "¡Mucha suerte!",
                    icon: "success",
                    }).then(function() {
                    window.location = "/pronosticadorUsuario";
                    });
            },this.esElPrimero())

            .catch((error) => {
                this.errors = [];
                if(this.form.resultado == ''){
                    this.errors.push('El resultado es obligatorio');
                }
                console.log(error)
                swal("¡El pronóstico no ha sido creado!", "", "error")
            })

        },

    getUsuarioId(){
            var decodedPayload = atob(this.$session.get('token').split('.')[1]);
            var payloadSplittedByComa = decodedPayload.split(',')[0];
            return payloadSplittedByComa.split(':')[1];
        },

    getPronosticos(){

      const path = 'http://localhost:8000/api/v1.0/pronosticos/'
      axios.get(path).then((response) => {
        this.pronosticos = response.data
      })
      .catch((error) => {
        console.log(error)
      })
     },

    getLogro(){
        const path = `http://localhost:8000/api/v1.0/logros/3/`

        axios.get(path).then((response) =>{

                this.logro.nombre = response.data.nombre
                this.logro.usuarios = response.data.usuarios

            })
            .catch((error) => {
                console.log(error)
            })

    },

    esElPrimero(){
        if(this.pronosticosDelUsuario.length === 0){
            this.logro.usuarios.push(this.getUsuarioId());
            this.asignarLogroAUsuario();
        }
    },

    asignarLogroAUsuario(){
        const path = `http://localhost:8000/api/v1.0/logros/3/`

        axios.put(path, this.logro)

        .catch((error) => {
            console.log(error)
            swal("¡Fallo al asignar!", "", "error")
        })
    }

    },

    computed: {
      pronosticosDelUsuario: function (){
        return this.pronosticos.filter((pronostico) => pronostico.usuario == this.getUsuarioId());
      },

    },
    created() {
        this.getPronosticos(),
        this.getLogro()
    }
}
</script>>

<style lang="css" scoped>
</style>