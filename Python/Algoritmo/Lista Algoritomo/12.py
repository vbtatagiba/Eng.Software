"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
comprar, sabendo que a decisão é sempre pelo mais barato."""

produto = []

p1 = float(input("Digite o valor do primeiro produto: "))
p2 = float(input("Digite o valor do segundo produto: "))
p3 = float(input("Digite o valor do terceiro produto: "))

produto.append(p1)
produto.append(p2)
produto.append(p3)

produto.sort(reverse=True)
print(produto)
print ('Produto mais barato é: ',produto[2])