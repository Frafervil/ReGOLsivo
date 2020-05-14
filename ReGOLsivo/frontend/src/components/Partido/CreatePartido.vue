<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Crear partido</h2>
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
                            <label for="dia" class="col-sm-2 col-form-label">Día</label>    
                            <div class="col-sm-6">
                             <input type="date" name="dia" class="form-control" v-model.trim="form.dia">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="hora" class="col-sm-2 col-form-label">Hora</label>    
                            <div class="col-sm-6">
                             <input type="time" name="hora" class="form-control" v-model.trim="form.hora">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="premio" class="col-sm-2 col-form-label">Premio</label>    
                            <div class="col-sm-6">
                             <input type="number" min="1" placeholder="1" name="premio" class="form-control" v-model.trim="form.premio">
                            </div>
                        </div>

                        <!--<div class="form-group row">
                            <label for="dificultad" class="col-sm-2 col-form-label">Dificultad</label>    
                            <div class="col-sm-6">
                             <input type="radio" id="facil" value="Fácil" v-model.trim="form.dificultad">
                             <label for="facil">Fácil</label>
                             <br>
                             <input type="radio" id="intermedia" value="Intermedia" v-model.trim="form.dificultad">
                             <label for="intermedia">Intermedia</label>
                             <br>
                             <input type="radio" id="dificil" value="Difícil" v-model.trim="form.dificultad">
                             <label for="dificil">Difícil</label>
                            </div>
                        </div>-->

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Crear</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'Pronosticador'}">Cancelar</b-button>
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
                nombreLocal: '',
                nombreVisitante: '',
                resultado: 'Por determinar',
                hora: '',
                dia: '',
                pronosticoSistema: 'Por determinar',
                premio: '',
                dificultad: ''
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

        obtenerDificultad(){
            //swal("¡Se ha llegado aquí!", "", "error") 
            if(this.form.premio < 50)
                this.form.dificultad = 'Fácil'
            else if(this.form.premio >= 50 && this.form.premio < 100)
                this.form.dificultad = 'Intermedia' 
            else if(this.form.premio >= 100)
                this.form.dificultad = 'Difícil'   
        },

        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/partidos/`

            axios.post(path, this.form).then((response) =>{

                this.form.nombreLocal = response.data.nombreLocal
                this.form.nombreVisitante = response.data.nombreVisitante
                this.form.hora = response.data.hora
                this.form.dia = response.data.dia
                this.form.premio = response.data.premio
                this.form.dificultad = this.obtenerDificultad

                swal("¡Partido creado con éxito!", "", "success")
            })
            .catch((error) => {
                console.log(error)
                swal("¡El partido no ha sido creado!", "", "error")
            })

        },
    },
    created() {
        //this.obtenerDificultad()
    }
}
</script>>

<style lang="css" scoped>
</style>