#Gestor de compras con totales

#Ejercicio con IA: 
class CarroCompras:
    def __init__(self):
        self.articulos = {}   # diccionario {nombre: precio}

    def agregar_articulo(self, nombre, precio):
        # Agrega el artículo o actualiza su precio si ya existe
        self.articulos[nombre] = precio

    def total_carrito(self):
        # Suma todos los precios almacenados en el diccionario
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        # Devuelve los nombres de los artículos cuyo precio está dentro del rango dado
        return [
            nombre for nombre, precio in self.articulos.items()
            if precio_min <= precio <= precio_max
        ]

#Ejercicio:
class CarroCompras:
    def __init__(self):
        self.articulo = {}  

    def agregar_articulo(self, nombre, precio):
        self.articulo[nombre] = precio

    def total_carrito(self):
        return sum(self.articulo.values())

    def articulos_por_rango(self, precio_min, precio_max):
        return [
            nombre for nombre, precio in self.articulo.items()
                if precio_min <= precio <= precio_max
        ]