#Selector de rango con tuplas
#Ejercicio con IA:
class SelectorRango:

    def crear_rango(self, inicio, fin):
        # Genera una tupla con todos los números desde 'inicio' hasta 'fin' (incluido)
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        # Recibe varios rangos como tuplas (inicio, fin), por ejemplo: (1,5), (3,8)
        conjunto_combinado = set()
        for inicio, fin in rangos:
            # Agrega todos los números del rango actual, sin duplicar los que ya estaban
            conjunto_combinado.update(self.crear_rango(inicio, fin))
        return list(conjunto_combinado)

#Ejercicio:
class SelectorRango:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        combinados = set()
        for inicio, fin in rangos:
            combinados.update(self.crear_rango(inicio, fin))
        return sorted(combinados)
