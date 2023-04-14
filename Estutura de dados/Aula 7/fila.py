# Implementação de uma pilha
"""""
enqueue - inclui elementos na fila
dequeue  - remove o elemento da fila
is_empty - retorna se a fila esta vazia
size - retorna o tamanho da fila

"""
# Criação da Classe
class Fila:

    # Criação do construtor
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def rem_par(self):
        for valor in self.items:
            if valor %2 == 0 :
                self.items.remove(valor)

    def exibir(self):
        print(self.items)
    
    def elemento_na_posicao(self, posicao):
        if posicao < len(self.items):
            return self.items[posicao]
        else:
            return None
    
    def sort(self):
        pilha = []
        while not self.is_empty():
            elemento = self.dequeue()
            pilha.append(elemento)
        
        while len(pilha) > 0:
            elemento = pilha.pop()
            self.enqueue(elemento)

    def remover_maior_valor(self):
        if self.is_empty():
            return None
        
        maior_valor = self.items[0]
        for i in range(1, len(self.items)):
            if self.items[i] > maior_valor:
                maior_valor = self.items[i]
        
        for i in range(len(self.items)):
            if self.items[i] == maior_valor:
                return self.items.pop(i)
    
    def remover_menor_valor(self):
        from random import randint
        if self.is_empty():
            return None
        
        menor_valor = self.items[0]
        for i in range(1, len(self.items)):
            if self.items[i] < menor_valor:
                menor_valor = self.items[i]
        
        for i in range(len(self.items)):
            if self.items[i] == menor_valor:
                novo_valor = randint(menor_valor,99)
                self.items[i]= novo_valor
        
    def idade(self):
        self.items.sort(key=lambda x: x[1])

# Fim da Classe