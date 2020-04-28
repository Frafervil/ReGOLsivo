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
              <b-button size="sm" variant="primary" :to="{ name:'EditAdministrador', params: {administradorId: data.item.id} }">
                Editar
              </b-button>
              <b-button size="sm" variant="danger" :to="{ name:'DeleteAdministrador', params: {administradorId: data.item.id} }">
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
        { key: 'nombre', label: 'Nombre' },
        { key: 'apellidos', label: 'Apellidos' },
        { key: 'email', label: 'Email' },
        { key: 'action', label: '' }
      ],
      administradores: []
    }
  },
  methods: {

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
