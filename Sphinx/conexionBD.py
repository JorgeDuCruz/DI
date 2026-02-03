import sqlite3 as dbapi


class ConexionBD:
    """Clase para realizar a conexión a una base de datos SQlite.

    """

    def __init__(self,rutaBd):
        """Crea as propiedades necesarias para o acceso a unha base de datos e as inicializa.
        
        A clase ConexiónBD utiliza tres propiedades: rutaBd para saber cal é o lugar onde está localizado o ficheiro, conexion que referencia o obxecto connection cando este se crea e cursor que referencia o obxecto cursor cando este é inicializado. A conexión e a creación do cursor non é automática, ten que ser invocada polo programador.

        :param rutaBd: Ruta onde se encontra o ficheiro da base de datos SQlite

        """
        self.rutaBd = rutaBd
        self.conexion = None
        self.cursor = None


    def conectaBD (self):
        """Método que crea a conexión da base de datos.

        Para realizar a conexión precisa da ruta onde está a base de datos que selle pasa no método __init__.

        """

        try:
            if self.conexion is None:
                if self.rutaBd is None:
                    print ("A ruta da base de datos é: None ")
                else:
                    self.conexion = dbapi.connect (self.rutaBd)
            else:
                print ("Base de datos conectada: " + self.conexion)

        except dbapi.StandardError as e:
            print ("Erro o facer a conexión a base de datos " + self.rutaBd + ": " + e)
        else:
            print ("Conexión de base de datos realizada")


    def creaCursor(self):
        """Método que crea o cursor da base de datos.

        Para realizar o cursor precísase previamente da execución do método conectaBD, que crea a conexión a base de 
        datos na ruta onde está padada o método __init__.

        """

        try:
            if self.conexion is None:
                print ("Creando o cursor: É necesario realizar a conexión a base de datos previamente")


            else:
                if self.cursor is None:
                    self.cursor = self.conexion.cursor()
                else:
                    print ("O cursor xa esta inicializado: " + self.cursor)


        except dbapi.Error as e:
            print (e)
        else:
            print ("Cursor preparado")


    def consultaSenParametros (self, consultaSQL):
        """Retorna unha lista cos rexistros dunha consulta realizada sen pasarlle parámetros.

        :param consultaSQL. Código da consulta sql a executar
        :return listaConsulta

        """

        listaConsulta = list()
        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(consultaSQL)

                    for fila in self.cursor.fetchall():
                        listaConsulta.append (fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
            return None
        else:
            print("Consulta executada")
            return listaConsulta

    def consultaConParametros(self, consultaSQL, *parametros):
        """Retorna unha lista cos rexistros dunha consulta realizada pasandolle os parámetros.

        A consulta ten que estar definida con '?' na clausula where de SQL.

        :param consultaSQL. Código da consulta sql a executar
        :param *parametros. Parámetros para introducir na consulta
        :return listaConsulta

        """

        listaConsulta = list()
        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(consultaSQL, parametros)

                    for fila in self.cursor.fetchall():
                        listaConsulta.append(fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
            return None
        else:
            print("Consulta executada")
            return listaConsulta

    def engadeRexistro(self, insertSQL, *parametros):
        try:
            if self.conexion is None:
                print("Realizando inserción: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Realizando inserción: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(insertSQL, parametros)
                    self.conexion.commit()

        except dbapi.DatabaseError as e:
            print("Erro facendo a inserción: " + str(e))
        else:
            print("Inserción executada")

    def actualizaRexistro(self, updateSQL, *parametros):
        try:
            if self.conexion is None:
                print("Realizando actualización rexistro: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Realizando actualización rexistro: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(updateSQL, parametros)
                    self.conexion.commit()

        except dbapi.DatabaseError as e:
            print("Erro facendo a actualización rexistro: " + str(e))
        else:
            print("Actualización rexistro executada")

    def borraRexistro (self, borraSQL, *parametros):
        try:
            if self.conexion is None:
                print("Realizando borrado rexistro: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Realizando borrado rexistro: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(borraSQL, parametros)
                    self.conexion.commit()

        except dbapi.DatabaseError as e:
            print("Erro facendo o borrado rexistro: " + str(e))
        else:
            print("Borrado de rexistro executado")


    def pechaBD(self):
        """Pecha o cursor e a conexión da base de datos si esta existe.

                Comproba si a conexión e o cursor existe e si é asi a pecha.



                """

        if self.cursor is not None:
            self.cursor.close()
        if self.conexion is not None:
            self.conexion.close()