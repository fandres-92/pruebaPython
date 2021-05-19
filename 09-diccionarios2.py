# inicar un diccionario vacio
jugador = {}
print(jugador)

# Se une un jugador
jugador["nombre"] = "Faber"
jugador["puntaje"] = 0
print(jugador)

# incrementando el puntaje
jugador["puntaje"] = 200
print(jugador)

#acceder a un valor
print(jugador.get("consola", "No existe ese valor")) # la segunda variable muestra un mensaje personalizado

#Iterar en el diccionario
for llave, valor in jugador.items():
    print(llave, valor)

# eliminar jugador y puntaje
del jugador["nombre"]
del jugador["puntaje"]
print(jugador)
    