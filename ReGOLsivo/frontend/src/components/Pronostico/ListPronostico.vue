<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Lista de pronósticos</h2>
          <b-button size="sm" :to="{name: 'CreatePronostico'}" variant="primary">
            Crear pronóstico
          </b-button>
        </div>
        <br>
        <div class="col-md-12">
          <b-table striped hover :items="pronosticos" :fields="fields">

            <template v-slot:cell(action)="data">
              <b-button size="sm" variant="primary" :to="{ name:'EditPronostico', params: {pronosticoId: data.item.id} }">
                Editar
              </b-button>
              <b-button size="sm" variant="danger" :to="{ name:'DeletePronostico', params: {pronosticoId: data.item.id} }">
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
  data () {
    return {
      fields: [
        { key: 'resultado', label: 'Resultado' },
        { key: 'acertado', label: '¿Acertado?' },
        { key: 'usuario', label: 'Usuario' },
        { key: 'partido', label: 'Partido' },
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

    getPronosticos (){

      const path = 'http://localhost:8000/api/v1.0/pronosticos/'
      axios.get(path).then((response) => {
        this.pronosticos = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },

  created(){
    this.getPronosticos()
  }
}
</script>

<style lang="css" scoped>
</style>
