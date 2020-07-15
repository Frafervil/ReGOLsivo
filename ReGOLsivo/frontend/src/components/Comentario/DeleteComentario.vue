<template lang="html">
     <div class="container">
        <div class="row">
            <div class="col">
         
                <h3>¿Seguro que quieres eliminar este comentario?</h3>
                <p>Momento : {{ this.element.momento }}</p>
                <p>Texto : {{ this.element.texto }}</p>
                <p>Número de "me gustas" : {{ this.element.meGustas }}</p>
                <p>Autor : {{ this.element.autor }}</p>
                <p>Partido : {{ this.element.partido }}</p>

            </div> 
        </div> 

        <div class="row">
         <div class="col">
            <b-button v-if="element.autor == usuario" v-on:click="deleteComentario" variant="danger">Eliminar</b-button>
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
            comentarioId: this.$route.params.comentarioId,
            element: {
                momento: '',
                texto: '',
                meGustas: '',
                autor: '',
                partido: ''
            },
            usuario: this.getUsuarioId()
        }
    },
    methods: {

        checkLoggedIn() {
         this.$session.start();
        if (!this.$session.has("token")) {
            router.push("/auth");
            }
        },

        getUsuarioId(){
            var decodedPayload = atob(this.$session.get('token').split('.')[1]);
            var payloadSplittedByComa = decodedPayload.split(',')[0];
            return payloadSplittedByComa.split(':')[1];
        },

        getComentario (){
            const path = `http://localhost:8000/api/v1.0/comentarios/${this.comentarioId}/`

            axios.get(path).then((response) =>{

                this.element.momento = response.data.momento
                this.element.texto = response.data.texto
                this.element.meGustas = response.data.meGustas
                this.element.autor = response.data.autor
                this.element.partido = response.data.partido

            })
            .catch((error) => {
                console.log(error)
            })
        },
        deleteComentario () {
            const path = `http://localhost:8000/api/v1.0/comentarios/${this.comentarioId}/`

            axios.delete(path).then((response) => {
                location.href = '/pronosticadorUsuario'
            })
            .catch((error) => {
                swal("No es posible eliminar el comentario", "", "error")
            })
        }
    },
    created() {
        this.getComentario()
    }
}
</script>>

<style lang="css" scoped>
</style> 