class SueldoInvalidoException(Exception):
    pass

class CargoInvalidoException(Exception):
    pass

class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def mostrar(self):
        print("nombre:", self.nombre)
        print("cargo:", self.cargo)
        print("sueldo:", self.sueldo)
        print()

class Empresa:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.empleados = [None] * cantidad

    def registrar_empleados(self):
        for i in range(len(self.empleados)):
            print("\nempleado", i + 1)

            nombre = input("ingrese nombre: ")

            while True:
                try:
                    cargo = input("ingrese cargo: ")

                    for c in cargo:
                        if c.isdigit():
                            raise CargoInvalidoException(
                                "el cargo no puede contener numeros"
                            )

                    break

                except CargoInvalidoException as e:
                    print(e)

            try:
                sueldo = float(input("ingrese sueldo: "))

                if sueldo < 2500:
                    raise SueldoInvalidoException(
                        "el sueldo es menor al salario minimo nacional"
                    )

            except SueldoInvalidoException as e:
                print(e)
                print("se asignara automaticamente 2500 bs")
                sueldo = 2500

            self.empleados[i] = Empleado(nombre, cargo, sueldo)

    def mostrar_empleados(self):
        print("\nempresa:", self.nombre)
        print("-" * 30)

        for i in range(len(self.empleados)):
            self.empleados[i].mostrar()


n = int(input("cuantos empleados desea registrar: "))

empresa = Empresa("empresa bolivia", n)

empresa.registrar_empleados()
empresa.mostrar_empleados()