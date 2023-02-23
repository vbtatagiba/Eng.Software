nomes=[]

numero_de_nomes = int(input("Quantos nomes você deseja inserir? "))

for i in range(numero_de_nomes):
    nome = input("Insira o nome: ")
    nomes.append(nome)

print(sorted(nomes))