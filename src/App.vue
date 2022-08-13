<template>
  <router-view 
  :class="{dark:dol=='dark',light:dol=='light'}"
  :theme="dol"
  @changeTheme="changeTheme"
  ></router-view>
</template>


<script>
export default {
  name: 'App',
  data(){
    return {
      dol: 'dark' //dark or light
    }
  },
  methods: {
    changeTheme(){
      this.dol = this.dol=='dark'?'light':'dark'
    }
  },
  }
</script>



<style>
@import './styles/style.css';
@import './styles/theme.css';
</style>