<template>
  <div id="app">
   {{msg}}
   <Form />
  </div>
</template>

<script>
import Form from './components/Form'

export default {
  name: 'App',
  data() {
    return {
      msg: ' Please fiil the form:'
    }
  },
  components: {
    Form,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
