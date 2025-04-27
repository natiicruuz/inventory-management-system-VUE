import strawberry
from typing import List, Optional
from data import products

@strawberry.type
class Product:
    id: int
    nombre: str
    precio: float
    stock: int
    disponible: bool

@strawberry.type
class Query:
    @strawberry.field
    def all_products(self) -> List[Product]:
        return [Product(**p) for p in products]

    @strawberry.field
    def product_by_id(self, id: int) -> Optional[Product]:
        return next((Product(**p) for p in products if p["id"] == id), None)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def update_stock(self, id: int, quantity: int) -> Optional[Product]:
        for p in products:
            if p["id"] == id:
                p["stock"] = quantity
                p["disponible"] = quantity > 0
                return Product(**p)
        return None

schema = strawberry.Schema(query=Query, mutation=Mutation)
