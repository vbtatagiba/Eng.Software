def sort_caseiro(array):
    for i in range(len(array)):
        menor_elemento = i #armazena o menor elemento
        for j in range(i+1, len(array)):
            if array[j] < array[menor_elemento]:
                menor_elemento = j
        if menor_elemento != i: #se for diferente existe um elemento menor ainda 
            array[i], array[menor_elemento] = array[menor_elemento], array[i] #troca a ordem de armazenamento
    return array

nomes = []

numero_de_nomes = int(input("Quantos nomes você deseja inserir? "))
for i in range(numero_de_nomes):
    nome = input("Insira o nome: ")
    nomes.append(nome)

nomes_organizado = sort_caseiro(nomes)

print("Nomes ordenados: ", nomes_organizado)
