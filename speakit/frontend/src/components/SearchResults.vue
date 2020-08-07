<template>
    <div>

        <v-container>
            <v-row no-glutters>
                <v-col cols="2" class="links">
                    Links
                </v-col>

                <v-col cols="12" md="7">
                    <h3>
                        Results for: {{ this.query }}
                    </h3>
                    <div class="users-container">
                        <div v-for="(user, index) in results" :key="index">
                            <v-card max-width="90%" class="mx-auto">
                                <v-list-item>
                                    <v-list-item-avatar color="grey"></v-list-item-avatar>
                                    <v-list-item-content>
                                        <v-list-item-title class="headline">{{ user.first_name }} {{ user.last_name }}</v-list-item-title>
                                        <v-list-item-subtitle>@{{user.username}}</v-list-item-subtitle>
                                    </v-list-item-content>
                                </v-list-item>
                    
                                <v-card-text>
                                    "Profile description"
                                </v-card-text>
                    
                                <v-card-actions class="actions mb-4">
                                    <v-btn text color="deep-purple accent-4" v-on:click="redirect_to_profile(user.username)">
                                        View profile
                                    </v-btn>
                                    <v-btn color="error" class="ml-4 mr-5" v-bind:disabled="username == user.username" v-if="user_is_logged">Follow</v-btn>
                                </v-card-actions>
                            </v-card>
                        </div>
                    </div>
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
                results: [],
                username: this.$store.state.username,
                user_is_logged: this.$store.user_is_logged
            }
        },
        props: {
            query: String
        },
        created() {
            this.getUsers(this.query)
            console.log(this.username);
        },
        updated() {
            this.getUsers(this.query)
        },
        methods: {
            getUsers(search){
                var info = {user: search}
                var data = new FormData()
                data.append("json", JSON.stringify(info))

                fetch(this.$store.state.api + 'search_users/', {
                    method: "POST",
                    body: data 
                }).then((response) => response.json())
                .then((data) => {
                    this.results = data
                })
            },

            redirect_to_profile(username){
                this.$router.push({name: "profile", params: {username: username}})
            }
        },
    }
</script>