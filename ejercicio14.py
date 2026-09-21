#Mapeo de estudiantes a notas
#Ejercicio con IA:
class RegistroNotas:

    def __init__(self):
        self.notas = {}   # diccionario {estudiante: nota}

    def registrar(self, estudiante, nota):
        # Registra la nota del estudiante (si ya existía, la sobrescribe)
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        # Devuelve los nombres de los estudiantes cuya nota alcanza el mínimo requerido
        return [
            estudiante for estudiante, nota in self.notas.items()
            if nota >= nota_minima
        ]

    def mejor_estudiante(self):
        # Evita error si aún no hay notas registradas
        if not self.notas:
            return None
        # Busca el nombre del estudiante con la nota más alta
        nombre = max(self.notas, key=lambda estudiante: self.notas[estudiante])
        # Devuelve una tupla (nombre, nota) en vez de solo el nombre
        return (nombre, self.notas[nombre])

#Ejercicio:
class RegistroNotas: 
    def __init__(self):
        self.notas = {}  # {estudiante: nota}
 
    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota
 
    def estudiantes_aprobados(self, nota_minima):
        return [nombre for nombre, nota in self.notas.items()
                if nota >= nota_minima]
 
    def mejor_estudiante(self):
        if not self.notas:
            return None
 
        mejor_nombre = None
        mejor_nota = -1
        for nombre, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = nombre
 
        return (mejor_nombre, mejor_nota)