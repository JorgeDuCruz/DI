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

    nome = property(getNome,setNome)
    dni = property(getDni,setDni)
    edade = property(getEdade,setEdade)



p3 = Persona("jorge",546,15)
p3.edade = 101
print(p3.edade)