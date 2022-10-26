count=1
count2=1

lista1 = []
lista2 = []
while count <= 10:
    num1=int(input('Insira o Primeiro numero: '))
    count=count + 1
    lista1.append(num1)
while count2<=5:
    num2=int(input('Insira o Segundo numero: '))
    count2 = count2 + 1
    lista2.append(num2)


calc= num1/num2
if calc == 0:
    print('É Divisivel')
else:
   print('não é divisivel')

# cont = 0
# lista1 = []
# lista2 = []
# while True:
#     n1 = int(input('Digite 10 números:'))
#     lista1.append(n1)
#     cont+=1
#     if cont == 10:
#         break

# for i in range(1,6):
#     n2 = int(input('Agora digite 5 números: '))
#     lista2.append(n2)

# for n in lista1:
#     print(len(lista1[2]))

    

# print(f'A primeira lista é {lista1} e a segunda lista é {lista2}.')
