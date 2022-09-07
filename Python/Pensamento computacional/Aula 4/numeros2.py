n1 = int(input('\nDigite o PRIMEIRO NÚMERO: '))
n2 = int(input('Digite o SEGUNDO NÚMERO: '))
n3 = int(input('Digite o TERCEIRO NÚMERO: '))
if n1<n2 and n2<n3:
    print('A ordem crescente é',n1,n2,n3)
elif n1<n3 and n3<n2:
    print('A ordem crescente é',n1,n3,n2)
elif n2<n1 and n1<n3:
    print,('A ordem crescente é',n2,n1,n3)
elif n2<n3 and n3<n1:
    print('A ordem crescente é',n2,n3,n1)
elif n3<n1 and n1<n2:
    print ('A ordem crescente é',n3,n1,n2)
elif n3<n2 and n2<n1:
    print ('A ordem crescente é',n3,n2,n1)
elif n1==n2 and n2<n3:
    print ('A ordem crescente é',n1,'e',n3)
elif n1==n2 and n2>n3:
    print ('A ordem crescente é',n3,'e',n1)
elif n1==n3 and n3<n2:
    print ('A ordem crescente é',n1,'e',n2)
elif n1==n3 and n3>n2:
    print ('A ordem crescente é',n2,'e',n1)
elif n2==n1 and n1<n3:
    print ('A ordem crescente é',n2,'e',n3)
elif n2==n1 and n1>n3:
    print ('A ordem crescente é',n3,'e',n2)
elif n2==n3 and n3<n1:
    print ('A ordem crescente é',n3,'e',n1)
elif n2==n3 and n3>n1:
    print ('A ordem crescente é',n1,'e',n3)
elif n3==n1 and n1<n2:
    print ('A ordem crescente é',n3,'e',n2)
elif n3==n1 and n1>n2:
    print ('A ordem crescente é',n2,'e',n3)
else:
    print("O numero são iguais")
