import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/users/Login.vue'
import Feed from '../components/users/Feed.vue'
import Registration from '../components/users/Registration.vue'
import store from '../store.js'
Vue.use(VueRouter)

const user_is_authenticated = (to, from, next) => {
  if(store.state.user_is_logged)
    next();
  else
    next({name: "Login"})
}

  const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: "/feed/",
    name: 'feed',
    component: Feed,
    beforeEnter: user_is_authenticated
  },
  {
    path: "/registration/",
    name: "registration",
    component: Registration
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})



export default router
