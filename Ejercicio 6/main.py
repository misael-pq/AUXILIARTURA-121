from docente import Docente
from estudiante import Estudiante
from materia import Materia
from nota import Nota
from examen import Examen

doc = Docente("Carlos", "123", "Programacion", 40)

est = Estudiante("Ana", "456", "2023001", 3)

mat = Materia("POO", "INF-121", doc)

# Inscripción
mat.inscribir_estudiante(est)

# Nota
mat.agregar_nota(est, Nota(85, "Parcial"))

# Promedio
print("Promedio:", mat.promedio_estudiante(est))

# Examen
mat.asignar_examen(Examen("10/06/2026", "Aula 101"))

print(est.nombre, "está en", mat.nombre)
