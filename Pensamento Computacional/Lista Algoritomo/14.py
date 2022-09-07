'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou VVespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.'''
turno=str(input("Digite seu turno sendo:M-matutino ou V Vespertino ou N- Noturno"))

if turno=="M" or turno=='m':
    print('Bom dia!')
if turno=="V" or turno=='v':
    print('Bom tarde!')
if turno=="N" or turno=="n":
    print('Boa noite!')
else:
    print('digite APENAS M-matutino ou V Vespertino ou N- Noturno')