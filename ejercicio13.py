#Combinador de listas
#Ejercicio con IA:
from functools import reduce

class CombinadorListas:

    def intercalar(self, lista1, lista2):
        # Combina dos listas alternando sus elementos: l1[0], l2[0], l1[1], l2[1], ...
        resultado = []
        max_len = max(len(lista1), len(lista2))   # usa la longitud de la lista más larga
        for i in range(max_len):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        # Permite intercalar más de dos listas a la vez
        if not listas:
            return []
        return reduce(self.intercalar, listas)

#Ejercicio:
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []
        resultado = list(listas[0])
        for siguiente in listas[1:]:
            resultado = self.intercalar(resultado, siguiente)
        return resultado