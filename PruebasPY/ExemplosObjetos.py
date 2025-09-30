from pyclbr import Class


class Persona:
    """Clase para definir una persona"""
    def __init__(self,nome,dni,edade):
        self.nome = nome
        self.dni = dni
        self.edade = self.comprobarEdade(edade)

    def comprobarEdade(self,edade):
        if (edade>=0) and edade <100:
            return edade
        else:
            return 0

class Posto:
    def __init__(self,tarea,horario,salario,formacion):
        self.tarea = tarea
        self.horario = horario
        self.salario = salario
        self.formacion = formacion

class Trabajador (Persona,Posto):
    def __init__(self,nome,dni,edade,tarea,horario,salario,formacion,NUSS):
        Persona.__init__(self,nome,dni,edade)
        Posto.__init__(self,tarea,horario,salario,formacion)
        self.NUSS = NUSS

p = Persona("Manuel","3651D",36)

print(p.edade)
p.edade = -1
print(p.edade)
p.edade = 100
print(p.edade)

t = Trabajador("Pepe","54L",36,"Hogar","18:30-19",2000,"Niguna",54321)

print(t)

#Excepciones

class ErroIdade (Exception):
    def __init__(self,edade):
        self.edade = edade
    def __str__(self):
        return "Erro edade inadecuada: " +str(self.edade)+ " incorrecta"


class Persona4:
    """Clase para definir una persona"""
    def __init__(self,nome,dni,edade):
        self.nome = nome
        self.dni = dni
        self.edade = self.comprobarEdade(edade)

    def comprobarEdade(self,edade):
        if (edade>=0) and edade <100:
            return edade
        else:
            raise ErroIdade(edade)

try:
    persoa4 = Persona4("pepe",354,100)
    juan = Persona4("juan",354,57)
except ErroIdade:
    print("Erro de edad ")
