def tempoASegundos (hora,min,seg):
    segH = hora*3600
    segMin= min*60
    seg += segH+segMin

    return seg

print(tempoASegundos(6,61,59))

def segundosAtempo(segundos):
    segundosRes = segundos%3600
    hora = segundos//3600

    minutos = segundosRes//60
    segundosRes = segundosRes%60

    return hora,minutos,segundosRes

print(segundosAtempo(25319))