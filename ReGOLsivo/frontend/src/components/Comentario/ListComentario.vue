<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Lista de comentarios</h2>
          <b-button size="sm" :to="{name: 'CreateComentario'}" variant="primary">
            Crear comentario
          </b-button>
        </div>
        <br>
        <div class="col-md-12">
          <b-table striped hover :items="comentarios" :fields="fields">

            <template v-slot:cell(action)="data">
              <b-button size="sm" variant="primary" :to="{ name:'EditComentario', params: {comentarioId: data.item.id} }">
                Editar
              </b-button>
              <b-button size="sm" variant="danger" :to="{ name:'DeleteComentario', params: {comentarioId: data.item.id} }">
                Eliminar
              </b-button>
            </template>

          </b-table>

        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import router from "../../router";

export default {

  mounted() {
        this.checkLoggedIn();
    },

  data () {
    return {
      fields: [
        { key: 'momento', label: 'Momento' },
        { key: 'texto', label: 'Texto' },
        { key: 'meGustas', label: 'Número de "me gustas"' },
        { key: 'autor', label: 'Autor' },
        { key: 'partido', label: 'Partido' },
        { key: 'action', label: '' }
      ],
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

    getComentarios (){

      const path = 'http://localhost:8000/api/v1.0/comentarios/'
      axios.get(path).then((response) => {
        this.comentarios = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },

  created(){
    this.getComentarios()
  }
}
</script>

<style lang="css" scoped>
</style>
