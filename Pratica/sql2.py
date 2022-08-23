from asyncore import read
import sqlite3
import csv
import os

#Abrindo o arquivo csv e manipulando-o
with open('salarios.csv','r') as d:
    data = d.read()
linhas = data.split("\n")

total_dados = []
for x in linhas:
    total_dados.append(x.split(","))

del total_dados[0]
for x in total_dados:
    x[0].strip()
    x[1].strip()
    x[2].strip()
    x[3].strip()
    x[4].strip()
print(total_dados[1][0],'.')
os.remove('salarios.db') if os.path.exists('salarios.db') else None

conex = sqlite3.connect('salarios.db')
cursor = conex.cursor()

sql_create= 'create table salarios (sobrenome varchar(100),nome varchar(100), titulo varchar(100), departamento varchar(100), salario varchar(100))'
sql_insert= 'insert into salarios values (?, ?, ?, ?, ?)'
sql_select= 'select * from salarios'

cursor.execute(sql_create)
for x in total_dados:
    cursor.execute(sql_insert, x)
conex.commit()
print(f'{"NOME":^40}{"TITULO":^50}{"DEPARTAMENTO":^57}{"SALARIO":>17}')
cursor.execute(sql_select)
for x in cursor.fetchall():
    print(f'{x[0]}{x[1]:^50}{x[2]:<50}{x[3]:<50}{x[4]:<50}')