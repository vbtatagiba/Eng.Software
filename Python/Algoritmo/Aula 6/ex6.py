'''#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um
programa capaz de gerar a série até o n−ésimo termo'''
posi=int(input('Insira a posição do termo desejado: '))
ntermo=1
penultimo=1
contador=1
print(ntermo)
print(penultimo)
while contador<=posi:
    termo=ntermo+penultimo
    penultimo=ntermo
    ntermo=termo
    contador+=1
    print(termo)
print('Essa é a série de Fibonacci do n−ésimo termo !')