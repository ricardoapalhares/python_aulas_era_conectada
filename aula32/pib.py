import ast
import numpy as np
import pandas as pd

file = open('/home/dados_brasil.csv', 'r')
lines = file.readLines()

for line in lines:
    if 'Aumento do PIB' in line:
        pib_list = list(ast.literal_eval(line)[4:])
    elif 'Country Code' in line:
        years = list(ast.literal_eval(line)[4:])

for index, value = enumerate(years):
    years[index] = int(value)

print (pib_list)

for index, value in enumerate(pib_list):
    if value == '':
        pib_list[index] = None
    else: 
        pib_list[index] = float(value)

file.close()

df = pd.DataFrame(data=pib_list)
print(df)
