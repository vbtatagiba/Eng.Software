from stack import Stack

MinhaPilha = Stack()
 
itens=MinhaPilha.items
rem=MinhaPilha.pop
add=MinhaPilha.push
topo=MinhaPilha.peek

add("Universidade de Vassouras - Campus Vassouras")
add("Universidade de Vassouras - Campus Maricá")
add("Universidade de Vassouras - Campus Saquarema")

print(itens)

print(topo())

rem()

print('Os Itens da pilha são',itens)

MinhaPilha.hello()
