'''9. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a
média alcançada por aluno e apresentar:
1. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
2. A mensagem "Reprovado", se a média for menor do que sete;
3. A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
nota1=int(input('Digite a nota 1:'))
nota2=int(input('Digite a nota 2:'))
media=(nota1+nota2)/2
if media<=7:
    print ("O Aluno está reprovado é sua média foi:",media)
elif media>= 7:
   print ("O Aluno está Aprovado é sua média foi:",media)
elif media == 10:
    print ('O aluno está Aprovado com Distinção é sua média foi:',media)