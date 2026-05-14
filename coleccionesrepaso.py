biblioteca = {
    "autores": {},
    "libros": {},
    "usuarios": {},
    "prestamos": {}
}

biblioteca["autores"] = {
    1: {
        "nombre": "Gabriel García Márquez",
        "nacionalidad": "Colombiana",
        "nacimiento": 1927
    },
    2: {
        "nombre": "J.K. Rowling",
        "nacionalidad": "Británica",
        "nacimiento": 1965
    },
    3: {
        "nombre": "George Orwell",
        "nacionalidad": "Británica",
        "nacimiento": 1903
    }
}

biblioteca["libros"] = {
    "9780307474728": {
        "titulo": "Cien años de soledad",
        "anio": 1967,
        "autores": [1],
        "categorias": {"Novela", "Realismo mágico"},
        "copias_totales": 5,
        "copias_disponibles": 3,
        "veces_prestado": 2
    },
    "9788478884452": {
        "titulo": "Harry Potter y la piedra filosofal",
        "anio": 1997,
        "autores": [2],
        "categorias": {"Fantasía", "Aventura"},
        "copias_totales": 8,
        "copias_disponibles": 6,
        "veces_prestado": 2
    },
    "9780451524935": {
        "titulo": "1984",
        "anio": 1949,
        "autores": [3],
        "categorias": {"Distopía", "Política"},
        "copias_totales": 4,
        "copias_disponibles": 3,
        "veces_prestado": 1
    },
    "9780307389732": {
        "titulo": "Rebelión en la granja",
        "anio": 1945,
        "autores": [3],
        "categorias": {"Sátira", "Política"},
        "copias_totales": 3,
        "copias_disponibles": 3,
        "veces_prestado": 0
    },
    "9788498382662": {
        "titulo": "Harry Potter y la cámara secreta",
        "anio": 1998,
        "autores": [2],
        "categorias": {"Fantasía", "Aventura"},
        "copias_totales": 6,
        "copias_disponibles": 5,
        "veces_prestado": 1
    }
}

biblioteca["usuarios"] = {
    101: {
        "nombre": "Carlos Fadul",
        "email": "carlos@example.com",
        "telefono": "3001111111"
    },
    102: {
        "nombre": "Ana Gómez",
        "email": "ana@example.com",
        "telefono": "3002222222"
    },
    103: {
        "nombre": "Luis Pérez",
        "email": "luis@example.com",
        "telefono": "3003333333"
    },
    104: {
        "nombre": "María Torres",
        "email": "maria@example.com",
        "telefono": "3004444444"
    }
}

biblioteca["prestamos"] = {
    1: {
        "usuario_id": 101,
        "isbn": "9780307474728",
        "fecha_prestamo": (2026, 4, 1),
        "fecha_devolucion": (2026, 4, 15),
        "estado": "devuelto"
    },
    2: {
        "usuario_id": 102,
        "isbn": "9788478884452",
        "fecha_prestamo": (2026, 5, 1),
        "fecha_devolucion": (2026, 5, 15),
        "estado": "activo"
    },
    3: {
        "usuario_id": 103,
        "isbn": "9780451524935",
        "fecha_prestamo": (2026, 4, 20),
        "fecha_devolucion": (2026, 5, 5),
        "estado": "atrasado"
    }
}

print("=" * 60)
print("LIBROS DISPONIBLES")
print("=" * 60)

for isbn, libro in biblioteca["libros"].items():
    if libro["copias_disponibles"] > 0:
        print(f"{libro['titulo']} - Disponibles: {libro['copias_disponibles']}")

print("\n" + "=" * 60)
print("LIBROS DE GEORGE ORWELL")
print("=" * 60)

autor_id = 3

for isbn, libro in biblioteca["libros"].items():
    if autor_id in libro["autores"]:
        print(libro["titulo"])

print("\n" + "=" * 60)
print("PRÉSTAMOS ACTIVOS")
print("=" * 60)

for prestamo_id, prestamo in biblioteca["prestamos"].items():
    if prestamo["estado"] == "activo":
        usuario = biblioteca["usuarios"][prestamo["usuario_id"]]["nombre"]
        libro = biblioteca["libros"][prestamo["isbn"]]["titulo"]
        print(f"Préstamo {prestamo_id}: {usuario} -> {libro}")

print("\n" + "=" * 60)
print("USUARIOS CON PRÉSTAMOS ATRASADOS")
print("=" * 60)

for prestamo in biblioteca["prestamos"].values():
    if prestamo["estado"] == "atrasado":
        usuario = biblioteca["usuarios"][prestamo["usuario_id"]]["nombre"]
        print(usuario)

print("\n" + "=" * 60)
print("CATEGORÍAS EXISTENTES")
print("=" * 60)

categorias = set()

for libro in biblioteca["libros"].values():
    categorias.update(libro["categorias"])

for categoria in sorted(categorias):
    print(categoria)

print("\n" + "=" * 60)
print("LIBRO MÁS PRESTADO")
print("=" * 60)

isbn_mas_prestado = max(
    biblioteca["libros"],
    key=lambda isbn: biblioteca["libros"][isbn]["veces_prestado"]
)

print(biblioteca["libros"][isbn_mas_prestado]["titulo"])

print("\n" + "=" * 60)
print("TOTAL DE COPIAS EN LA BIBLIOTECA")
print("=" * 60)

total_copias = 0

for libro in biblioteca["libros"].values():
    total_copias += libro["copias_totales"]

print(total_copias)

print("\n" + "=" * 60)
print("TOTAL DE PRÉSTAMOS ACTIVOS")
print("=" * 60)

activos = 0

for prestamo in biblioteca["prestamos"].values():
    if prestamo["estado"] == "activo":
        activos += 1

print(activos)

print("\n" + "=" * 60)
print("HISTORIAL DE PRÉSTAMOS POR USUARIO")
print("=" * 60)

for usuario_id, usuario in biblioteca["usuarios"].items():
    print(f"\n{usuario['nombre']}:")
    tiene_prestamos = False

    for prestamo in biblioteca["prestamos"].values():
        if prestamo["usuario_id"] == usuario_id:
            titulo = biblioteca["libros"][prestamo["isbn"]]["titulo"]
            print(f" - {titulo} ({prestamo['estado']})")
            tiene_prestamos = True

    if not tiene_prestamos:
        print(" - Sin préstamos")