#Estadísticas de temperatura

#Ejercicio con IA:
class GestorTemperatura:

    def __init__(self):
        # Lista donde se van guardando todas las temperaturas registradas
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        # Agrega una única temperatura al historial
        self.temperaturas.append(temp)

    def minima(self):
        # Evita error si la lista está vacía; devuelve la temperatura más baja
        if not self.temperaturas:
            return None
        return min(self.temperaturas)

    def maxima(self):
        # Evita error si la lista está vacía; devuelve la temperatura más alta
        if not self.temperaturas:
            return None
        return max(self.temperaturas)

    def promedio(self):
        # Evita división por cero; calcula el promedio de las temperaturas
        if not self.temperaturas:
            return None
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        # Permite registrar varias temperaturas de una sola vez (cualquier cantidad)
        for temp in temps:
            self.registrar_temperatura(temp)

#Ejercicio:
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)