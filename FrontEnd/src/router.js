import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from './views/DashboardView.vue'
import ProductsView from './views/ProductsView.vue'

const routes = [
  { path: '/', component: ProductsView },
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})
