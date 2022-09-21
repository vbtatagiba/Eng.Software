# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
# lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da
# média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro,
# . . . ).

import statistics

cont = 0
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
temp = []
media = 0

while True:
    mes = float(input('Digite a temperaura média do mês:'))
    temp.append(mes)
    cont +=1
    if cont==12:
        break   

media = sum(temp)/12

for i in range(len(meses)):
    if temp[i] > media:
        print(f'O mês {meses[i]} com temperatura de {temp[i]}, ficou acima da média anual')

    






