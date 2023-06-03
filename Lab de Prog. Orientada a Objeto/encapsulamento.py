'''Encapsulamento é um princípio da programação orientada a objetos que consiste em esconder os detalhes internos de implementação de uma classe, fornecendo uma interface pública para interagir com o objeto. O encapsulamento permite que o estado interno de um objeto seja protegido de acesso e modificação não autorizados.'''
from contabancaria import ContaBancaria

# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.__titular = titular
#         self.__saldo = saldo

#     def depositar(self, valor):
#         self.__saldo += valor

#     def sacar(self, valor):
#         if self.__saldo >= valor:
#             self.__saldo -= valor
#         else:
#             print("Saldo insuficiente.")

#     def obter_saldo(self):
#         return self.__saldo


conta = ContaBancaria("João", 1000)

conta.depositar(500)
conta.sacar(200)

print(conta.obter_saldo())

'''Neste exemplo, a classe ContaBancaria encapsula os atributos titular e saldo usando o prefixo de dois underscores (__) antes de seus nomes. Essa convenção indica que esses atributos são privados e não devem ser acessados diretamente de fora da classe.

Em vez disso, a classe fornece métodos públicos como depositar(), sacar() e obter_saldo() para interagir com os atributos encapsulados. Isso garante que o saldo só possa ser acessado e modificado através desses métodos, permitindo que a classe mantenha o controle sobre as operações realizadas nos dados internos.

No exemplo, o encapsulamento protege o saldo da conta bancária de acesso direto e manipulação indevida, garantindo que as operações de depósito e saque sejam executadas corretamente e que o saldo só possa ser obtido através do método apropriado.'''