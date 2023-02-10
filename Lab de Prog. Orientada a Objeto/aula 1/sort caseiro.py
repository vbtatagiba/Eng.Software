'''Este código usa dois loops aninhados para percorrer todos os elementos do array e encontrar o menor elemento não ordenado. O loop externo controla o elemento de início de comparação e o loop interno percorre o restante do array em busca de elementos menores. Quando um elemento menor é encontrado, sua posição é armazenada em min_index. No final da iteração interna, o elemento em min_index é trocado com o elemento em i se min_index for diferente de i, o que significa que um elemento menor foi encontrado e precisa ser colocado na posição correta para ordenar o array. Este processo é repetido até que todos os elementos sejam ordenados e o array ordenado é retornado como resultado.'''
def sort_caseiro(array):
    # Loop através de cada elemento do array
    for i in range(len(array)):
        # Inicializa min_index como o índice atual
        min_index = i
        # Loop através dos elementos restantes do array
        for j in range(i+1, len(array)):
            # Verifica se o elemento atual é menor do que o elemento armazenado em min_index
            if array[j] < array[min_index]:
                # Atualiza min_index com o índice do elemento atual se ele for menor
                min_index = j
        # Verifica se min_index é diferente de i
        # Isso significa que um elemento menor foi encontrado e precisa ser colocado na posição correta
        if min_index != i:
            # Troca o elemento em i com o elemento em min_index
            array[i], array[min_index] = array[min_index], array[i]
    # Retorna o array ordenado
    return array


nomes = []

numero_de_nomes = int(input("Quantos nomes você deseja inserir? "))
for i in range(numero_de_nomes):
    nome = input("Insira o nome: ")
    nomes.append(nome)

nomes_organizado = sort_caseiro(nomes)

print("Nomes ordenados: ", nomes_organizado)
