# Ejemplo con Elif
ocupacion = "Jubilado"
if ocupacion == "Estudiante":
    print("Tienes 50% de descuento")
elif ocupacion == "Jubilado":
    print("Tienes 75% de descuento")
elif ocupacion == "Desempleado": # puedo colocar todos los elif que necesite
    print("Tienes el 95% de descuento")
else:
    print("Dedes pagar el 100%")