def encontrar_maior_soma_submatriz(matriz):
    """
    Encontra a maior soma entre todas as submatrizes 3x3 de uma matriz.

    Args:
        matriz (list): Uma matriz bidimensional de inteiros.

    Returns:
        int: A maior soma encontrada entre todas as submatrizes 3x3 da matriz.
    """
    linhas = len(matriz)
    colunas = len(matriz[0])
    maior_soma = float('-inf')
    for i in range(linhas-2):
        for j in range(colunas-2):
            soma = matriz[i][j] + matriz[i][j+1] + matriz[i][j+2] \
                + matriz[i+1][j] + matriz[i+1][j+1] + matriz[i+1][j+2] \
                + matriz[i+2][j] + matriz[i+2][j+1] + matriz[i+2][j+2]
            maior_soma = max(maior_soma, soma)
    return maior_soma


# Exemplo de uso.
matriz = [[1, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 2, 0],
          [0, 0, 0, 1, 2, 2],
          [0, 0, 0, 2, 2, 2]]

maior_soma = encontrar_maior_soma_submatriz(matriz)
print("A maior soma encontrada foi:", maior_soma)
