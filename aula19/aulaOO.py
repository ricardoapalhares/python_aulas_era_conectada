from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Animal():

    # __ para dizer que é privado
    nome: int
    # construtor
    #def __init__(self, nome):
    #    self.nome = nome
    
    @abstractmethod
    def emitir_som(self):
        pass

@dataclass
class Cachorro():
    emitir: str
    
    #self quer dizer que quando instanciar o objeto, deverá mostrar o método emitir_som, ex: rex.emitir_som()
    def emitir_som(self):
        print(self.emitir)

class Gato(Animal):
    def emitir_som(self):
        print('Miau miau')

class Lesma(Animal):
    def rastejar(self):
        pass

    def bill(self):
        return "bELLA"

    def __casulo(self):
        pass

rex = Cachorro('Ralf')
#rex.emitir = "auauauauau"
rex.emitir_som()

mimi = Gato("mimi")
mimi.emitir_som()

lesma = Lesma("Lesma")
lesma.rastejar()
#lesma.casulo()
print(lesma.bill())
#lesma.emitir_som()



