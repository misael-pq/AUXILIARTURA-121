class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Carnet:", self.carnet)
        print("Edad:", self.edad)


class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera

    def mostrar(self):
        super().mostrar()
        print("Matrícula:", self.matricula)
        print("Carrera:", self.carrera)

    def misma_carrera(self, otro):
        return self.carrera == otro.carrera


class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.antiguedad = antiguedad
        self.sueldo = sueldo

    def mostrar(self):
        super().mostrar()
        print("Antigüedad:", self.antiguedad)
        print("Sueldo:", self.sueldo)


e1 = Estudiante("Juan", 123, 20, 1001, "Sistemas")
e2 = Estudiante("Maria", 456, 25, 1002, "Industrial")
d1 = Docente("Carlos", 789, 25, 10, 5000)

print("=== Estudiante 1 ===")
e1.mostrar()

print("\n=== Estudiante 2 ===")
e2.mostrar()

print("\n=== Docente ===")
d1.mostrar()

if e1.edad == d1.edad or e2.edad == d1.edad:
    print("\nAlgún estudiante tiene la misma edad que el docente")
else:
    print("\nNingún estudiante tiene la misma edad que el docente")

if e1.misma_carrera(e2):
    print("Los estudiantes están en la misma carrera")
else:
    print("Los estudiantes NO están en la misma carrera")