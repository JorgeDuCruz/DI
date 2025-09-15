"""Colecciones:

Listas
Tuples
Diccionarios


"""

#Listas

l = [23,25.5,3+4j,-15,"pepe",[23,25,51],12+45] # la lista puede contener de distintos tipos en la misma lista
print(l[-1])
print(l)
l[-2] = "Personaje npc" #se puede modificar una lista


print(l)
print(type(l))

#lista dentro de lista
print(l[5][2:6])

#Slicing puedes pillar un rango con : estnado el primer numero incluido y el segundo excluido
print(l[2:5])
print(l[:5])
print(l[2:])
print(l[1:6:3]) # el ultimo numero es cada cuantos saltos pilla en este caso pilla un valor cada 3
print(l[::-1]) # puedes hacer que la direccion del salto sea al reves
