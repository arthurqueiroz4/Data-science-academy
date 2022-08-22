import sqlite3
import os 

os.remove("faculdade.db") if os.path.exists("faculdade.db") else None

con = sqlite3.connect('faculdade.db')
cur = con.cursor()
sql_create = 'create table aulas (salas integer primary key, prof varchar(100), cadeira varchar(100))'
cur.execute(sql_create)

sql_insert = 'insert into aulas values (?, ?, ?)'
aulas = [
    (100, 'Daniel', 'Laboratorio de prog'),
    (101,'Edson','Algebra Linear'),
    (102,'Joao','Fisica')
]
for x in aulas:
    cur.execute(sql_insert, x)
con.commit()

sql_select = 'select * from aulas'
cur.execute(sql_select)
for x in cur.fetchall():
    print(f'SALA: {x[0]} \nPROF: {x[1]} \nDISC: {x[2]}')
    print('-'*20)
print('='*20)
aulas1 = [
    (103, 'Fabio', 'Fundamentos de prog'),
    (104,'Thiago','Ingles'),
    (105,'Joao Vitor','Redes neurais')
]

for x in aulas1:
    cur.execute(sql_insert, x)
con.commit()

sql_select = 'select * from aulas'
cur.execute(sql_select)
for x in cur.fetchall():
    print(f'SALA: {x[0]} \nPROF: {x[1]} \nDISC: {x[2]}')
    print('-'*20)