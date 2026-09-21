#Detector de números pares e impares

#Ejercicio con IA:
class AnalizadorNumeros:

    def __init__(self):
        # Guarda el resultado de la última separación (inicia vacío)
        self.ultimo_resultado = {'pares': [], 'impares': []}

    def es_par(self, numero):
        # True si el número es divisible entre 2 (resto 0)
        return numero % 2 == 0

    def separar(self, *numeros):
        # Recibe cualquier cantidad de números y los clasifica
        resultado = {'pares': [], 'impares': []}
        for numero in numeros:
            if self.es_par(numero):
                resultado['pares'].append(numero)
            else:
                resultado['impares'].append(numero)
        self.ultimo_resultado = resultado  # se guarda para cantidad_pares_impares()
        return resultado

    def cantidad_pares_impares(self):
        # Devuelve una tupla (cantidad_pares, cantidad_impares) del último resultado
        return (len(self.ultimo_resultado['pares']), len(self.ultimo_resultado['impares']))
    
#Ejercicio:
class AnalizadorNumeros:
    def es_par(self, num):
        return num % 2 == 0

    def separar(self, *numeros):
        resultado = {"pares": [], "impares": []}
        for num in numeros:
            if self.es_par(num):
                resultado["pares"].append(num)
            else:
                resultado["impares"].append(num)
        return resultado

    def cantidad_pares_impares(self, *numeros):
        clasificados = self.separar(*numeros)
        return (len(clasificados["pares"]), len(clasificados["impares"]))