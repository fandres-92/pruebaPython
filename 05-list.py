lenguajes = ["Python", "Java", "PHP", "JavaScript"]
print(lenguajes)
print(lenguajes[1])

# Ordenar el list
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendo {lenguajes[3]}" # f permite unir string y variables
print(aprendiendo)

# Modificar un valor del list
lenguajes[2] = ".NET"
print(lenguajes)

# Agregar elementos al list
lenguajes.append("PHP")
print(lenguajes)

# Eliminar elementos del list
del lenguajes[1]
print(lenguajes)

#Eliminar el ultimo elemento del list
lenguajes.pop()
print(lenguajes)

#Eliminar con pop un elemento especifico
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre
lenguajes.remove(".NET")
print(lenguajes)