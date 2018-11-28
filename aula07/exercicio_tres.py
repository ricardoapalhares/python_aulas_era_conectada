#Exercicio3
#Desenvolva um jogo da forca
#O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
#O jogador poderá errar 6 vezes antes de ser enforcado

#Ex.
#Digite uma letra: A
#Você errou -> 
#
#


import random

arquivo = open("palavras.txt", "r")
palavras = arquivo.readlines()
tam = len(palavras)

for index, palavra in enumerate(palavras):
	palavras[index] = palavra.replace('\n','')

print(palavras[random.randrange(tam)])




