# Criando um dicionário vazio
dic = {}

# Adicionando as informações pessoais com input()
dic["nome"] = input("Digite seu nome: ")
dic["idade"] = int(input("Digite sua idade: "))
dic["endereco"] = input("Digite seu endereço: ")
dic["telefone"] = input("Digite seu telefone: ")

#mostrando antes de remover
print(dic)
#removendo 
rem = input("digite a chave que deseja remover: ")

if rem in dic:
    dic.pop(rem)

#mostrando depois de remover 
print(dic)

#atulizando a informção
att = input("Digite a chave que deseja atualizar: ")

#att no dic
if att in dic:
    novo = input("Digite o novo valor para a chave {}: ".format(att))
    dic[att] = novo

#mostrando a atulização
print(dic)

# mostrando o número de itens no dicionário
print("O dicionário possui {} itens.".format(len(dic)))

#verificando se esta presente
ver=input("O que deseja ver ?")
if ver in dic:
    print("A chave" ,ver, "está presente no dicionário.")
else:
    print("A chave" ,ver, " não está presente no dicionário.")

#mostrando chave valor do dic
for chave in dic:
    # Obtendo o valor associado à chave atual
    valor = dic[chave]
    # Imprimindo a chave e o valor correspondente
    print(chave + ":", valor)