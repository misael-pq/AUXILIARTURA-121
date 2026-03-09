class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.precio = 1.50

    def subir(self, cantidad):
        self.pasajeros += cantidad

    def cobrar(self):
        return self.pasajeros * self.precio

    def disponibles(self):
        return self.capacidad - self.pasajeros


bus = Bus(40)

bus.subir(10)

print("Total:", bus.cobrar())
print("Disponibles:", bus.disponibles())