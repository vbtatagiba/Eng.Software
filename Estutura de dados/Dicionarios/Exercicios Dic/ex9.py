# Criando um dic aninhado com os dados(semelhande json)
contatos = {
    "Victor": {
        "telefone": "(21) 1234-5678",
        "email": "victor@email.com",
        "endereco": "Rua A, 1723"
    },
    "Maria": {
        "telefone": "(21) 9876-5432",
        "email": "maria@email.com",
        "endereco": "Rua B, 45"
    },
    "Renata": {
        "telefone": "(21) 4002-8922",
        "email": "renata@email.com",
        "endereco": "Rua C, 769"
    }
}

# Mostrando as informações de contato de cada pessoa
for pessoa in contatos:
    print("Informações de contato de", pessoa + ":")
    print("Telefone:", contatos[pessoa]["telefone"])
    print("E-mail:", contatos[pessoa]["email"])
    print("Endereço:", contatos[pessoa]["endereco"])
    print()
