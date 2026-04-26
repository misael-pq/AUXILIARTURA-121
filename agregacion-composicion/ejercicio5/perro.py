from animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueno, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueno)
        self.requiereBosal = requiereBosal
        self.ladraFuerte = ladraFuerte