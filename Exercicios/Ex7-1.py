t1 = 2,10,9,58
def isOrderAsc(tupla):
    maximo = tupla[0]
    for num in tupla:
        if maximo>num:
            return False
        maximo=num
    return True

print(isOrderAsc(t1))