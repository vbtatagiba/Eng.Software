'''Escreva uma função que calcule o tempo necessário para cozinhar um ovo, sabendo que o tempo de cozimento para um ovo de tamanho médio é de 3 minutos e que cada ovo adicionado aumenta o tempo em 1 minuto.'''
ovotempo=3
ovos=1
addovo=int(input('Quantos ovos você deseja adicionar:'))
if addovo>0:
    ovotempo+= addovo
    ovos+= addovo

print(f'O Tempo Cozimento será de : {ovotempo} minutos')
print(f'O Total de ovos é: {ovos} ')