import strawberry
from typing import List, Optional

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
        return inventory

    @strawberry.field
    def product(self, id: int) -> Optional[Product]:
        for product in inventory:
            if product.id == id:
                return product
        return None

@strawberry.type
class Mutation:

    @strawberry.mutation
    def update_stock(self, id: int, quantity: int) -> Optional[Product]:
        for product in inventory:
            if product.id == id:
                product.stock += quantity
                product.disponible = product.stock > 0
                return product
        return None

schema = strawberry.Schema(query=Query, mutation=Mutation)
