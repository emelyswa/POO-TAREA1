print("--- Ejercicio 1: Calificador ---")
c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())


print("\n--- Ejercicio 2: AnalizadorTexto ---")
at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())


print("\n--- Ejercicio 3: CarroCompras ---")
carro = CarroCompras()
carro.agregar_articulo("pan", 2.50)
carro.agregar_articulo("leche", 3.00)
print(carro.total_carrito())


print("\n--- Ejercicio 4: InversorSecuencia ---")
inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(inv.invertir_multiples([1, 2, 3], [4, 5]))


print("\n--- Ejercicio 5: AnalizadorNumeros ---")
an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares(1, 2, 3, 4, 5))


print("\n--- Ejercicio 6: GestorTemperatura ---")
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())


print("\n--- Ejercicio 7: GestorPersonas ---")
gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))


print("\n--- Ejercicio 8: Equipos ---")
eq = Equipos()
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.agregar_jugador("B", "Luis")
print(eq.equipo_mayor_integrantes())


print("\n--- Ejercicio 9: AnalizadorString ---")
astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))


print("\n--- Ejercicio 10: Tareas ---")
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())


print("\n--- Ejercicio 11: ContadorFrecuencia ---")
cf = ContadorFrecuencia()
for elem in ["a", "b", "a"]:
    cf.agregar_elemento(elem)
print(cf.elemento_mas_frecuente())


print("\n--- Ejercicio 12: SelectorRango ---")
sr = SelectorRango()
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))


print("\n--- Ejercicio 13: CombinadorListas ---")
cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))


print("\n--- Ejercicio 14: RegistroNotas ---")
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.mejor_estudiante())


print("\n--- Ejercicio 15: DivisorFinder ---")
df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(6))


print("\n--- Ejercicio 16: CodificadorCesar ---")
cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))


print("\n--- Ejercicio 17: AgrupadorEdades ---")
ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))


print("\n--- Ejercicio 18: CalculadorDistancia ---")
cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))


print("\n--- Ejercicio 19: Inventario ---")
inventario = Inventario()
inventario.agregar_stock("pan", 50)
print(inventario.restar_stock("pan", 30))
print(inventario.productos_bajo_stock(25))


print("\n--- Ejercicio 20: AnalizadorPatrones ---")
ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato esta aqui"))
