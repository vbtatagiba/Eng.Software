# Definindo o texto
texto='Num ninho de mafagafos há sete mafagafinhos. Quando a mafagafa gafa, gafam os sete mafagafinhos.'
# Separando as palavras
palavras = texto.split()


cont = {}

# Percorrendo todas as palavras e atualizando a contagem no dicionário
for palavra in palavras:
    if palavra in cont:
        cont[palavra] += 1
    else:
        cont[palavra] = 1

# Imprimindo a contagem de palavras
for palavra, quantidade in cont.items():
    print(palavra, quantidade)
