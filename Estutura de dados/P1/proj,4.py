import time
import matplotlib.pyplot as plt

# Define a matriz a ser utilizada
elementos = [['a', 'b', 'c', 'd'],
             ['q', 'i', 'n', 'm'],
             ['f', 'e', 'h', 'j'],
             ['p', 'o', 'l', 'g']]

# Lista para armazenar os valores de n e o tempo de execução
ns_for = []
tempos_for = []
ns_ordenando = []
tempos_ordenando = []

# Tamanhos de matrizes a serem testados
testes = [10, 20, 30, 40, 50, 1000]

# Testa o algoritmo para várias matrizes com tamanhos diferentes
for n in range(1, 1001):
    start_for = time.perf_counter()
    
    # Cria uma matriz maior, com n cópias da matriz original
    matriz = elementos * n
    
    valores = []
    posicao_dict = {}

    # Adiciona os elementos da matriz aos valores e suas posições ao dicionário
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valores.append(matriz[i][j])
            posicao_dict[matriz[i][j]] = f'{i}:{j}'

    # Ordena o dicionário e cria uma lista com os valores ordenados
    ordenando_dict = sorted(posicao_dict.items())
    lista_pra_dict = dict(ordenando_dict)
    valores_do_dict = lista_pra_dict.values()
    valores_final = list(valores_do_dict)

    end_for = time.perf_counter()

    start_ordenando = time.perf_counter()

    # Ordena novamente o dicionário e cria uma lista com os valores ordenados
    ordenando_dict = sorted(posicao_dict.items())
    lista_pra_dict = dict(ordenando_dict)
    valores_do_dict = lista_pra_dict.values()
    valores_final = list(valores_do_dict)

    end_ordenando = time.perf_counter()

    # Armazena os resultados
    ms_for = (end_for - start_for) * 10**6
    ns_for.append(n)
    tempos_for.append(ms_for)

    ms_ordenando = (end_ordenando - start_ordenando) * 10**6
    ns_ordenando.append(n)
    tempos_ordenando.append(ms_ordenando)

print(posicao_dict)
# Cria o gráfico
plt.plot(ns_for, tempos_for, label="Loop For")
plt.plot(ns_ordenando, tempos_ordenando, label="Ordenando Dicionário")
plt.xlabel('Tamanho da matriz')
plt.ylabel('Tempo de execução (micro segundos)')
plt.legend()
plt.show()