<template>
  <div v-if="show" class="modal-overlay">
    <div class="modal-content">
      <h3>Salida de Producto</h3>

      <div class="form-group">
        <label>Seleccione Producto:</label>
        <select v-model="selectedProduct">
          <option v-for="product in inventory" :key="product.id" :value="product">
            {{ product.nombre }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Cantidad a retirar:</label>
        <input type="number" v-model.number="quantity" min="1" class="small-input" />
      </div>

      <div class="modal-buttons">
        <button class="remove-btn" @click="removeStock">Retirar</button>
        <button class="close-btn" @click="close">Cancelar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, ref } from 'vue';

defineProps({
  inventory: Array,
  show: Boolean
});
const emit = defineEmits(['update:show', 'stockRemoved']);
const selectedProduct = ref(null);
const quantity = ref(1);

const removeStock = () => {
  if (selectedProduct.value && selectedProduct.value.stock >= quantity.value) {
    emit('stockRemoved', { product: selectedProduct.value, quantity: -quantity.value });
    close();
  }
};

const close = () => {
  emit('update:show', false);
};



</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 25px;
  border-radius: 8px;
  width: 360px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-group {
  width: 100%;
  margin-bottom: 15px;
}

select, .small-input {
  width: calc(100% - 16px);
  padding: 6px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.modal-buttons {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-top: 10px;
}

.remove-btn {
  background-color: #ff9800;
  color: white;
  padding: 8px 12px;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

.close-btn {
  background-color: #dc3545;
  color: white;
  padding: 8px 12px;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}
</style>
