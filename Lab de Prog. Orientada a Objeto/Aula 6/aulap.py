contas = {'Nome': 'Victor', 'Numero': 124-5, 'saldo': 120.0, 'limite': 500.0}

def cria_cadastro():
    titular = input('Insira o Nome do Titular da conta: ')
    numero = input('Insira o Numero da conta: ')
    saldo = float(input('Insira o saldo da conta: '))
    limite = float(input('Insira o limite da conta: '))
    
    conta = {'Nome': titular, 'Numero': numero, 'saldo': saldo, 'limite': limite}
    contas[numero] = conta
    
contas['124-5'] = {'Nome': 'Victor', 'Numero': '124-5', 'saldo': 120.0, 'limite': 500.0}

def altera():
    global contas
    print('''Seja Bem Vindo ao sistema de Alteração de dados bancarios
Caso precise mudar o NOME da conta Insira "Nome"
Caso precise mudar o NUMERO da conta Insira "Numero".
Caso precise mudar o SALDO da conta Insira "saldo" .
caso precise mudar o limite da conta Insira "limite".''')
    oq=input(f'O que deseja alterar ?')
    if oq in contas:
        print('OK localizei o item que deseja mudar.')
        new=input('Qual será o novo valor? ')
        contas.update({oq: new})
    else:
        print('Não foi possivel encontrar no nosso banco de dados esse item tente novamente mais tarde. ')

def imprime_extrato():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        conta = contas
        print('-='*30)
        print(f"Extrato da conta {conta['Numero']}:")
        print(f"Titular: {conta['Nome']}")
        print(f"Saldo: R${conta['saldo']:.2f}")
        print(f"Limite: R${conta['limite']:.2f}")
        print('-='*30)
    else:
        print("Conta não encontrada.")
    
def deposito():
    global contas
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input('O quanto deseja Depositar: '))
        contas[numero_conta]['saldo'] += valor
        conta = contas
        print('-='*30)
        print(f"Extrato da conta {conta['Numero']}:")
        print(f"Titular: {conta['Nome']}")
        print(f"Saldo: R${conta['saldo']:.2f}")
        print(f"Limite: R${conta['limite']:.2f}")
        print('-='*30)
    else:
        print("Conta não encontrada.")

def saca():
    global contas
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input('O quanto deseja sacar: '))
        if valor <= contas[numero_conta]['saldo']:
            contas[numero_conta]['saldo'] -= valor
            conta = contas
            print('-='*30)
            print(f"Extrato da conta {conta['Numero']}:")
            print(f"Titular: {conta['Nome']}")
            print(f"Saldo: R${conta['saldo']:.2f}")
            print(f"Limite: R${conta['limite']:.2f}")
            print('-='*30)
        else:
            print('Saldo insuficiente')
    else:
        print("Conta não encontrada.")


def menu():
    while True:
        opc = input('''O que deseja Qual opção deseja realizar:
1- Mostrar os dados da conta
2- Criar um novo cadastro
3- Depositar
4- Sacar
5- Imprimir extrato
6- Alterar Dados
7- Sair\n''')
        if opc == "1":
            print('-='*30)
            print(contas)
            print('-='*30)
        elif opc == "2":
            cria_cadastro()
        elif opc == "3":
            deposito()
        elif opc == "4":
            saca()
        elif opc == "5":
            imprime_extrato()
        elif opc == "6":
            altera()
        elif opc == "7":
            print('-='*30)
            print('PROGRAMA FINALIZADO')
            print('-='*30)
            break
        else:
            print('Opção inválida')

menu()