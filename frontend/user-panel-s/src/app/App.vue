<template>
  <div id="app">
    <AppBar />
    <router-view/>
    <FooterVue />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import '@/assets/style.css'
import AppBar from './general/appBar/AppBar.vue'
import FooterVue from './general/footer/Footer.vue'

export default defineComponent({
  components: { AppBar, FooterVue }
})
</script>

<style lang="scss" scoped>
#app {
  font-family: fsrailway55;
  // -webkit-font-smoothing: antialiased;
  // -moz-osx-font-smoothing: grayscale;
}

h1, h2, h3, h4, h5, h6 {
  font-family: RussianRail!important;;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
