#Exercício2

#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

#Ex.
#Data de Nascimento: 29/10/1973
#Você nasceu em 29 de Outubro de 1973

dtNascimento = input("Digite a sua data de nascimento: ")
meses = {"01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril", "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto", "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"}

#split
dia, mes, ano = dtNascimento.split("/")
#imprimir usando format
print('Você nasceu em {dia} de {mes} de {ano}'.format(dia=dia,mes=meses[mes],ano=ano))
