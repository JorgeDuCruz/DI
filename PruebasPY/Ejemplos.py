#Sentecias condicionales
import random

n1 = random.randint(1,10)
if n1>5:
    print(n1)
elif(n1==3):
    print("Si es",n1,"nfn")#Para concatenar en lugar de usar "+" se usa simplemente una ",". Cada concatenacion añade autopmaticamente un espacio para que no se peguen las distintas partes
else: # Prueba
 print(n1)
 print(n1)

#VehiculoTipo = (n1>3) ? "Moto":"Coche" --> Esto es Java
vehiculoTipo = "Coche" if (n1>3) else "Moto" # -> equivalente en Python al operador ternario
print(vehiculoTipo)


#Bucle while que cuente de n1 a 10

while n1<=10:
    print(n1)
    n1+=1


# do-wile no existe como tal en python
while True:
    print(n1)
    if n1>10:
        break # Esta configuracion(Con el if) seria el equivalente al do while

#Bucle for
suma=0
numeros = [1,2,5,4,846,654,654,3,12]
for numero in numeros: # recorres cada elemento de una lista con un nombre especifico
    print(numero)
    suma += numero
print(suma)

dicconario = {"A":23,"B":25}
for dic in dicconario:
    print(dic)
    print(dicconario[dic])
