# Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, e imprimir en 
# pantalla el valor de cada elemento indicando si es par, impar o cero.

i = 0 

for i in range(10) :
    i = i+1
    if i % 2 == 0 :
        print ('El número', i, 'es par.') 
    else: 
        print ('El número', i, 'es impar.')