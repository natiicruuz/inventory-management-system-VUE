# Sistema de Inventario Reactivo
Proyecto 1 Programación web 2, 2025

Este proyecto es una aplicación web construida con Vue 3 que permite gestionar el inventario de una tienda online de manera reactiva. Se enfoca en la actualización dinámica del stock sin necesidad de computed(), utilizando reactive() y watch().

## 🎯 Características principales
- Dashboard: Muestra métricas clave con gráficos de ventas y pagos.
- Gestión de Productos: Visualización del inventario con actualización automática de stock. Los productos fueron obtenidos de la API ```https://fakestoreapi.com/products```
- Entrada y salida de productos: Permite agregar y reducir stock.
- Reactividad sin computed(): Los productos cambian su estado de disponibilidad automáticamente.

## 📂 Estructura
```
📦 inventory-management-system-VUE
├── 📂 src
│   ├── 📂 assets       
│   ├── 📂 components   
│   ├── 📂 views        
│   ├── 📄router       
│   ├── 📄App.vue        
│   ├── 📄main.js         
│   ├── 📄style.css        
├── 📄 package.json     
├── 📄 README.md        
└── 📄 vite.config.js         
```

## ❓ Preguntas proyecto
1. **Vue no detecta cambios dentro de objetos reactivos de la forma que esperarías. ¿Cómo podrías observar un cambio en una propiedad anidada?**

Vue 3 no reacciona automáticamente a cambios dentro de propiedades anidadas en reactive(), por lo que se necesita usar ```watch()``` con la opción ```{ deep: true }```. Esto asegura que Vue detecte cambios en cualquier propiedad dentro de un objeto o array reactivo.

```
watch(
  inventory,
  (newInventory) => {
    newInventory.forEach((product) => {
      product.disponible = product.stock > 0;
    });
  },
  { deep: true }
);
```

Aquí ```watch()``` está observando inventory en profundidad { deep: true }, permitiendo detectar cambios en stock dentro de cada producto y actualizar disponible en consecuencia.

2. **watch() permite escuchar cambios en propiedades específicas dentro de reactive(), explica cómo funciona.**
```watch()``` en Vue 3 permite reaccionar a cambios en variables reactivas. Su estructura básica es:

```watch(source, callback, options);```
- source: La variable reactiva o función que devuelve la propiedad a observar.
- callback: Función que se ejecuta cuando la propiedad cambia.
- options: Parámetros opcionales como { deep: true } para observar cambios en propiedades anidadas.

En el  código, ```watch(inventory, callback, { deep: true })``` revisa el array inventory y, cuando cambia, recorre cada producto para actualizar la disponibilidad.

3. **¿Cómo harías que un watch() detecte cambios en stock dentro de un array de productos?**
Sería observar directamente la propiedad stock de cada producto dentro del array:

```
inventory.forEach((product) => {
  watch(
    () => product.stock,
    (newStock) => {
      product.disponible = newStock > 0;
    }
  );
});
```

Esto asegura que cada producto tenga su propio watch(), reaccionando únicamente cuando su stock cambia.

## [ 📷 Ver Prototipos ](/img/IMAGES.md)



## 🔨 Instalación y Uso
1.  Clonar el repositorio
```
git clone https://github.com/natiicruuz/inventory-management-system-VUE.git
```

2. Instalar dependencias
```
npm install
```

3.  Ejecutar el proyecto en desarrollo
```
npm run dev
```
La aplicación estará disponible en http://localhost:5173.

