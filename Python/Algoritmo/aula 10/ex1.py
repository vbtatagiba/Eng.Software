'Faça um progama que realize a media de uma nota'

notas=[]
for i in range(4):
    nota=float(input('Insira as notas: '))
    notas.append(nota)
media=sum(notas)/len(notas)
print ('A media foi de :', media)
print ('As notas digitadas foram:',notas)