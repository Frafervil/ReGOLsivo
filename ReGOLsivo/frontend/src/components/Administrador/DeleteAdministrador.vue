<template lang="html">
     <div class="container">
        <div class="row">
            <div class="col">
         
                <h3>¿Seguro que quieres eliminar este administrador?</h3>
                <p>Nombre : {{ this.element.nombre }}</p>
                <p>Apellidos : {{ this.element.apellidos }}</p>
                <p>Email : {{ this.element.email }}</p>

            </div> 
        </div> 

        <div class="row">
         <div class="col">
            <b-button v-on:click="deleteAdministrador" variant="danger">Eliminar</b-button>
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
            administradorId: this.$route.params.administradorId,
            element: {
                nombre: '',
                apellidos: '',
                email: ''
            }
        }
    },
    methods: {
        getAdministrador (){
            const path = `http://localhost:8000/api/v1.0/administradores/${this.administradorId}/`

            axios.get(path).then((response) =>{

                this.element.nombre = response.data.nombre
                this.element.apellidos = response.data.apellidos
                this.element.email = response.data.email

            })
            .catch((error) => {
                console.log(error)
            })
        },
        deleteAdministrador () {
            const path = `http://localhost:8000/api/v1.0/administradores/${this.administradorId}/`

            axios.delete(path).then((response) => {
                location.href = '/administradores'
            })
            .catch((error) => {
                swal("No es posible eliminar el administrador", "", "error")
            })
        }
    },
    created() {
        this.getAdministrador()
    }
}
</script>>

<style lang="css" scoped>
</style> 