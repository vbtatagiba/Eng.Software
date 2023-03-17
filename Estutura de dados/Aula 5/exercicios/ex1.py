from stack import Stack
import random
MinhaPilha = Stack()
 

rem=MinhaPilha.pop
add=MinhaPilha.push
topo=MinhaPilha.peek

for i in range(10):
    add(random.randint(0,99))

print(MinhaPilha.items)

print(topo())

rem()

print('Os Itens da pilha são',MinhaPilha.items)

MinhaPilha.inverse()
print(MinhaPilha.items)
MinhaPilha.rem_menor()
MinhaPilha.rem_maior()
print(MinhaPilha.items)
MinhaPilha.sort
print(MinhaPilha.items)