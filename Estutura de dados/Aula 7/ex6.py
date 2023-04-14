from fila import Fila
from random import randint

fila= Fila()

for i in range(10):
    num = randint(1, 99)
    fila.enqueue(num)


fila.exibir()

fila.remover_menor_valor()


fila.exibir()