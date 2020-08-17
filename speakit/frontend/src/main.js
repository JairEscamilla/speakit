import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import store from './store.js'
import Notifications from 'vue-notification'
import infiniteScroll from 'vue-infinite-scroll'

Vue.config.productionTip = false

Vue.use(Notifications)
Vue.use(infiniteScroll)

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
