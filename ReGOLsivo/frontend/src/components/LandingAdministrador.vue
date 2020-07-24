<template>
  <div class="LandingAdministrador">
    <h1>{{ msg }}</h1>
    <div class="">
    <b-button size="sm" :to="{name: 'ListUsuario'}" variant="primary">
            Usuarios
    </b-button>
    <b-button size="sm" :to="{name: 'ListAdministrador'}" variant="primary">
            Administradores
    </b-button>
    <b-button size="sm" :to="{name: 'Pronosticador'}" variant="primary">
            Pronosticador
    </b-button>
    <b-button size="sm" :to="{name: 'Estadisticas'}" variant="primary">
            Estadísticas
    </b-button>
    <b-button size="sm" :to="{name: 'EditConfiguracion'}" variant="primary">
            Configuración
    </b-button>
    <b-button size="sm" :to="{name: 'PerfilAdministrador'}" variant="primary">
            Perfil
    </b-button>
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
      msg: '¡Bienvenido a la zona de administradores!'
    }
  },

  methods: {

    checkLoggedIn() {
         this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
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
