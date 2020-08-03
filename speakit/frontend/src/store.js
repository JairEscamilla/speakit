import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        token: "",
        username: "",
        user_is_logged: false,
        api: "http://localhost:8000/api/v1.0/",
        user_id: 0
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
        },
        set_user_id(state, id){
            state.user_id = id
        }
    }
})

export default store;