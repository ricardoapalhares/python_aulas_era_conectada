#list comprehensions

matriz = [[1, 2], [2, 4]]
print(matriz)

for index, valor in enumerate(matriz):
	for i, numero in enumerate(valor):
		matriz[index][i] = numero**2

matriz = [[value**2 for value in line] for line in matriz]
print(matriz)

squares = [x**2 for x in range(10)]
print(squares)

listaComprehensions = [1,2,3,4,5,6]
print(listaComprehensions)

#list comprehensions
print([value*10 if value > 3 else value**2 for value in listaComprehensions])

new_list = [i*10 for i in listaComprehensions if i > 3]
print(new_list)