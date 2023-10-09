<template style="margin: 0;">
  <Header></Header>

  <div>
   <router-view />
  </div>

   <Footer></Footer>
</template>

<script>
  import Header from './components/TheHeader.vue'
  import Footer from './components/TheFooter.vue'
  export default {
  
  components: {
    Header,
    Footer
  }
  }
</script>

<style>
    #app {
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
      margin-top: -8px;
      margin-left: -8px;
      margin-right: -8px;
      margin-bottom: -8px;
      padding: 0;
    }

</style>