<template>
    <div>
        Bienvenido a speakit {{ $store.state.username }}!
        <p>
            user is logged? {{ $store.state.user_is_logged }}
        </p>
        <v-container>
            <v-row no-glutters>
                <v-col cols="2">
                    asd
                </v-col>
                <v-col cols="12" md="7" > 
                    <NuevoPost/>
                </v-col>
                <v-col cols="2">
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
        {{$store.state.token}}
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
                posts: []
            }
        },
        components: {
            NuevoPost
        },
        created() {
            console.log(this.$store.state.token);
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
            }
        },
    }
</script>