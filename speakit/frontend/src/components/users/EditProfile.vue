<template>
    <div>
        <v-container>
            <v-row no-glutters>
                <v-col cols="2" class="links">
                    Links
                </v-col>
                <v-col cols="12" md="7">
                    <v-card class="mx-auto" mx-width="90%">
                        <v-card-text class="headline font-weight-bold">
                            Edit your profile!
                        </v-card-text>
                        <v-card-text>
                            <form @submit.prevent="sendForm">
                                <div>
                                    <v-text-field label="First name" v-model="first_name"></v-text-field>
                                </div>
                                <div>
                                    <v-text-field label="Last name" v-model="last_name"></v-text-field>
                                </div>
                                <div>
                                    <v-text-field label="Email" v-model="email" :rules="rules"></v-text-field>
                                </div>
                                <div>
                                    <v-textarea label="Profile description"  color="teal" v-model="bio"></v-textarea>
                                </div>
                                <v-btn type="submit" :loading="loading" :disabled="loading" color="blue-grey" class="ma-2 white--text">
                                    Save
                                    <v-icon right dark>mdi-checkbox-marked-circle</v-icon>
                                </v-btn>
                            </form>
                        </v-card-text>
                    </v-card>
                </v-col>
                <v-col cols="2" class="links">
                    Links
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>


<script>
    import axios from 'axios'

    export default{
        data() {
            return {
                first_name: "",
                last_name: "",
                email: "",
                bio: "",
                loading: false,
                rules: [
                    v => !!v || 'Email is required',
                    v => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        this.email_is_valid = pattern.test(v);
                        return pattern.test(v) || 'Invalid email.'
                    }
                ],
                email_is_valid: false
            }
        },

        methods: {
            get_user_profile_info(){
                fetch(this.$store.state.api+'get_users_info/' + this.$store.state.username + '/', {
                    method: 'GET',
                    headers: {
                        Authorization: 'Token ' + this.$store.state.token
                    }
                }).then((response) => response.json())
                .then((data) => {
                    this.first_name = data.first_name
                    this.last_name = data.last_name
                    this.email = data.email
                    this.bio = data.profile.profile_description
                }).catch((error) => {
                    console.log("Ha ocurrido un error");
                    console.log(error);
                })
            },

            sendForm(){
                if(!this.email_is_valid || this.email.length <= 0)
                    return;
                
                axios.put(this.$store.state.api + 'get_users_info/' + this.$store.state.username + '/', {
                    email: this.email,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    profile: {
                        profile_description: this.bio
                    },
                    username: this.$store.state.username
                }, {
                    headers: {
                        Authorization: 'Token ' + this.$store.state.token
                    }
                }).then((response) => {
                    console.log("Respuesta del servidor...");
                    console.log(response);
                    this.$notify({
                            group: 'foo',
                            title: 'New notification',
                            text: 'Your profile has been updated!', 
                            type: 'success'
                    });
                }).catch(() => {
                    this.$notify({
                        group: "foo",
                        title: "New notification",
                        text: "An error has occurred, try it later",
                        type: "error"
                    })
                })
            }
        },

        created() {
            this.get_user_profile_info()
        },
    }
</script>