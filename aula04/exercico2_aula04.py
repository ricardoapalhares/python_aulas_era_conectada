#Crie uma função conta digitos
#inteiro = n
#inteiro = 

n = input("Digite o valor de n: ")
d = input("Digite o valor de d [0 < d < 9]: ")

def qtdContem(n,d):
	cont = 0
	for digito in n:
		if digito == d:
			cont += 1

	return cont

print(qtdContem(n,d))


