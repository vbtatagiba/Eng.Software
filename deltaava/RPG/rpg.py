#-----------------------------------------RPG em python Versão 1.0-------------------------------------------------------------#
dados = []

def login():   
    check = 0
    print('LOGIN: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    for i in dados:
        if email == i[0]:
            if senha == i[1]:
                print('Você logou!!!')
                introducao()    
                check = 1  
                break
    if check == 0:
        print('Não encontramos nenhuma conta com esse registro.')
        menu()

def registro():
    print('REGISTRO: ')
    check = 0
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    for i in dados:
        if email == i[0]:
            print('E-mail já cadastrado.')
            check = 1
            break

    if check == 0:
        dados.append([email, senha])
        print('Registro realizado com sucesso!')

    print(dados)

    menu()


def menu():
    print("""
    Digite um número de acordo com o que deseja fazer:
    1 - Login
    2 - Criar uma nova conta
    3 - Sair
    """)
    opc = int(input('Escolha uma das opções: '))
    if opc == 1:
        login()
    elif opc == 2:
        registro()
    elif opc == 3:
        return print('Até a próxima!')
    

def introducao():
    print(""""
        Olá, jogador! Seja bem-vindo ao... Vamos iniciar sua jornada.
        Se você já tem uma jornada, digite 1 para logar. Caso seja um novo aventureiro, digite 2 para criar sua conta. Ou digite 3 para sair.
       """)
    menu()
    
introducao()