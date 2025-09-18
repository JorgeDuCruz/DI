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

def persoa (nome,dni,**maisDatos):
    print(nome,dni)
    for dato in maisDatos.keys():
        print(dato,"é",maisDatos[dato])

persoa("Alfred","5438464G",fecha_nacimiento="15/4/1990",localidade="Vigo",estado="Civil") # Para mandar los valores del diccionario tratalos como si fueran parameros donde debes especificar su nombre


def cambiarLista(lista):
    l = ["Jose"] # este l que se crea aqui es un l distinto del que hay fuera de la funcion y por ende no modifica a la lista original l
    print(l)
    lista[0] = l # Aqui la variable lista es equivalente a la variable l de fuera de la funcion y por ende si modifica a la lista original l

l = ["pepe"]
print(l)
cambiarLista(l)
print(l)

#Funcion con return
def suma(listaSumar): # Es literal Java pero sin especificar que valor vas a devolver
    suma = 0
    for numero in listaSumar:
        suma += numero
    return suma

print(suma([5,48,2.5]))

def sumaMedia(listaSumar):
    suma = 0
    for numero in listaSumar:
        suma += numero
    return suma, suma/len(listaSumar) #retorna los dos valores, se envia como tupla o como dos valores distinto

a,s = sumaMedia([10,5,7.5]) # cada variable recibe uno de los resultado que retonra la funcion
_,m = sumaMedia([1,2,3]) # ignora el valor en la posicion del _ y solo aigna los valores que coincidan con una variable
tupla = sumaMedia([5,2.5,7.5]) # la variable se convierte en una tupla con los dos valores que retonra la funcion
print(tupla)
print(a,s)
