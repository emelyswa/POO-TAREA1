#Asignador de Equipos
#Ejercicio con IA:
class Equipos:

    def __init__(self):
        self.equipos = {}   # diccionario {nombre_equipo: [jugadores]}

    def crear_equipo(self, nombre_equipo):
        # Crea el equipo solo si no existe (evita sobrescribir jugadores ya cargados)
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        # Si el equipo no existe todavía, lo crea automáticamente
        if equipo not in self.equipos:
            self.crear_equipo(equipo)
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        # Evita error si no hay equipos cargados
        if not self.equipos:
            return None
        # Busca el equipo con más jugadores, comparando por la longitud de cada lista
        return max(self.equipos, key=lambda equipo: len(self.equipos[equipo]))

#Ejercicio:
class Equipos:
    def __init__(self):
        self.equipos = {}  # {nombre_equipo: [jugadores]}

    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.crear_equipo(equipo)
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        
        equipo_ganador = None
        mayor_cantidad = 0
        for nombre_equipo, jugadores in self.equipos.items():
            cantidad = len(jugadores)
            if cantidad > mayor_cantidad:
                mayor_cantidad = cantidad
                equipo_ganador = nombre_equipo
        
        return equipo_ganador