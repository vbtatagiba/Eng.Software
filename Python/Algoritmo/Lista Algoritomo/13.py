n1 = int(input('Insira o Primeiro numero: '))
n2  = int(input('Insira o Segundo numero : '))
n3 = int(input('Insira o Terceiro numero: '))

print(n1,'-',n2,'-',n3)

if(n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux

if(n2 > n1):
    aux = n2
    n2 = n1
    n1 = aux

if(n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux
print(n1,'-',n2,'-',n3)