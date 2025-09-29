"""Colecciones:

Listas
Tuples
Diccionarios


"""
from time import process_time_ns

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

#Tuplas son listas pero no se pueden modificar

l = (2,5,2+4j,"un texto",[22,3,5,6],3,9) # el parentesis es solo visual la tupla existe con las comas directamente los parentesis pueden no aparecer
t = 2,5,2+4j,"un texto",[22,3,5,6],3,9  #Ejemplo de tupla sin parentesis
t2 = 2,5,2+4j,"un texto",(22,3,5,6),3,9 #Ejemplo de necesidad de parentesis en dupla
t3 = 5, # ejemplo de tupla de un solo valor
t4 =None,54 # ejemplo de añadir un elemento vacio, no sirve para casi nada porque lo que este vacio casi siempre se puede omitir
print(t4)
print(t3)
print(t)
print(l)
print(l[2])
l[-3][2] = 4 # se puede modificar una lista si esta en una tupla siempre que solo se modifique la lista y no la tupla
print(l)


#Diccionarios estructura de datos donde se trabaja de forma clave:valor

d = {1:"Pepe",
     "pepe":"Antonio",
     3:["Jose"," Luis"]
}#parecido a los objetos de JavaScript
print(d[3])
d[3] = "jose Luis" # se puede modificar un valor sabiendo su clave
print(d[3])
print(d["pepe"]) #Las claves pueden ser numeros, string,etc pero no con letras o palabras sueltas


l2 = [1,2,3]
l3 = list((1,2,3,4))

t5 = (1,2,3)
t6 = tuple(l2)

d2 = {1:"1",2:"11",3:"111"}
d3 = dict()


l2.append([3,2,1,0]) #Añade el objeto tal cual (Solo añade un valor por uso)
l2.extend([3,2,1]) # añade los objetos de la coleccion (para añadir varios valores a la vez)
print(l2)

l2.insert(7,"prueba") # Añade un valor en la posicion indicad (el -1 no lo insertara como ultimo valor sino como penultimo)
print(l2.count(2))
print(l2)
print(l2.index(1,3,7)) # devuelve el indice del valor que busque(primera coincidencia), 2º parametro es la posicion a partir de la que busca y el 3º parametro es hasta que posicion busca
print(l2.pop(3)) # Devuelve el valor en la posicion indicada y luego lo elimina de la lista
print(l2)
l2.remove(2) # elimina la primera coincidencia del valor indicado
print(l2)
l2.reverse() # le da la vuelta a la lista
print(l2)
l4 = ["uno","Dous","Tres","Cinco","Cuatro","Seis"]
l4.sort(key = len)
print(l4)

taboa_alturas = [("Manuela",1.82),("Pepe",2.05),("Ana",1.76)]

def altura (persoa): # Devuelve la altura de cada persona que forma parte de la tabla altura
     return persoa[1]

taboa_alturas.sort(key = altura) # key es la funcion que usa para hacer el orden, la funcion recibe un parametro por cada objeto en la tabla a ordenar
print(taboa_alturas)

def saudar(lingua):
     def saudar_es():
          print("hola")

     def saudar_gl():
          print("ola")

     def saudar_ig():
          print("hello")

     func_saudo = {"es": saudar_es, #Tener cuidado con no poner los () porque sino se ejecutan las funciones y ya
                   "gl":saudar_gl,
                   "ig":saudar_ig
                   }
     return func_saudo[lingua] # Puedes pasar funciones como si fueran variables

f = saudar("gl")
print(f)
f()

def es_par(n):
     return n%2 == 0

pruebaLis = [1,2,3,4]
copiarLis = filter(es_par,pruebaLis) # Filtra de la lista PruebaLis usando la funcion es_par

copiarLis2 = filter(lambda n: n%2==0,pruebaLis)

for n in copiarLis2:
     print(n)

# filter, map, reduce importantes en python 2 pero prescindibles en python 3

#Compresion de listas para sustituir a filter,map y reduce
# [<contenido en lista> for <n> in <Lista>] esto permite hacerle algun cambio a los elemntos de una lista en la igualacion
l3 = [n+1 for n in pruebaLis] # Le suma 1 a cada elemento de pruebaLis
print(l3)
# Al concepto anterior se le puede añadir una condicion para añadir el valor
l4 = [n for n in pruebaLis if n%2==0]#Guarda solo los valores pares
print(l4)

m = ["+","*"]
z = []
for s in m:
     for n in pruebaLis:
          if n<4:
               z.append(n*s)
print(z)

z2 = [n*s for s in m
               for n in pruebaLis
                    if n<4]
#Se puede poner en una linea pero se entiende un poco peor[n*s for s in m for n in pruebaLis if n<4]
print(z2)

x2 = (n**2 for n in pruebaLis) # No es una lista, es un generador que es más parecido a una funcion
for n in x2:
     print(n)