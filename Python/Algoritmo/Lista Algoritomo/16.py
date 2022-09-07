'''16. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que
deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
1. Desconto do IR:
2. Salário Bruto até 900 (inclusive) - isento
3. Salário Bruto até 1500 (inclusive) - desconto de 5%
4. Salário Bruto até 2500 (inclusive) - desconto de 10%
5. Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de
hora é 220'''
vhora=float(input('Insira o valor da hora: '))
horas=float(input('Insira quantas horas: '))
bruto=horas*vhora
sind=0.03
fgts=bruto*0.11
inss=0.10
print('Seu FGTS é: ', fgts )
print('O salário Bruto é: ', bruto)
percentual=0
if (bruto<=900):
    percentual=0
elif (bruto<=1500):
    percentual=5
elif (bruto<=2500):
    percentual=10
elif (bruto>=2500):
    percentual=20
percentual=percentual/100.0
print("porcentual", percentual)
descontos=inss+percentual
tdesconto=bruto*descontos
print('O total de desconto é: $',tdesconto)
salarioliquido=bruto-tdesconto
print('Seu Salário Liquido é: ',salarioliquido)