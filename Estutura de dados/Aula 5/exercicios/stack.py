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
    def inverse(self):
        pilha_aux = Stack() # Cria uma pilha auxiliar vazia
        while self.size() > 0:
            elemento = self.pop() # Retira o elemento da pilha original
            pilha_aux.push(elemento) # Coloca o elemento na pilha auxiliar
        self.items = pilha_aux.items # Atribui a pilha invertida à pilha original
    def rem_maior(self):
        maior = self.peek()
        for item in self.items:
            if item > maior:
                maior = item
        self.items.remove(maior)
        return maior
    def rem_menor(self):
        menor = self.peek()
        for item in self.items:
            if item < menor:
                menor = item
        self.items.remove(menor)
        return menor
    def is_empty(self):
        return len(self.items) == 0
    def sort(self):
        sorted_stack = Stack()
        while not self.is_empty():
            temp = self.pop()
            while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
                self.push(sorted_stack.pop())
            sorted_stack.push(temp)
        self.items = sorted_stack.items
        
# Fim da Classe
