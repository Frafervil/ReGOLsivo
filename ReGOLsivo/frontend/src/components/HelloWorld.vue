<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="">
    <h2>Usuarios</h2>
    <b-button size="sm" :to="{name: 'RegistrarUsuario'}" variant="primary">
            Registrarse
    </b-button>
    <b-button size="sm" :to="{name: 'CreateUsuario'}" variant="primary">
            Iniciar sesión
    </b-button>
    <b-button size="sm" :to="{name: 'CreateUsuario'}" variant="primary">
            Pronosticador
    </b-button>
    </div>
    <br>
    <h2>Administradores</h2>
    <b-button size="sm" :to="{name: 'CreateUsuario'}" variant="primary">
            Iniciar sesión
    </b-button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
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
