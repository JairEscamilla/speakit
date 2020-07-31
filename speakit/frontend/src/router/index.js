import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/users/Login.vue'
import Feed from '../components/users/Feed.vue'

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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
