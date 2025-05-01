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
    ),
    Product(
        id=11,
        nombre="Silicon Power 256GB SSD 3D NAND Armored 2.5 Inch SATA III 2000MB/s",
        precio=109.0,        
        stock=randint(0, 100),        
        disponible=True,        
        imagen="https://fakestoreapi.com/img/71kWymZ+c+L._AC_SX679_.jpg",
        descripcion="3D NAND flash are applied to deliver high transfer speeds Remarkable transfer speeds that enable faster bootup and improved overall system performance. The advanced SLC Cache Technology allows performance boost and longer lifespan",
        rating=4.8,
    ),
    Product(
        id=12,
        nombre="WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive",
        precio=114.0,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/61mtL65D4cL._AC_SX679_.jpg",
        descripcion="Expand your PS4 gaming experience, Play anywhere Fast and easy, setup Sleek design with high capacity, 3-year manufacturer's limited warranty",
        rating=4.8,
    ),
    Product(
        id=13,
        nombre="Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin",
        precio=599.0,        
        stock=randint(0, 100),        
        disponible=True,        
        imagen="https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_.jpg",        
        descripcion="21. 5 inches Full HD (1920 x 1080) widescreen IPS display And Radeon free Sync technology.",
        rating=4.8,
    ),
    Product(
        id=14,
        nombre="Samsung 49-Inch CHG9059 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED ",
        precio=999.99,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/81Zt42ioCgL._AC_SX679_.jpg",
        descripcion="49 INCH SUPER ULTRAWIDE 32:9 CURVED GAMING MONITOR with dual 27 inch screen side by side QUANTUM DOT (QLED) TECHNOLOGY, HDR support and factory calibration provides stunningly realistic and accurate color and contrast 144HZ HIGH REFRESH RATE and 1ms ultra fast response time.",
        rating=4.8,
    ),
    Product(
        id=15,
        nombre="BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats",
        precio=56.99,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg",
        descripcion="Note:The Jacket is made from water resistant material that allows water to evaporate away, but does not allow water vapor to infiltrate.",
        rating=4.6,
    ),
    Product(
        id=16,
        nombre="Lock and Love Women's Removable Hooded Faux Leather Motorcycle Jacket",
        precio=29.95,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg",
        descripcion="100% POLYURETHANE, Machine washable.",
        rating=4.9,
    ),
    Product(
        id=17,
        nombre="Rain Jacket Women Windbreaker Striped Climbing Raincoats",
        precio=39.99,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2.jpg",
        descripcion="Lightweight perfet for trip or casual wear---Long sleeve with hooded, adjustable drawstring waist design.",
        rating=4.7,
    ),
    Product(
        id=18,
        nombre="MBJ Women's Solid Short Sleeve Boat Neck V ",
        precio=9.85,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/71z3kpMAYsL._AC_UY879_.jpg",
        descripcion="95% RAYON 5% SPANDEX, Made in USA or Imported, Do Not Bleach, Lightweight fabric with great stretch for comfort, Ribbed on sleeves and neckline / Double stitching on bottom hem",
        rating=4.7, 
    ),
    Product(
        id=19,
        nombre="Opna Women's Short Sleeve Moisture",
        precio=7.95,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg",
        descripcion="100% Polyester, Machine wash, 100% cationic polyester interlock, Machine Wash & Pre Shrunk for a Great Fit, Lightweight, roomy and highly breathable with moisture wicking fabric which helps to keep moisture away, Soft Lightweight Fabric with comfortable V-neck collar and a slimmer fit, delivers a sleek look",
        rating=4.5,
    ),    
    Product(
        id=20,
        nombre="DANVOUY Womens T Shirt Casual Cotton Short",
        precio=12.99,
        stock=randint(0, 100),
        disponible=True,
        imagen="https://fakestoreapi.com/img/61pHAEJ4NML._AC_UX679_.jpg",
        descripcion="95%Cotton,5%Spandex, Features: Casual, Short Sleeve, Letter Print,V-Neck,Fashion Tees, The fabric is soft and has some stretch.",
        rating=4.6,
    )
]

# Ajustamos disponible después
for p in inventory:
    p.disponible = p.stock > 0

