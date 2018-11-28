#Exercicio 1
#Faça um programa que leia duas strings e informe o conteúdo delas seguido do seu comprimento.
#Exercício1
#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

#Ex.
#String 1: Brasil Hexa 2006
#String 2: Brasil! Hexa 2006!
#Tamanho de 'Brasil Hexa 2006': 16 caracteres
#Tamanho de 'Brasil! Hexa 2006!': 18 caracteres
#As duas strings são de tamanhos diferentes
#As duas strings possuem conteúdo diferente

string1 = input("Digite a string1: ")
string2 = input("Digite a string2: ")

print("Tamanho de ", string1, len(string1))
print("Tamanho de ", string2, len(string2))

if len(string1) == len(string2):
	print("As duas strings são de tamanhos iguais")
else:
	print("As duas strings são de tamanhos diferentes")

if string1 == string2:
	print("As duas strings tem conteúdos iguais")
else:
	print("As duas strings tem conteúdos diferentes")
