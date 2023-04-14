from fila import Fila

fila_atendimento = Fila()

# Adiciona clientes à fila de atendimento
fila_atendimento.enqueue('Marcio')
fila_atendimento.enqueue('Alexandre')
fila_atendimento.enqueue('Dias')
fila_atendimento.enqueue('Garrido')

# Atende os clientes em ordem
while not fila_atendimento.is_empty():
    cliente_atual = fila_atendimento.dequeue()
    print(f"Atendendo o cliente {cliente_atual}")

print('-='*30)
fila_impressao = Fila()

# Adiciona arquivos à fila
fila_impressao.enqueue('turmaA.txt')
fila_impressao.enqueue('turmaB.txt')
fila_impressao.enqueue('turmaAdap.txt')

# Imprime os arquivos em ordem
while not fila_impressao.is_empty():
    arquivo_atual = fila_impressao.dequeue()
    print(f"Impressão do arquivo {arquivo_atual}")
