#-------------------------1--------------------------
import random

# Criar tupla com 10 números inteiros aleatórios
numeros = tuple(random.sample(range(100), 10))

# Imprimir maior e menor número da tupla
print("Tupla de números: ", numeros)
print("Maior número: ", max(numeros))
print("Menor número: ", min(numeros))


#------------------------------------2-------------
# Criar as duas tuplas
t1 = (3, 8, 1, 10, 5)
t2 = (7, 4, 6, 2, 9)

# Mesclar as tuplas em ordem crescente
t3 = tuple(sorted(t1 + t2))

# Imprimir a tupla mesclada
print("Tupla mesclada em ordem crescente: ", t3)


#--------------------------------3-------------------------------
# Criar a tupla com nomes de pessoas
tnomes = ("Ana", "Carlos", "Bruno", "Daniela", "Felipe")

# Ordenar a tupla alfabeticamente
tordenada = tuple(sorted(tnomes))

# Imprimir a tupla ordenada
print("Tupla de nomes ordenada: ", tordenada)


#-------------------4,5,6,8,9---------------------------------------

tnumeros = (1, 5, 3, 7, 5, 2, 5, 8)
rem = 5
# Remover todas as ocorrências do número da tupla
tsnum = tuple(filter(lambda x: x != rem, tnumeros))

# Imprimir a tupla sem o número
print("Tupla sem o número {}: {}".format(rem, tsnum))

# Contar números pares e ímpares
pares = len(tuple(filter(lambda x: x % 2 == 0, tnumeros)))
impares = len(tuple(filter(lambda x: x % 2 != 0, tnumeros)))
print("Tupla de números: ", tnumeros)
print("Número de pares: ", pares)
print("Número de ímpares: ", impares)

# Definir o número a ser verificado
num = 5

if num in tnumeros:
    print("O número {} está na tupla.".format(num))
else:
    print("O número {} não está na tupla.".format(num))

soma = sum(tnumeros)
media = sum(tnumeros) / len(tnumeros)

print("Soma dos números: ", soma)
print("Média dos números: ", media)

#---------------------7------------------------
# Criar a tupla com nomes de frutas
tfrutas = ("maçã", "banana", "laranja", "abacaxi", "uva")

# Definir a fruta a ser verificada
fruta = "laranja"

# Verificar se a fruta está na tupla
if fruta in tfrutas:
    print("A fruta {} está na tupla.".format(fruta))
else:
    print("A fruta {} não está na tupla.".format(fruta))


#----------------------------10------------------
# Criar a tupla com nomes de pessoas
tupla_nomes = ("Ana", "Carlos", "Bruno", "Daniela", "Felipe")

# Imprimir o primeiro e o último nome da tupla
print("Tupla de nomes: ", tupla_nomes)
print("Primeiro nome: ", tupla_nomes[0])
print("Último nome: ", tupla_nomes[-1])

