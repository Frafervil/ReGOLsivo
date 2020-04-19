<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Listado de usuarios</h2>

        <div class="col-md-12">
          <b-table striped hover :items="usuarios" :fields="fields">

            <template v-slot:cell(action)="data">
              <b-button size="sm" variant="primary">
                Editar
              </b-button>
              <b-button size="sm" variant="danger">
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

export default {
  data () {
    return {
      fields: [
        { key: 'Nombre', label: 'Nombre' },
        { key: 'Apellidos', label: 'Apellidos' },
        { key: 'Email', label: 'Email' },
        { key: 'Karma', label: 'Karma' },
        { key: 'action', label: '' }
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
