<template lang="html">
     <div class="container">
        <div class="row">
            <div class="col">
         
                <h3>¿Seguro que quieres eliminar este partido?</h3>
                <p>Local : {{ this.element.nombreLocal }}</p>
                <p>Visitante : {{ this.element.nombreVisitante }}</p>
                <p>Resultado : {{ this.element.resultado }}</p>
                <p>Pronóstico del sistema : {{ this.element.pronosticoSistema }}</p>
                <p>Premio : {{ this.element.premio }}</p>
                <p>Dificultad : {{ this.element.dificultad }}</p>

            </div> 
        </div> 

        <div class="row">
         <div class="col">
            <b-button v-on:click="deletePartido" variant="danger">Eliminar</b-button>
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

    data () {
        return {
            partidoId: this.$route.params.partidoId,
            element: {
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

        checkLoggedIn() {
         this.$session.start();
        if (!this.$session.has("token")) {
            router.push("/auth");
            }
        },

        getPartido (){
            const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

            axios.get(path).then((response) =>{

                this.element.nombreLocal = response.data.nombreLocal
                this.element.nombreVisitante = response.data.nombreVisitante
                this.element.resultado = response.data.resultado
                this.element.pronosticoSistema = response.data.pronosticoSistema
                this.element.premio = response.data.premio
                this.element.dificultad = response.data.dificultad

            })
            .catch((error) => {
                console.log(error)
            })
        },
        deletePartido () {
            const path = `http://localhost:8000/api/v1.0/partidos/${this.partidoId}/`

            axios.delete(path).then((response) => {
                swal({
                    title: "¡Partido eliminado con éxito!",
                    icon: "success",
                    button: "Ok"}).then(function() {
                    window.location = "/pronosticador";
                    });
            })
            .catch((error) => {
                swal("No es posible eliminar el partido", "", "error")
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