<template>
    <div>
        Bienvenido a speakit {{ $store.state.username }}!
        <p>
            user is logged? {{ $store.state.user_is_logged }}
        </p>
        {{$store.state.token}}
        <v-btn color="error" @click="logout">Logout</v-btn>
    </div>
</template>

<script>
    export default{
        data() {
            return {
                message: "Welcome"
            }
        },
        created() {
            console.log(this.$store.state.token);
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