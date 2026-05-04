class Persona:
    def __init__(self, nombre, ci):
        self.nombre = nombre
        self.ci = ci

    def mostrar_info(self):
        return f"Nombre: {self.nombre} | CI: {self.ci}"
