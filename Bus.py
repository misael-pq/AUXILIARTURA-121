class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.costo = 1.50

    def subir(self, cantidad):
        if self.pasajeros + cantidad > self.capacidad:
            print("No hay suficientes asientos")
        else:
            self.pasajeros += cantidad
            print(cantidad, "pasajeros subieron")

    def cobrar(self):
        print("Total recaudado:", self.pasajeros * self.costo)

    def asientos(self):
        print("Asientos disponibles:", self.capacidad - self.pasajeros)

    def mostrar(self):
        print("Capacidad:", self.capacidad)
        print("Pasajeros:", self.pasajeros)
        print("Asientos disponibles:", self.capacidad - self.pasajeros)

bus = Bus(40)
bus.subir(30)
bus.cobrar()
bus.asientos()
bus.subir(15) 
bus.subir(10)
bus.mostrar()