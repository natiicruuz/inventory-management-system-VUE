
# Sistema de inventario con Flask + GraphQL + Vue.js

Este proyecto consiste en una aplicación de inventario de productos para una tienda online. El frontend fue desarrollado en **Vue 3**, mientras que el backend utiliza **Flask** con **GraphQL (Strawberry)** como motor de consultas y mutaciones. La aplicación permite consultar productos, gestionar su stock y reflejar automáticamente su disponibilidad tanto en el frontend como en el backend. Con esta implementación, se logra un flujo de datos eficiente, reactivo y coherente entre el frontend y el backend, garantizando una experiencia de usuario consistente y una arquitectura limpia.


---

## 📁 Estructura del proyecto

```
📦 FrontEnd (Vue 3 + Apollo)
│
├── 📂 src
│   ├── 📂 assets               
│   ├── 📂 components          
│   │   ├── ProductEntry.vue   → Agrega stock a un producto
│   │   ├── ProductOutput.vue  → Quita stock a un producto
│   │   ├── ProductModal.vue   → Muestra detalles del producto
│   ├── 📂 views
│   │   ├── DashboardView.vue  → Vista de resumen general (Deshabilitado para el entregable, ya que nos enfocamos en backend)
│   │   ├── ProductsView.vue   → Lista de productos y acciones
│   ├── App.vue
│   ├── main.js
│   ├── apollo.js
│   ├── router.js
│   └── style.css
├── package.json
└── vite.config.js

📦 BackEnd (Flask + Strawberry GraphQL)
│
├── venv                     → Entorno virtual de Python
├── requirements.txt         → Dependencias del proyecto
├── app.py                   → Servidor Flask + GraphQL
├── data.py                  → Lista de productos simulada
└── schema.py                → Definición del esquema GraphQL
```

---

## 🔨 Instalación y Uso
1. Clonar el repositorio (rama Entregable2)
```
git clone -b Entregable2 https://github.com/natiicruuz/inventory-management-system-VUE.git
cd inventory-management-system-VUE
```
### 📦 Frontend (Vue + Vite)

1. Ir a la carpeta del frontend:
```
cd FrontEnd
```
2. Instalar dependencias:
```
npm install
```

3.  Ejecutar el proyecto en desarrollo
```
npm run dev
```
El frontend estará disponible en http://localhost:5173.



### 🖥️ Backend (Flask + GraphQL)
1. Ir a la carpeta del backend:
```
cd BackEnd
```

2. Crear entorno virtual:
```
python -m venv venv
```

3. Activar entorno virtual:

- En Windows:

    ```
    .\venv\Scripts\activate
    ```

- En Linux/macOS:
    ```
    source venv/bin/activate
    ```
    
4. Instalar dependencias:
```
pip install -r requirements.txt
```

5. Ejecutar servidor backend:
```
python app.py
```
El backend estará disponible en http://localhost:5000/graphql.

### Ejemplos de Queries y Mutaciones
1.  Obtener todos los productos:
    ```
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
    ```
2. Obtener un producto por ID:
    ```
    query {
        product(id: 1) {
            id
            nombre
            precio
            stock
            disponible
            descripcion
        }
    }
    ```

3. Actualizar el stock de un producto:
    ```
    mutation {
        updateStock(id: 1, quantity: 3) {
            id
            nombre
            stock
            disponible
        }
    }
    ```

# Preguntas proyecto y aprendizaje obtenido:
[❓ Preguntas proyecto](Respuestas.md)

