import numpy
print('Criando uma matriz a partir da lista :')
l=[[3,4,5], [6,7,8], [9,0,1]]
z=numpy.matrix(l)
print("Matriz")
print(z)
print('transporta a matriz')
print(z.T)
