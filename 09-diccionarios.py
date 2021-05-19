# creando un diccionario simple
cancion = {
    "artista" : "Metallica", # llave y valor
    "cancion" : "Enter Sadman",
    "lanzamiento" : 1992,
    "likes" : 3000
}

# acceder a los elementos del diccionario
print(cancion["cancion"]) # entre los corchetes ingresas la llave y te imprime el valor de esa llave
print(cancion["artista"])

# mesclar con un string
artista = cancion["artista"]
print(f"Estoy escuchando la cancion {artista} ")

# agregar nuevos valores
cancion["playlist"] = "Heavy Metal"
print(cancion)

# Reemplazar valor existente
cancion["cancion"] = "Seek y Destroyed"
print(cancion)

# Eliminar un elemento
del cancion["lanzamiento"]
print(cancion)