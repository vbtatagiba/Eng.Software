from stack import Stack

MinhaPilha = Stack()

MinhaPilha.push("Universidade de Vassouras - Campus Vassouras")
MinhaPilha.push("Universidade de Vassouras - Campus Maricá")
MinhaPilha.push("Universidade de Vassouras - Campus Saquarema")

print(MinhaPilha.items)

print(MinhaPilha.peek())

MinhaPilha.pop()

print(MinhaPilha.items)