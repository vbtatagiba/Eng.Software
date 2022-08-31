'''3. Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''
n1=int(input('Digite a nota 1:'))
n2=int(input('Digite a nota 2:'))
n3=int(input('Digite a nota 3:'))
n4=int(input('Digite a nota 4:'))
media=(n1+n2+n3+n4)/4
if media<=4:
    print ("O Aluno está reprovado é sua média foi:",media)
elif media >= 5 and media <=6:
    print ("O Aluno está de recuperação é sua média foi:",media)
else:
    print ('O aluno está Aprovado é sua média foi:',media)