<template>
    <v-card color="grey lighten-4" flat tile>
        <v-toolbar dense :dark="true">
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
    
            <v-toolbar-title class="title" @click="redirect_to_feed_or_login">Speakit</v-toolbar-title>
    
            <v-spacer></v-spacer>
    
            <v-btn icon>
                <v-icon>mdi-magnify</v-icon>
            </v-btn>
    
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
                ]
            }
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
            }
        },
    }
</script>

<style>
    .items, .title{
        cursor: pointer;
    }
</style>