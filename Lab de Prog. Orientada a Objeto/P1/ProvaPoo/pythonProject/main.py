from conta import Conta

if __name__ == '__main__':
    conta1 = Conta('Lucas Cerqueira', '1234', 2000, 3000)
    conta2 = Conta('Fabrício Dias', '4321', 3000, 3500)

    conta1.extrato()
    conta2.extrato()
    conta1.transfere(conta2, 200)
    conta1.extrato()
    conta2.extrato()
    conta1.saca(1200)
    conta1.extrato()
    conta2.deposita(1000)
    conta2.extrato()