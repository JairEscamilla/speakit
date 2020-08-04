<template>
    <div>
        <template v-for="(notification, index) in notifications">
            <v-alert type="success" dismissible :key="index">
                {{ notification }}
            </v-alert>
        </template>
        <v-container>
            <v-row no-glutters>
                <v-col cols="2" class="links">
                    asd
                </v-col>
                <v-col cols="12" md="7" > 
                    <NuevoPost @new_post="updatePosts" @send_notification="add_notification" class="mb-10"></NuevoPost>
                    <div v-for="(item, index) in posts" :key="index" class="mb-15">
                        <v-card class="mx-auto" mx-width="90%">
                            <v-card-text class="headline font-weight-bold">
                                {{ item.post }}
                            </v-card-text>
                            <v-card-actions>
                                <v-list-item class="grow">
                                    <v-list-item-avatar color="grey">
                                        <v-img class="elevation-6"
                                            src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light">
                                        </v-img>
                                    </v-list-item-avatar>
                                    <v-list-item-content>
                                        <v-list-item-title>Username</v-list-item-title>
                                    </v-list-item-content>
                                    <v-row align="center" justify="end">
                                        <v-icon class="mr-1">mdi-heart</v-icon>
                                        <span class="subheading mr-2">256</span>
                                        <span class="mr-1">·</span>
                                        <v-icon class="mr-1">mdi-share-variant</v-icon>
                                        <span class="subheading">45</span>
                                    </v-row>
                                </v-list-item>
                            </v-card-actions>
                        </v-card>
                    </div>
                </v-col>
                <v-col cols="2" class="links">
                    NUevos links
                </v-col>
            </v-row>

        </v-container>
        <v-btn color="error" @click="logout">Logout</v-btn>
    </div>
</template>

<script>
    import axios from 'axios';
    import NuevoPost from '../forms/NewPost.vue'
    export default{
        data() {
            return {
                message: "Welcome",
                posts: [],
                notifications: [], 
            }
        },
        components: {
            NuevoPost
        },
        created() {
            this.getPosts();
          

        },
        methods: {
            logout(){
                this.$store.commit('update_auth_token', '')
                this.$store.commit('set_username', '')
                this.$store.commit('set_user_is_logged', false)
                this.$router.push({name: "Login"})
            },
            updatePosts(post) {
                this.posts.unshift(post)
            }, 
            getPosts(){
                // Cargando los posts
                axios.get(this.$store.state.api + 'posts/', {
                    headers: {
                        Authorization: 'Token ' + this.$store.state.token
                    }
                }).then((response) => {
                    this.posts = response.data
                }).catch((error) => {
                    console.log("Ha ocurrido un error");
                    console.log(error);
                })
            },
            add_notification(notification){
                this.notifications.push(notification)
            }
        },
        
    }
</script>

<style>
    @media screen and (max-width: 800px){
        .links{
            display: none;
        }
    }
</style>