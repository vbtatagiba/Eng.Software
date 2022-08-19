#numeros de 5 a 100 que são divisiveis por 7 mas não são multiplos de 5

for i in range (5, 100):
    if i%7 == 0 and i% 5!=0:
        print(i)