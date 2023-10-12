<!-- Отображение сущностей с картинками и маркдовн-->

<template>
  <div class="home">
    <h1>Домашняя страница</h1>
    <button @click="getData()">Кнопка</button>
    <!-- <p>{{ data }}</p> -->
    <template v-for="(women, key) in data" :key="key">
      <p>{{  women.title }}</p>
      <img v-bind:src="women.photo" width="100" height="100">
      <div v-html="markdown(women.myfield)"></div>
      <p>---------------------------------------------------------</p>
    </template>
    
    <p>{{ username }}</p>
    {{ errors }}

    <!-- Проверить авторизован ли юзер -->
    {{ $store.state.isAuthenticated }}

  </div>
</template>

<script>
import axios from "axios";
import { marked } from 'marked';

export default {
  data() {
    return {
      data: "",
      username: "",
      errors: [],
    };
  },

  computed: {
   markdownToHtml(){
    return marked("# Hello");
   }
 },



  // это название страницы в закладках браузера
  mounted() {
        document.title = 'Главная'
    },

  methods: {
    markdown(s){
      return marked(s);
    },

    async getData() {
       // формирую данные, которые отправлю на сервак (json'чик)
      // const formData = {
      //     username: this.username,
      //     password: this.password
      // }

      // отправляю на сервак пост запрос
      await axios
          .get("womenlist/")
          .then(response => {
              this.data = response.data
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
              this.username = response.data
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


