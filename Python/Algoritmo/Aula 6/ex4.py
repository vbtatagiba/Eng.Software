'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com
os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
• Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
• 1 0
• 3 10
• 6 15
• 9 20
• 12 25
• Exemplo de saída do programa:
Valor da Dívida - Valor dos Juros - Quantidade de Parcelas - Valor da Parcela
• R$ 1.000,00 - 0 - 1 - R$ 1.000,00
• R$ 1.100,00 - 100 - 3 - R$ 366,00
• R$ 1.150,00 - 150 - 6 - R$ 191,67'''
divida=float(input('Insira o Valor da Divida: '))
parcelas=float(input('Insira quantas Parcelas: '))
parcelas2=divida/parcelas
juros=0
if parcelas==1:
    juros=0
elif parcelas==3:
    juros=0.1
elif parcelas==6 :
    juros=0.15
elif parcelas==9 :
    juros=0.2
elif parcelas==12:
    juros=0.25
vjuros=divida*juros
vparcela=parcelas2*juros
print('Valor da Dívida - Valor dos Juros - Quantidade de Parcelas - Valor da Parcela')
print('R$',divida,'-',vjuros,'-',parcelas,'-','R$',parcelas2 )
