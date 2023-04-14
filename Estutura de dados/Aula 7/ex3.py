from fila import Fila
from random import randint

fila= Fila()

for i in range(10):
    num = randint(1, 99)
    fila.enqueue(num)


print("Fila:")
fila.exibir()

elemento = fila.elemento_na_posicao(3)

if elemento is not None:
    print("Elemento na posição 4:", elemento)
else:
    print("A posição 4 não existe na fila")