l1=[]
l2=[]
for i in range(10):
    n10=int(input('digite 10 numeros: '))
    l1.append(n10)

for b in range(5):
    n5=int(input('digite 05 numeros: '))
    l2.append(n5)

for c in l1:
    for i,v in enumerate(l2):
        if c%v==0:
            print(f'{c} é divisivel por {v} na posição {i}')