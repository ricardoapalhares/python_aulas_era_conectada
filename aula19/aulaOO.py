from abc import ABC, abstractmethod

class Animal():
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print('Au au')

class Gato(Animal):
    def emitir_som(self):
        print('Miau miau')

class Lesma(Animal):
    def rastejar(self):
        pass

rex = Cachorro("rex")
rex.emitir_som()

mimi = Gato("mimi")
mimi.emitir_som()

lesma = Lesma("Lesma")
lesma.rastejar()
#lesma.emitir_som()



