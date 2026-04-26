class Libro:
    def __init__(self, nombre, autor, anio):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio

    def mostrar(self):
        print(f"Libro: {self.nombre}, Autor: {self.autor}, Año: {self.anio}")