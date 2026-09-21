#Codificador/Decodificador (César)
#Ejercicio con IA:
class CodificadorCesar:

    def __init__(self):
        self.historial = {}   # {palabra_original: palabra_codificada}

    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra   # deja sin cambios espacios, signos, números, etc.

        # Determina el punto de partida del alfabeto según sea mayúscula o minúscula
        base = ord('A') if letra.isupper() else ord('a')
        # Calcula la posición de la letra dentro del alfabeto (0-25)
        posicion = ord(letra) - base
        # Desplaza la posición y usa % 26 para "dar la vuelta" si se pasa de la Z/z
        nueva_posicion = (posicion + desplazamiento) % 26
        # Convierte la nueva posición de vuelta a carácter
        return chr(base + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        # Codifica cada letra de la palabra usando el Cifrado César
        codificada = ""
        for letra in palabra:
            codificada += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = codificada   # guarda el resultado en el historial

#Ejercicio:
class CodificadorCesar:
    def __init__(self):
        self.historial = {}  # {palabra_original: palabra_codificada}

    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra
        base = ord('a') if letra.islower() else ord('A')
        posicion = ord(letra) - base
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(base + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = resultado
        return resultado