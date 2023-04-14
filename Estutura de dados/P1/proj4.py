# UNIVERSIDADE DE VASSOURAS - MARICÁ
# PROFESSOR: MÁRCIO GARRIDO
# ESTUDANTES: FÁBIO LIMA, HYGOR RASEC, VICTOR BERNARDO
# 30/03/2023
# PROJETO 04

# O objetivo deste projeto é criar um algoritmo capaz de determinar a posição de cada elemento de um conjunto e imprimir esses valores de forma ascendente, bem como imprimir separadamente as posições atuais. Por fim, a notação Big'O do resultado deve ser impressa de forma gráfica.

# // Entrada

# elementos = [[a,b,c,d],[q,i,n,m],[f,e,h,j],[p,o,l,g]]

# // Saída

# [a,b,c,d,e,f,g,h,i,j,l,m,n,o,p,q]
# [0:0,0:1,0:2,0:3,2:1,2:0,3:3,2:2,1:1,2:3,3:2,1:3,1:2,3:1,3:0,1:0]

import time  # biblioteca para medir o tempo de execução de um código.
import matplotlib.pyplot as plt  # biblioteca para plotar gráficos.

# Definição da função que ordena os elementos da matriz
def func_ordenar(matriz):
    elementos = []  # Lista vazia que irá armazenar todos os elementos da matriz
    posicao_dict = {}  # Dicionário vazio que irá armazenar a posição de cada valor da matriz

    # Laço duplo para percorrer a matriz e armazenar os valores e suas respectivas posições no dicionário
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elementos.append(matriz[i][j])  # Adiciona o elemento na lista de elementos
            posicao_dict[matriz[i][j]] = f'{i}:{j}'  # Adiciona a posição do valor no dicionário

    ordenando_dict = sorted(posicao_dict.items())  # Ordena o dicionário em ordem crescente
    lista_pra_dict = dict(ordenando_dict)  # Converte o dicionário ordenado em um dicionário final
    valores_do_dict = lista_pra_dict.values()  # Pega os valores ordenados do dicionário
    return list(valores_do_dict), elementos  # Retorna os valores ordenados e a lista de elementos original

matriz = [['a','b','c','d'],['q','i','n','m'],['f','e','h','j'],['p','o','l','g']]
valores_final, elementos = func_ordenar(matriz)  # Chama a função para ordenar a matriz

print(sorted(elementos))  # Imprime a lista de elementos original ordenada
print(valores_final)  # Imprime a lista de valores ordenados

tamanho_matriz = []
tempo_execucao = []

# Loop para testar o tempo de execução para diferentes tamanhos de matriz
for i in range(1, 401, 4):
    
    start_for = time.perf_counter()  # Inicia o contador de tempo
    
    matriz = [['a','b','c','d'],['q','i','n','m'],['f','e','h','j'],['p','o','l','g']]
    matriz = matriz * i  # Multiplica a matriz pelo número de i especificado

    func_ordenar(matriz)  # Chama a função para ordenar a matriz multiplicada

    end_for = time.perf_counter()  # Para o contador de tempo
    
    microsegundos = (end_for-start_for) * 10**6  # Calcula o tempo de execução em microssegundos
    
    tamanho_matriz.append(i)  # Adiciona o tamanho da matriz à lista de tamanhos
    tempo_execucao.append(microsegundos)  # Adiciona o tempo de execução à lista de tempos

plt.plot(tamanho_matriz, tempo_execucao, label="Função func_ordenar(matriz)")  # Plota um gráfico com os tamanhos de matriz e seus respectivos tempos de execução
plt.xlabel('Tamanho da matriz (matriz = matriz * i)')  # Legenda para o eixo x
plt.ylabel('Tempo de execução (micro segundos)')  # Legenda para o eixo y
plt.legend()  # Mostra a legenda do gráfico
plt.show()  # Exibe o gráfico plotado