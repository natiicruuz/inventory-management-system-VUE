<template>
  <div>
    <h1>Listado de Productos</h1>

    <button @click="showEntry = true">Entrada de Producto</button>
    <button @click="showOutput = true">Salida de Producto</button>

    <div class="product-grid">
      <div v-for="product in inventory" :key="product.id" class="product-card" @click="fetchProductDetails(product.id)">
        <img :src="product.imagen" alt="Imagen del producto" class="product-image" />
        <h3>{{ product.nombre }}</h3>
        <p class="price">${{ product.precio }}</p>
        <p class="stock" :style="{ color: product.disponible ? 'green' : 'red' }">
          {{ product.disponible ? `Disponible (${product.stock})` : 'Agotado' }}
        </p>
      </div>
    </div>

    <ProductEntry v-model:show="showEntry" :inventory="inventory" @stockAdded="updateStock" />
    <ProductOutput v-model:show="showOutput" :inventory="inventory" @stockRemoved="updateStock" />
    <ProductModal v-if="showModal" :show="showModal" :product="selectedProduct" @close="showModal = false" />
  </div>
</template>

<script setup>
import { reactive, ref, watch } from "vue";
import { useQuery, useLazyQuery } from "@vue/apollo-composable";
import gql from "graphql-tag";

import ProductEntry from "../components/ProductEntry.vue";
import ProductOutput from "../components/ProductOutput.vue";
import ProductModal from "../components/ProductModal.vue";

const inventory = reactive([]);
const showEntry = ref(false);
const showOutput = ref(false);
const showModal = ref(false);
const selectedProduct = ref({});

// --- GraphQL Queries ---
const GET_PRODUCTS = gql`
  query {
    products {
      id
      nombre
      precio
      stock
      disponible
      imagen
      descripcion
      rating
    }
  }
`;

const GET_PRODUCT_BY_ID = gql`
  query GetProductById($id: Int!) {
    product(id: $id) {
      id
      nombre
      precio
      stock
      disponible
      imagen
      descripcion
      rating
    }
  }
`;

// --- Apollo useQuery para traer todos los productos ---
const { result, loading, error } = useQuery(GET_PRODUCTS);

// --- Apollo useLazyQuery para traer producto por ID ---
const { load: fetchProductById } = useLazyQuery(GET_PRODUCT_BY_ID, { id: 0 });

// --- Rellenar inventory reactivamente cuando result esté listo ---
watch(result, (newResult) => {
  if (newResult?.products) {
    inventory.length = 0; // Limpia el array reactivo
    newResult.products.forEach((product) => {
      inventory.push({
        ...product,
        disponible: product.stock > 0, // Calcula disponible por si acaso
      });
    });
  }
});

// Obtener detalles de un producto por ID (para modal)
const fetchProductDetails = async (productId) => {
  const { onResult } = fetchProductById({ id: productId });
  onResult((queryResult) => {
    selectedProduct.value = queryResult.data.product;
    showModal.value = true;
  });
};

// Watch para stock
watch(
  inventory,
  (newInventory) => {
    newInventory.forEach((product) => {
      product.disponible = product.stock > 0;
    });
  },
  { deep: true }
);

// Actualizar stock (entrada/salida)
const updateStock = ({ product, quantity }) => {
  const item = inventory.find((p) => p.id === product.id);
  if (item) {
    item.stock += quantity;
    item.disponible = item.stock > 0;
  }
};
</script>



<style scoped>
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
