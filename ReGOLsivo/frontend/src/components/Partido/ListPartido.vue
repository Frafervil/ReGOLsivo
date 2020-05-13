<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Lista de partidos</h2>
        <div class="col-md-12">
          <b-table striped hover :items="partidos" :fields="fields">
          </b-table>
          <b-button type="submit" class="btn-large-space" :to="{ name: 'LandingPage'}">Atrás</b-button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {

  data () {
    return {
      fields: [
        { key: 'nombreLocal', label: 'Local' },
        { key: 'nombreVisitante', label: 'Visitante' }
      ],
      partidos: []
    }
  },
  methods: {

    getPartidos (){

      const path = 'http://localhost:8000/api/v1.0/partidos/'
      axios.get(path).then((response) => {
        this.partidos = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },

  created(){
    this.getPartidos()
  }
}
</script>

<style lang="css" scoped>
</style>
