<template>
    <div class="home">
      <p>{{ data }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        // получение переменной из запроса
        data: this.$route.params.id,
      };
    },
  
    methods: {
      
    },
  };
  </script>
  
  <style>
    .home{
      height: 1000px;
    }
  </style>
  
  
  