from libro import Libro

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        if len(self.libros) < 100:
            self.libros.append(libro)

    def buscar_libro(self, nombre):
        for libro in self.libros:
            if libro.nombre == nombre:
                print(f"Libro encontrado en {self.nombre}:")
                libro.mostrar()
                return True
        return False

    def cantidad_libros(self):
        return len(self.libros)

    def mostrar_libros(self):
        print(f"\nBiblioteca: {self.nombre}")
        for libro in self.libros:
            libro.mostrar()