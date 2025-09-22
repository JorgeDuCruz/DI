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

p = Persona("Manuel","3651D",36)

print(p.edade)
p.edade = -1
print(p.edade)
p.edade = 100
print(p.edade)