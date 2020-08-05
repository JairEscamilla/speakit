<template>
    <div>
        <v-list>
            <v-list-item>
                <router-link v-bind:to="'profile/'+username" class="user_links">My profile</router-link>
            </v-list-item>
        </v-list>
    </div>
</template>

<script>
    export default{
        data() {
            return {
                username: this.$store.state.username
            }
        },
    }
</script>

<style>
    .user_links{
        text-decoration: none;
    }
</style>