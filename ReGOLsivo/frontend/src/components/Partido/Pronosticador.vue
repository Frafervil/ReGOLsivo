<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Lista de partidos</h2>
          <b-button :to="{name: 'CreatePartido'}" variant="primary">
            Crear partido
          </b-button>
        </div>
        <br>
        <div class="col-md-12">
          <b-table 
          id="tabla"
          striped hover 
          :items="partidos" 
          :fields="fields"
          :per-page="perPage" 
          :current-page="currentPage">
            <template v-slot:cell(action)="data">
              <b-button size="sm" variant="info" :to="{ name:'ShowPartidoAdministrador', params: {partidoId: data.item.id} }">
                Ver detalles
              </b-button>
              <b-button size="sm" variant="primary" :to="{ name:'EditPartido', params: {partidoId: data.item.id} }">
                Editar
              </b-button>
              <b-button size="sm" variant="danger" :to="{ name:'DeletePartido', params: {partidoId: data.item.id} }">
                Eliminar
              </b-button>
            </template>
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
      currentPage: 1,
      perPage: 10,

      fields: [
        { key: 'nombreLocal', label: 'Local' },
        { key: 'nombreVisitante', label: 'Visitante' },
        { key: 'resultado', label: 'Resultado' },
        { key: 'pronosticoSistema', label: 'Pronóstico del sistema' },
        { key: 'action', label: '' }
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
      },

    },

  created(){
    this.getPartidos()
  }
}
</script>

<style lang="css" scoped>
</style>
