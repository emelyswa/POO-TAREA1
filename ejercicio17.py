#Grupo de edades
#Ejercicio con IA:
class AgrupadorEdades:

    def __init__(self):
        self.grupos = {}   # {categoria: [edades]}

    def clasificar_edad(self, edad):
        # Determina la categoría etaria según rangos de edad predefinidos
        if edad <= 12:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        # Clasifica cualquier cantidad de edades en sus respectivas categorías
        resultado = {"niño": [], "adolescente": [], "adulto": [], "mayor": []}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            resultado[categoria].append(edad)
        self.grupos = resultado   # se guarda para edad_promedio_categoria()
        return resultado

    def edad_promedio_categoria(self, categoria):
        # Calcula el promedio de edades de una categoría específica
        edades = self.grupos.get(categoria, [])
        if not edades:
            return None
        return sum(edades) / len(edades)

#Ejercicio:
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {"niño": [], "adolescente": [], "adulto": [], "mayor": []}

    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])
        if not edades:
            return 0
        return sum(edades) / len(edades)
