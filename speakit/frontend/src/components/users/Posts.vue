<template>
    <div class="posts">
                            <div v-for="(item, index) in posts" :key="index" class="mb-15">
                                <v-card class="mx-auto" mx-width="90%">
                                    <v-card-text class="headline font-weight-bold">
                                        {{ item.post }}
                                    </v-card-text>
                                    <v-card-actions>
                                        <v-list-item class="grow">
                                            <v-list-item-avatar color="grey">
                                                <v-img class="elevation-6"
                                                    src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light">
                                                </v-img>
                                            </v-list-item-avatar>
                                            <v-list-item-content>
                                                <v-list-item-title>{{username}}</v-list-item-title>
                                            </v-list-item-content>
                                            <v-row align="center" justify="end">
                                                <v-icon class="mr-1">mdi-heart</v-icon>
                                                <span class="subheading mr-2">256</span>
                                                <span class="mr-1">·</span>
                                                <v-icon class="mr-1">mdi-share-variant</v-icon>
                                                <span class="subheading">45</span>
                                            </v-row>
                                        </v-list-item>
                                    </v-card-actions>
                                </v-card>
                            </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default{
        data() {
            return {
                posts: [],
            }
        },
        props: {
            username: {
                type: String
            }
        },

        created() {
            this.get_user_posts(this.$props.username);
        },

        methods: {
            get_user_posts(username){
                axios.get(this.$store.state.api + 'posts_by_user/?search=' + username).then((response) => {
                    this.posts = response.data
                }).catch((error) => {
                    console.log("Ha ocurrido un error");
                    console.log(error);
                })
            }
        },
    }
</script>