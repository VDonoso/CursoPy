"""
Crear una función que acepte 3 números como parámetros, sume todos los valores, y 
adicionalmente reste el segundo y tercer parámetro al primero.
Al invocar la función, debemos pasarle los parámetros en forma de lista. Esta devolverá ambos 
resultados en una tupla. Los resultados se deben imprimir en pantalla
"""
def suma(a,b,c):
    sumar = a + b + c
    restar = a - (b+c)
    resultado = (sumar, restar)
    return resultado

resultado = suma(10, 15, 7)
print(resultado)
