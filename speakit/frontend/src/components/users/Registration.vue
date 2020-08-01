<template>
    <div>
        <v-container>
            <v-row>
                <v-col class="col-12">
                    <v-card class="mx-auto" max-width="90%">
                        <v-card-title>
                            ¡Register now!
                        </v-card-title>
                        <v-card-text>
                            <form @submit.prevent="submitForm">
                                <div>
                                    <v-text-field label="Username" v-model="form.username" :rules="rules.username">
                                    </v-text-field>
                                </div>
                                <div>
                                    <v-text-field label="Email" v-model="form.email" :rules="rules.email">
                                    </v-text-field>
                                </div>
                                <div>
                                    <v-text-field label="Password" type="password" v-model="form.password" :rules="rules.password">
                                    </v-text-field>
                                </div>
                                <div>
                                    <v-text-field label="Password confirmation" type="password" v-model="form.password_confirmation" :rules="rules.password_confirmation">
                                    </v-text-field>
                                </div>
                                <div>
                                    <v-btn color="primary" type="submit">Register</v-btn>
                                </div>
                            </form>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
    import axios from 'axios';
    export default{
        data() {
            return {
                form: {
                    username: "",
                    email: "",
                    password: "",
                    password_confirmation: ""
                },
                rules: {
                    username: [
                        value => !!value || 'Required',
                        value => (value || '').length <= 100 || 'Max 100 characters'
                    ],
                    email: [
                        value => !!value || 'Required',
                        value => {
                            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                            return pattern.test(value) || 'Invalid email.'
                        }
                    ],
                    password: [
                        value => !! value || 'Required',
                        value => (value || '').length >= 5 || 'Min 5 characters'
                    ],
                    password_confirmation: [
                        value => !(value != this.form.password) || 'Password confirmation is wrong'
                    ]
                },
                token: ""
            }
        },
        methods: {
            submitForm(){
                const API = "http://localhost:8000/api/v1.0/register/";
                axios.post(API, {
                   username: this.form.username,
                   email: this.form.email,
                   password: this.form.password 
                }).then((response) => {
                    alert("Se ha registrado con éxito el nuevo usuario")
                    this.token = response.data.token;
                }).catch((error) => {
                    alert("Ha ocurrido un error");
                    console.log(error);
                })
            }
        },
    }
</script>