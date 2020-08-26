<template lang="html">
     <div class="container">
        <div class="row">
            <div class="col">
         
                <h3>¿Seguro que quieres eliminar este administrador?</h3>
                <p>Nombre : {{ this.element.first_name }}</p>
                <p>Apellidos : {{ this.element.last_name }}</p>
                <p>Email : {{ this.element.email }}</p>
                <p>Nombre de usuario : {{ this.element.username }}</p>

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
import router from "../../router";

export default {

    mounted() {
        this.checkLoggedIn();
    },

    data () {
        return {
            administradorId: this.$route.params.administradorId,
            element: {
                first_name: '',
                last_name: '',
                email: '',
                username: ''
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

        getAdministrador (){
            const path = `http://localhost:8000/api/v1.0/administradores/${this.administradorId}/`

            axios.get(path).then((response) =>{

                this.element.first_name = response.data.first_name
                this.element.last_name = response.data.last_name
                this.element.email = response.data.email
                this.element.username = response.data.username

            })
            .catch((error) => {
                console.log(error)
            })
        },
        deleteAdministrador () {
            const path = `http://localhost:8000/api/v1.0/administradores/${this.administradorId}/`

            axios.delete(path).then((response) => {
                swal({
                    title: "¡Administrador eliminado con éxito!",
                    icon: "success",
                    button: "Ok"}).then(function() {
                    window.location = "/administradores";
                    });
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