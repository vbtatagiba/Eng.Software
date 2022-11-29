# Fabricio de Souza e Victor Bernardo

# Importação de Biblioteca
import os
from json import dump, load
from os import stat
# Declaração das listas usadas.
motoristas={}
carros = []
base_motoristas={}
base_carros={}
nome=[]
matricula=[]
sexo=[]
numero_carro=[]
rota=[]
viagens=[]

#Nomeclatura dos arquivos
arquivo_motoristas = 'motorista.json'
arquivo_carros = 'veiculos.json'


#Cria um arquivo Json
def criar_arquivo():
    open(arquivo_motoristas, 'w', encoding='utf-8')
    open(arquivo_carros, 'w', encoding='utf-8')

#Atualiza o arquivo Existente
def att_flie():
    with open(arquivo_motoristas, 'w', encoding='utf-8') as base_motoristas:
        dump(motoristas, base_motoristas, ensure_ascii=False, indent=4, separators=(',', ': '))

    with open(arquivo_carros, 'w', encoding='utf-8') as base_carros:
        dump(carros, base_carros, ensure_ascii=False, indent=4, separators=(',', ': '))

#Procurando o Arquivo de motoristas
while True:
    try:
        if stat(arquivo_motoristas).st_size > 0:
            with open(arquivo_motoristas, encoding='utf-8') as acc:
                motoristas = load(acc)
        else:
            motoristas = {}
        break
    except FileNotFoundError as err:
        # Caso não existe o arquivo, ele vai criar um arquivo vazio.
        criar_arquivo()
        break

#Procurando o Arquivo de Veiculos
while True:
    try:
        if stat(arquivo_carros).st_size > 0:
            with open(arquivo_carros, encoding='utf-8') as acc:
                base_carros = load(acc)
        else:
            carros = []
        break
    except FileNotFoundError as err:
        # Caso não existe o arquivo, ele vai criar um arquivo vazio.
        criar_arquivo()
        break

    # Início do menu de motoristas.
def motorista():
        menu_motorista = input('| Seja bem-vindo, Sr Motorista.\n| Se for novo, digite 1 para se registrar; \n| Digite 2 para logar:')
        while True:
            if menu_motorista == '1':
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
                #TRATATIVA PARA O INPUT DA MATRICULA
                while True:
                    matricula = int(input('|Digite sua matrícula (Número de 6 dígitos que correspondem ao seu registro na empresa):'))
                    if matricula > 6:
                        break
                    else:
                        print("Insira uma matricula valida")
                #TRATATIVA PARA O INPUT DA NUMERAÇÃO DO CARRO
                while True:
                    numero_carro=int(input('Insira a Numeração do seu carro'))
                    if numero_carro>=5:
                        break
                    else:
                        print('insira um numero valido de digitos')
                #TRATATIVA PARA O INPUT DA ROTA
                while True:
                    rota=input('Insira sua rota')
                    try:
                        rota = int(rota)
                        print('Por favor, digite um valor correto.')
                    except:
                        break
                #TRATATIVA PARA O INPUT DE VIAGENS
                while True:            
                    viagens=int(input('Insira quantas Viagens vc dará'))
                    if viagens>0:
                        break
                    else:
                        print('Insira Apenas Numeros')

                motoristas[nome] = {"matricula": matricula, "sexo": sexo, "numero do Carro": numero_carro, "rota": rota, "viagens": viagens}
                print(motoristas)
                att_flie()
                break

            elif menu_motorista == '2':
                print('| Menu de login.')
                nome = input('| Digite seu primeiro nome:')
                matricula = input('| Digite sua senha (Sua matrícula)')
                print('Logado!')
                print(motoristas)


    # Início do menu de despachante.
def despachante():
        senha = input('| Seja bem-vindo ao menu de despachantes! \n Digite a senha de despachante para passar: ')
        if senha == "@teste":
            menu_despachante = input(
                                '''| O que deseja ver, Sr Despachante? 
            |Se deseja adicionar carros por favor insira o caracter "+" se deseja alterar a escala de um motorista insira o caracter "*": ''')
            if menu_despachante=='+':
                while True:
                    add_carro=input('Insira os Carros que deseja inserir,caso deseje voltar ao menu digite a tecla "="')
                    if add_carro == "=":
                        break
                    else:
                        carros.append(add_carro)
            elif menu_despachante== "!" :
                print(motoristas)
         
    # Encerra o programa
def fim():
        print("Operação encerrada.")
    # Mostra todos os carros
def carro():
    print (carros)
    print (base_carros)

    # Mostra todos os motoristas
def pessoa():
    print(motoristas)
    print(base_motoristas)
# Repetição usada no menu.
while True:
    # Primeira parte para seleção dos menus.
    
    menu = input('| Seja bem-vindo(a) à garagem. \n| Digite 1 se for motorista. \n| Digite 2 se for o despachante responsável.\n| Digite 4 para ver os carros.\n| Ou 5 para sair\n| Digite aqui: ')
    
    if menu == "1": 
        motorista()
    elif menu == "2":
        despachante()
    elif menu =="4":
        carro()
    elif menu =="5":
        pessoa()
    elif menu== "6":
        break

print(' ================ \n      F I M \n ================')