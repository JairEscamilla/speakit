<template>
    <div>
        <form @submit.prevent="submitForm">
            <div>
                <label for="username">Username: </label>
                <input type="text" name="username" id="username" v-model="form.username">
            </div>
            <div>
                <label for="password">Password: </label>
                <input type="password" name="password" id="password" v-model="form.password">
            </div>
            <button type="submit">Entrar</button>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';
    export default{
        data() {
            return {
                message: "Pruebas",
                form: {
                    username: "",
                    password: ""
                },
                token: ""
            }
        },
        methods: {
            submitForm(){
                const API = "http://127.0.0.1:8000/api/v1.0/login/";
                axios.post(API, {
                    username: this.form.username,
                    password: this.form.password
                }).then((response) => {
                    this.token = response.data.token;
                    window.location.href = "/feed";
                }).catch(() => {
                    alert("Verifica que tus datos sean correctos");
                })
            }
        },
    }
</script>