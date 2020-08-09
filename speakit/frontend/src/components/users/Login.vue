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
                                    <v-btn color="primary" type="submit" :loading="loader" :disabled="loader">Iniciar sesión</v-btn>
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
                token: "",
                loader: false
            }
        },
        methods: {
            submitForm(){
                this.loader = true
                axios.post(this.$store.state.api + 'login/', {
                    username: this.form.username,
                    password: this.form.password
                }).then((response) => {
                    this.token = response.data.token;
                    this.$store.commit('update_auth_token', this.token)
                    this.$store.commit('set_username', this.form.username)
                    this.$store.commit('set_user_is_logged', true)
                    var info = {username: this.form.username}
                    var data = new FormData();
                    data.append("json", JSON.stringify(info))
                    fetch(this.$store.state.api + 'get_user_id/', {
                        method: "POST",
                        body: data,
                        headers: {
                            Authorization: 'Token ' + this.$store.state.token
                        }
                    }).then((response) => response.json())
                    .then((data) => {
                        this.$store.commit('set_user_id', data.id);
                        this.$router.push({ name: "feed" });
                    })
                }).catch(() => {
                    this.$notify({
                        group: "foo",
                        title: "New notification!",
                        text: "Your credentials are wrong",
                        type: "error"
                    })                   
                    this.loader = false
                })
            },
        },
    }
</script>