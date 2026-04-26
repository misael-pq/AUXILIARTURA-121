from perro import Perro
from gato import Gato
from centro_veterinario import CentroVeterinario

c1 = CentroVeterinario("Centro 1")
c2 = CentroVeterinario("Centro 2")

p1 = Perro("Max", 5, "Juan", True, True)
p2 = Perro("Rocky", 3, "Luis", False, True)
p3 = Perro("Toby", 5, "Juan", True, False)
p4 = Perro("Firulais", 2, "Carlos", False, True)

g1 = Gato("Michi", 2, "Ana", True, True)
g2 = Gato("Pelusa", 4, "Ana", False, False)
g3 = Gato("Garfield", 5, "Luis", True, True)
g4 = Gato("Tom", 3, "Pedro", False, True)

c1.agregar_perro(p1)
c1.agregar_perro(p2)
c1.agregar_gato(g1)
c1.agregar_gato(g2)

c2.agregar_perro(p3)
c2.agregar_perro(p4)
c2.agregar_gato(g3)
c2.agregar_gato(g4)

c1.ordenar_perros()
c1.ordenar_gatos()
c2.ordenar_perros()
c2.ordenar_gatos()

print("\nCENTRO 1")
c1.mostrar_perros()
c1.mostrar_gatos()
c1.verificar_dueno()

print("\nCENTRO 2")
c2.mostrar_perros()
c2.mostrar_gatos()
c2.verificar_dueno()