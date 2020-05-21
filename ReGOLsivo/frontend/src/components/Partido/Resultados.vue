<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Lista de partidos</h2>
        <div class="col-md-12">
          <b-table striped hover :items="partidos" :fields="fields">
          </b-table>
          <b-button type="submit" class="btn-large-space" :to="{ name: 'LandingUsuario'}">Atrás</b-button>
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
        { key: 'nombreVisitante', label: 'Visitante' },
        { key: 'dia', label: 'Día' },
        { key: 'hora', label: 'Hora' },
        { key: 'pronosticoSistema', label: 'Pronóstico del sistema' }
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
