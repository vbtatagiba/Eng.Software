'''
Curso: Engenharia de Software
Disciplina: Algoritmo
Professora: Alessandra Fonseca
Turma: B
Nome: Hygor Rasec
Matrícula: 202212020
Data: 04/10/2022
'''

'''
1. Definições
Em uma agência bancária dos anos 80 existem 10 caixas e uma fila para cada caixa. Implementar um programa para simulação das filas na agência. Considerar que o tamanho das filas é indeterminado. Nessa agência está sendo realizada uma pesquisa, e todos as pessoas, ao serem atendidas em um dos caixas preenchem uma ficha fornecendo as seguintes informações: nome; sexo; data de nascimento; operação realizada (depósito ou retirada); e informação se é cliente do banco ou não. Em cada caixa existe uma pilha de fichas preenchidas com essas informações. Implementar um programa para realizar a simulação desse sistema, contendo os seguintes módulos:

• Inclusão de pessoas ; 
• Atendimento das pessoas (com preenchimento da ficha); 
• Emissão de relatório. A qualquer momento o gerente do banco poderá solicitar as seguintes informações aos caixas: 

1. O total de clientes atendidos até o momento em cada caixa;
2. O nome de todas as pessoas do sexo feminino atendidos em cada caixa;
3. O nome de todos os clientes que realizaram um depósito em cada caixa;
4. O nome das duas últimas pessoas a realizar uma retirada em cada caixa;
5. O número do caixa que atendeu o maior número de pessoas até o momento da pesquisa.

Ao ser realizada uma pesquisa por parte do gerente da agência todas as fichas preenchidas existentes nos caixas são recolhidas.
'''

import os
from json import dump, load
from os import stat

clientes = []
caixas = []
sexos = []
operacoes = []

clientes_file = 'clientes.json'


def create_file():
    open(clientes_file, 'w', encoding='utf-8')


def update_file():
    with open(clientes_file, 'w', encoding='utf-8') as clientes_l:
        dump(clientes, clientes_l, ensure_ascii=False, indent=4, separators=(',', ': '))


while True:
    try:
        if stat(clientes_file).st_size > 0:
            with open(clientes_file, encoding='utf-8') as acc:
                clientes = load(acc)
        else:
            clientes = []
        break
    except FileNotFoundError as err:
        # Caso não existe o arquivo, ele vai criar um arquivo vazio.
        create_file()
        break

print('\nSeja bem vindo(a) a agência bancária SEU DINHEIRO BEM GUARDADO!')
print('===============================================================\n')

