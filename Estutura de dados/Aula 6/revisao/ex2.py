# Dado um dicionário, escreva um programa que inverta as chaves e os valores do dicionário.

conta=str(input('Insira o numero da Conta: '))
dic={'conta':conta}

for chave in dic:
    valor=dic[chave]
    print(dic)
    dic={valor:chave}
    print(dic)