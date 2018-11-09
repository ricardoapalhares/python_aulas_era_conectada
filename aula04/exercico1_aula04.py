#Crie uma função que receba três valores, 'a','b','c'
#Delta = b2 - 4ac

a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")
c = input("Digite o valor de c: ")

def expressao(a,b,c):
	return b**2 - 4 * a * c

print (expressao(int(a),int(b),int(c)))

