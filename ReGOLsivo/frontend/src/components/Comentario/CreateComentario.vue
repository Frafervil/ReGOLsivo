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
                partido: this.$route.params.partidoId
            },
            logro: {
                nombre: '',
                usuarios: []
            },
            logroDe50Comentarios: {
                nombre: '',
                usuarios: []
            },
            errors: [],
            comentarios: []
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

            const auth = {
                headers: {Authorization:'JWT ' + this.$session.get('token')} 
            }

            axios.post(path, this.form, auth).then((response) =>{

                this.form.texto = response.data.texto

            swal({
                    title: "¡Comentario creado con éxito!",
                    icon: "success",
                    button: "Ok"}).then(function() {
                    window.location = "/pronosticadorUsuario";
                    });
            },this.esElPrimero(),
            this.esEl50())

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

    getComentarios (){

      const path = 'http://localhost:8000/api/v1.0/comentarios/'
      axios.get(path).then((response) => {
        this.comentarios = response.data
      })
      .catch((error) => {
        console.log(error)
      })
     },

    getLogro(){
        const path = `http://localhost:8000/api/v1.0/logros/2/`

        axios.get(path).then((response) =>{

                this.logro.nombre = response.data.nombre
                this.logro.usuarios = response.data.usuarios

            })
            .catch((error) => {
                console.log(error)
            })

    },

    getLogroDe50Comentarios(){
        const path = `http://localhost:8000/api/v1.0/logros/4/`

        axios.get(path).then((response) =>{

                this.logroDe50Comentarios.nombre = response.data.nombre
                this.logroDe50Comentarios.usuarios = response.data.usuarios

            })
            .catch((error) => {
                console.log(error)
            })

    },

    esElPrimero(){
        if(this.comentariosDelUsuario.length === 0){
            this.logro.usuarios.push(this.getUsuarioId());
            this.asignarLogroAUsuario();
        }
    },

    esEl50(){
        if(this.comentariosDelUsuario.length === 49){
            this.logroDe50Comentarios.usuarios.push(this.getUsuarioId());
            this.asignarLogroDe50ComentariosAUsuario();
        }
    },

    asignarLogroAUsuario(){
        const path = `http://localhost:8000/api/v1.0/logros/2/`

        axios.put(path, this.logro)

        .catch((error) => {
            console.log(error)
            swal("¡Fallo al asignar!", "", "error")
        })
    },

    asignarLogroDe50ComentariosAUsuario(){
        const path = `http://localhost:8000/api/v1.0/logros/4/`

        axios.put(path, this.logroDe50Comentarios)

        .catch((error) => {
            console.log(error)
            swal("¡Fallo al asignar!", "", "error")
        })
    }

    },

    computed: {
      comentariosDelUsuario: function (){
        return this.comentarios.filter((comentario) => comentario.autor == this.getUsuarioId());
      },

    },

    created() {
        this.getComentarios(),
        this.getLogro(),
        this.getLogroDe50Comentarios()
    }
}
</script>>

<style lang="css" scoped>
</style>