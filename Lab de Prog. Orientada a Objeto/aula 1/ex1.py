n1=int(input("Insira a nota 1: "))
n2=int(input("Insira a nota 2: "))
n3=int(input("Insira a nota 3: "))
n4=int(input("Insira a nota 4: "))
soma=n1+n2+n3+n4
print(soma)
media=soma/4
print(media)
if media >= 7:
    print("Aprovado")
if media <4:
    print("Reprovado")
if media <7 and media >=4 :
    print('Exame Final')