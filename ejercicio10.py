#Gestor de tareas con prioridad 
#Ejercicio con IA:
class Tareas:

    def __init__(self):
        self.tareas = []   # lista de tuplas (descripcion, prioridad)

    def agregar_tarea(self, descripcion, prioridad):
        # Agrega una nueva tarea como tupla (descripcion, prioridad)
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        # Devuelve solo las tareas cuya prioridad es "alta" (sin importar mayúsculas/minúsculas)
        return [
            tarea for tarea in self.tareas
            if tarea[1].lower() == "alta"
        ]

    def eliminar_completada(self, descripcion):
        # Busca la primera tarea que coincida con la descripción y la elimina
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True   # confirma que sí se eliminó algo
        return False   # no se encontró ninguna tarea con esa descripción

#Ejercicio:
class Tareas: 
    def __init__(self):
        self.lista_tareas = []  # [(descripcion, prioridad), ...]
 
    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))
 
    def tareas_prioritarias(self):
        prioritarias = []
        for tarea in self.lista_tareas:
            descripcion = tarea[0]
            prioridad = tarea[1]
            if prioridad == "alta":
                prioritarias.append((descripcion, prioridad))
        return prioritarias
 
    def eliminar_completada(self, descripcion):
        nueva_lista = []
        for tarea in self.lista_tareas:
            if tarea[0] != descripcion:
                nueva_lista.append(tarea)
        self.lista_tareas = nueva_lista