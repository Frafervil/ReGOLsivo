<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Mis logros</h2>
        </div>
        <div class="col-md-12">
          <b-table striped hover :items="misLogros" :fields="fields">
          </b-table>
          <b-button type="submit" class="btn-large-space" :to="{ name: 'LandingUsuario'}">Atrás</b-button>
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
        { key: 'nombre', label: 'Nombre' }
      ],
      logros: []
    }
  },
  methods: {

    checkLoggedIn() {
         this.$session.start();
        if (!this.$session.has("token")) {
            router.push("/auth");
            }
        },

    getLogros (){

      const path = 'http://localhost:8000/api/v1.0/logros/'
      axios.get(path).then((response) => {
        this.logros = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },

    getUsuarioId(){
            var decodedPayload = atob(this.$session.get('token').split('.')[1]);
            var payloadSplittedByComa = decodedPayload.split(',')[0];
            return payloadSplittedByComa.split(':')[1];
    }

  },

  computed: {
      misLogros: function (){
        return this.logros.filter((logro) => logro.usuarios == this.getUsuarioId());
      }

    },

  created(){
    this.getLogros()
  }
}
</script>

<style lang="css" scoped>
</style>
