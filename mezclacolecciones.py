biblioteca = {
    "libros":{},
    "usuarios":{},
    "prestamos":[]
}

biblioteca["libros"]["L001"]= {
    "titulo":"El Quijote",
    "autor":"Miguel de Cervantes",
    "anio":1605,
    "disponible":True
}

biblioteca["usuarios"]["usuario1"]= {
    "nombre":"Juan Pérez",
    "telefono":"555-1234"
}

prestamo = {
    "usuario":"usuario1",
    "libro":"L001",
    "fecha_prestamo":"2024-06-01",
    "fecha_devolucion":"2024-06-15"
}


biblioteca["libros"].remove("L001")

print(biblioteca["libros"]["L001"])



