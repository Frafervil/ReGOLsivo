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

        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/comentarios/`

            const auth = {
                headers: {Authorization:'JWT ' + this.$session.get('token')} 
            }

            axios.post(path, this.form, auth).then((response) =>{

                this.form.texto = response.data.texto

                swal("Comentario creado con éxito!", "", "success")
            })
            .catch((error) => {
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

<style lang="css" scoped>
</style>