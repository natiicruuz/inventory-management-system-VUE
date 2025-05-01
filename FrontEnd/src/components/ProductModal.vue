<template>
  <div v-if="show" class="modal-overlay" @click.self="closeModal">
    <div class="modal-content">
      <button class="close-button" @click="closeModal">X</button>
      <img :src="product.imagen" alt="Imagen del producto" class="modal-image" />
      <h2>{{ product.nombre }}</h2>
      <p class="description">{{ product.descripcion }}</p>
      <p class="price">Precio: ${{ product.precio }}</p>
      <p class="rating" v-if="product.rating">Rating: ⭐{{ product.rating }}</p>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";

defineProps({
  show: Boolean,
  product: Object,
});

const emit = defineEmits(["close"]);

const closeModal = () => {
  emit("close");
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
  text-align: center;
  position: relative;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

.modal-image {
  width: 100%;
  height: auto;
  max-height: 200px;
  object-fit: contain;
  margin-bottom: 10px;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 15px;
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
}

.description {
  margin: 10px 0;
  font-size: 14px;
  color: #555;
}

.rating {
  font-weight: bold;
  margin-top: 10px;
}
</style>
