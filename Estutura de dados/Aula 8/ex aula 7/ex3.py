# Escreva uma função que calcule o número de passos necessários para se chegar ao topo de uma montanha com n metros de altura, sabendo que cada passo dado aumenta a altitude em 10 centímetros e que um passo corresponde a 1 metro.
tamanhopasso=1 #Metros
tamanhomontanha=float(input('Insira o tamanho (em metros) da montanha que você ira escalar:'))
totalpassos=tamanhomontanha/tamanhopasso

print(f'O total de passos será de : {totalpassos} passos')