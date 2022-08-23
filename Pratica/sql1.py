import sqlite3
import os

#Se o arquivo Cinema.db ja existir na maquina, ele sera removido.
os.remove("Cinema.db") if os.path.exists("Cinema.db") else None

#Variaveis que vou usar:
sql_create= 'create table filmes (id integer primary key, titulo varchar(100), sala integer, situacao varchar(10))'
sql_insert= 'insert into filmes values (?, ?, ?, ?)'
sql_select= 'select * from filmes'

#Criando o db Cinema e instanciei um cursor.
criador = sqlite3.connect("Cinema.db")
cursor1 = criador.cursor()

#Criando a tabela
cursor1.execute(sql_create)

filmes = [
    (1000, '45 do segundo tempo', 3, 'Em cartaz'),
    (1001, 'Dragonball Z ', 1, 'Em cartaz'),
    (1002, 'Superpets', 4, 'Em cartaz'),
    (1003, 'Elvis', 5, 'Em cartaz'),
    (1004, 'Thor', 6, 'Em cartaz'),
    (1005, 'Invocação do mal 4', 0, 'Em breve')
]
criador.commit()
filmesatualização =[
    (1006, 'O Telefone Preto', 7, 'Em cartaz'),
    (1007, 'Top Gun: Maverick',10, 'Em cartaz'),
    (1008, 'Papai é Pop',9, 'Em cartaz')
]

for x in filmesatualização:
    cursor1.execute(sql_insert, x)
criador.commit()
#Printar os elementos do db
for x in filmes:
    cursor1.execute(sql_insert, x)
cursor1.execute(sql_select)
for x in cursor1.fetchall():
    print('x='*20)
    print(f'  ID: {x[0]} / TÍTULO: {x[1] }\n  SALA: {x[2]} / SITUAÇÃO: {x[3]}')
    print('x='*20)
    print()

#O filme de id 1004 trocou de sala com o 1006.
