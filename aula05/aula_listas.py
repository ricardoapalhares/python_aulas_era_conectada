#Operacoes com lista.
#página com documentacao: https://docs.python.org/3/tutorial/datastructures.html

#***********************************************************************************************
# Aula parte I

# lista = [1,2,3,4,5,6,7,8,9,10]
# print("Minha lista: ", lista)
# print("Tamanho da lista: ", len(lista))
# print("Menor item da lista: ", min(lista))
# print("Maximo item da lista: ", max(lista))

# del lista[0]
# print("Minha lista: ", lista)

# lista_com_range = range(0,10)
# print("range posicao ultima posicao: ", lista_com_range[-1])
# print("imprimindo lista: ", list(lista_com_range))

# ll = list("Ricardo")
# print("Criando lista por nome", ll)

# print(ll.pop())

#***********************************************************************************************
# Aula parte II

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista.append(5)
print(lista)

lista.insert(0,10)
print(lista)

for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

print("Elemento esta na lista: ", 3 in lista)

#Remove pelo indice
del lista[0]

#Remove pelo valor da lista
lista.remove(4)
print(lista)

#limpar listar
#lista.clear()
#print(lista)

lista.append(4)
#Saber quantas vezes o numero 4 apareceu

print("O numero 4 aparece: ", lista.count(4), " vez(es)")

#Ordenar a lista
lista.sort()

#Ordenar inversamente
lista.sort(reverse=True)
print(lista)

print("O numero 2 esta no indice: ", lista.index(2,0))

lista.reverse()
print("Lista invertida: ", lista)

print("Lista a partir do indice 3 ", lista[3:])

print("Lista a partir do indice 3 a 6 ", lista[3:6])

print("Lista a partir de tres em tres ", lista[::3])

print("Lista ate o penultimo elemento ", lista[:-2])

lista1 = [1,2,3,4,5]
lista2 = [100,220,330]
lista3 = lista1[:3] + lista2
print(lista3)

lista3.insert(0,[10,100,1000])
lista3[0].append([1,2,3])

print("Nova lista dentro de outra lista", lista3)
print("Achando posicao dentro de uma lista dentro da outra: ", lista3[0][3][1])

#***********************************************************************************************
