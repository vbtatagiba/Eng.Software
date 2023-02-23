lista = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,15,16]

n = int(input("Insira um número: "))

if n in lista:
    print('-='*30)
    print(f"O número {n} está na lista!")
    print('-='*30)
else:
    print('-='*30)
    print(f"O número {n} não está na lista.")
    print('-='*30)