'Faça um progama que realize a media de uma nota'

notas=[]
while True:
    nota=float(input('Insira as notas:'))
    print(notas)
    if nota== 11.0:
        notas.remove(11.0)
        break
    else: 
        notas.append(nota)
media=sum(notas)/len(notas)
print ('A media foi de :', media)
print ('As notas digitadas foram:',notas)