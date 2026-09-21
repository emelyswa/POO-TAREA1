#Validador de notas con promedio 

#Ejercicio con IA:
class Calificador:

    def __init__(self):
        # Inicializa la lista vacía donde se guardarán las notas válidas
        self.notas = []  # lista de notas validas

    def validar_nota(self, nota):
        # Verifica que la nota esté en el rango permitido (0 a 100)
        return 0 <= nota <= 100

    def cargar_notas(self, *args): 
        #*args: acepta cualquier cantidad de argumentos sin importar cuantos
        # Recibe cualquier cantidad de notas como argumentos
        for nota in args:
        # Solo agrega la nota si pasa la validación
            if self.validar_nota(nota):
                self.notas.append(nota)
        # Devuelve la lista actualizada de notas válidas
        return self.notas

    def promedio(self):
        if not self.notas:
        # Evita división por cero si aún no hay notas cargadas
            return 0
        # Calcula el promedio de las notas almacenadas
        return sum(self.notas) / len(self.notas)


#Ejercicio:
class ValidadorNotas:

    def __init__(self): 
        self.notas = []

    def validar_nota(self, nota1):
        return 0 <= nota1 <= 100

    def cargar_notas(self, *args):
        for nota1 in args:
            if self.validar_nota(nota1):
                self.notas.append(nota1)
        return self.notas

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas)/len(self.notas)