<template>
  <div>
    <nav class="navbar">
      <div class="nav-left">
        <button @click="toggleMenu" class="hamburger">&#9776;</button>
        <div v-if="menuOpen" class="dropdown-menu">
          <router-link to="/" @click="closeMenu">Productos</router-link>
        </div>
      </div>
    </nav>

    <router-view :searchQuery="searchQuery" :selectedCategory="selectedCategory" />
  </div>
</template>

<script setup>
import { ref } from 'vue';

const menuOpen = ref(false);
const searchQuery = ref('');
const selectedCategory = ref('');

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
};

const closeMenu = () => {
  menuOpen.value = false;
};
</script>

<style>

.navbar {
  background: #1a237e;
  padding: 5px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: white;
}

.hamburger {
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
}

.dropdown-menu {
  position: absolute;
  top: 50px; 
  left: 10px;
  background: white;
  border-radius: 5px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  width: 150px;
  display: flex;
  flex-direction: column;
  z-index: 100;
}

.dropdown-menu a {
  padding: 10px;
  color: black;
  text-decoration: none;
  display: block;
}

.dropdown-menu a:hover {
  background: #ddd;
  border-radius: 5px;
}


</style>
