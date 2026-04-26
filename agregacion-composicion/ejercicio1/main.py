from libro import Libro
from biblioteca import Biblioteca

l1 = Libro("Python Basico", "Juan Perez", 2020)
l2 = Libro("Estructuras", "Maria Lopez", 2019)
l3 = Libro("Algoritmos", "Carlos Diaz", 2021)
l4 = Libro("POO", "Ana Torres", 2022)

b1 = Biblioteca("Central")
b2 = Biblioteca("Zona Sur")

b1.agregar_libro(l1)
b1.agregar_libro(l2)

b2.agregar_libro(l3)
b2.agregar_libro(l4)

b1.mostrar_libros()
b2.mostrar_libros()

nombre_buscar = "POO"

encontrado = b1.buscar_libro(nombre_buscar)
if not encontrado:
    b2.buscar_libro(nombre_buscar)

if b1.cantidad_libros() > b2.cantidad_libros():
    print(f"\nLa biblioteca con más libros es: {b1.nombre}")
elif b2.cantidad_libros() > b1.cantidad_libros():
    print(f"\nLa biblioteca con más libros es: {b2.nombre}")
else:
    print("\nAmbas bibliotecas tienen la misma cantidad de libros")