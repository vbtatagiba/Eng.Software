import random
import datetime

class CaixaEletronico:
    
    def __init__(self):
        self.saldo = self._gerar_saldo()
        
    def _gerar_saldo(self):
        return random.randint(0, 1000)
    
    def _verificar_cartao(self, matricula):
        # Validar o cartão pela matrícula do aluno e pela data do dia
        data_hoje = datetime.datetime.now().strftime('%d%m%Y')
        senha = matricula[:4][::-1] + data_hoje
        return senha
    
    def _verificar_saldo(self, valor):
        # Verificar se há saldo suficiente para realizar a operação
        if self.saldo >= valor:
            return True
        else:
            return False
    
    def _atualizar_saldo(self, valor):
        # Atualizar o saldo da conta do usuário
        self.saldo -= valor
    
    def cadastrar(self):
        matricula = input("Digite sua matrícula: ")
        senha = self._verificar_cartao(matricula)
        print("Seu cartão foi validado com sucesso!")
        return matricula, senha
    
    def sacar(self):
        valor = float(input("Digite o valor a ser sacado: R$"))
        if self._verificar_saldo(valor):
            self._atualizar_saldo(valor)
            print("Saque realizado com sucesso!")
            print("Novo saldo: R${:.2f}".format(self.saldo))
            return True
        else:
            print("Saldo insuficiente!")
            return False

