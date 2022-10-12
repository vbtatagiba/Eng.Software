lista=[]
while True:
    nota=input('Digite uma nota')

    if nota == '11':
        break
    else:
        lista.append(nota)

media=sum(lista)/ len(lista)
if media>=6:
    print('O aluno esta aprovado')
elif media<6:
    print('O Aluno esta reprovado')