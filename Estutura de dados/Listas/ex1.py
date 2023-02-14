import random
num=[]

for n in range(0,10):
    n=random.randrange(0,999)
    num.append(n)
print('-='*30)
print('O maior Numero da lista é', max(num))
print('O menor Numero da lista é', min(num))
print('-='*30)
