<template>
  <v-app>
    <Navbar></Navbar>
    <router-view></router-view>
    <notifications group="foo"/>
  </v-app>
</template>

<script>

import Navbar from './components/NavBar.vue'

export default {
  name: 'App',

  components: {
    Navbar
  },

  data: () => ({
    //
  }),
};
</script>
