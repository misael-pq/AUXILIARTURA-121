class Nota:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

    def mostrar(self):
        return f"{self.tipo}: {self.valor}"
