import csv
import sqlite3
import xlrd
from datetime import datetime,date
import pandas as pd

from geopy.geocoders import Nominatim

workbook = xlrd.open_workbook("input/infopreco-24-4-2019.xlsx")
sheet = workbook.sheet_by_index(0)

lista = []

for row in range(6, sheet.nrows):
    lista.append(sheet.row_values(row))
cols = sheet.row_values(5)

df = pd.DataFrame(data=lista, columns=cols)
df.to_csv('data.csv', encoding = "ISO-8859-1", sep=';', date_format='%d-%m-%Y-%H-%M-%S',float_format='%.4f')

con = sqlite3.connect("db.sqlite3") ## these statements belong outside the loop
cursor = con.cursor()  ## execute them just once

first = True
with open ('data.csv', 'r', encoding='cp437') as f:
    reader = csv.reader(f, delimiter=';')
    columns = next(reader)
    columns.insert(1, 'id')
    columns.insert(13, 'LATITUDE')
    columns.insert(14, 'LONGITUDE')
    print(columns[1:])
    columns = [h.strip() for h in columns[1:]]
    if first:
        print(columns)
        sql = 'CREATE TABLE IF NOT EXISTS combustivel (%s)' % ', '.join(['%s text'%column for column in columns])
        sql = sql.replace('VALOR_VENDA text','VALOR_VENDA real')
        sql = sql.replace('DATA_CADASTRO text','DATA_CADASTRO datetime')
        
        print (sql)        
        #VALOR_VENDA text
        
        cursor.execute(sql)
        first = False
    # for row in reader:    ## we will read the rows later in the loop
    #    print(row)

    query = 'insert into combustivel({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    print(query)
    cursor = con.cursor()
    linha = 0
    for row in reader:
        numero = ''
        if row[4] != 'S/N':
            numero = row[4]
        endereco = row[3]+', ' + numero + ' ' + row[7] + ' ' + row[8]
        geolocator = Nominatim(user_agent="specify_your_app_name_here")
        #location = geolocator.geocode(endereco)

        #if location is None:
        row.insert(13,'')
        #else:
        #    row.insert(13,str(location.latitude))
        
        #if location is None:
        row.insert(14,'')
        #else:
        #    row.insert(14,str(location.longitude))
        valor = float(row[10])
        row[10] = valor

        date_str = row[11]
        day, month, year = map(int, date_str.split('/'))
        date_object = datetime(year, month, day)

        row[11] = date_object

        print(row)
        cursor.execute(query, row)
        linha = linha + 1
    con.commit()
    con.close()
