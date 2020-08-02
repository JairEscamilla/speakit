import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        token: ""
    },
    mutations: {
        update_auth_token(state, token){
            state.token=token
        }
    }
})

export default store;