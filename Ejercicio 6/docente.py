from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, ci, especialidad, carga_horaria):
        super().__init__(nombre, ci)
        self.especialidad = especialidad
        self.carga_horaria = carga_horaria
        self.materias = []

    def asignar_materia(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)

    def listar_materias(self):
        return [m.nombre for m in self.materias]
