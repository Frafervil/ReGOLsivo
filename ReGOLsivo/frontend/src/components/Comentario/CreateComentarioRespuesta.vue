<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Crear comentario</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                        <form @submit="onSubmit">

                        <p v-if="errors.length">
                            <b>Por favor, corrija el(los) siguiente(s) error(es):</b>
                            <ul>
                                <li v-for="error in errors">{{ error }}</li>
                            </ul>
                        </p>

                        <div class="form-group row">
                            <label for="texto" class="col-sm-2 col-form-label">Texto</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Texto" name="texto" class="form-control" v-model.trim="form.texto">
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Crear</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'PronosticadorUsuario'}">Cancelar</b-button>
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
                texto: '',
                autor: this.getUsuarioId(),
                partido: this.$route.params.partidoId,
                comentarioRespuesta: this.$route.params.comentarioId
            },
            errors: []
        }
    },
    methods: {

        checkLoggedIn() {
         this.$session.start();
        if (!this.$session.has("token")) {
            router.push("/auth");
            }
        },

        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/comentarios/`

            axios.post(path, this.form).then((response) =>{

                this.form.texto = response.data.texto

                swal({
                    title: "¡Comentario creado con éxito!",
                    icon: "success",
                    button: "Ok"}).then(function() {
                    window.location = "/pronosticadorUsuario";
                    });
            })
            .catch((error) => {
                this.errors = [];
                if(this.form.texto == ''){
                    this.errors.push('El texto es obligatorio');
                }
                console.log(error)
                swal("¡El comentario no ha sido creado!", "", "error")
            })

        },

    getUsuarioId(){
            var decodedPayload = atob(this.$session.get('token').split('.')[1]);
            var payloadSplittedByComa = decodedPayload.split(',')[0];
            return payloadSplittedByComa.split(':')[1];
        },

    },

    created() {

    }
}
</script>>