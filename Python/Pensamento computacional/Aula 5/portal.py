user1=input('Digite um nome: ')
senha1=input('Insira sua senha: ')

while senha1==user1:
    print('ERRO! Escolha um senha diferente do seu nome: ')
    user1= input('digite um nome: ')
    senha1=float(input('Digite sua senha: '))
else:
    print('Acesso Autorizado! ')
