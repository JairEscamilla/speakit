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
                                    <v-text-field autocomplete="off" label="Username" v-model="username" :error-messages="username_errors" :rules="rules.username">
                                    </v-text-field>
                                </div>
                                <div>
                                    <v-text-field label="Email" v-model="email" :rules="rules.email" :error-messages="email_errors">
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
                username: "",
                email: "",
                form: {
                    email: "",
                    password: "",
                    password_confirmation: ""
                },
                username_errors: [],
                email_errors: [],
                rules: {
                    username: [
                        value => !!value || 'Required',
                        value => (value || '').length <= 100 || 'Max 100 characters',
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
                        value => {
                            this.password_confirmation_is_validated = value === this.form.password;
                            return !(value != this.form.password) || 'Password confirmation is wrong'
                        }
                    ]
                },
                token: "",
                username_is_validated: false,
                password_confirmation_is_validated: false,
                email_is_validated: false
            }
        },
        watch: {
            username(val){
                const API = "http://localhost:8000/api/v1.0/validate_username/";
                this.username_errors = [];
                var info = {username: val}
                var data = new FormData();
                data.append("json", JSON.stringify(info))
                
                fetch(API, {
                    method: "POST",
                    body: data
                }).then((response) => response.json())
                .then((data) => {
                    this.username_is_validated = data.validated;
                    if(!this.username_is_validated)
                        this.username_errors.push("Username is already taken")
                })
            },
            email(val){
                const API = "http://localhost:8000/api/v1.0/validate_email/";
                this.email_errors = [];
                var info = {email: val}
                var data = new FormData();
                data.append("json", JSON.stringify(info));

                fetch(API, {
                    method: "POST",
                    body: data
                }).then((response) => response.json())
                .then((data) => {
                    this.email_is_validated = data.validated;
                    if(!this.email_is_validated)
                        this.email_errors.push("Email  is already taken")
                })
            }
        },
        methods: {
            submitForm(){
                const API = "http://localhost:8000/api/v1.0/register/";
                if(!this.password_confirmation_is_validated || !this.email_is_validated || !this.username_is_validated)
                    return;
                axios.post(API, {
                   username: this.username,
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
        },
    }
</script>