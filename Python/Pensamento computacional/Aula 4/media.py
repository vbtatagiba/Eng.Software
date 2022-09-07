n1=int(input('Digite a primeiro nota:'))
n2=int(input('Digite a segundo nota:'))
n3=int(input('Digite a terceiro nota:'))
n4=int(input('Digite a Quarta nota'))
media=(n1+n2+n3+n4)/4
if media<=4:
    print ("O Aluno está reprovado")
elif media >= 5 and media <=6:
    print ("O Aluno está de recuperação")
else:
    print ('O aluno está Aprovado')