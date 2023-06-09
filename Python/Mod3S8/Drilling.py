"""
Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones: 
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista, 
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
• Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la 
segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D. 
• Finalmente, imprimiremos en pantalla el diccionario resultante.
"""

lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for sublista in lista:
    if sublista[0] == 0:
        continue
    for elemento in sublista:
        if elemento == 0:
            continue
        print(elemento)

diccionario = {}

for indice, sublista in enumerate(lista):
    clave = chr(ord('A') + indice)
    diccionario[clave] = sublista

print(diccionario)

