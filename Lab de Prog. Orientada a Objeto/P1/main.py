from conta import Conta
#numero da conta, nome do titular,saldo, limite
conta1=Conta('1','Victor Bernardo',100.0,50.0)
conta2=Conta('2','Gabriel',500.0,150.0)


def menu():
    opc=input('Seja Bem Vindo ao Banco V1 se deseja sacar Digite 1 se deseja ver o extrato digite 2 se deseja tranferir digite 3 se deseja depositar digite 4 e digite 5 para sair: ')
    print('-='*30)
    if opc =="1":
        nconta=(input('Qual a conta que você deseja sacar?: '))
        valor=float(input('Insira o Valor que deseja sacar:'))
        if nconta== '1':
            conta1.saca(valor)
        elif nconta=='2':
            conta2.saca(valor)
        menu()
    elif opc=='2':
        nconta=(input('Qual a conta que você deseja ver o extrato?: '))
        if nconta== '1':
            conta1.extrato('1')
        elif nconta=='2':
            conta2.extrato('2')
        menu()
    elif opc=='3':
        nconta=(input('Qual a sua conta: '))
        valor=float(input('Insira o Valor que deseja Transferir:'))
        if nconta== '1':
            conta1.tranferencia(conta1.saldo,valor)
        elif nconta=='2':
            conta2.tranferencia(conta2.saldo,valor)
        menu()
    elif opc=='4':
        nconta=(input('Qual a conta que você deseja depositar?: '))
        valor=float(input('Insira o Valor que deseja depositar:'))
        if nconta== '1':
            conta1.depositar(valor)
        elif nconta=='2':
            conta2.depositar(valor)
        menu()
    elif opc=='5':
        print('Programa encerrado')
menu()