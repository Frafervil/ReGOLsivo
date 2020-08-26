<template lang="html">
     <div class="container">
        <div class="row">
            <div class="col">
         
                <h3>¿Seguro que quieres eliminar este partido?</h3>
                <p>Local : {{ this.element.nombreLocal }}</p>
                <p>Visitante : {{ this.element.nombreVisitante }}</p>
                <p>Resultado : {{ this.element.resultado }}</p>
                <p>Pronóstico del sistema : {{ this.element.pronosticoSistema }}</p>
                <p>Probabilidad de victoria del equipo local (%) : {{ this.element.probabilidadVictoriaLocal }}</p>
                <p>Probabilidad de empate (%) : {{ this.element.probabilidadEmpate }}</p>
                <p>Probabilidad de victoria del equipo visitante (%) : {{ this.element.probabilidadVictoriaVisitante }}</p>
                <p>Premio : {{ this.element.premio }}</p>
                <p>Dificultad : {{ this.element.dificultad }}</p>
                <p>Proporción de puntos del equipo local : {{ this.element.proporcion_de_puntos_del_equipo_local }}</p>
                <p>Proporción de puntos del equipo visitante : {{ this.element.proporcion_de_puntos_del_equipo_visitante }}</p>
                <p>Proporción de goles por partido del equipo local : {{ this.element.goles_por_partido_del_equipo_local }}</p>
                <p>Proporción de goles por partido del equipo visitante : {{ this.element.goles_por_partido_del_equipo_visitante }}</p>

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
                probabilidadVictoriaLocal: '',
                probabilidadEmpate: '',
                probabilidadVictoriaVisitante: '',
                premio: '',
                dificultad: '',
                proporcion_de_puntos_del_equipo_local: '',
                proporcion_de_puntos_del_equipo_visitante: '',
                goles_por_partido_del_equipo_local: '',
                goles_por_partido_del_equipo_visitante: ''
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
                this.element.probabilidadVictoriaLocal = response.data.probabilidadVictoriaLocal
                this.element.probabilidadEmpate = response.data.probabilidadEmpate
                this.element.probabilidadVictoriaVisitante = response.data.probabilidadVictoriaVisitante
                this.element.premio = response.data.premio
                this.element.dificultad = response.data.dificultad
                this.element.proporcion_de_puntos_del_equipo_local = response.data.proporcion_de_puntos_del_equipo_local
                this.element.proporcion_de_puntos_del_equipo_visitante = response.data.proporcion_de_puntos_del_equipo_visitante
                this.element.goles_por_partido_del_equipo_local = response.data.goles_por_partido_del_equipo_local
                this.element.goles_por_partido_del_equipo_visitante = response.data.goles_por_partido_del_equipo_visitante

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