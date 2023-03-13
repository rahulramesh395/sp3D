<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="App">
    <h1><u>Project Sp3D</u></h1>
    <br/>
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <br/>
    <router-view/>
    <footer>
      &copy; Awesome Project
    </footer>
  </div>
</template>

<style>
container {
		width:10%;  
		height: 100vh;
		border: 2px solid grey;
            }


.logo {
  display: block;
  margin: 0 auto 2rem;
  width: 100vh;
  align: right;
}


</style>
