class Persona:
    """Clase para definir una persona"""
    def __init__(self,nome,dni,edade,**outros): #Outros con ** para recibir mas datos de los que necesita
        self.nome = nome
        self.dni = dni
        self.edade = self.comprobarEdade(edade)

    def comprobarEdade(self,edade):
        if (edade>=0) and edade <100:
            return edade
        else:
            return 0

class Posto:
    def __init__(self,tarea,horario,salario,formacion,**outros): #Outros con ** para recibir mas datos de los que necesita
        self.tarea = tarea
        self.horario = horario
        self.salario = salario
        self.formacion = formacion

class Trabajador (Persona,Posto):
    def __init__(self,nome,dni,edade,tarea,horario,salario,formacion,NUSS):
        super().__init__(nome=nome,dni=dni,edade=edade,tarea=tarea,horario=horario,salario=salario,formacion=formacion) # manda a los dos constructores pero con los nombre para que los padres puedan saber que valor recojer
        self.NUSS = NUSS

t2 = Trabajador("Juan",5679,45,"Soldador",7,2300,"CM","13515/UN")
print(t2.edade)