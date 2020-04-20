<template lang="html">
     <div class="container">
        <div class="row">
            <div class="col">
         
                <h3>¿Seguro que quieres eliminar este usuario?</h3>
                <p>Nombre : {{ this.element.Nombre }}</p>
                <p>Apellidos : {{ this.element.Apellidos }}</p>
                <p>Email : {{ this.element.Email }}</p>
                <p>Karma : {{ this.element.Karma }}</p>

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
                Nombre: '',
                Apellidos: '',
                Email: '',
                Karma: ''
            }
        }
    },
    methods: {
        getUsuario (){
            const path = `http://localhost:8000/api/v1.0/usuarios/${this.usuarioId}/`

            axios.get(path).then((response) =>{

                this.element.Nombre = response.data.Nombre
                this.element.Apellidos = response.data.Apellidos
                this.element.Email = response.data.Email
                this.element.Karma = response.data.Karma

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