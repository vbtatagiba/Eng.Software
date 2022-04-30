"""
3.Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
"""
nome = input(str("Digite o seu nome: "))
while len(nome) <= 3:
  nome= input('Digite um nome com mais de 3 caracteres. ')

idade=int(input('Digite sua Idade: '))

while idade>150 or idade<0:
    idade=int(input('digite uma idade compreendida entre 0 e 150 para que seja valida: '))

salario=float (input('Digite o seu salário: '))
while salario<=0:
    salario=float(input('Por favor insira um salario maior que zero: '))

sexo=input(str('Digite o seu Sexo m para Masculino e f para Feminino: '))

while sexo != "f" and sexo != 'm':
    sexo=input(str('Por favor digite m para Masculino e f para Feminino '))
if sexo == 'f':
    print('Feminino')
elif sexo == 'm':
    print ("Masculino")

estado=input(str('Digite seu Estado Civil sendo s para solteiro(a) c para casado(a) v para viuvo(a) d para divorciado(a): '))

while estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
    estado=input(str('Por favor insira um Estado Civil valido sendo s para solteiro(a) c para casado(a) v para viuvo(a) d para divorciado(a)'))

if estado== 's':
    print ('Solteiro(a)')
elif estado == 'c':
    print ('Casado(a)')
elif estado == 'v':
    print ('Viuvo(a)')
elif estado == 'd':
    print ('Divorciado(a)')