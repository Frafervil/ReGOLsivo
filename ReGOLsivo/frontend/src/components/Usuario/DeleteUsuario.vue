<template lang="html">
     <div class="container">
        <div class="row">
            <div class="col">
         
                <h3>¿Seguro que quieres eliminar este usuario?</h3>
                <p>Nombre : {{ this.element.nombre }}</p>
                <p>Apellidos : {{ this.element.apellidos }}</p>
                <p>Email : {{ this.element.email }}</p>
                <p>Karma : {{ this.element.karma }}</p>

            </div> 
        </div> 

        <div class="row">
         <div class="col">
            <b-button v-on:click="deleteUsuario" variant="danger">Eliminar</b-button>
         </div>  
        </div> 

    </div>  

</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
    data () {
        return {
            usuarioId: this.$route.params.usuarioId,
            element: {
                nombre: '',
                apellidos: '',
                email: '',
                karma: ''
            }
        }
    },
    methods: {
        getUsuario (){
            const path = `http://localhost:8000/api/v1.0/usuarios/${this.usuarioId}/`

            axios.get(path).then((response) =>{

                this.element.nombre = response.data.nombre
                this.element.apellidos = response.data.apellidos
                this.element.email = response.data.email
                this.element.karma = response.data.karma

            })
            .catch((error) => {
                console.log(error)
            })
        },
        deleteUsuario () {
            const path = `http://localhost:8000/api/v1.0/usuarios/${this.usuarioId}/`

            axios.delete(path).then((response) => {
                location.href = '/usuarios'
            })
            .catch((error) => {
                swal("No es posible eliminar el usuario", "", "error")
            })
        }
    },
    created() {
        this.getUsuario()
    }
}
</script>>

<style lang="css" scoped>
</style> 