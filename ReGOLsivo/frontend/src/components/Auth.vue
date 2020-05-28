<template>
    <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm8 lg4 md5>
          <v-card class="login-card">
            <v-card-title>
              <span class="headline">Iniciar sesión</span>
            </v-card-title>

            <v-spacer/>

            <v-card-text>

              <v-layout
                row
                fill-height
                justify-center
                align-center
                v-if="loading"
              >
                <v-progress-circular
                  :size="50"
                  color="primary"
                  indeterminate
                />
              </v-layout>


              <v-form v-else ref="form" v-model="valid" lazy-validation>
                <v-container>

                  <v-text-field
                    v-model="credentials.username"
                    :counter="70"
                    label="Nombre de usuario"
                    :rules="rules.username"
                    maxlength="70"
                    required
                  />

                  <v-text-field
                    type="password"
                    v-model="credentials.password"
                    :counter="20"
                    label="Contraseña"
                    :rules="rules.password"
                    maxlength="20"
                    required
                  />

                </v-container>
                <v-btn class="pink white--text" :disabled="!valid" @click="login">Acceder</v-btn>

              </v-form>


            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert';
import router from '../router';
export default {
    name: 'Auth',
    data: () => ({
        credentials: {},
        valid:true,
        loading:false,
        rules: {
          username: [
            v => !!v || "El nombre de usuario es necesario",
            v => (v && v.length > 3) || "Un nombre de usuario deber tener más de 3 caracteres de longitud",
            v => /^[a-z0-9_]+$/.test(v) || "Un nombre de usuario debe tener letras y números"
          ],
          password: [
            v => !!v || "La contraseña es necesaria",
            v => (v && v.length > 7) || "La contraseña deber tener más de 7 caracteres de longitud"
          ]
        }
    }),
    methods: {
        login() {
          // checking if the input is valid
            if (this.$refs.form.validate()) {
              this.loading = true;
              axios.post('http://localhost:8000/auth/', this.credentials).then(res => {
                this.$session.start();
                this.$session.set('token', res.data.token);
                router.push('/landingUsuario');
              }).catch(e => {
                this.loading = false;
                swal({
                  type: 'warning',
                  title: 'Error',
                  text: 'Wrong username or password',
                  showConfirmButton:false,
                  showCloseButton:false,
                  timer:3000
                })
              })
            }
        }
    }
}
</script>