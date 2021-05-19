# Condicion mayor a 
balance = 1
if balance > 0:
    print("Puedes pagar")
else:
    print("No tiene saldo")

#likes
likes = 200
if likes > 200:
    print("Excelente")
else:
    print("ya casi")

# if con texto
lenguaje = "Java"
if not lenguaje == "Java": # el not despues del if niega el condicional
    print("Es diferente")
else:
    print (f"Lenguaje es igual a {lenguaje}")

#Evaluar un Boolean
usuario_autenticado = True

if usuario_autenticado: #no es necesario colocar == True porque por defecto asume que es True
    print("Acceso al sistema")
else:
    print("Debes inicar sesion")

# Evaluar un elemento de una lista
lenguajes = ["Python", "Java", "PHP", "JavaScript"]
if "Java" in lenguajes:
    print("Esta en la lista")
else:
    print("No esta en la lista")

# IF anidado
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado: #no es necesario colocar == True porque por defecto asume que es True
    if usuario_admin:
        print("Acceso Total")
    else:
        print("Acceso al sistema")
else:
    print("Debes inicar sesion")
