<template>
  <div class="landingPage">
    <h1>{{ msg }}</h1>
    <div class="">
    <b-button size="sm" :to="{name: 'CreateUsuario'}" variant="primary">
            Registrarse
    </b-button>
    <b-button size="sm" :to="{name: 'Auth'}" variant="primary">
            Iniciar sesión
    </b-button>
    <b-button size="sm" :to="{name: 'ListPartido'}" variant="primary">
            Partidos
    </b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  data () {
    return {
      msg: '¡Bienvenido a ReGOLsivo!'
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