while True:
    cliente= {}  # lista temporária

    # TRATATIVA PARA O INPUT DE DIGITAR O NÚMERO DO CAIXA.
    while True:
        caixa = input('Escolha uma caixa para você ir (de 1 à 10)? ')
        try:
            caixa = int(caixa)
            if caixa >= 1 and caixa <= 10:
                break
            else:
                print('Por favor, digite um número de 1 à 10.')
        except:
            print('Por favor, digite um valor correto.')

    # TRATATIVA PARA O INPUT DE DIGITAR O NOME.
    while True:
        nome = input('Qual o seu nome? ').title()
        try:
            nome = int(nome)
            print('Por favor, digite um valor correto.')
        except:
            if len(nome) >= 3:
                break
            else:
                print('Por favor, um nome com mais de 3 letras.')

    # TRATATIVA PARA O INPUT DE DIGITAR DO SEXO.
    while True:
        sexo = input('Qual seu sexo (feminino ou masculino)? ').lower()
        try:
            sexo = int(sexo)
            print('Por favor, digite um valor correto.')
        except:
            if sexo == 'f' or sexo == 'm' or sexo == 'feminino' or sexo == 'masculino':
                break
            else:
                print('Por favor, digite feminino ou masculino.')

    # TRATATIVA PARA O INPUT DE DIGITAR A DATA DE NASCIMENTO.
    while True:
        inteiros = []
        letras = []
        nascimento = input('Qual a sua data de nascimento (dia/mês/ano)? ')

        for _ in list(nascimento):
            try:
                inteiro = int(_)
                inteiros.append(_)
            except:
                letras.append(_)
        
        if len(inteiros) == 8 and len(letras) == 2:
            break
        else:
            print('Por favor, digite um valor correto. A data tem que ter formado (dd/mm/aaaa).')
    
    # TRATATIVA PARA O INPUT DE DIGITAR A OPERAÇÃO.
    while True:
        operacao = input('Qual operação você vai realizar (depósito ou retirada)? ').lower()
        try:
            operacao = int(operacao)
            print('Por favor, digite um valor correto.')
        except:
            if operacao == 'depósito' or operacao == 'retirada':
                break
            else:
                print('Por favor, digite depósito ou retirada.')

    # TRATATIVA PARA O INPUT DE DIGITAR SE É CADASTRADO OU NÃO.
    while True:
        cadastrado = input('Você já é cadastrado aqui em nossa agência (sim ou não)? ').lower()
        try:
            cadastrado = int(cadastrado)
            print('Por favor, digite um valor correto.')
        except:
            if cadastrado == 'sim' or cadastrado == 'não':
                break
            else:
                print('Por favor, digite sim ou não.')

    cliente[nome] = {"caixa": caixa, "sexo": sexo, "nascimento": nascimento, "operacao": operacao, "cliente": cadastrado}
    clientes.append(cliente)
    update_file()

    # TRATATIVA PARA O INPUT DE VER RELATÓRIO.
    while True:
        gerente = 0
        gerente = input('O gerente deseja ver os relatórios (sim ou não)? ').lower()
        try:
            gerente = int(gerente)
            print('Por favor, digite um valor correto.')
        except:
            if gerente == 'sim':
                for c in range(len(clientes)):
                    # print(clientes[c])  # {'a': {'caixa': '1', 'sexo': 'a', 'nascimento': 'a', 'operacao': 'a', 'cliente': 'a'}}
                    for n, d in clientes[c].items():
                        # print(f'nome do cliente = {n} | dados = {d}')
                        caixas.append(d['caixa'])
                        sexos.append([d['caixa'], n, d['sexo']])  # caixa, nome, sexo
                        operacoes.append([d['caixa'], n, d['operacao']])  # caixa, nome, operacao

                print('')
                print('===============================')
                print('========== RELARÓTIO ==========')
                print('===============================')
                print('')

                # 1. Aqui imprime o total de clientes atendidos até o momento em cada caixa:

                for c in range(1,11):
                    if caixas.count(c) > 1:
                        print(f'Tivemos {caixas.count(c)} clientes atendidos no caixa {c}.')
                    elif caixas.count(c) == 1:
                        print(f'Tivemos {caixas.count(c)} cliente atendido no caixa {c}.')

                # 2. Aqui imprime o nome de todas as pessoas do sexo feminino atendidos em cada caixa:

                cx_sexo_dict = {}
                cx_sexo_list = []
                cx_f = {}

                for c in range(1,11):
                    for s in range(len(sexos)):
                        if sexos[s][0] == c:
                            cx_sexo_dict[c] = [sexos[s][1], sexos[s][2]]
                            cx_sexo_list.append(cx_sexo_dict)
                            cx_sexo_dict = {}

                for l in cx_sexo_list:
                    for c in range(1,11):
                        for k, v in l.items():
                            if c == k:
                                if v[1] == 'f' or v[1] == 'feminino':
                                    try:
                                        cx_f[k].append(v[0])
                                    except:
                                        cx_f[k] = []
                                        cx_f[k].append(v[0])

                if len(cx_f) == 0:
                    print(f'Por enquanto nenhuma mulher foi atendida.')

                for k, v in cx_f.items():
                    v_temp = ', '.join(v)
                    if len(v) > 1:
                        print(f'O caixa {k} atendeu {len(v)} mulheres e as clientes foram: {v_temp}.')
                    elif len(v) == 1:
                        print(f'O caixa {k} atendeu apenas {len(v)} mulher e a cliente foi: {v_temp}.')

                # 3. O nome de todos os clientes que realizaram um depósito em cada caixa:

                cx_operacoes_dict = {}
                cx_operacoes_list = []
                cx_deposito = {}
                cx_retirada = {}

                for c in range(1,11):
                    for s in range(len(operacoes)):
                        if operacoes[s][0] == c:
                            cx_operacoes_dict[c] = [operacoes[s][1], operacoes[s][2]]
                            cx_operacoes_list.append(cx_operacoes_dict)
                            cx_operacoes_dict = {}

                for l in cx_operacoes_list:
                    for c in range(1,11):
                        for k, v in l.items():
                            if c == k:
                                if v[1] == 'depósito':
                                    try:
                                        cx_deposito[k].append(v[0])
                                    except:
                                        cx_deposito[k] = []
                                        cx_deposito[k].append(v[0])
                                elif v[1] == 'retirada':
                                    try:
                                        cx_retirada[k].append(v[0])
                                    except:
                                        cx_retirada[k] = []
                                        cx_retirada[k].append(v[0])

                if len(cx_deposito) == 0:
                    print(f'Por enquanto ainda não houve nenhum depósito.')

                for k, v in cx_deposito.items():
                    v_temp = ', '.join(v)
                    if len(v) > 1:
                        print(f'O caixa {k} realizou {len(v)} depósitos e os(as) clientes foram: {v_temp}.')
                    elif len(v) == 1:
                        print(f'O caixa {k} realizou apenas 1 depósito e o(a) cliente foi: {v_temp}.')

                # 4. O nome das duas últimas pessoas a realizar uma retirada em cada caixa:

                if len(cx_retirada) == 0:
                    print(f'Por enquanto ainda não houve nenhum retirada.')

                for k, v in cx_retirada.items():
                    invert_v = v[::-1]
                    dois_primeiros = invert_v[:2]

                    v_temp = ', '.join(dois_primeiros)
                    if len(dois_primeiros) > 1:
                        print(f'O caixa {k} realizou {len(dois_primeiros)} retiradas e os(as) clientes foram: {v_temp}.')
                    elif len(dois_primeiros) == 1:
                        print(f'O caixa {k} realizou apenas 1 retirada e o(a) cliente foi: {v_temp}.')
                    else:
                        print(f'O caixa {k} não realizou nenhum retirada.')

                # 5. O número do caixa que atendeu o maior número de pessoas até o momento da pesquisa.

                cx_max = {}
                for c in range(1,11):
                    if caixas.count(c) != 0:
                        try:
                            cx_max[c].append(caixas.count(c))
                        except:
                            cx_max[c] = []
                            cx_max[c].append(caixas.count(c))

                max_cli = [{1:[0]}]
                for k1, v1 in cx_max.items():
                    for n in max_cli:
                        for k2, v2 in n.items():
                            if v1[0] > v2[0]:
                                max_cli.clear()
                                max_cli.append({k1: v1})
                            elif v1[0] == v2[0]:
                                max_cli.append({k1: v1})
                            break
                        break

                for v1 in max_cli:
                    for v2 in v1.values():
                        valor_total = v2[0]
                        break
                    break

                if len(max_cli) > 1:
                    print(f'{len(max_cli)} caixas empataram com um número máximo de {valor_total} atendimentos cada. Os caixas foram: ', end='')
                    for v1 in max_cli:
                        for k in v1.keys():
                            print(f'{k}, ', end='')

                        print('')
                elif len(max_cli) == 1:
                    for v1 in max_cli:
                        for k, v2 in v1.items():
                            if v2[0] > 1:
                                print(f'O caixa {k} realizou {v2[0]} atendimentos e foi o caixa que mais atendeu.')
                            else:
                                print(f'O caixa {k} realizou {v2[0]} atendimento e foi o caixa que mais atendeu.')
                else:
                    print('Não houve atendimento em nenhum caixa.')

                # DEPOIS DO GERENTE VERIFICAR OS RELATÓRIOS, TUDO É APAGADO.
                clientes.clear()
                caixas.clear()
                sexos.clear()
                operacoes.clear()

                os.remove(clientes_file)
                create_file()

                print('')

                break
            elif gerente == 'não':
                break
            else:
                print('Por favor, digite sim ou não.')

    while True:
        fechar_banco = input('Deseja fechar o banco (sim ou não)? ').lower()
        try:
            fechar_banco = int(fechar_banco)
            print('Por favor, digite um valor correto.')
        except:
            if fechar_banco == 'sim' or fechar_banco == 'não':
                break
            else:
                print('Por favor, digite sim ou não.')

    print('')
    if fechar_banco == 'sim':
        break

print('Agradecemos a sua visita, volte sempre!')