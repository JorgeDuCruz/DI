class Persona:
    """Clase para definir una persona"""
    def __init__(self,nome,dni,edade):
        self.nome = nome
        self.dni = dni
        self.edade = self.comprobarEdade(edade)

    def comprobarEdade(self,edade):
        if (edade>=0) and edade <100:
            return id
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