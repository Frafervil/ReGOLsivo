<template>
  <div class="LandingAdministrador">
    <h1>{{ msg }}</h1>
    <div class="">
    <b-button size="sm" :to="{name: 'CreateAdministrador'}" variant="primary">
            Crear cuenta
    </b-button>
    <b-button size="sm" :to="{name: 'Configuracion'}" variant="primary">
            Configuración
    </b-button>
    <b-button size="sm" :to="{name: 'Estadisticas'}" variant="primary">
            Estadísticas
    </b-button>
    <b-button size="sm" :to="{name: 'Pronosticador', params: {usuarioToken: this.$session.get('token')}}" variant="primary">
            Pronosticador
    </b-button>
    <b-button size="sm" v-on:click="logout" variant="danger">Cerrar sesión</b-button>
    </div>
  </div>
</template>

<script>

import router from "../router";

export default {
  name: 'LandingAdministrador',

  mounted() {
    this.checkLoggedIn();
  },

  data () {
    return {
      msg: '¡Bienvenido!'
    }
  },

  methods: {

    checkLoggedIn() {
         this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    },

    logout(){
      this.$session.destroy();
      location.href = '/'
    },
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #ffffff;
}
</style>
