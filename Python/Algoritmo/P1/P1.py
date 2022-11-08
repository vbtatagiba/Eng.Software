'''Em uma agência bancária dos anos 80 existem 10 caixas e uma fila para cada
caixa. Implementar um programa para simulação das filas na agência. Considerar
que o tamanho das filas é indeterminado.
Nessa agência está sendo realizada uma pesquisa, e todos as pessoas, ao serem
atendidas em um dos caixas preenchem uma ficha fornecendo as seguintes
informações: nome; sexo; data de nascimento; operação realizada (depósito ou
retirada); e informação se é cliente do banco ou não. Em cada caixa existe uma
pilha de fichas preenchidas com essas informações.
Implementar um programa para realizar a simulação desse sistema, contendo os
seguintes módulos:
• Inclusão de pessoas ;
• Atendimento das pessoas (com preenchimento da ficha);
• Emissão de relatório. A qualquer momento o gerente do banco poderá solicitar as
seguintes informações aos caixas:
1. O total de clientes atendidos até o momento em cada caixa;
2. O nome de todas as pessoas do sexo feminino atendidos em
cada caixa;
3. O nome de todos os clientes que realizaram um depósito em
cada caixa;
4. O nome das duas últimas pessoas a realizar uma retirada em
cada caixa;
5. O número do caixa que atendeu o maior número de pessoas
até o momento da pesquisa.
Ao ser realizada uma pesquisa por parte do gerente da agência todas as fichas
preenchidas existentes nos caixas são recolhidas'''


import os
from json import dump, load
from os import stat

clientes = []
caixas = []
sexos = []
operacoes = []

arquivo_clientes = 'clientes.json'


def criar_arquivo():
    open(arquivo_clientes, 'w', encoding='utf-8')

#Atualiza o arquivo Existente
def att_flie():
    with open(arquivo_clientes, 'w', encoding='utf-8') as clientes_l:
        dump(clientes, clientes_l, ensure_ascii=False, indent=4, separators=(',', ': '))

#procurando o Arquivo de clientes
while True:
    try:
        if stat(arquivo_clientes).st_size > 0:
            with open(arquivo_clientes, encoding='utf-8') as acc:
                base = load(acc)
        else:
            clientes = []
        break
    except FileNotFoundError as err:
        # Caso não existe o arquivo, ele vai criar um arquivo vazio.
        criar_arquivo()
        break

#Cadrasto de Cliente 
def cadrasto():
    cliente={} #dicionario temporario
    ncaixa=str(input('Qual O seu Caixa:'))
    nome=str(input('Insira o seu Nome: '))
    sexo=str(input('Insira o seu sexo: '))
    data_nascimento=str(input('Insira sua data de nascimento: '))
    ope=str(input('Qual foi a operação realizada? Digite "R"para Retirada e "D" para depósito '))
    cli=str(input('Já e nosso Cliente? '))
    cliente[nome] = {"caixa": ncaixa, "sexo": sexo, "nascimento": data_nascimento, "operacao": ope, "cliente": cli}
    clientes.append(cliente)
    att_flie()
    menu()

#imprime o relatorio inclusive da base 
def relatorio():
    print(clientes)
    if input('Deseja ver os cliente ja em nosso Banco de dados?:')=='S'or 'sim':
            print(base)
    


def menu():
    while True:
        print('Olá seja bem vindo ao nosso sistema. O que deseja fazer?')
        esc=int(input('Digite 1 para Atendimento 2 Emissão de relatório e 3 para finalizar o sistema:'))
        break
    if esc==1:
        cadrasto()
    elif esc==2:
        relatorio()
    elif esc==3:
        print('''-------------- SISTEMA ENCERRADO    ---------------''')


menu()
