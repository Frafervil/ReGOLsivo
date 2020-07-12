<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Lista de partidos</h2>
        <div class="col-md-12">
          <b-table 
            id="tabla"
            striped hover 
            :items="partidos" 
            :fields="fields" 
            :per-page="perPage"
            :current-page="currentPage"
            :sort-by.sync="sortBy" 
            :sort-desc.sync="sortDesc">
          </b-table>
          <b-pagination 
            v-model="currentPage" 
            :total-rows="rows" 
            :per-page="perPage" 
            aria-controls="tabla" 
            first-text="Primera jornada" 
            prev-text="Jornada anterior" 
            next-text="Siguiente jornada" 
            last-text="Última jornada">
          </b-pagination>
          <b-button type="submit" class="btn-large-space" :to="{ name: 'LandingUsuario'}">Atrás</b-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import router from "../../router";
import moment from 'moment'

export default {

  mounted() {
        this.checkLoggedIn();
    },

  data () {
    return {
      sortBy: 'dia',
      sortDesc: false,
      currentPage: 1,
      perPage: 10,

      fields: [
        { key: 'nombreLocal', label: 'Local' },
        { key: 'nombreVisitante', label: 'Visitante' },
        { key: 'dia', formatter: "formatDia", label: 'Día', sortable: true},
        { key: 'hora', label: 'Hora', sortable: true},
        { key: 'resultado', label: 'Resultado' },
        { key: 'pronosticoSistema', label: 'Pronóstico del sistema' }
      ],
      partidos: []
    }
  },
  methods: {

    checkLoggedIn() {
         this.$session.start();
        if (!this.$session.has("token")) {
            router.push("/auth");
            }
        },

    formatDia(value) {
            const formattedDate = moment(value).format('DD/MM/YYYY')
            return formattedDate;
        },

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

  computed: {
      rows() {
        return this.partidos.length
      }
    },

  created(){
    this.getPartidos()
  }
}
</script>

<style lang="css" scoped>
</style>
