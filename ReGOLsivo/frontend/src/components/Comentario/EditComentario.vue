<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Editar comentario</h2>
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
                             <textarea name="texto" class="form-control" placeholder="Texto" rows="3" v-model.trim="form.texto"></textarea>
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Editar</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'ListComentario'}">Cancelar</b-button>
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
    data() {
        return {
            comentarioId: this.$route.params.comentarioId,
            form: {
                momento: '',
                texto: '',
                meGustas: '',
                autor: '',
                partido: ''
            }
        }
    },
    methods: {
        onSubmit(evt){
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/comentarios/${this.comentarioId}/`

            axios.put(path, this.form).then((response) =>{

                this.form.momento = response.data.momento
                this.form.texto = response.data.texto
                this.form.meGustas = response.data.meGustas
                this.form.autor = response.data.autor
                this.form.partido = response.data.partido

                swal("¡Comentario actualizado con éxito!", "", "success")
            })
            .catch((error) => {
                console.log(error)
            })

        },

        getComentario (){
            const path = `http://localhost:8000/api/v1.0/comentarios/${this.comentarioId}/`

            axios.get(path).then((response) =>{

                this.form.momento = response.data.momento
                this.form.texto = response.data.texto
                this.form.meGustas = response.data.meGustas
                this.form.autor = response.data.autor
                this.form.partido = response.data.partido

            })
            .catch((error) => {
                console.log(error)
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