import ast
import csv
import sqlite3
import xlrd

import pandas as pd

workbook = xlrd.open_workbook("input/infopreco-24-4-2019.xlsx")
sheet = workbook.sheet_by_index(0)

lista = []

for row in range(6, sheet.nrows):
    lista.append(sheet.row_values(row))
cols = sheet.row_values(5)

df = pd.DataFrame(data=lista, columns=cols)
df.to_csv('data.csv', encoding = "ISO-8859-1", sep=';', date_format='%d-%m-%Y-%H-%M-%S',float_format='%.4f')

list_columns = df.columns.to_list()
list_columns.insert(0, 'id')

for index, x in enumerate(list_columns):
    list_columns[index] = str(x)

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute("CREATE TABLE combustivel {}".format(tuple(list_columns)))
#print(tuple(list_columns))

#with open('data.csv','rb') as data:
#    lines = data.readlines()
#    print(lines)
#    for line in lines[1:]:
#        line = str(line).split(';')
        #line = str(line).replace('n', '').replace('\\','').replace('r','').replace('\"','').replace('b''', '').replace('[\'"','[')
        #line = str(line).replace('n', '').replace('\\','').replace('r','').replace('\"b','').replace('\"',"'").replace("''","'").replace(", ',",", '',")
#        line = str(line)        
        #print(line)
        #cur.execute("INSERT INTO combustivel VALUES {};".format(tuple(line)))
csvFile = open('data.csv', encoding='cp437')
#with open('data.csv', 'r') as csvFile:
reader = csv.reader(csvFile)
count = 0
for row in reader:
    if count != 0:
        print(row)
        line = str(row).split(';')
        #line = str(line).replace('[').replace(']')
        cur.execute("INSERT INTO combustivel VALUES {};".format(tuple(line)))
    count = count + 1 

csvFile.close()

con.commit()
con.close()
