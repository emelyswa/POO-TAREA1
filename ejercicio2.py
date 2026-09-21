# Contador de palabras unicas

#Ejercicio con IA: 
class AnalizadorTexto:
    def __init__(self):
        self.conjunto_palabras = set()   # evita duplicados (búsqueda rápida O(1))
        self.lista_palabras = []         # conserva el orden de inserción

    def agregar_palabra(self, palabra):
        # Solo agrega la palabra si no existe ya en el set
        if palabra not in self.conjunto_palabras:
            self.conjunto_palabras.add(palabra)   # registra la palabra como "ya vista"
            self.lista_palabras.append(palabra)   # la guarda respetando el orden en que llegó

    def contar_palabras(self):
        # Devuelve la cantidad de palabras únicas almacenadas
        return len(self.conjunto_palabras)

    def agregar_multiples(self, *args):
        # Permite agregar varias palabras de una sola vez (cualquier cantidad)
        for palabra in args:
            self.agregar_palabra(palabra)

#Ejercicio:
class AnalizadorTexto:

    def __init__(self):
        self.palabras_unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
