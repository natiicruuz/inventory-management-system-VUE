# Sistema de Inventario Reactivo en VUE y Backend con Flask + GraphQL 
## Entregable 2
Proyecto 1 Programación web 2, 2025

Este proyecto es una aplicación web construida con Vue 3 que permite gestionar el inventario de una tienda online de manera reactiva. Se enfoca en la actualización dinámica del stock sin necesidad de computed(), utilizando reactive() y watch().

## 🎯 Características principales
- Dashboard: Muestra métricas clave de los productos mas vendidos y ventas.
- Gestión de Productos: Visualización del inventario con actualización automática de stock. Los productos fueron obtenidos de la API ```https://fakestoreapi.com/products```
- Entrada y salida de productos: Permite agregar y reducir stock.
- Reactividad sin computed(): Los productos cambian su estado de disponibilidad automáticamente.

## 📂 Estructura
```
📦 inventory-management-system-VUE
├── 📂 src
│   ├── 📂 assets       
│   ├── 📂 components   
│   │   ├── 📄 ProductEntry.vue  
│   │   ├── 📄 ProductOutput.vue  
│   │   ├── 📄 ProductModal.vue  
│   ├── 📂 views        
│   │   ├── 📄 DashboardView.vue  
│   │   ├── 📄 ProductsView.vue  
│   ├── 📄 router       
│   ├── 📄 App.vue        
│   ├── 📄 main.js         
│   ├── 📄 style.css        
├── 📄 package.json     
├── 📄 README.md        
└── 📄 vite.config.js                
```

## ❓ Preguntas proyecto


## 🔨 Instalación y Uso


