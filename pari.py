
salario = float(input('Digite seu salário para calcular o reajuste: '))
reajusteum = float(salario + salario*15/100)
reajustedois = float(salario + salario*10/100)
reajustetres = float(salario + salario*5/100)

if salario < 500:
    print('De acordo com os cálculos de reajuste, seu salário ficou: ',reajusteum)

if 500 <= salario and salario <= 1000:
    print('De acordo com os cálculos de reajuste, seu salário ficou: ',reajustedois)

if salario > 1000:
    print('De acordo com os cálculos de reajuste, seu salário ficou: ',reajustetres)