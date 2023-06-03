'''A herança é um conceito fundamental na programação orientada a objetos, que permite que uma classe herde características (atributos e métodos) de outra classe, chamada de classe pai ou superclasse. A classe que herda essas características é chamada de classe filha ou subclasse.'''
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome}.")

class Estudante(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula

    def saudacao(self):
        print(f"Oi, eu sou o(a) estudante {self.nome} e minha matrícula é {self.matricula}.")

pessoa = Pessoa("João")
estudante = Estudante("Maria", "12345")

pessoa.saudacao()
estudante.saudacao()
'''Neste exemplo, temos uma classe base chamada Pessoa, que possui um construtor que inicializa o atributo nome e um método saudacao().

A classe Estudante é uma subclasse de Pessoa e herda o construtor através do método super().__init__(nome), além de adicionar seu próprio atributo matricula. A subclasse também redefine o método saudacao() para incluir a matrícula do estudante.

Quando criamos objetos das classes Pessoa e Estudante e chamamos o método saudacao(), a herança permite que o comportamento específico de cada classe seja executado corretamente.'''