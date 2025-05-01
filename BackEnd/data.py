from random import randint
from typing import List

import strawberry

@strawberry.type
class Product:
    id: int
    nombre: str
    precio: float
    stock: int
    disponible: bool
    imagen: str
    descripcion: str
    rating: float

# Simulamos el inventario
inventory: List[Product] = [
    Product(
        id=1,
        nombre="Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        precio=109.95,
        stock=randint(0, 100),
        disponible=True,  # Vamos a actualizar luego si stock > 0
        imagen="https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
        descripcion="Your perfect pack for everyday use and walks in the forest.",
        rating=3.9,
    ),
    Product(
        id=2,
        nombre="Mens Casual Premium Slim Fit T-Shirts",
        precio=22.3,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
        descripcion="Slim-fitting style, contrast raglan long sleeve, lightweight & breathable.",
        rating=4.1,
    ),
    Product(
        id=3,
        nombre="Mens Cotton Jacket",
        precio=55.99,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg",
        descripcion="Great jacket for Spring/Autumn/Winter, perfect for hiking and traveling.",
        rating=4.7,
    ),
    Product(
        id=4,
        nombre="Mens Casual Slim Fit",
        precio=15.99,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg",
        descripcion="Stylish slim fit perfect for casual wear.",
        rating=2.1,
    ),
    Product(
        id=5,
        nombre="John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
        precio=695.0,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg",
        descripcion="Inspired by the mythical water dragon that protects the ocean's pearl.",
        rating=4.6,
    ),
    Product(
        id=6,
        nombre="Solid Gold Petite Micropave ",
        precio=168.0,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_.jpg",
        descripcion="Satisfaction Guaranteed. Return or exchange any order within 30 days.Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.",
        rating=3.9,
    ),
    Product(
        id=7,
        nombre="White Gold Plated Princess",
        precio=9.99,        
        stock=randint(0, 100),        
        disponible=True,        
        imagen="https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg",
        descripcion="Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more than ever.",
        rating=3.3,
    ),
    Product(
        id=8,
        nombre="Pierced Owl Rose Gold Plated Stainless Steel Double",
        precio=10.99,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg",
        descripcion="Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel",
        rating=4.7,
    ),
    Product(
        id=9,
        nombre="WD 2TB Elements Portable External Hard Drive - USB 3.0 ",
        precio=64.99,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/61IBBVJvSDL._AC_SY879_.jpg",
        descripcion="USB 3.0 and USB 2.0 Compatibility Fast data transfers Improve PC Performance High Capacity; Compatibility Formatted NTFS for Windows 10, Windows 8.1, Windows 7; Reformatting may be required for other operating systems; Compatibility may vary depending on user’s hardware configuration and operating system",
        rating=3.3,
    ),
    Product(
        id=10,
        nombre="SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
        precio=109.0,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_.jpg",
        descripcion="Easy upgrade for faster boot up, shutdown, application launch and file access.",
        rating=4.6,
    )
]

# Ajustamos disponible después
for p in inventory:
    p.disponible = p.stock > 0

