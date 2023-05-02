#Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan
# son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las 
# personas con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente, 
# imprimiremos en pantalla la lista

nombre1 = "Fulano"
nombre2 = "Margarita"
nombre3 = "Pedro"

apellido1 = "Detal"
apellido2 = "Flores"
apellido3 = "Pascal"

telefono1 = 987654321
telefono2 = 912345678
telefono3 = 924681012

diccionario1 = {nombre1, apellido1, telefono1}
print(diccionario1)

diccionario2 = {nombre2, apellido2, telefono2} 
print(diccionario2)

diccionario3 = {nombre3, apellido3, telefono3}
print(diccionario3)

lista = [diccionario1, diccionario2, diccionario3]
print(lista)
