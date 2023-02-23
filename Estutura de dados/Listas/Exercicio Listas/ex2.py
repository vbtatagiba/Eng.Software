import random

num=[]
num2=[]

lista=num+num2

for n in range(0,5):
    n=random.randrange(0,99)
    num.append(n)

for n in range(0,5):
    n=random.randrange(0,99)
    num2.append(n)

lista=num+num2
print(sorted(lista))
