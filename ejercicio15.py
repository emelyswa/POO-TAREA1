#Divisores de un número
#Ejercicio con IA:
class DivisorFinder:

    def encontrar_divisores(self, numero):
        # Recorre todos los números del 1 al 'numero' y guarda los que dividen exacto
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)   # devuelve una tupla (inmutable) con los divisores

    def es_perfecto(self, numero):
        # Un número perfecto es aquel que es igual a la suma de sus divisores propios
        divisores = self.encontrar_divisores(numero)
        # se excluye el propio número (el último divisor)
        suma_propios = sum(divisores) - numero
        return suma_propios == numero

    def encontrar_multiples_divisores(self, *numeros):
        # Calcula los divisores de varios números a la vez
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado

#Ejercicio:
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma_propios = sum(divisores) - numero
        return suma_propios == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado