t1 = 2,10,58
def isOrderAsc(tupla):
    maximo = tupla[0]
    for num in tupla:
        if maximo>num:
            return False
    return True

print(isOrderAsc(t1))