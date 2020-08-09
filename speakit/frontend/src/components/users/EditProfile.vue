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
                            <form>
                                <div>
                                    <v-text-field label="First name" v-model="first_name"></v-text-field>
                                </div>
                                <div>
                                    <v-text-field label="Last name" v-model="last_name"></v-text-field>
                                </div>
                                <div>
                                    <v-text-field label="Email" v-model="email"></v-text-field>
                                </div>
                                <div>
                                    <v-textarea label="Profile description"  color="teal" v-model="bio"></v-textarea>
                                </div>
                                <v-btn :loading="loading" :disabled="loading" color="blue-grey" class="ma-2 white--text">
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

    export default{
        data() {
            return {
                first_name: "",
                last_name: "",
                email: "",
                bio: "",
                loading: false
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
            }
        },

        created() {
            this.get_user_profile_info()
        },
    }
</script>