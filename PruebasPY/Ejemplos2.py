# Funciones

def nome_da_funcion(parametro1, parametro2):
    """Instruccions da funcion
       que procesan los parametros"""
    print(parametro2)
    print(parametro1)
    print(parametro2,parametro1)


nome_da_funcion("José Luís","Baja de ahí")

nome_da_funcion(parametro2="Baja de ahí",parametro1="José Luis")
nome_da_funcion("PRUEBA numeros",564)

def repetir_mensaxe(mensaxe,veces = 5):
    print(mensaxe*veces)

repetir_mensaxe(mensaxe="Anota eso!\n")
repetir_mensaxe(veces=2,mensaxe="Es igual!\n")

def repetir_mensaxes (mensaxe,veces = 5,*maisMensaxes): # El * simboliza que el parametro es especificamente una tupla
    print(str(mensaxe)*veces) #Parear el mensaje a string para garantizar que si le pasas un numero no se multiplique sin más
    print(len(maisMensaxes)) # funcion len devulve la longitud de una coleccion
    for outroMensaxe in maisMensaxes: # Ejemplo de como acceder al parametro indefinido
        print("mensaje extra:",str(outroMensaxe) * veces)

repetir_mensaxes("Ola",2,"Caracola",5,"Probar a hacer un bucle que mande un chingo de parametros") # Realmente el parametro indefinido es simplemente que puedes pasar una tupla
repetir_mensaxes(5) # si no le pasas la tupla entonces estara vacia, lo que suele significar que no deberia estallar en casos normales

