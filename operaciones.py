# Preguntar al usuario qué operación quiere realizar
operacion = input("¿Qué operación deseas realizar? (multiplicación/división): ")

#pedir los dos números
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Realizar la operación según la elección del usuario
if operacion == "multiplicación":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "división":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")