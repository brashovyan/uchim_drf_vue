<template>
    <header>
        <p><router-link to="/app">Home</router-link></p>
        <p><router-link to="/app/about">About</router-link></p>

        <!-- Если челик авторизован -->
        <template v-if="$store.state.isAuthenticated">
            <button @click="logout()">Logout</button>
            {{ errors }}
        </template>

        <!-- Если челик неавторизован -->
        <template v-else>
            <p><router-link to="/app/login">Login</router-link></p>
            <p><router-link to="/app/register">Register</router-link></p>
        </template>
    </header>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      errors: [],
    };
  },

  methods: {
    async logout() {

        // отправляю на сервак пост запрос, что хочу разлогиниться
        await axios
                .post("auth/token/logout/")

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

        // обнуляю дефолтный хэдер
        axios.defaults.headers.common["Authorization"] = "";

        // обнуляю localStorage
        localStorage.removeItem("token");

        // удаляю токен из store
        this.$store.commit('removeToken');

        // перезагружаю страницу, чтобы всё отчистилось
        window.location.reload();
    },
  },
};
</script>

<style>
    header{
        background-color: aqua;
        width: 100%;
        height: 100%;
        margin-top: -8px;
        display: flex;
    }

    p{
        margin: 5px;
    }



</style>