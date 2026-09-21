#Validador de Caracteres
#Ejercicio con IA:
class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""   # guarda el texto más largo analizado

    def solo_vocales(self, letra):
        # True si el carácter (en minúscula) es una vocal
        return letra.lower() in "aeiou"

    def es_digito(self, caracter):
        # True si el carácter es un dígito (0-9)
        return caracter.isdigit()

    def es_consonante(self, caracter):
        # True si es una letra del alfabeto pero no es vocal
        return caracter.isalpha() and not self.solo_vocales(caracter)

    def contar_por_tipo(self, texto):
        # Cuenta cuántas vocales, consonantes y dígitos hay en el texto
        resultado = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
        for caracter in texto:
            if self.solo_vocales(caracter):
                resultado['vocales'] += 1
            elif self.es_consonante(caracter):
                resultado['consonantes'] += 1
            elif self.es_digito(caracter):
                resultado['digitos'] += 1
            # cualquier otro carácter (espacios, símbolos, etc.) no se cuenta

        # Actualiza el texto más largo analizado hasta ahora
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return resultado

#Ejercicio:
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteo = {"vocales": 0, "consonantes": 0, "digitos": 0}
        for caracter in texto:
            if caracter.isdigit():
                conteo["digitos"] += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    conteo["vocales"] += 1
                else:
                    conteo["consonantes"] += 1
        return conteo