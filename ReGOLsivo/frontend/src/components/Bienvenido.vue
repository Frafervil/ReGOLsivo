<template>
  <div class="Bienvenido">
    <h1>{{ msg }}</h1>
    <h2>{{ msg2 }}</h2>
    <div class="">
    <b-button type="submit" class="btn-large-space" :to="{ name: 'Auth'}">Continuar</b-button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LandingUsuario',

  data () {
    return {
      msg: '¡Bienvenido!',
      msg2: '¡Enhorabuena! acabas de conseguir 20 puntos de karma al registrarte en ReGOLsivo.'
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
