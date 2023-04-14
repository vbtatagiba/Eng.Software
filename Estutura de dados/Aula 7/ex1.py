from fila import Fila

fila_atendimento = Fila()

# Adiciona clientes à fila de atendimento
fila_atendimento.enqueue('1')
fila_atendimento.enqueue('2')
fila_atendimento.enqueue('3')
fila_atendimento.enqueue('4')
fila_atendimento.enqueue('5')

# Atende os clientes em ordem
for i in range(2):
    cliente_atual = fila_atendimento.dequeue()
    print(f"Atendendo o cliente {cliente_atual}")
