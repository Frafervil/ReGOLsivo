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

export default {

    mounted() {
        this.checkLoggedIn();
    },

    data() {
        return {
            partidoId: this.$route.params.partidoId,
            form: {
                resultado: '',
                acertado: 'Por determinar',
                nombreLocal: '',
                nombreVisitante: '',
                resultado: '',
                pronosticoSistema: '',
                premio: '',
                dificultad: '',
                username: '',
                password: '',
                email: '',
                first_name: '',
                last_name: '',
                karma: ''
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

            const path = `http://localhost:8000/api/v1.0/pronosticos/`

            axios.post(path, this.form).then((response) =>{

                this.form.resultado = response.data.resultado
                this.form.partido = response.data.partido
                this.form.usuario = response.data.usuario

                swal("¡Pronóstico creado con éxito!", "", "success")
            })
            .catch((error) => {
                console.log(error)
                swal("¡El pronóstico no ha sido creado!", "", "error")
            })

        },
        
    getPartido (){
        
      const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

      axios.get(path).then((response) => {

                this.form.nombreLocal = response.data.nombreLocal
                this.form.nombreVisitante = response.data.nombreVisitante
                this.form.resultado = response.data.resultado
                this.form.pronosticoSistema = response.data.pronosticoSistema
                this.form.premio = response.data.premio
                this.form.dificultad = response.data.dificultad

      })
      .catch((error) => {
        console.log(error)
        swal("¡No existe ese partido!", "", "error")
      })
    }

    },

    getUsuarioId(){
            var decodedPayload = atob(this.$session.get('token').split('.')[1]);
            var payloadSplittedByComa = decodedPayload.split(',')[0];
            return payloadSplittedByComa.split(':')[1];
        },

    getUsuario (){
            const usuarioId = this.getUsuarioId();

            const path = `http://localhost:8000/api/v1.0/usuarios/${usuarioId}/`

            axios.get(path).then((response) =>{

                this.form.username = response.data.username
                this.form.password = response.data.password
                this.form.email = response.data.email
                this.form.first_name = response.data.first_name
                this.form.last_name = response.data.last_name
                this.form.karma = response.data.karma

            })
            .catch((error) => {
                console.log(error)
            })
        },

    created() {
        this.getPartido(),
        this.getUsuario()
    }
}
</script>>

<style lang="css" scoped>
</style>