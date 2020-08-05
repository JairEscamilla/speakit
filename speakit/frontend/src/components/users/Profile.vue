<template>
    <div>
        <v-container>
            <v-row no-glutters->
                <v-col cols="2" class="links">
                    Links
                </v-col>

                <v-col cols="12" md="7">
                    <v-card max-width="100%" class="mx-auto">
                        <v-list-item>
                            <v-list-item-avatar color="grey"></v-list-item-avatar>
                            <v-list-item-content>
                                <v-list-item-title class="headline">First name, Last name</v-list-item-title>
                                <v-list-item-subtitle>@username</v-list-item-subtitle>
                                <v-list-item-subtitle class="mt-2 followers">
                                    <p id="followers" class="mr-2">
                                        15 followers 
                                    </p>
                                    <p id="following">
                                        20 following
                                    </p>
                                </v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                        <v-card-text>
                            "Add a description to your speakit profile!"
                        </v-card-text>
                        
                        <v-card-actions class="actions mb-4">
                            <v-btn text color="deep-purple accent-4">
                                Edit my profile
                            </v-btn>
                            <v-btn color="error" class="ml-4 mr-5">Follow</v-btn>
                        </v-card-actions>

                    </v-card>

                    <v-container max-width="90%">
                        <h3>Posts</h3>
                    </v-container>                    

                </v-col>

                <v-col cols="2" class="links">
                    Links
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<style>
    .followers{
        display: flex;
    }
    
    #followers, #following{
        font-weight: bold;
    }

    .actions{
        display: flex;
        justify-content: flex-end;
    }
</style>