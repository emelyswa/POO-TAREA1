#Inversor de secuencias

#Ejercicio con IA:
class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []
        # Recorre el índice desde el final (len-1) hasta el inicio (0), paso -1
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])   # agrega los elementos en orden inverso
        return invertida

    def invertir_multiples(self, *listas):
        # Permite invertir varias listas a la vez (cualquier cantidad)
        resultado = {}
        for lista in listas:
            # Las listas no son "hashables", así que se usa una tupla
            # de la lista original como llave del diccionario.
            clave = tuple(lista)
            resultado[clave] = self.invertir_lista(lista)
        return resultado

#Ejercicio:
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            clave = tuple(lista)  # una lista no puede ser clave; se usa tupla
            resultado[clave] = self.invertir_lista(lista)
        return resultado