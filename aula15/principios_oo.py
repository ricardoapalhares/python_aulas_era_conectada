class Carro:
	def __init__(self, cor, modelo):
		self.cor = cor
		self.modelo = modelo

	def run(self):
		print("Go go go!!! RRRNNNN")

carro = Carro(cor='preto', modelo='fusca 79')

carro.run()

print(carro.cor)