<!-- Добавление одной картинки -->
<!-- про маркдовн -->
<!-- крч, помимо npm install marked устанавливаем npm install @babel/plugin-transform-private-methods --save-dev -->
<!-- и в babel.config.js вписываем "plugins": ["@babel/plugin-transform-private-methods"] -->
<!-- Но маркдовн без картинок( -->
<!-- В теории надо вылавливать когда челик перетаскивает картинку, отправлять и сохранять её на сервак, возвращать картинку -->
<!-- в джанго админке это уже из коробки, тут надо мучиться -->

<template>
  <div class="about">
    <h1>Добавь женщину)</h1>
    <input type="text" v-model="title">
    <input type="file" accept="image/*,image/jpeg" id="file">
    
    <textarea v-model="markdown" id="textArea"></textarea>
    <div v-html="markdownToHtml"></div>


    <button @click="create()">Создать</button>
    {{ data }}
    {{ errors }}
  </div>
</template>

<script>
import axios from "axios";
import { marked } from 'marked';

export default {
  data() {
    return {
      title: "",
      errors: [],
      data: "",
      markdown:  "",
    };
  },

  computed: {
   markdownToHtml(){
     return marked(this.markdown);
   }
 },

  mounted() {
  },

  methods: {
    async create() {
  
      var imagefile = document.querySelector('#file').files[0];
      var formData = new FormData()
        formData.append("title", this.title)
        formData.append("photo", imagefile)
        formData.append("myfield", this.markdown)

      await axios
          .post("womenlist/", formData)
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
    },
  },
}
</script>

