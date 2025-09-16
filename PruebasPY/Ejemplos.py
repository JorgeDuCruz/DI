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
