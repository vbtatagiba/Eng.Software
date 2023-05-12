from ex import CaixaEletronico
# Exemplo de uso do caixa eletrônico
caixa = CaixaEletronico()
while True:
    print('-='*20)
    print("Bem-vindo ao caixa eletrônico!")
    print("Insira seu cartão...")
    matricula, senha = caixa.cadastrar()
    print('-='*35)
    print(senha)

    inputsenha = input("Digite sua senha: ")
    if inputsenha == senha:
        if caixa.sacar():
            inputconfirmacao = input("Deseja confirmar a operação? (S/N) ")
            if inputconfirmacao.upper() == "S":
                print("Operação confirmada!")
                print('-='*35)
            else:
                print("Operação cancelada!")
                print('-='*35)
    else:
        print("Senha incorreta!")
        print('-='*35)
