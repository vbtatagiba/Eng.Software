def sort_caseiro(array):
    for i in range(len(array)):
        menor_elemento = i #armazena o menor elemento
        for j in range(i+1, len(array)):
            if array[j] < array[menor_elemento]:
                menor_elemento = j
        if menor_elemento != i: #se for diferente existe um elemento menor ainda 
            array[i], array[menor_elemento] = array[menor_elemento], array[i] #troca a ordem de armazenamento
    return array

cidades = []

numero_de_cidades = int(input("Quantas cidades você deseja inserir? "))
for i in range(numero_de_cidades):
    cidade = input("Insira o nome: ")
    cidades.append(cidade)

nomes_organizado = sort_caseiro(cidades)
print('-='*35)
print("Cidades ordenadas: ", nomes_organizado)
print('-='*35)