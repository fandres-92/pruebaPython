lenguajes = ("Python", "Java", "PHP", "JavaScript")
for i in lenguajes: # iterador i imprime todo en lineas segun los elementos que tenga el list
    print(lenguajes)

lenguajes = ("Python", "Java", "PHP", "JavaScript")
for lenguaje in lenguajes: # si el iterado es distinto a i imprime cada elemento por linea
    print(lenguaje)

intentos=1
while intentos <= 4:
    intentos +=1 # suma 1 antes de realizar la primera iteracion
    print(intentos)

intentos=1
while intentos <= 4:
    print(intentos)
    intentos +=1 # suma 1 despues de realizar la primera iteracion

intentos=int(input("escriba numero de intentos: "))
print(f"tienes {intentos} intentos disponibles")
   



   
    