<template>
  <div class="home">
    <h1>Домашняя страница</h1>
    <button @click="getData()">Кнопка</button>
    <p>{{ data }}</p>
    <p>{{ username }}</p>
    {{ errors }}

    <!-- Проверить авторизован ли юзер -->
    {{ $store.state.isAuthenticated }}

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      data: "",
      username: "",
      errors: [],
    };
  },

  // это название страницы в закладках браузера
  mounted() {
        document.title = 'Главная'
    },

  methods: {
    async getData() {
       // формирую данные, которые отправлю на сервак (json'чик)
      // const formData = {
      //     username: this.username,
      //     password: this.password
      // }

      // отправляю на сервак пост запрос
      await axios
          .get("tasks/")
          .then(response => {
              this.data = response.data.tasks
          })
          // здесь обрабатываем ошибки
          .catch(error => {
              if (error.response) {
                  for (const property in error.response.data) {
                      this.errors.push(`${property}: ${error.response.data[property]}`)
                  }
              } else {
                  this.errors.push('Something went wrong. Please try again')
                  
                  console.log(JSON.stringify(error))
              }
          })

          // отправляю на сервак пост запрос
      await axios
          .get("auth/users/me/")
          .then(response => {
              this.username = response.data.username
          })
          // здесь обрабатываем ошибки
          .catch(error => {
              if (error.response) {
                  for (const property in error.response.data) {
                      this.errors.push(`${property}: ${error.response.data[property]}`)
                  }
              } else {
                  this.errors.push('Something went wrong. Please try again')
                  
                  console.log(JSON.stringify(error))
              }
          })
    },
  },
};
</script>

<style>
  .home{
    height: 1000px;
  }
</style>


