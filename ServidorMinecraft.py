class ServidorMinecraft:
    def __init__(self):
        self.nombres = []
        self.diamantes = []

    def agregarJugador(self, nombre, diamante):
        if len(self.nombres) < 10:
            self.nombres.append(nombre)
            self.diamantes.append(diamante)
            print(nombre, "agregado con", diamante, "diamantes")
        else:
            print("Servidor lleno")

    def stacks(self):
        print("Stacks de diamantes:")
        for i in range(len(self.nombres)):
            print(self.nombres[i], ":", self.diamantes[i] // 64, "stack(s)")

    def mayorDiamante(self):
        if len(self.nombres) == 0:
            print("No hay jugadores")
            return
        mayor = 0
        jugador = ""
        for i in range(len(self.diamantes)):
            if self.diamantes[i] > mayor:
                mayor = self.diamantes[i]
                jugador = self.nombres[i]
        print("Jugador con más diamantes:", jugador, "con", mayor)

    def totalDiamantes(self):
        total = sum(self.diamantes)
        print("Total de diamantes:", total)

servidor = ServidorMinecraft()
servidor.agregarJugador("Alex", 130)
servidor.agregarJugador("Steve", 64)
servidor.agregarJugador("Herobrine", 200)
servidor.stacks()
servidor.mayorDiamante()
servidor.totalDiamantes()