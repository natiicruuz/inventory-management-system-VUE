## Preguntas Entregable 2
- **¿Qué ventajas ofrece GraphQL sobre REST en este contexto?**

GraphQL permitió hacer que se tuviera un control más preciso sobre los datos que se solicitan desde el frontend. En lugar de crear múltiples endpoints como sería necesario con REST, solo se usa una única ruta (/graphql) para hacer todas las consultas y mutaciones. Esto hizo que fuera mucho más flexible al momento de obtener solo los campos que. Además, simplificó la comunicación entre frontend y backend, haciendo el código más limpio y eficiente porque simplemente haces una query y eso te devuelve lo que le pidas, sin informacion adicional innecesaria. 

- **¿Cómo se definen los tipos y resolvers en una API con GraphQL?**

Los tipos se definen con decoradores usando la librería strawberry, que facilita mucho la estructura. Por ejemplo, se usó `@strawberry.type` para definir el tipo Product, que incluye campos como id, nombre, precio, stock, etc. Luego, los resolvers también se definen como funciones decoradas, por ejemplo `@strawberry.field` para consultas (Query) y `@strawberry.mutation` para las operaciones que modifican el estado, como actualizar el stock. Cada resolver implementa la lógica que debe ejecutar cuando se llama desde el frontend.

- **¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?**

Es importante porque la lógica de negocio no debería depender únicamente de la interfaz del usuario. Si solo el frontend actualizara el campo disponible, entonces cualquier otro cliente (por ejemplo, una app móvil o una integración externa) podría tener datos inconsistentes. Literalmente al depender de la interfaz de usuario, le estamos dando poder al usuario a que haga lo que quiera y no es una buena práctica.

- **¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?**

Implementamos esa lógica directamente en el resolver del backend. En la mutación `update_stock`, después de modificar el stock, comprobamos si llegó a 0 para cambiar disponible a false, o si aumentó desde 0 para ponerlo en true. Al centralizar esta lógica en el backend, nos aseguramos de que se aplique de forma consistente sin importar desde qué parte del sistema se dispare el cambio. En este caso, al refrescar la pagina evidentemente no se espera persistencia del stock entre reinicios. En un entorno real, se usaría una base de datos para mantener los cambios del stock, pero en este ejercicio se buscaba enfocarse en GraphQL, resolvers y control del estado, no en persistencia.

## Tecnologías y librerías utilizadas

### Backend
| Librería         | Propósito                                                                 |
|------------------|--------------------------------------------------------------------------|
| **Flask**        | Framework ligero para exponer un servidor web.                           |
| [**Strawberry**](https://strawberry.rocks/)   | Librería moderna para definir APIs GraphQL de forma declarativa en Python. |
| **GraphQL**      | Protocolo de consulta eficiente para APIs. Permite obtener datos flexibles y precisos. |

> *¿Por qué Strawberry y no Graphene?*  
> Elegí **Strawberry** por su integración natural con Python 3 usando anotaciones `@strawberry.type`, tipado fuerte con `Optional`, y su facilidad para exponer tipos complejos como listas y mutaciones con mínima configuración. 
> Ademas usar `graphene` con la version de python que utilice (3.13) hacia que algunas librerías (como `flask_graphql` y `graphql_server`) las cuales todavía intentan importar `MutableMapping` desde collections, no funcionaran correctamente. Por lo que usar preferi optar por `strawberry` que funciona mejor con versiones más nuevas de Python.


### Frontend
| Librería              | Propósito                                                           |
|-----------------------|---------------------------------------------------------------------|
| **Vue 3**             | Framework frontend progresivo con soporte para composición.         |
| **@vue/apollo-composable** | Integración de Vue con GraphQL para hacer queries reactivas. |
| **Vite**              | Herramienta de compilacion moderno rápido para entornos Vue.                          |


## Requisitos funcionales cumplidos

| Requisito                                                                                   | Estado |
|---------------------------------------------------------------------------------------------|--------|
| Base de datos en memoria con productos en lista de Python                                   | ✅     |
| Consulta GraphQL para obtener todos los productos                                           | ✅     |
| Consulta GraphQL para obtener un producto por ID                                            | ✅     |
| Mutación GraphQL para actualizar el stock de un producto                                    | ✅     |
| Lógica backend para cambiar el campo `disponible` según el stock (sin depender del frontend) | ✅     |
| Integración Vue → GraphQL → Flask funcionando y reactiva                                    | ✅     |


## Desafíos técnicos y cómo se solucionaron

### 1. Problemas al consultar un producto por ID
**Problema:** Al hacer clic en un producto, la query `product(id: Int!)` devolvía `undefined`, y no se abría el modal.

**Causa raíz:**  
- El uso de `useQuery` de forma reactiva con variables `ref` y `enabled: false` no ejecutaba la consulta correctamente.
- Apollo requería que el esquema fuera exactamente válido (verificación estricta de documentos y tipos GraphQL).
- Se probó reemplazando `useQuery` por `useLazyQuery`, el cual permite ejecutar la consulta dinámicamente cuando se necesita
- El uso de `useLazyQuery` no solucionó el problema, ya que aunque parecía la herramienta adecuada para ejecutar queries bajo demanda, en este caso no entregaba el data esperado.

**Solución:**  
- El verdadero problema estaba en cómo se estaba ejecutando la consulta. Se necesitaba más control sobre el envío de variables y el formato del query.
- Se confirmó que el backend acepta `Int` como tipo (`id: int`), y el cliente lo enviaba correctamente usando `Number(id)`.
- Se reemplazó completamente `useLazyQuery` por el cliente Apollo directo, accediendo a `apolloClient.client.query(...)`.
- Esto permitió ejecutar la query con control total sobre el query y las variables, garantizando que el id fuera tratado como Int usando Number(id).
- A partir de ese cambio, la consulta funcionó correctamente y los datos del producto se mostraban en el modal.


### 2. Lógica de negocio duplicada
**Problema:**  
Originalmente la lógica para actualizar `disponible` se ejecutaba tanto en el frontend como en el backend, causando inconsistencias.

**Solución:**  
Se centralizó la lógica en el backend dentro de la mutación `update_stock`. El campo `disponible` se actualiza automáticamente cada vez que se modifica el stock, eliminando la necesidad de esta lógica en Vue.

