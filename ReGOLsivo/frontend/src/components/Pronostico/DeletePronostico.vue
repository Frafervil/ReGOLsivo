<template lang="html">
     <div class="container">
        <div class="row">
            <div class="col">
         
                <h3>¿Seguro que quieres eliminar este pronóstico?</h3>
                <p>Resultado : {{ this.element.resultado }}</p>
                <p>Acertado : {{ this.element.acertado }}</p>
                <p>Usuario : {{ this.element.usuario }}</p>
                <p>Partido : {{ this.element.partido }}</p>

            </div> 
        </div> 

        <div class="row">
         <div class="col">
            <b-button v-on:click="deletePronostico" variant="danger">Eliminar</b-button>
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
            pronosticoId: this.$route.params.pronosticoId,
            element: {
                resultado: '',
                acertado: '',
                usuario: '',
                partido: ''
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

        getPronostico (){
            const path = `http://localhost:8000/api/v1.0/pronosticos/${this.pronosticoId}/`

            axios.get(path).then((response) =>{

                this.element.resultado = response.data.resultado
                this.element.acertado = response.data.acertado
                this.element.usuario = response.data.usuario
                this.element.partido = response.data.partido

            })
            .catch((error) => {
                console.log(error)
            })
        },
        deletePronostico () {
            const path = `http://localhost:8000/api/v1.0/pronosticos/${this.pronosticoId}/`

            axios.delete(path).then((response) => {
                location.href = '/pronosticadorUsuario'
            })
            .catch((error) => {
                swal("No es posible eliminar el pronostico", "", "error")
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