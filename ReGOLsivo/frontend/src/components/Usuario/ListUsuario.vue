<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Lista de usuarios</h2>
        </div>
        <div class="col-md-12">
          <b-table striped hover :items="usuarios" :fields="fields">

            <template v-slot:cell(action)="data">
              <b-button size="sm" variant="danger" :to="{ name:'DeleteUsuario', params: {usuarioId: data.item.id} }">
                Eliminar
              </b-button>
            </template>

          </b-table>
         <b-button type="submit" class="btn-large-space" :to="{ name: 'LandingAdministrador'}">Atrás</b-button>
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
        { key: 'username', label: 'Nombre de usuario', sortable: true},
        { key: 'karma', label: 'Karma', sortable: true},
        { key: 'action', label: '' }
      ],
      usuarios: []
    }
  },
  methods: {

    checkLoggedIn() {
         this.$session.start();
        if (!this.$session.has("token")) {
            router.push("/auth");
            }
        },

    getUsuarios (){

      const path = 'http://localhost:8000/api/v1.0/usuarios/'
      axios.get(path).then((response) => {
        this.usuarios = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },

  created(){
    this.getUsuarios()
  }
}
</script>
