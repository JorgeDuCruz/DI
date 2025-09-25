#Encapsulacion

class Persona:
    """Clase para definir una persona"""
    def __init__(self,nome,dni,edade):
        self.__nome = nome # __ -> privacidad de clase
        self.__dni = dni
        self.setEdade(edade)

    def setNome(self,nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setEdade(self,edade):
        if (edade>=0) and edade <100:
            self.__edade = edade
        else:
            self.__edade = 0
    def getEdade(self):
        return self.__edade

    def setDni(self,dni):
        if type(dni) == str:
            if len(dni)==9:
                self.__dni = dni
            else:
                self.__dni = "000000000T"
        else:
            self.__dni = "ERROR"
    def getDni(self):
        return self.__dni

    def __str__(self):
        return "Mango con huevo para: "+self.nome
    nome = property(getNome,setNome)
    dni = property(getDni,setDni)
    edade = property(getEdade,setEdade)

    def __len__(self):
        return len(vars(self)) # Devuelve cuantas variables diferentes guarda el objeto

    def __eq__(self, other):
        return self.__dni == other.__dni

    def __ne__(self, other):
        return self.__dni != other.__dni

p3 = Persona("jorge",546,15)
p3.edade = 101
p3.respuesta = "cago en todo" #Puedes añadirle propiedades a una clase porque patata
print(p3)
print(p3.edade)
print(p3._Persona__dni) #Esto te permite saltarte la privacidad de las variables

p2 = Persona("none",547,25)
p4 = Persona("jorge",546,15)
print(p3.__ne__(p2))
print(p3==(p4)) # Puedes usar __eq__ si lo implementas en la clase
print(p3.__len__())
print(p2.__len__())