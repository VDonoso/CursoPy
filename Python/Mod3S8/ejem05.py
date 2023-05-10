"""
#1
lista = [10,50,75,83]

for x in range(len(lista)):
    print(lista[x])

#2
lista = [10,50,75,83]

for x in lista:
    print(x)
#3
lista = [10,50,75,83]
while x < len(lista):
    print(lista[x])
    x= x+1

#4
lista = [10,50,75,83]

for x, val in enumerate(lista) :
    print(val)
 
#5
mi_set = {'london','new york', 'seattle', 'sidney'}

for item in iter(mi_set) :
    print(item)
"""
#6
paises_y_capitales = {'japon':"tokio",'inglaterra':'londres','francia':'paris','alemania':'berlin'}

keys = paises_y_capitales.keys()

for clave in keys :
    print(f"{clave}-{paises_y_capitales[clave]}")