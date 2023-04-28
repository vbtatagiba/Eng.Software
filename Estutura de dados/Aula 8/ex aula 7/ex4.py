# Escreva uma função que calcule o número de dias necessários para percorrer uma distância de d quilômetros, sabendo que cada dia o viajante percorre p quilômetros e que ele precisa descansar a cada x dias percorridos.
qkm=float(input('Quantos Quilometros vc irá pecorrer? '))
maxkm=float(input('Quantos Quilometros vc caminha em 1 dia?'))
maxtemp=int(input('De quanto em quantos dias você precisa descansar?'))
dias=0
distancia_percorrida=0

while distancia_percorrida < qkm:
        dias += 1
        distancia_percorrida += maxkm
        
        if dias % maxtemp == 0:
            distancia_percorrida -= maxkm / 2
            
print(dias)
