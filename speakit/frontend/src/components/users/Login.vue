<template>
    <div>
        <v-app id="login"> 
            <v-container class="">
                <v-row>
                    <v-col class="col-12">
                        <v-card class="mx-auto" max-width="90%">
                            <v-card-text>
                                <div class="display-1 text--primary">
                                    Inica sesión
                                </div>
                                <form class="mt-4" @submit.prevent="submitForm">
                                    <div>
                                        <v-text-field label="Username" v-model="form.username"></v-text-field>
                                    </div>
                                    <div>
                                        <v-text-field label="Password" type="password" v-model="form.password"></v-text-field>
                                    </div>
                                    <v-btn color="primary" type="submit">Iniciar sesión</v-btn>
                                </form>
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-app>
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
                    this.$store.commit('update_auth_token', this.token)
                    this.$store.commit('set_username', this.form.username)
                    this.$store.commit('set_user_is_logged', true)
                    this.$router.push({name: "feed"});
                }).catch(() => {
                    alert("Verifica que tus datos sean correctos");
                })
            },
        },
    }
</script>