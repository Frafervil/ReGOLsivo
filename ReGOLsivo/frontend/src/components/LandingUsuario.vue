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
    <b-button size="sm" :to="{name: 'PerfilUsuario', params: {usuarioId: this.$session.get('user_id')}}" variant="primary">
            Perfil
    </b-button>
    <b-button size="sm" :to="{name: 'Logros'}" variant="primary">
            Logros
    </b-button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LandingUsuario',

  mounted() {
    this.checkLoggedIn();
  },

  checkLoggedIn() {
         this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    },

  data () {
    return {
      msg: '¡Bienvenido!'
    }
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
