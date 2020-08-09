<template>
    <div>
        Editing profile
    </div>
</template>


<script>

    export default{
        data() {
            return {
                profile: []
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
                    console.log("Respuesta del servidor");
                    console.log(data);
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