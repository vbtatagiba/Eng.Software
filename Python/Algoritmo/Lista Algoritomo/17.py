'''17. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';'''
nome = input(str("Digite o seu nome: "))
while len(nome) <= 3:
  nome= input('Digite um nome com mais de 3 caracteres. ')
if len(nome)>3:
    print("Nome OK!")
idade=int(input('Digite sua Idade: '))

while idade>150 or idade<0:
    idade=int(input('digite uma idade compreendida entre 0 e 150 para que seja valida: '))
if idade>0:
    print('Idade OK!')

salario=float (input('Digite o seu salário: '))
while salario<=0:
    salario=float(input('Por favor insira um salario maior que zero: '))

if salario>0:
    print('Salário OK!')
sexo=input(str('Digite o seu Sexo m para Masculino e f para Feminino: '))

while sexo != "f" and sexo != 'm':
    sexo=input(str('Por favor digite m para Masculino e f para Feminino '))
if sexo== "f" or sexo=="m":
    print('Sexo OK!')

estado=str(input('Digite seu Estado Civil sendo s para solteiro(a) c para casado(a) v para viuvo(a) d para divorciado(a): '))
if estado== 's' or estado != 'c' or estado != 'v' or estado != 'd':
    print('Estado Civil OK! ')
while estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
    estado=str(input('Por favor insira um Estado Civil valido sendo s para solteiro(a) c para casado(a) v para viuvo(a) d para divorciado(a)'))
