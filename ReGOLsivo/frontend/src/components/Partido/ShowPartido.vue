<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Detalles del partido</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                        <form @submit="onSubmit">

                        <div class="form-group row">
                            <label for="nombreLocal" class="col-sm-2 col-form-label">Local</label>    
                            <div class="col-sm-6">
                             <input type="text" name="nombreLocal" class="form-control" readonly v-model.trim="form.nombreLocal">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="nombreVisitante" class="col-sm-2 col-form-label">Visitante</label>    
                            <div class="col-sm-6">
                             <input type="text" name="nombreVisitante" class="form-control" readonly v-model.trim="form.nombreVisitante">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="resultado" class="col-sm-2 col-form-label">Resultado</label>    
                            <div class="col-sm-6">
                             <input type="text" name="resultado" class="form-control" readonly v-model.trim="form.resultado">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="pronosticoSistema" class="col-sm-2 col-form-label">Pronóstico del sistema</label>    
                            <div class="col-sm-6">
                             <input type="text" name="pronosticoSistema" class="form-control" readonly v-model.trim="form.pronosticoSistema">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="premio" class="col-sm-2 col-form-label">Premio</label>    
                            <div class="col-sm-6">
                             <input type="number" name="premio" class="form-control" readonly v-model.trim="form.premio">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="dificultad" class="col-sm-2 col-form-label">Dificultad</label>    
                            <div class="col-sm-6">
                             <input type="text" name="dificultad" class="form-control" readonly v-model.trim="form.dificultad">
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button size="sm" variant="primary" :to="{ name:'CreatePronostico', params: {partidoId: this.partidoId} }">
                            Pronosticar
                            </b-button>    
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'PronosticadorUsuario'}">Atrás</b-button>
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
            partidoId: this.$route.params.partidoId,
            form: {
                nombreLocal: '',
                nombreVisitante: '',
                resultado: '',
                pronosticoSistema: '',
                premio: '',
                dificultad: ''
            }
        }
    },
    methods: {
        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.nombreLocal = response.data.nombreLocal
                this.form.nombreVisitante = response.data.nombreVisitante
                this.form.resultado = response.data.resultado
                this.form.pronosticoSistema = response.data.pronosticoSistema
                this.form.premio = response.data.premio
                this.form.dificultad = response.data.dificultad

                swal("¡Partido actualizado con éxito!", "", "success")
            })
            .catch((error) => {
                console.log(error)
            })

        },

        getPartido (){
            const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

            axios.get(path).then((response) =>{

                this.form.nombreLocal = response.data.nombreLocal
                this.form.nombreVisitante = response.data.nombreVisitante
                this.form.resultado = response.data.resultado
                this.form.pronosticoSistema = response.data.pronosticoSistema
                this.form.premio = response.data.premio
                this.form.dificultad = response.data.dificultad

            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getPartido()
    }
}
</script>>

<style lang="css" scoped>
</style>