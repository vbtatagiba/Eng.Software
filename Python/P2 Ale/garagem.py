# Fabricio de Souza e Victor Bernardo

# Importação de Biblioteca
from json import dump, load
from os import stat
# Declaração dos dicionarios usadas.
motoristas={}
carros = {}
base_motoristas={}
base_carros={}

#Listas usadas para motoristas
nome=[]
matricula=[]
sexo=[]
numero_carro=[]
rota=[]
viagens=[]

# Listas usadas para carros
mat_carro=[]
Motorista=[]
matricula=[]
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
        # Caso não existe o arquivo, ele vai criar um arquivo vazio.
    except FileNotFoundError as err:
        criar_arquivo()
        break

#Procurando o Arquivo de Veiculos
while True:
    try:
        if stat(arquivo_carros).st_size > 0:
            with open(arquivo_carros, encoding='utf-8') as acc:
                carros = load(acc)
        else:
            carros = []
        break
        # Caso não existe o arquivo, ele vai criar um arquivo vazio.
    except FileNotFoundError as err:
        criar_arquivo()
        break

    # Início do menu de motoristas.
def motorista():
        menu_motorista = input('| Seja bem-vindo, Sr Motorista.\n| Se for novo, digite 1 para se registrar; \n| Digite 2 para logar:')
        while True:
            if menu_motorista == '1': # Se a opção for 1 o programa vai começar o processo de registro
                # TRATATIVA PARA O INPUT DE DIGITAR O NOME.
                while True:
                    nome = input('|Qual o seu nome? ').title()
                    try:
                        nome = int(nome)
                        print('|Por favor, digite um valor correto.')
                    except:
                        if len(nome) >= 3:
                            break
                        else:
                            print('|Por favor, um nome com mais de 3 letras.')

                # TRATATIVA PARA O INPUT DE DIGITAR DO SEXO.
                while True:
                    sexo = input('|Qual seu sexo (feminino ou masculino)? ').lower()
                    try:
                        sexo = int(sexo)
                        print('|Por favor, digite um valor correto.')
                    except:
                        if sexo == 'f' or sexo == 'm' or sexo == 'feminino' or sexo == 'masculino':
                            break
                #TRATATIVA PARA O INPUT DA MATRICULA
                while True:
                    matricula = int(input('|Digite sua matrícula (Número de até 4 dígitos que correspondem ao seu registro na empresa):'))
                    if matricula > 4:
                        break
                    else:
                        print("|Insira uma matricula valida")
                #TRATATIVA PARA O INPUT DA NUMERAÇÃO DO CARRO
                while True:
                    numero_carro=int(input('|Insira a numeração do seu carro'))
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
                #nesse momentos formatamos todas as inforções em forma de dicionario
                motoristas[nome] = {"matricula": matricula, "sexo": sexo, "numero do Carro": numero_carro, "rota": rota, "viagens": viagens}
                for k,v in motoristas.items():
                    print (k,v)

                att_flie()
                break

            elif menu_motorista == '2': # Se a opção escolhida for 2 o programa vai apresentar as escalas
                print('| Menu de login.')
                nome = input('| Digite seu primeiro nome:')
                print('Logado!')
                for k,v in motoristas.items():
                    print (k,v)

                
        


    # Início do menu de despachante.
def despachante():
        senha = input('| Seja bem-vindo ao menu de despachantes! \n Digite a senha de despachante para passar: ')
        if senha == "@teste":
            menu_despachante = input(
         '''| O que deseja ver, Sr Despachante? 
            |Se deseja adicionar carros por favor insira o caracter "+" se deseja ver as escalas dos motorista insira o caracter "!": ''')
            if menu_despachante=='+':    
                while True:            
                    #TRATATIVA PARA O INPUT DA NUMERAÇÃO DO CARRO
                    while True:
                        mat_carro=int(input('|Insira a Numeração do carro:'))
                        if mat_carro>=5:
                            carros.append(mat_carro)
                            break
                        else:
                            print('insira um numero valido de digitos')
                    #TRATATIVA DE INPUT DO NOME DO MOTORISTA
                    while True:
                        Motorista = input('|Qual o nome do motorista: ').title() # deixa a primeira letra maiuscula
                        try:
                            Motorista = int(Motorista)
                            print('Por favor, digite um valor correto.')
                        except:
                            if len(Motorista) >= 3:
                                carros.append(Motorista)
                                break
                            else:
                                print('Por favor, um nome com mais de 3 letras.')
                    #Tratativa de input Matricula
                    while True:
                        matricula = int(input('|Digite a matrícula (Número de 6 dígitos que correspondem ao seu registro na empresa):'))
                        if matricula > 6:
                            carros.append(matricula)
                            break
                        else:
                            print("Insira uma matricula valida")
                    #TRATATIVA PARA O INPUT DA ROTA
                    while True:
                        rota=input('|Insira a rota: ')
                        try:
                            rota = int(rota)
                            print('Por favor, digite um valor correto.')
                        except:
                            carros.append(rota)
                            break
                    #TRATATIVA PARA O INPUT DE VIAGENS
                    while True:
                        viagens = input('|Qual o número de viagens?  ').title() # deixa a primeira letra maiuscula
                        try:
                            viagens = int(viagens)
                            print('Por favor, digite um valor correto.')
                        except:
                            if len(viagens) >= 1:
                                carros.append(viagens)
                                break
                            else:
                                print('Por favor, digite um número inteiro.')
                    print(carros)
      
                    carros[mat_carro] = {"Motorista": Motorista, "matricula": matricula, "rota": rota, "viagens": viagens}
                    att_flie()
                     
                    break     
                    #tratando em dicionario        
            elif menu_despachante== "!" :
                for k,v in motoristas.items():
                    print (k,v)
         
    # Encerra o programa
def fim():
        print("Operação encerrada.")
    # Mostra todos os carros
def carro():
     for k,v in carros.items():
        print(k,v)

    # Mostra todos os motoristas


# Repetição usada no menu.
while True:
    menu = input('| Seja bem-vindo(a) à garagem. \n| Digite 1 se for motorista. \n| Digite 2 se for o despachante responsável.\n| Digite 3 para ver os carros.\n| Ou 4 para sair\n| Digite aqui: ')
    
    if menu == "1": 
        motorista()
    elif menu == "2":
        despachante()
    elif menu =="3":
        carro()
    elif menu== "4":
        print(' F I M ')
