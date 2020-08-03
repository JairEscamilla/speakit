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
                    <NuevoPost @clicked="updatePosts"></NuevoPost>
                </v-col>
                <v-col cols="2" class="links">
                    NUevos links
                </v-col>
            </v-row>

        </v-container>
        <div >
            <ul>
                <li v-for="(item, index) in posts" :key="index">
                    {{ item.post }}
                </li>
            </ul>
        </div>
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
                notifications: []
            }
        },
        components: {
            NuevoPost
        },
        created() {
            console.log(this.$store.state.user_id);
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
        methods: {
            logout(){
                this.$store.commit('update_auth_token', '')
                this.$store.commit('set_username', '')
                this.$store.commit('set_user_is_logged', false)
                this.$router.push({name: "Login"})
            },
            updatePosts(value) {
                console.log("Vamos a actualizar los posts");
                var post = {
                    id: value.data.id,
                    post: value.data.post, 
                    user: value.data.user,
                    created_at: value.data.created_at
                }
                this.posts.unshift(post)
                this.notifications.push("Post was created successfully")
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