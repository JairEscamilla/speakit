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
                this.loader = true;
                if(this.post.length <= 0){
                    this.loader = false;
                    return;
                }
                var post = JSON.stringify({'post': this.post, 'username': this.$store.state.username})
                this.post = ""
                this.connection.send(post)
                 this.$notify({
                    group: 'foo',
                    title: 'New notification',
                    text: 'Post was created successfully!',
                    type: 'success'
                });
            }
        },
        created() {
                this.connection = new WebSocket('ws://192.168.1.79:8000/ws/feed/feed/')
                this.connection.onmessage = (event) => {
                    var info = JSON.parse(event.data)
                    var data = {
                        post: info.post,
                        user: {
                            username: info.username
                        }
                    };
                    this.$emit('new_post', data)
                    this.loader = false
                }

                this.connection.onopen = () => {
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