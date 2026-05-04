class Materia:
    def __init__(self, nombre, codigo, docente):
        self.nombre = nombre
        self.codigo = codigo
        self.docente = docente
        self.estudiantes = []
        self.notas = {}
        self.examen = None

        docente.asignar_materia(self)

    def inscribir_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
            self.notas[estudiante] = []

    def agregar_nota(self, estudiante, nota):
        if estudiante in self.notas:
            self.notas[estudiante].append(nota)

    def promedio_estudiante(self, estudiante):
        notas = self.notas.get(estudiante, [])
        if not notas:
            return 0
        return sum(n.valor for n in notas) / len(notas)

    def asignar_examen(self, examen):
        self.examen = examen
