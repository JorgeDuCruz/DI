class ErroIdade(Exception):
    def __init__(self,id):
        self.idade = id
    def __str__(self):
        return self.idade

class Persoa:
    def __init__(self,idade):
        self.idade = idade


    def comprobarIdade(self,id):
        """
        Verifica idade

        :param id: idade
        :return: idade
        :raise: ErrorIdade

        """
        if id<18:
            return id
        else:
            raise ErroIdade(id)