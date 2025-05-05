# Preguntar al usuario qué operación quiere realizar
operacion = input("¿Qué operación deseas realizar? (suma/resta): ").strip().lower()

# Pedir los dos números
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Realizar la operación según la elección del usuario
if operacion == "suma":
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "resta":
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
else:
    print("Operación no válida. Por favor elige 'suma' o 'resta'.")