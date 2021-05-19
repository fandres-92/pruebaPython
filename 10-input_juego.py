pregunta = "Ingresa un numero y te dire si es par o impar \r\n"
pregunta += "(Escribe 'cerrar' para salir de la aplicacion) \r\n" # += concatena las 2 preguntas
preguntar = True

while preguntar:

    numero = input(pregunta)

    if numero == "cerrar":
        preguntar = False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f"El numero {numero} es par")
        else:
            print(f"El numero {numero} es impar")