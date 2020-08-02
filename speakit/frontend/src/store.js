import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        token: "",
        username: "",
        user_is_logged: false
    },
    mutations: {
        update_auth_token(state, token){
            state.token=token
        },
        set_username(state, username){
            state.username = username
        },
        set_user_is_logged(state, status){
            state.user_is_logged = status;
        }
    }
})

export default store;