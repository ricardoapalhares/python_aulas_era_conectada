#Aulas Dicionários

livro = {'autor': 'Ze', 'titulo': 'Aventuras de Programação', 'paginas': 300}
print(livro)

livro2 = {'autor': 'Joao', 'titulo': 'Java para Iniciantes', 'paginas': 10000}
print(livro2)

biblioteca = {'livros': [livro, livro2], 'endereco': 'Praça XV'}
print(biblioteca)

print("livros: ", biblioteca['livros'])
print("endereço", biblioteca['endereco'])
print("autor:", biblioteca['livros'])

biblioteca['livros'].append({'autor': 'Maira', 'titulo': 'Python fluente', 'paginas': 600})
print(biblioteca)

livro['data_lancamento'] = '22/10/2018'
print(livro)

print("autor:", biblioteca['livros'])

for x in livro:
	print('chaves', x)

for x in livro.keys():
	print('keys', x)

for x in livro.values():
	print('valor', x)

print(sorted(livro))

print(biblioteca['endereco'])

print("Pagina esta contido no livro: ",'paginas' in livro)

#print(biblioteca['livros']['autor'])

print(livro.keys())

print(livro.items())