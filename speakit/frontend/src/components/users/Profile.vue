<template>
    <div>
        <v-container>
            <v-row no-glutters->
                <v-col cols="2" class="links">
                    Links
                </v-col>

                <v-col cols="12" md="7">
                    <v-card max-width="100%" class="mx-auto">
                        <v-list-item>
                            <v-list-item-avatar color="grey"></v-list-item-avatar>
                            <v-list-item-content>
                                <v-list-item-title class="headline">{{ first_name }}, {{ last_name }}</v-list-item-title>
                                <v-list-item-subtitle>@{{username}}</v-list-item-subtitle>
                                <v-list-item-subtitle class="mt-2 followers">
                                    <p id="followers" class="mr-2">
                                        15 followers 
                                    </p>
                                    <p id="following">
                                        20 following
                                    </p>
                                </v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                        <v-card-text>
                            {{ description }}
                        </v-card-text>
                        
                        <v-card-actions class="actions mb-4">
                            <v-btn @click="redirect_to_edit_profile" text color="deep-purple accent-4" v-if="username === user_logged">
                                Edit my profile
                            </v-btn>
                            <v-btn color="error" class="ml-4 mr-5" v-if="username != user_logged" :disabled="!user_is_logged">Follow</v-btn>
                        </v-card-actions>

                    </v-card>

                    <v-container max-width="90%">
                        <h3>Posts</h3>
                        <Posts v-bind:username="username"/>
                    </v-container>                    

                </v-col>

                <v-col cols="2" class="links">
                    Links
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
    import Posts from './Posts.vue'
    import axios from 'axios'

    export default{
        data() {
            return {
                username: this.$route.params.username,
                user_logged: this.$store.state.username,
                user_is_logged: this.$store.state.user_is_logged,
                first_name: "",
                last_name: "",
                description: ""
            }
        },

        components: {
            Posts
        },

        created() {
            this.get_user_info(this.username)
        },

        methods: {
            redirect_to_edit_profile(){
                this.$router.push({name: "editProfile"})
            },
            
            get_user_info(username){
                axios.get(this.$store.state.api + 'get_users_info/' + username + '/').then((response) => {
                    this.first_name = response.data.first_name.length > 0 ? response.data.first_name : "First name"
                    this.last_name = response.data.last_name.length > 0 ? response.data.last_name : "Last name"
                    this.description = response.data.profile.profile_description.length > 0 ? response.data.profile.profile_description : "Add a description to your speakit profile!"
                }).catch((error) => {
                    console.log(error);
                })
            }
        },

    }
</script>

<style>
    .followers{
        display: flex;
    }
    
    #followers, #following{
        font-weight: bold;
    }

    .actions{
        display: flex;
        justify-content: flex-end;
    }
</style>