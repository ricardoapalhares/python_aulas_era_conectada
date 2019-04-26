import csv
import sqlite3
import xlrd

import pandas as pd


workbook = xlrd.open_workbook("IMR_mortality_rate_2018.xlsx")
sheet = workbook.sheet_by_index(0)

lista = []

for row in range(12, sheet.nrow-5,s):
    lista.append(sheet.row_values(row))
cols = sheet.row_values(11)

df = pd.DataFrame(data=lista, columns=cols)
csv_file = df.to_csv('data.csv')

list_columns = df.columns.to_list()
list_columns.insert(0, 'id')

con = sqlite3.connect('db.sqlite')
cur = con.cursor()
cur.execute('CREATE TABLE morality ({})')
with open ('data.csv', 'rb'):


#with open('data.csv', 'w+') as file:
#    file.write(csv_file)
    #print(df)

#list_columns = df.columns.to_list()
#con
#bur
#converter quem stava 