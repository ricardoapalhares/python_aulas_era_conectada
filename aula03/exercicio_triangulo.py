#equilatero = todos iguais
#Isóceles = dois lados iguais e um diferente
#escaleno = todos diferentes

#Qual o tipo do Triângulo?
#A soma das medidas de dois lados de um triângulo é maior que a medida do terceiro lado

medida1 = input("Digite a primeira medida: ")
medida2 = input("Digite a segunda medida: ")
medida3 = input("Digite a terceira medida: ")

x = int(medida1)
y = int(medida2)
z = int(medida3)

if (x+y)<z or (x+z)<y or (y+z)<x:
	print("As medidas Medida 1, Medida 2 e Medida 3 não formam um triângulo.")
elif x == y and x == z:
	print("As medidas Medida 1, Medida 2 e Medida 3 formam um triângulo Equilátero.")
elif (x == y and x != z) or (x == z and x != y) or (y == z and x != y):
	print("As medidas Medida 1, Medida 2 e Medida 3 formam um triângulo Isósceles.")
elif x != y and y != z:
	print ("As medidas Medida 1, Medida 2 e Medida 3 formam um triângulo Escaleno.")

