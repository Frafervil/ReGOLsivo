<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Editar partido</h2>
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
                             <input type="text" placeholder="Local" name="nombreLocal" class="form-control" v-model.trim="form.nombreLocal">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="nombreVisitante" class="col-sm-2 col-form-label">Visitante</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Visitante" name="nombreVisitante" class="form-control" v-model.trim="form.nombreVisitante">
                            </div>
                        </div>

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

                        <div class="form-group row">
                            <label for="pronosticoSistema" class="col-sm-2 col-form-label">Pronóstico del sistema</label>    
                            <div class="col-sm-6">
                             <input type="radio" id="1" value="1" v-model.trim="form.pronosticoSistema">
                             <label for="1">1</label>
                             <br>
                             <input type="radio" id="X" value="X" v-model.trim="form.pronosticoSistema">
                             <label for="X">X</label>
                             <br>
                             <input type="radio" id="2" value="2" v-model.trim="form.pronosticoSistema">
                             <label for="2">2</label>
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="premio" class="col-sm-2 col-form-label">Premio</label>    
                            <div class="col-sm-6">
                             <input type="number" min="0" placeholder="0" name="premio" class="form-control" v-model.trim="form.premio">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="dificultad" class="col-sm-2 col-form-label">Dificultad</label>    
                            <div class="col-sm-6">
                             <input type="radio" id="facil" value="Facil" v-model.trim="form.dificultad">
                             <label for="facil">Facil</label>
                             <br>
                             <input type="radio" id="intermedia" value="Intermedia" v-model.trim="form.dificultad">
                             <label for="intermedia">Intermedia</label>
                             <br>
                             <input type="radio" id="dificil" value="Dificil" v-model.trim="form.dificultad">
                             <label for="dificil">Dificil</label>
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Editar</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'ListPartido'}">Cancelar</b-button>
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