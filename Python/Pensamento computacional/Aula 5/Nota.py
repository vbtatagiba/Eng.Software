#nota
nota=float(input('Insire uma nota de 0 a 10: '))
while(nota<=0 or nota>10):
    nota=float(input('Valor invalido tente novamente: '))
else:
    print ('O sistema agradece!')