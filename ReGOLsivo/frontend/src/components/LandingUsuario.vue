<template>
  <div class="LandingUsuario">
    <h1>{{ msg }}</h1>
    <div class="">
    <b-button size="sm" :to="{name: 'PronosticadorUsuario'}" variant="primary">
            Pronosticador
    </b-button>
    <b-button size="sm" :to="{name: 'Resultados'}" variant="primary">
            Resultados ReGOLsivo
    </b-button>
    <b-button size="sm" :to="{name: 'Clasificacion'}" variant="primary">
            Clasificación
    </b-button>
    <b-button size="sm" :to="{name: 'PerfilUsuario'}" variant="primary">
            Perfil
    </b-button>
    <b-button size="sm" :to="{name: 'ListLogro'}" variant="primary">
            Logros
    </b-button>
    </div>
    <br>
    <h3>Contacto</h3>
    <h4>Correo electrónico: primodepapadecho@gmail.com</h4>
    <br>
    <b-button type="button" class="btn btn-link" variant="info" :to="{ name: 'TerminosYCondicionesUsuario'}">Términos y condiciones</b-button>
  </div>
</template>

<script>

import router from "../router";

export default {
  name: 'LandingUsuario',

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
    }
  },
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
