# Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla. 
# Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay 
# entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.

n = int(input("Ingrese un número: "))

if n < 0:
    print("El número ingresado debe ser positivo")
else:
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    print(f"El factorial de {n} es {factorial}")
