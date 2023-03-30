<template>

<form v-if="!TOKEN_GETTER" id="auth_form">
    <h2>Авторизация</h2>
    <label for="auth_login">Логин</label>
    <input v-model="username" id="auth_login" type="text" placeholder="Введите логин">
    <label for="auth_pass">Пароль</label>
    <input v-model="password" id="auth_pass" type="text" placeholder="Введите пароль">
    <button @click="auth" type="button">Войти</button>
</form>
<form v-else id="auth_form">
  Привет, {{ username }}
  <button @click="out('')" type="button" class="btn_logout">Выход</button>
</form>
</template>

<script>
import axios from 'axios'
import { ref } from 'vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'Auth',
  setup() {
    const username = ref(localStorage.getItem('user'))
    const password = ref('')

    return {
      username,
      password,
    }
  },

  computed: {
    ...mapGetters(['TOKEN_GETTER'])
  },
  
  methods: {
    ...mapActions(['TOKEN_ACTION']),

    // Авторизация пользователя
    async auth() {
      const data = {
          username: this.username,
          password: this.password
      }
      const response = await axios.post('http://127.0.0.1:8000/auth/token/login/', data)
      .then(response => {
          console.log(`Успешно ${response.data}`) // Обработка успешного ответа
          this.TOKEN_ACTION(`Token ${response.data['auth_token']}`)
          localStorage.setItem('token', `Token ${response.data['auth_token']}`)
          localStorage.setItem('user', this.username)
      })
      .catch(error => {
          console.error(`Неудача ${error}`) // Обработка ошибки
      })
      const instance = axios.create({
                headers: {'Authorization': localStorage.getItem('token')}
          });
      const log = await instance.get('http://127.0.0.1:8000/userinfo/')
      console.log(log)
      localStorage.setItem('id', log.data['id'])
    },

    // Выход пользователя из личного кабинета
    async out(token) {
      const instance = axios.create({
                headers: {'Authorization': localStorage.getItem('token')}
            });
      const logout = await instance.post('http://127.0.0.1:8000/auth/token/logout/')
      localStorage.removeItem('user')
      localStorage.removeItem('token')
      this.username = ''
      this.password = ''
      this.TOKEN_ACTION(token)
    },
  }

}
</script>

<style>
form button {
  margin: 10px 10% 0 10%;
  width: 80%;
}

.btn_logout {
width: 100%;
margin: 20px 0px 0px 0px;
}
</style>