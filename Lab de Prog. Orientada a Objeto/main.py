#Aluno: Victor Bernardo Gomes de Tatagiba
#Matricula:202211960
#P2
from banco import Banco
from cliente import Cliente
from pessoa import Pessoa

'Nomeando o banco'
N_banco = input('Qual Nome do Banco ? ')
print('-='*35)
banco=Banco(N_banco)
'Cadrastrando os cliente'
print('------Cliente 1---')
nome=input('Qual o Seu nome? ')
idade=input('Qual o Sua idade? ')
sexo=input('Qual o Seu Sexo? ')
Pessoa1= (Pessoa('Victor','19 Anos','Masculino'))
Pessoa1.dados(nome,idade,sexo)
print('------Cliente 2---')
Pessoa1= (Pessoa('Victoria','19 Anos','Feminino'))
nome2=input('Qual o Seu nome? ')
idade2=input('Qual o Sua idade? ')
sexo2=input('Qual o Seu Sexo? ')
print('-='*35)

'Criando os Clientes'
cliente1=Cliente(nome,banco,idade,sexo)
print('-='*35)
cliente2 = Cliente(nome2,banco,idade2,sexo2)

'Listando os cliente'
banco.adicionar_cliente(cliente1)
print('-='*35)
banco.adicionar_cliente(cliente2)
print('-='*35)

'Listando eles'
print('-='*35)
banco.listar_clientes()
print('-='*35)


#  operações nas contas dos clientes
def deposito():
    cliente=str(input('Insira seu ID: '))
    valor=float(input('Qual Valor deseja Depositar: '))
    if cliente == '1':
        cliente1.conta.deposito(valor)
    elif cliente == '2':
        cliente2.conta.deposito(valor)

def saque():
    cliente=str(input('Insira seu ID: '))
    valor=float(input('Qual Valor deseja Sacar: '))
    if cliente == '1':
        cliente1.conta.saque(valor)
    elif cliente == '2':
        cliente2.conta.saque(valor)

def transfere ():
    cliente=str(input('Insira seu ID: '))
    valor=float(input('Qual Valor deseja trabsferir: '))
    if cliente == '1':
        cliente1.conta.transfere_para(cliente2.conta, valor)
    elif cliente == '2':
        cliente2.conta.transfere_para(cliente1.conta, valor)

def info():
    cliente=str(input('Insira seu ID: '))
    if cliente == '1':
        cliente1.exibir_cliente()
    elif cliente == '2':
        cliente2.exibir_cliente()

def extrato():
    cliente=str(input('Insira seu ID: '))
    if cliente == '1':   
        cliente1.conta.extrato()
    elif cliente == '2':
        cliente2.conta.extrato()

def menu():
    while True:
        opc=input(f'''Seja Bem Vindo ao sistema Bancario do {N_banco}\n
            Para Acessar o Sistema de Deposito Digite 1 
            Para Acessar o Sistema de Saque Digite 2
            Para Acessar o Sistema de Tranferencia Digite 3
            Para Acessar o Sistema de Informação Digite 4
            Para Acessar o Sistema de Extrato Digite 5
            Para Encerrar Digite 6 : ''')
        if opc == '1':
            deposito()
            print('-='*35)
        elif opc == '2':
            saque()
            print('-='*35)
        elif opc == '3':
            transfere()
            print('-='*35)
        elif opc == '4':
            info()
            print('-='*35)
        elif opc == '5':
            extrato()
            print('-='*35)
        elif opc == '6':
            break
        else:
            print('Opção Invalida')
            print('-='*35)
menu()
        