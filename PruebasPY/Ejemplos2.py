# Funciones

def nome_da_funcion(parametro1, parametro2):
    """Instruccions da funcion
       que procesan los parametros"""
    print(parametro2)
    print(parametro1)
    print(parametro2,parametro1)


nome_da_funcion("José Luís","Baja de ahí")

nome_da_funcion(parametro2="Baja de ahí",parametro1="José Luis")

def repetir_mensaxe(mensaxe,veces = 5):
    print(mensaxe*veces)

repetir_mensaxe(mensaxe="Anota eso!\n")
repetir_mensaxe(veces=2,mensaxe="Es igual!\n")

def repetir_mensaxes (mensaxe,veces = 5,*maisMensaxes): # El * simboliza que el parametro puede ser recibido desde 0 veces hasta indefinidas veces. Para usar el parametro tratalo como Tupla
    print(mensaxe*veces)
    for outroMensaxe in maisMensaxes: # Ejemplo de como acceder al parametro indefinido
        print(outroMensaxe)

repetir_mensaxes("Ola",2,"Caracola","Reporte del dia","Probar a hacer un bucle que mande un chingo de parametros") # Realmente el parametro indefinido es simplemente que puedes pasar una tupla