class Jugador:
    def __init__(self, nombre, diamantes):
        self.nombre = nombre
        self.diamantes = diamantes


class Servidor:
    def __init__(self):
        self.lista = []

    def agregar(self, jugador):
        if len(self.lista) < 10:
            self.lista.append(jugador)

    def stacks(self):
        for j in self.lista:
            s = j.diamantes // 64
            print(j.nombre, "stacks:", s)

    def mayor(self):
        m = max(self.lista, key=lambda j: j.diamantes)
        print("Mayor:", m.nombre)

    def total(self):
        t = sum(j.diamantes for j in self.lista)
        print("Total:", t)


server = Servidor()

server.agregar(Jugador("Steve", 120))
server.agregar(Jugador("Alex", 50))

server.stacks()
server.mayor()
server.total()