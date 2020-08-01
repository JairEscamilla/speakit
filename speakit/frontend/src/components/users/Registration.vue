<template>
    <div>
        <v-container>
            <v-row>
                <v-col class="col-12">
                    <v-card class="mx-auto" max-width="90%">
                        <v-card-title>
                            Register now!
                        </v-card-title>
                        <v-card-text>
                            <form @submit.prevent="submitForm">
                                <div>
                                    <v-text-field label="Username" v-model="form.username" @keyup="validateUsername">
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
    import swal from 'sweetalert'
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
                        value => (value || '').length <= 100 || 'Max 100 characters',
                        value => (this.validateUsername(value)) || 'Username is already taken'
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
                token: "",
                username_is_validated: Boolean
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
                    swal("Se ha registrado con éxito el nuevo usuario", "", "success")
                    this.token = response.data.token;
                }).catch((error) => {
                    swal("Verifica que tus datos sean correctos", "", "error")
                    console.log(error);
                })
            },
            
            validateUsername(){
                const API = "http://localhost:8000/api/v1.0/validate_username/";

                var payload = {
                    username: "jair"
                };

                var data = new FormData();
                data.append("json", JSON.stringify(payload));

                fetch(API,
                    {
                        method: "POST",
                        body: data
                    })
                    .then(function (res) { return res.json(); })
                    .then(function (data) { alert(JSON.stringify(data)) })
            },
        },
    }
</script>