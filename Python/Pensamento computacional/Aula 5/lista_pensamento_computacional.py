#Aluno Victor Bernardo
"""1.	Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""

nota=float(input('Insire uma nota de 0 a 10: '))
while(nota<=0 or nota>10):
    nota=float(input('Valor invalido tente novamente: '))
else:
    print ('O sistema agradece!')


'''2.	Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

user1=input('Digite um nome: ')
senha1=input('Insira sua senha: ')

while senha1==user1:
    print('ERRO! Escolha um senha diferente do seu nome: ')
    user1= input('digite um nome: ')
    senha1=float(input('Digite sua senha: '))
else:
    print('Acesso Autorizado! ')

'''3.	Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
'''
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

""" 4.	Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""
a = 80000
b = 200000
ano = 0

while a <= b:
	a += a * 0.03
	b += b * 0.015
	ano += 1

print ( "A ultrapassa ou iguala a B em %d anos" %ano )

"""5.	Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação"""
a =int(input('Insira sua população1: '))
b =int (input('Insira sua população2: '))
cres1=float(input('Insira seu crescimento1: '))
cres2=float(input('Insira seu crescimento2: '))
ano = 0

while a <= b:
	a += a * cres1
	b += b * cres2
	ano += 1

print ( "A ultrapassa ou iguala a B em %d anos" %ano )

"""6-Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro."""
for i in range (21):
	print (i)
print(list(range(1,21)))

""" 7.	A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo."""
n=int(input('Digite o a posição do termo: '))
enésimotermo = 1
penultimo = 1
contador = 1
print(enésimotermo = 1)
print(penultimo)
while contador <= n:
        termo = enésimotermo + penultimo
        penultimo = enésimotermo
        enésimotermo = termo
        contador += 1
        print(termo)

"""8.	Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

n1=int(input('Digite um numero inteiro: '))

cont = 0

divisor = []

for i in range(n1):

    if n1%(i+1) == 0:

        cont += 1
        divisor.append(i+1)

    else:

        cont
        

if cont == 2:

    print ("O numero é primo divisivel por ",divisor)

else:

    print ("O numero não é primo pois é divisivel por ",divisor)


#DATA TERMINADA 30/04/2022 AS 3H30 DA MANHÃ 