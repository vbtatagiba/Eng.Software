'''1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
2. Faça um programa que leia um nome de usuário e a sua senha e não
aceite a senha igual ao nome do usuário, mostrando uma mensagem de
erro e voltando a pedir as informações.
3. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
8. Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números impares.
9. Faça um programa que calcule o fatorial de um número inteiro fornecido
pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
#1)


while True:
    n1=float(input('Digite uma nota de 0 a 10: '))
    try:
        float(n1)
        if float(n1)>0 and float(n1)<=10 :
            break
    except:
        print('Digite apenas numeros')
#2)
while True:
    user=input('Insira o Usuário:')
    senha=input('Insira a Senha:')
    if user==senha:
        print("ERRO!")
    else:
        break
#3)

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

#8)
pares=0
impar=0
for i in range (10):
    if int(input("Insira um numero: "))%2==0:
        pares+=1
    else:
        impar+=1

print('Numeros pares: ',pares,'Numesros impares:',impar)
#9)
fatorial = int(input("Insira o Fatorial que deseja calcular: ") )
resultado=1
count=1
while count <= fatorial:
    resultado *= count
    count += 1
print('O resultado desse Fatorial é: ',resultado)