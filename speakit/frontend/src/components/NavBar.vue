<template>
    <v-card color="grey lighten-4" flat tile>
        <v-toolbar dense :dark="true" height="60">
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
    
            <v-toolbar-title class="title" @click="redirect_to_feed_or_login">Speakit</v-toolbar-title>
    
            <v-spacer></v-spacer>
            
            <form class="form mt-7" @submit.prevent="search_user">
                <v-text-field id="search" v-model="search" label="Find a person you know..." solo-inverted></v-text-field>
                <v-btn type="submit" icon>
                    <v-icon>mdi-magnify</v-icon>
                </v-btn>
            </form>

            <v-btn icon>
                <v-icon>mdi-heart</v-icon>
            </v-btn>
            
            <template v-slot:activator="{on, attrs}">
                <v-btn icon v-bind="attrs" v-on="on">
                    <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
            </template>
            


            <v-menu transition="slide-y-transition" bottom>
                <template v-slot:activator="{ on, attrs }">
                    <v-btn icon v-bind="attrs" v-on="on">
                        <v-icon>mdi-dots-vertical</v-icon>
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item class="items">
                        <v-list-item-title @click="redirect_to_profile" >My profile</v-list-item-title>
                    </v-list-item>
                    <v-list-item class="items">
                        <v-list-item-title @click="logout">Logout</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>

        
                

            

        </v-toolbar>
    </v-card>
</template>

<script>
    export default{
        data() {
            return {
                items: [
                    {title: "My profile"},
                    {title: "Logout"}
                ],
                search: ""
            }
        },
        created() {
            console.log("Creando componente!")
        },

        methods: {
            logout() {
                this.$store.commit('update_auth_token', '')
                this.$store.commit('set_username', '')
                this.$store.commit('set_user_is_logged', false)
                this.$router.push({ name: "Login" })
            },
            
            redirect_to_profile(){
                this.$router.push({ name: "profile", params: { username: this.$store.state.username } })
            },

            redirect_to_feed_or_login(){
                if(this.$store.state.user_is_logged)
                    this.$router.push({ name: "feed" })
                else 
                    this.$router.push({ name: "Login" })
            },

            search_user(){
                this.$router.push({name: "search", query: {q: this.search}})
            }
        },
    }
</script>

<style>
    .items, .title{
        cursor: pointer;
    }
    .form{
        display: flex;
    }
    #search{
        padding: 0 !important;
    }
</style>