<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Lista de administradores</h2>
          <b-button size="sm" :to="{name: 'CreateAdministrador'}" variant="primary">
            Crear administrador
          </b-button>
        </div>
        <br>
        <div class="col-md-12">
          <b-table striped hover :items="administradores" :fields="fields">

            <template v-slot:cell(action)="data">
              <b-button size="sm" variant="danger" :to="{ name:'DeleteAdministrador', params: {administradorId: data.item.id} }">
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
        { key: 'username', label: 'Nombre de usuario'},
        { key: 'first_name', label: 'Nombre'},
        { key: 'last_name', label: 'Apellidos'},
        { key: 'email', label: 'Email' },
        { key: 'action', label: '' }
      ],
      administradores: []
    }
  },
  methods: {

    checkLoggedIn() {
         this.$session.start();
        if (!this.$session.has("token")) {
            router.push("/auth");
            }
        },

    getAdministradores (){

      const path = 'http://localhost:8000/api/v1.0/administradores/'
      axios.get(path).then((response) => {
        this.administradores = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },

  created(){
    this.getAdministradores()
  }
}
</script>

<style lang="css" scoped>
</style>
