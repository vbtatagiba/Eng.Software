'''Polimorfismo é um conceito de programação orientada a objetos que permite que objetos de classes diferentes sejam tratados de forma uniforme por meio de uma interface comum. Isso significa que um objeto pode ser referenciado por um tipo mais genérico, mas ainda assim executar seu próprio comportamento específico.'''
class Animal:
    def falar(self):
        raise NotImplementedError("Método falar deve ser implementado na subclasse.")

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau Miau!"

def fazer_animal_falar(animal):
    print(animal.falar())

cachorro = Cachorro()
gato = Gato()

fazer_animal_falar(cachorro)
fazer_animal_falar(gato)

'''Neste exemplo acima, temos uma classe base chamada Animal que possui um método falar(). No entanto, essa classe é vazia, pois o método falar() é deixado sem implementação.

As classes Cachorro e Gato são subclasses de Animal e implementam seu próprio comportamento específico para o método falar(). Quando chamamos a função fazer_animal_falar() passando um objeto Cachorro ou Gato, o polimorfismo entra em ação e o método falar() específico de cada classe é executado.'''