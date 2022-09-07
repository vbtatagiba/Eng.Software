agenda = [] 

def pede_nome():  # função para pedir o nome 
     return(input("Nome: "))#retorna o valor da função
 
def pede_telefone():
     return(input("Telefone: "))

def novo(): #função para adicionar novo contato
     global agenda#definindo var global
     nome = pede_nome() #entrada de dados e chamada de função 
     telefone = pede_telefone()
     agenda.append([nome, telefone]) #adicionando os cadastros na agenda
     

def pede_nome_arquivo():
     return(input("Nome do arquivo: "))

def pesquisa(nome):#função para pesquisar
     mnome = nome.lower() #convertendo todas as letras em minúsculas
     for p, e in enumerate(agenda): #executando o loop
         if e[0].lower() == mnome:
               return p
     return None



def apaga():
     global agenda
     nome = pede_nome()
     p = pesquisa(nome)#cria uma var e chama a função pesquisa
     if p != None: #condição se p for diferente de nada 
         del agenda[p] #apaga o elemento em p da agenda 
     else:
         print("Nome não encontrado.")

def altera():
     p = pesquisa(pede_nome())
     if p != None:
         nome = agenda[p][0] #procurando os dados na agenda 
         telefone = agenda[p][1]
         print("Encontrado:")
         mostra_dados(nome, telefone)
         nome = pede_nome()
         telefone = pede_telefone()
         agenda[p] = [nome, telefone]
     else:
         print("Nome não encontrado."),

         
def mostra_dados(nome, telefone): #função para listar
     print("Nome: %s Telefone: %s" % (nome, telefone))


def lista():  # mostra toda a lista de contato
     print("\nAgenda\n\n------")
     for e in agenda:
         mostra_dados(e[0], e[1])
     print("------\n")

def lê():
     global agenda
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "r", encoding = "utf-8")
     agenda = []
     for l in arquivo.readlines():
         nome, telefone = l.strip().split("#")
         agenda.append([nome, telefone])
     arquivo.close()

def grava():
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "w", encoding = "utf-8")
     for e in agenda:
         arquivo.write("%s#%s\n" % (e[0], e[1]))
     arquivo.close()

def valida_faixa_inteiro(pergunta, inicio, fim): #função para validar os números inteiros 
     while True:  #criando um loop infinito
         try:      #criando um acordo /condição
               valor = int(input(pergunta)) #se foi atribuido um valor dif de inteiro , tratamento de erro
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:  #caso falso 
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

"""
usando a instrução Try-except, para tratar erro inesperado que possa ocorrer durante a execução do programa.
caso o usuário digite o valor (ValueError) e irá fazer com que nosso programa pare de funcionar e mostre uma mensagem de erro na tela.
com isso , utiza essa instrução para criar nossa própria mensagem de erro, e assim pode evitar a aparada do programa .
"""

def menu():  #função menu opções
     print("""
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Grava
   6 - Lê

   0 - Sai
""")
     return valida_faixa_inteiro("Escolha uma opção: ",0,6)

while True:  #criando loop infinito
     opção = menu()
     if opção == 0:
         break
     if opção == 1:
         novo()
     if opção == 2:
         altera()
     if opção == 3:
         apaga()
     elif opção == 4:
         lista()
     elif opção == 5:
         grava()
     elif opção == 6:
         lê()