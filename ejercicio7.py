#Mapeador de edades
#Ejercicio con IA:
class GestorPersonas:

    def __init__(self):
        self.personas = {}   # diccionario {nombre: edad}

    def agregar_persona(self, nombre, edad):
        # Agrega la persona o actualiza su edad si el nombre ya existe
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        # Devuelve los nombres de las personas cuya edad es igual o mayor al límite dado
        return [
            nombre for nombre, edad in self.personas.items()
            if edad >= edad_minima
        ]

    def edad_promedio(self):
        # Evita división por cero; calcula el promedio de edades registradas
        if not self.personas:
            return None
        return sum(self.personas.values()) / len(self.personas)

#Ejercicio:
class GestorPersonas:
    def __init__(self):
        self.personas = {}  # {nombre: edad}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        return [nombre for nombre, edad in self.personas.items()
                if edad >= edad_minima]

    def edad_promedio(self):
        if not self.personas:
            return 0
        return sum(self.personas.values())/len(self.personas)