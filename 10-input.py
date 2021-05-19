# nombre = input("Cual es tu nombre: \r\n") # \r\n realiza salto de linea
# print(f"Hola {nombre}")

edad = int(input("Cual es tu edad?: "))
# convertir edad string a un entero

if edad >= 18:
    print("Ya puedes votar")
else:
    print("Aun no puedes votar")

numero = int(input("Ingresa un numero y te dire si es par o no \r\n"))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")