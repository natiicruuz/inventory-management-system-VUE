<template>
  <div>
    <h1>Listado de Productos</h1>

    <button @click="showEntry = true">Entrada de Producto</button>
    <button @click="showOutput = true">Salida de Producto</button>

    <!-- Contenedor de productos -->
    <div class="product-grid">
      <div v-for="product in inventory" :key="product.id" class="product-card" @click="fetchProductDetails(product.id)">
        <img :src="product.image" alt="Imagen del producto" class="product-image" />
        <h3>{{ product.nombre }}</h3>
        <p class="price">${{ product.precio }}</p>
        <p class="stock" :style="{ color: product.disponible ? 'green' : 'red' }">
          {{ product.disponible ? `Disponible (${product.stock})` : 'Agotado' }}
        </p>
      </div>
    </div>

    <ProductEntry v-model:show="showEntry" :inventory="inventory" @stockAdded="updateStock" />
    <ProductOutput v-model:show="showOutput" :inventory="inventory" @stockRemoved="updateStock" />

    <!-- Modal de Producto -->
    <ProductModal v-if="showModal" :show="showModal" :product="selectedProduct" @close="showModal = false" />
  </div>
</template>

<script setup>
import { reactive, ref, onMounted, watch } from "vue";
import ProductEntry from "../components/ProductEntry.vue";
import ProductOutput from "../components/ProductOutput.vue";
import ProductModal from "../components/ProductModal.vue";

const inventory = reactive([]);
const showEntry = ref(false);
const showOutput = ref(false);
const showModal = ref(false);
const selectedProduct = ref({});

// Cargar productos desde la API
const fetchProducts = async () => {
  try {
    const response = await fetch("https://fakestoreapi.com/products");
    const data = await response.json();

    data.forEach((product) => {
      inventory.push({
        id: product.id,
        nombre: product.title,
        precio: product.price,
        stock: 5,  
        disponible: true, 
        image: product.image,
      });
    });
  } catch (error) {
    console.error("Error al obtener productos:", error);
  }
};

// Obtener detalles de un producto por ID
const fetchProductDetails = async (productId) => {
  try {
    const response = await fetch(`https://fakestoreapi.com/products/${productId}`);
    selectedProduct.value = await response.json();
    showModal.value = true;
  } catch (error) {
    console.error("Error al obtener detalles del producto:", error);
  }
};

// Detectar cambios en stock con watch()
watch(
  inventory,
  (newInventory) => {
    newInventory.forEach((product) => {
      product.disponible = product.stock > 0;
    });
  },
  { deep: true }
);

const updateStock = ({ product, quantity }) => {
  const item = inventory.find((p) => p.id === product.id);
  if (item) {
    item.stock += quantity;
    item.disponible = item.stock > 0;
  }
};

onMounted(fetchProducts);
</script>

<style>
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 20px;
  margin-left: 50px;
  margin-right: 50px;
}
.product-card {
  border: 1px solid #ddd;
  padding: 15px;
  text-align: center;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s;
}
.product-card:hover {
  transform: scale(1.05);
}
.product-image {
  width: 100%;
  height: auto;
  max-height: 150px;
  object-fit: contain;
}
.price {
  font-weight: bold;
  color: #333;
}
</style>
