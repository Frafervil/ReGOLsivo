<template lang="html">
     <div class="container">
        <div class="row">
            <div class="col">
         
                <h3>¿Seguro que quieres eliminar este usuario?</h3>
                <p>Nombre de usuario : {{ this.element.username }}</p>
                <p>Contraseña : {{ this.element.password }}</p>
                <p>Email : {{ this.element.email }}</p>
                <p>Nombre : {{ this.element.first_name }}</p>
                <p>Apellidos : {{ this.element.last_name }}</p>
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
import router from "../../router";

export default {

    mounted() {
        this.checkLoggedIn();
    },

    data () {
        return {
            usuarioId: this.$route.params.usuarioId,
            element: {
                username: '',
                password: '',
                email: '',
                first_name: '',
                last_name: '',
                karma: ''
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

        getUsuario (){
            const path = `http://localhost:8000/api/v1.0/usuarios/${this.usuarioId}/`

            axios.get(path).then((response) =>{

                this.element.username = response.data.username
                this.element.password = response.data.password
                this.element.email = response.data.email
                this.element.first_name = response.data.first_name
                this.element.last_name = response.data.last_name
                this.element.karma = response.data.karma

            })
            .catch((error) => {
                console.log(error)
            })
        },
        deleteUsuario () {
            const path = `http://localhost:8000/api/v1.0/usuarios/${this.usuarioId}/`

            const auth = {
                headers: {Authorization:'JWT ' + this.$session.get('token')} 
            }

            axios.delete(path, auth).then((response) => {
                swal({
                    title: "¡Usuario eliminado con éxito!",
                    icon: "success",
                    button: "Ok"}).then(function() {
                    window.location = "/usuarios";
                    });
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