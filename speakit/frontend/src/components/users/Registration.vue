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
                this.username_errors = [];
                var info = {username: val}
                var data = new FormData();
                data.append("json", JSON.stringify(info))
                
                fetch(this.$store.state.api + 'validate_username/', {
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
                this.email_errors = [];
                var info = {email: val}
                var data = new FormData();
                data.append("json", JSON.stringify(info));

                fetch(this.$store.state.api + 'validate_email/', {
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
                if(!this.password_confirmation_is_validated || !this.email_is_validated || !this.username_is_validated || this.form.password.length < 5)
                    return;
                axios.post(this.$store.state.api + 'register/', {
                   username: this.username,
                   email: this.email,
                   password: this.form.password 
                }).then((response) => {
                    this.token = response.data.token;
                    this.$store.commit('update_auth_token', this.token);
                    this.$store.commit('set_username', this.username)
                    this.$store.commit('set_user_is_logged', true)
                    this.$store.commit('set_user_id', response.data.user.id)
                    this.$router.push({name: "feed"})
                }).catch((error) => {
                    swal("Verifica que tus datos sean correctos", "", "error")
                    console.log(error);
                })
            },
        },
    }
</script>