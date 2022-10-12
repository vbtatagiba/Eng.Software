


numeros=(input('digite uma lista com numeros inteiros'))
lista=numeros.split()# transforma em listas

print('Voce digitou os seguintes numeros: ')
print(lista)
def rep (lista):
    l1=[]
    for numero in lista:
        if (numero in l1):
            pass
        else:
            l1.append(numero)
    return l1
lista=sorted(rep(lista))
print(lista)