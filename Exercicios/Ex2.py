#Ejercicio 2.3 pasar Farenhait a Celsius
def funcion1(grados):
    gradosC = (grados-32)*5/9
    return gradosC

#Ejercicio 2.4 Taboa de Conversion
gradosFa = ["ºF"]
gradosCel = ["ºC"]

for num in range(0,120,10):
    gradosFa.append(num)
    numC = funcion1(num)
    gradosCel.append(numC)

for indc in range(0,gradosFa.index(gradosFa[-1])):
    print(gradosFa[indc],"||",gradosCel[indc])