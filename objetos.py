class Libro:
    def __init__(self, titulo, autor, isbn, precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__precio = precio

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    def get_precio(self):
        return self.__precio

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("El precio debe ser mayor que 0")

    # Método para mostrar información
    def mostrar_info(self):
        print("Título:", self.get_titulo())
        print("Autor:", self.get_autor())
        print("ISBN:", self.get_isbn())
        print("Precio:", self.get_precio())
        print("------------------------")


# Clase principal
def main():
    libro1 = Libro("Python Básico", "Juan Pérez", "12345", 50000)
    libro2 = Libro("IA para todos", "Ana Gómez", "67890", 75000)
    libro3 = Libro("POO en Python", "Carlos Ruiz", "11223", 60000)

    libro1.mostrar_info()
    libro2.mostrar_info()
    libro3.mostrar_info()

    # Ejemplo de uso de setter
    libro1.set_precio(55000)
    print("Nuevo precio del libro 1:", libro1.get_precio())
    libro1.mostrar_info()


main()