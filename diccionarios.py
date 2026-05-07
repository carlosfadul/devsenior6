carro = {
    "marca" : "Toyota",
    "modelo" : "Corolla",
    "año" : 2020,
    "colores": ["rojo", "azul", "negro"],
    "electrico": False
        }


print(carro)
print(carro["colores"])
print(type(carro))
fruta = dict(nombre = "Manzana", color = "Rojo", sabor = "Dulce", valor = 2500)
print(fruta)
x = fruta["nombre"]
print(x)
print(fruta.keys())    
fruta["valor"] = 3000
print(fruta)