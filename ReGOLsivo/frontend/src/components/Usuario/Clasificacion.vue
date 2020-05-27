<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Clasificación</h2>
        </div>
        <div class="col-md-12">
          <b-table striped hover :items="usuarios" :fields="fields" :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" :per-page="perPage">
          </b-table>
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
      sortBy: 'karma',
      sortDesc: true,
      perPage: 10,
      fields: [
        { key: 'username', label: 'Nombre de usuario'},
        { key: 'karma', label: 'Karma', sortable: true}
      ],
      usuarios: []
    }
  },
  methods: {

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

<style lang="css" scoped>
</style>
