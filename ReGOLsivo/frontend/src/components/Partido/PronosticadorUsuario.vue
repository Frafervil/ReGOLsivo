<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Pronosticador</h2>
        </div>
        <div class="col-md-12">
          <b-table 
            id="tabla"
            striped hover 
            :items="partidos" 
            :fields="fields" 
            :per-page="perPage" 
            :current-page="currentPage">
            <template v-slot:cell(action)="data">
              <b-button size="sm" variant="info" :to="{ name:'ShowPartido', params: {partidoId: data.item.id} }">
                Ver detalles
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
        </div>

        <br>
        <h2>Mis pronósticos</h2>
        <br>
        <div class="misPronosticos">
          <b-table striped hover :items="misPronosticos" :fields="camposPronosticos">
            <template v-slot:cell(action)="data">
              <b-button size="sm" variant="success" :to="{ name:'ShowPronostico', params: {pronosticoId: data.item.id, partidoId: data.item.partido}  }">
                Comprobar
              </b-button>
              <b-button size="sm" variant="primary" :to="{ name:'EditPronostico', params: {pronosticoId: data.item.id} }">
                Editar
              </b-button>
              <b-button size="sm" variant="danger" :to="{ name:'DeletePronostico', params: {pronosticoId: data.item.id} }">
                Eliminar
              </b-button>
            </template>
            <template v-slot:cell(acertado)="row">
              <b-badge v-if="row.item.acertado" variant="success">Si</b-badge>
              <b-badge v-else variant="danger">No</b-badge>
            </template>
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
      currentPage: 1,
      perPage: 10,

      fields: [
        { key: 'nombreLocal', label: 'Local' },
        { key: 'nombreVisitante', label: 'Visitante' },
        { key: 'action', label: '' }
      ],
      partidos: [],

      camposPronosticos: [
        { key: 'resultado', label: 'Resultado' },
        { key: 'acertado', label: '¿Acertado?', sortable: true},
        { key: 'partido', formatter: "localYVisitante", label: 'Partido' },
        { key: 'action', label: '' }
      ],
      pronosticos: []
    }
  },
  methods: {

  checkLoggedIn() {
         this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    },

    localYVisitante(partidoId){

            const partido = this.partidos.find(p => p.id === partidoId);
            return partido ? `${partido.nombreLocal} - ` + `${partido.nombreVisitante}` : 'Cargando...';

        },

    getPartidos (){

      const path = 'http://localhost:8000/api/v1.0/partidos/'
      axios.get(path).then((response) => {
        this.partidos = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
  
    getPronosticos (){

      const path = 'http://localhost:8000/api/v1.0/pronosticos/'
      
      axios.get(path).then((response) => {
        this.pronosticos = response.data
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
      rows() {
        return this.partidos.length
      },

      misPronosticos: function (){
        return this.pronosticos.filter((pronostico) => pronostico.usuario == this.getUsuarioId());
      }

    },

  created(){
    this.getPartidos(),
    this.getPronosticos()
  }
}
</script>