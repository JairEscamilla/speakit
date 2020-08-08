import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/users/Login.vue'
import Feed from '../components/users/Feed.vue'
import Registration from '../components/users/Registration.vue'
import Profile from '../components/users/Profile.vue'
import store from '../store.js'
import SearchResults from '../components/SearchResults.vue'
import EditProfile from '../components/users/EditProfile.vue'


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
  },
  {
    path: "/profile/:username/",
    name: "profile",
    component: Profile
  },
  {
    path: "/search",
    name: "search",
    component: SearchResults,
    props: (route) => ({ query: route.query.q  })
  },
  {
    path: "/user/profile/edit_profile/",
    name: "editProfile",
    component: EditProfile,
    beforeEnter: user_is_authenticated
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})



export default router
