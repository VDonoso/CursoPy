#---------------------------
#Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar. 
#En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar 
#subcondiciones; en su lugar, usar condiciones anidadas.
#---------------

num = -4

if num >= 0 :
    if num == 0:
        print("El nmero es Cero")
    else :
        print("El número es positivo")
else:
    print("el número es negativo")
if num % 2 == 0: 
    print ('El número', num, 'es par.') 
else: 
    print ('El número', num, 'es impar.')