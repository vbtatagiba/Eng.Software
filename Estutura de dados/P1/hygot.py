import time
import matplotlib.pyplot as plt

def func_ordenar(elementos):
    valores = []
    posicao_dict = {}

    for i in range(len(elementos)):
        for j in range(len(elementos[i])):
            valores.append(elementos[i][j])
            posicao_dict[elementos[i][j]] = f'{i}:{j}'
    ordenando_dict = sorted(posicao_dict.items())
    lista_pra_dict = dict(ordenando_dict)
    valores_do_dict = lista_pra_dict.values()
    return list(valores_do_dict), valores

elementos = [['a','b','c','d'],['q','i','n','m'],['f','e','h','j'],['p','o','l','g']]

valores_final, valores = func_ordenar(elementos)

print(sorted(valores))
print(valores_final)

# listas para armazenar os valores de n e o tempo de execução
tamanho_matriz = []
tempo_execucao = []

# testa o algoritmo para várias matrizes com tamanhos diferentes
for e in range(1, 101):
    
    start_for = time.perf_counter()
    
    valores = []
    posicao_dict = {}
    
    elementos = [['a','b','c','d'],['q','i','n','m'],['f','e','h','j'],['p','o','l','g']]
    elementos = elementos * e

    func_ordenar(elementos)

    end_for = time.perf_counter()

    microsegundos = (end_for-start_for) * 10**6
    
    tamanho_matriz.append(e)
    tempo_execucao.append(microsegundos)

plt.plot(tamanho_matriz, tempo_execucao)
plt.xlabel('Tamanho da matriz')
plt.ylabel('Tempo de execução (micro segundos)')

plt.show()