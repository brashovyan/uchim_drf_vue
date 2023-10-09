<template>
  <div class="home">
    <h1>Домашняя страница</h1>
    <button @click="getData()">Кнопка</button>
    <p>{{ data }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      data: "",
    };
  },

  methods: {
    getData() {
      axios.get('http://127.0.0.1:8001/api/v1/all_tasks/').then(response => (this.data = response.data));
    },
  },
};
</script>

<style>
  .home{
    height: 1000px;
  }
</style>


