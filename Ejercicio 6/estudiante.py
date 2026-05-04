from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, ci, registro, semestre):
        super().__init__(nombre, ci)
        self.registro = registro
        self.semestre = semestre
        self.materias = []

    def inscribirse(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)
            materia.estudiantes.append(self)

    def listar_materias(self):
        return [m.nombre for m in self.materias]
