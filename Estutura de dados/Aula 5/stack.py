# Implementação de uma pilha
"""
push - inclui elementos no início da lista
pop  - remove um item do topo da pilha (e retorna o valor desse item)
size - retorna o tamanho da pilha
"""
# Criação da Classe
class Stack:

    # Criação do construtor
    def __init__(self):
        self.items = []
    #Coloca um item na pilha
    def push(self, item):
        self.items.append(item)
    #Mostra o Tamanho da  pilha
    def size(self):
        return len(self.items)
    #Mostra a base elemento
    def peek(self):
        # retorna o elemento do topo
        if self.size() != 0:
            return self.items[0]
    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
# Fim da Classe
