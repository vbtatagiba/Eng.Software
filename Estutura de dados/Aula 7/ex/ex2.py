from random import randint
from fila import Fila

fila_atendimento = Fila()
fila_atendimento.exibir()

for i in range(10):
    num = randint(1, 99)
    fila_atendimento.enqueue(num)


fila_atendimento.exibir()

fila_atendimento.rem_par()


fila_atendimento.exibir()
