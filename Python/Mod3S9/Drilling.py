"""
Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos 
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos 
números como parámetros y regrese el resultado en forma de tupla de su suma, resta, 
multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta, 
Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función 
creada anteriormente

def suma(a,b):
    resultado1 = (a + b) 
    return resultado1
    
def resta(a,b):
    resultado2 = (a - b) 
    return resultado2
   
def multiplicación(a,b):
    resultado3 = (a * b)
    return resultado3
    
def división(a,b):
    resultado4 = (a / b)
    return resultado4

def operaciones(a, b):
    resultado_suma = suma(a,b)
    resultado_resta = resta(a,b)
    resultado_multiplicacion = multiplicación(a,b)
    resultado_division = división(a,b)
    
    resultados = {
        "suma": resultado_suma,
        "resta": resultado_resta,
        "multiplicación": resultado_multiplicacion,
        "división": resultado_division
    }
    return (resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division)
resultado_tupla = operaciones(2, 5)
print(resultado_tupla)

def operaciones2(a,**b):
    resultado_suma = suma(a,b)
    resultado_resta = resta(a,b)
    resultado_multiplicacion = multiplicación(a,b)
    resultado_division = división(a,b)
    return(resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division)

operaciones2(a=suma, b=resta, c=multiplicación, d=división)
print(operaciones2)

"""
def suma(a,b):
    resultado1 = (a + b) 
    return resultado1
    
def resta(a,b):
    resultado2 = (a - b) 
    return resultado2
   
def multiplicación(a,b):
    resultado3 = (a * b)
    return resultado3
    
def división(a,b):
    resultado4 = (a / b)
    return resultado4

def operaciones(a, b):
    resultado_suma = suma(a,b)
    resultado_resta = resta(a,b)
    resultado_multiplicacion = multiplicación(a,b)
    resultado_division = división(a,b)
    
    resultados = {
        "suma": resultado_suma,
        "resta": resultado_resta,
        "multiplicación": resultado_multiplicacion,
        "división": resultado_division
    }
    return (resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division)

resultado_tupla = operaciones(2, 5)
print(resultado_tupla)

def operaciones2(a,b):
    resultado_suma = suma(a,b)
    resultado_resta = resta(a,b)
    resultado_multiplicacion = multiplicación(a,b)
    resultado_division = división(a,b)
    return (resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division)

resultado_diccionario = {
    "Suma": operaciones2(2, 5)[0],
    "Resta": operaciones2(2, 5)[1],
    "Multiplicación": operaciones2(2, 5)[2],
    "División": operaciones2(2, 5)[3]
}

print(resultado_diccionario)
