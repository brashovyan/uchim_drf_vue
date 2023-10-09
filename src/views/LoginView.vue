<template>
    <div>
        <input v-model="username" type="text">
        <input v-model="password" type="password">
        <button @click="login()">Войти</button>
        {{ errors }}
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },

    // это название страницы в закладках браузера
    mounted() {
        document.title = 'Авторизация'
    },

    methods: {
        async login() {
            // обнуляю дефолтный хэдер
            axios.defaults.headers.common["Authorization"] = ""

            // обнуляю localStorage
            localStorage.removeItem("token")

            // формирую данные, которые отправлю на сервак (json'чик)
            const formData = {
                username: this.username,
                password: this.password
            }

            // отправляю на сервак пост запрос
            await axios
                .post("auth/token/login/", formData)
                .then(response => {

                    // когда я получаю ответ, то извлекаю токен
                    const token = response.data.auth_token

                    // сохраняю его в localStorage (т.е. вызываю store/index.js/SetToken)
                    this.$store.commit('setToken', token)
                    
                    // ставлю дефолтный хэдер
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    // сохраняю его в классический localStorage
                    localStorage.setItem("token", token)

                    // перенаправляю его на главную страницу
                    this.$router.push('/')

                    // console.log(token);
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
        }
    }
}
</script>