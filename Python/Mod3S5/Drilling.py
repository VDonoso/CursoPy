# Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, e imprimir en pantalla las 
# consonantes restantes y su posición dentro de dicha palabra.

palabra = "paralelepípedo"
posicion = 0

for val in palabra:
    if val in "aeiouAEIOU":
        continue
    print(f"La consonante '{val}' en la posición {posicion} fue encontrada")
    posicion += 1

"""
palabra = "paralelepípedo"
posicion = 0
for val in "paralelepipedo":
    if val == "a"
        continue
    if val == "e":
        continue
    if val == "i": 
        continue
    if val == "o":
        continue
    if val == "u":
        continue
    print(val)
print("Fin")
"""