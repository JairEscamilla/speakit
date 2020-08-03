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
                post: ""
            }
        },
        methods: {
            sendForm(){
                this.loader=true;
                console.log(this.post);
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