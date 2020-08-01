import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/users/Login.vue'
import Feed from '../components/users/Feed.vue'
import Registration from '../components/users/Registration.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: "/feed/",
    name: 'feed',
    component: Feed
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
