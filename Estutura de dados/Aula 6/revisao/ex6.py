# Escreva um programa que remova os elementos duplicados de uma lista, mantendo a ordem original dos elementos.
lista=[1,2,3,4,5,1,3,2,1,3,5,6,9,]


dup = {x for x in lista if lista.count(x) >0}
print(dup)