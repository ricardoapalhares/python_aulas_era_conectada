#Exercicio3
#Desenvolva um jogo da forca
#O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
#O jogador poderá errar 6 vezes antes de ser enforcado

#Ex.
#Digite uma letra: A
#Você errou pela 1a vez. Tente de novo! 
#Digite uma letra: O
#A palavra é: _ _ _ _ O
#Digite uma letra: U
#Você errou pela 2a vez. Tente de novo! 

import random

def ImprimeResultado(resultado):
	print("A palavra é: ", *resultado, sep=' ')

arquivo = open("palavras.txt", "r")
palavras = arquivo.readlines()
tam = len(palavras)

for index, palavra in enumerate(palavras):
	palavras[index] = palavra.replace('\n','')

palavraSorteada = list(palavras[random.randrange(tam)])
palavraOculta = []

for i in palavraSorteada:
	palavraOculta.append("_")  

ImprimeResultado(palavraOculta)

qtdPossivelDeErro = 7
i = 1
while i <= qtdPossivelDeErro:
	letraDigitada = input("Digite uma letra: ")
	if letraDigitada not in palavraSorteada:
		print("Você errou pela {i} ª vez. Tente de novo!".format(i = i))
		i += 1
	else:
		for indice, valor in enumerate(palavraSorteada):
			if valor == letraDigitada:
				palavraOculta[indice] = letraDigitada

		ImprimeResultado(palavraOculta)

	if "_" not in palavraOculta:
		print("Parabéns! Você ganhou")
		break

	if i == qtdPossivelDeErro:
		print("Você perdeu!")
		break
