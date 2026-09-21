#Contador de frecuencia
#Ejercicio con IA:
class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}   # diccionario {elemento: cantidad}

    def agregar_elemento(self, elemento):
        # Si el elemento ya existe, suma 1 a su contador; si no, lo inicializa en 1
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        # Evita error si aún no se cargó ningún elemento
        if not self.frecuencias:
            return None
        # Busca la clave (elemento) cuyo valor (cantidad) es el más alto
        return max(self.frecuencias, key=lambda elemento: self.frecuencias[elemento])

    def frecuencia_elemento(self, elemento):
        # Devuelve la cantidad de veces que apareció el elemento; 0 si nunca se agregó
        return self.frecuencias.get(elemento, 0)

#Ejercicio:
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        
        elemento_ganador = None
        mayor_frecuencia = -1
        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > mayor_frecuencia:
                mayor_frecuencia = frecuencia
                elemento_ganador = elemento
 
        return elemento_ganador