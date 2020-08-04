<template>
    <div>
        <form @submit.prevent="sendForm"> 
            <v-textarea v-model="post" label="Share something with the community..."></v-textarea>
            <div class="button-container">
                <v-btn type="submit" class="ma-2" :loading="loader" :disabled="loader" color="primary">
                    Publish
                    <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
                </v-btn>
            </div>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';
    export default{
        data() {
            return {
                loader: false,
                post: "", 
                connection: null
            }
        },
        methods: {
            sendForm(){
                this.loader=true;
                axios.post(this.$store.state.api + 'posts/', {
                    post: this.post,
                    user: this.$store.state.user_id,
                    headers: {
                        Authorization: 'Token ' + this.$store.state.token
                    }
                }).then((data) => {
                    this.loader = false
                    this.$emit('clicked', data)
                    var post = JSON.stringify({'post': this.post, 'username': this.$store.state.username})
                    this.post = ""
                    this.connection.send(post)
                }).catch(() => {
                    console.log("Ha ocurrido un error");
                    this.loader = false
                })
            }
        },
        created() {
                this.connection = new WebSocket('ws://localhost:8000/ws/feed/feed/')
                this.connection.onmessage = function (event) {
                    console.log("Nuevo post");
                    console.log(event.data);
                }

                this.connection.onopen = function (event) {
                    console.log(event);
                    console.log("Successfully connected to echo websocket server...");
                }
        },
    }
</script>

<style lang="css" scoped> 
    .button-container{
        display: flex;
        align-items: flex-end;
        justify-content: flex-end;
    }
</style>