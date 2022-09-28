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




cliente=[]
sexo=[]
data_nascimento=[]
ope=[]
cli=[]
def cadrasto():
    while True:
        nome=str(input('Insira o seu Nome: '))
        cliente.append(nome)
        sexo2=str(input('Insira o seu sexo: '))
        sexo.append(sexo2)
        data_nascimento2=str(input('Insira sua data de nascimento: '))
        data_nascimento.append(data_nascimento2)
        ope2=str(input('Qual foi a operação realizada? Digite "R"para Retirada e "D" para depósito '))
        ope.append(ope2)
        cli2=str(input('Já e nosso Cliente? '))
        cli.append(cli2)
        print(cliente)
        print(sexo)
        print(data_nascimento)
        print(ope)
        print(cli)
        break
def atendimento():
    input('Insira o nome do seu ')

def menu():
    while True:
        print('Olá seja bem vindo ao nosso sistema. O que deseja fazer?')
        esc=int(input('Digite 1 para Inclusão de pessoas 2 para Atendimento das pessoas e 3 para Emissão de relatório:'))
        break
    if esc==1:
        cadrasto()
    elif esc==2:
        atendimento()
    elif esc==3:
        emissao()