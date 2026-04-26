from perro import Perro
from gato import Gato

class CentroVeterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
        self.gatos = []

    def agregar_perro(self, perro):
        if len(self.perros) < 100:
            self.perros.append(perro)

    def agregar_gato(self, gato):
        if len(self.gatos) < 100:
            self.gatos.append(gato)

    def ordenar_perros(self):
        self.perros.sort(key=lambda p: (p.edad, p.nombreDueno, p.nombre))

    def ordenar_gatos(self):
        self.gatos.sort(key=lambda g: (not g.tomaLeche, -g.edad, g.nombre))

    def mostrar_perros(self):
        print(f"\nPerros en {self.nombre}")
        for p in self.perros:
            print(f"{p.nombre} | Edad: {p.edad} | Dueño: {p.nombreDueno}")

    def mostrar_gatos(self):
        print(f"\nGatos en {self.nombre}")
        for g in self.gatos:
            print(f"{g.nombre} | Edad: {g.edad} | Dueño: {g.nombreDueno} | Toma leche: {g.tomaLeche}")

    def verificar_dueno(self):
        conteo = {}
        for p in self.perros:
            conteo[p.nombreDueno] = conteo.get(p.nombreDueno, 0) + 1
        for g in self.gatos:
            conteo[g.nombreDueno] = conteo.get(g.nombreDueno, 0) + 1

        print(f"\nDueños con más de un animal en {self.nombre}")
        for dueno, cantidad in conteo.items():
            if cantidad >= 2:
                print(f"{dueno} tiene {cantidad} animales")