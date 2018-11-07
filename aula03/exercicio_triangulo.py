#equilatero = todos iguais
#Isóceles = dois lados iguais e um diferente
#escaleno = todos diferentes

#Qual o tipo do Triângulo?
#A soma das medidas de dois lados de um triângulo é maior que a medida do terceiro lado

lado1 = input("Digite o primeiro lado: ")
lado2 = input("Digite o segundo lado: ")
lado3 = input("Digite o terceiro lado: ")

x = int(lado1)
y = int(lado2)
z = int(lado3)

if (x+y)>z or (x+z)>y or (y+z)>x:
	print("Não é um triângulo")
elif x == y and x == z:
	print("É um triângulo Equilátero")
elif (x == y and x != z) or (x == z and x != y):
	print("É um triângulo Isósceles")
elif x != y and y != z:
	print ("É um triângulo Escaleno")

# int(lado1) + int(lado2) > int(lado3)
# 	print("Não é um triângulo")
# elif int(lado1) + int(lado3) > int(lado2)
# 	print("Não é um triângulo")
# elif int(lado2) + int(lado3) > int(lado1)
# 	print("Não é um triângulo")