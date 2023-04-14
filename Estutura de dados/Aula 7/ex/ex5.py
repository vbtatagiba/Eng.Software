from fila import Fila
from random import randint

fila= Fila()

for i in range(10):
    num = randint(1, 99)
    fila.enqueue(num)

fila.exibir()


maiorvalor=fila.remover_maior_valor()
print('O maior valor da lista é:',maiorvalor)

fila.exibir()