# examen con 3 preguntas, respuesta si o no y dar calificacion
pregunta1 = input("Python es un lenguaje de programacion? \r\n")
pregunta2 = input("Las variables comienzan con numero? \r\n")
pregunta3 = input("Los iteradores permiten realizar ciclos? \r\n")

calificacion = 0
if pregunta1 == "si":
    calificacion +=1
if pregunta2 == "no": 
    calificacion +=1
if pregunta3 == "si":
    calificacion +=1
else:
    calificacion +=0

print(calificacion)



        