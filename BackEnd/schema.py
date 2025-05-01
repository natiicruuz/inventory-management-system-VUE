import strawberry
from typing import List, Optional

# Carga del inventario simulado desde data.py
from data import inventory

@strawberry.type
class Product:
    id: int
    nombre: str
    precio: float
    stock: int
    disponible: bool
    imagen: str
    descripcion: Optional[str] = None
    rating: Optional[float] = None

@strawberry.type
class Query:
    
    @strawberry.field
    def products(self) -> List[Product]:
        """Devuelve todos los productos"""
        return inventory

    @strawberry.field
    def product(self, id: int) -> Optional[Product]:
        """Devuelve un producto por ID"""
        for product in inventory:
            if product.id == id:
                return product
        return None

@strawberry.type
class Mutation:

    @strawberry.mutation
    def update_stock(self, id: int, quantity: int) -> Optional[Product]:
        """Suma o resta stock de un producto por ID"""
        for product in inventory:
            if product.id == id:
                product.stock += quantity
                product.disponible = product.stock > 0
                return product
        return None

schema = strawberry.Schema(query=Query, mutation=Mutation)
