# DB-API

import sqlite3 as dbapi
print(dbapi.apilevel) # version
print(dbapi.threadsafety) # 0-3 3:Totalmente usable por todos los hilos, 2:... investigar los distintos niveles del threadsafety
print(dbapi.paramstyle) # Estilo: usar "?", "<números>" o "<nombres>" para las consultas de sql, qmark significa que usamos el "?"


#Erroes de la interfaz: StandarError, InterfaceError, DataBaseError
#Errores de los datos: DataError,OperationalError,InternalError,ProgramingError,IntegrityError,


try:
    bdd = dbapi.connect("baseDatos.dat") # Crea una base de datos o abre una ya creada en sqlite
    print(bdd)
except dbapi.StandarError:
    print("Erro o abrir a base de datos")
try:
    cursor = bdd.cursor()
    print(cursor)
except dbapi.StandarError:
    print("Erro o crear o cursor")
try:
    '''
    cursor.execute("drop table usuarios;")
    cursor.execute("""create table usuarios( dni text,
                                             nome text,
                                             edade int)""")

    cursor.execute("insert into usuarios values ('12345678N','Pepe',34)")
    cursor.execute("insert into usuarios values ('87654321P','Jose',4)")
    cursor.execute("insert into usuarios values ('45678912Ñ','Joseph',56)")

    bdd.commit() # Guardar cambios
    '''
except dbapi.DatabaseError as e:
    print("Error coa taboa:",e)

try:
    cursor.execute("select * from usuarios;")

    for rexistro in cursor.fetchall():
        print("Dni:",rexistro[0])
        print("Nome:",rexistro[1])
        print("Edad:",rexistro[2])
except dbapi.DatabaseError as e:
    print("Error al hacer un select:",e)


try:
    cursor.execute("select * from usuarios where dni = ?",("12345678N",)) #La coma es importante, necesitas ponerla incluso siendo un solo parametro. También se puede pasar una lista, lo que necesita es una colección


    for rexistro in cursor.fetchall():
        print("Dni:",rexistro[0])
        print("Nome:",rexistro[1])
        print("Edad:",rexistro[2])
except dbapi.DatabaseError as e:
    print("Error al hacer un select:",e)
bdd.close()
