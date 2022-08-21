from asyncore import read
from functools import reduce


def tirarespaço(lista,lista1):
    for x in lista:
        if x != '':
            lista1.append(x)
#Função para transformar Bytes em MegaBytes
def BparaMB(tamanho):
    return tamanho/pow(2,20)

#Abrindo o .txt e alocando em uma variavel
with open('usuarios.txt', 'r') as d:
    data = d.read()

#Manipulando o arquivo
lst = (data.split('\n'))
lst1 = []
for x in lst:
    lst1.append(x.split(' '))
lst2 = []

#Retirando os espaços em brancos
for i in range(0,6):
    tirarespaço(lst1[i],lst2)

#Guardando o usuario e o espaço utilizado 
# em uma lista dentro de uma lista composta
lst_aux = []
lst_linha = []
for i in range(0,12,2):
    lst_aux.append(lst2[i])
    lst_aux.append(lst2[i+1])
    lst_linha.append(lst_aux[:])
    lst_aux.clear()

#Transformando os números de strings para 
# inteiros, aplicando a função BparaMB e
# alocando em uma lista  
lst_mb = []
for x in lst_linha:
    lst_mb.append(BparaMB(int(x[1])))

#Alocando os nomes em uma lista
lst_nome = []
for x in lst_linha:
    lst_nome.append(x[0])

#Somando todos os MegaBytes utilizados
somadorMB = reduce(lambda x,y: x+y, lst_mb)

#Transformando em porcentagem
porcent = []
for x in range(0,6):
    porcent.append((lst_mb[x]/somadorMB)*100)

#Criando a tabela
demonstracao = list(zip(lst_nome,lst_mb))
print(f'{"ACME Inc.":<20} Uso do espaço em disco pelos usuários')
print('-'*55)
print(f'{"Nr.":<5}{"Usuário":<15}{"Espaco utilizado":<15}{"% do uso":>15}')
print()
for y,x in enumerate(demonstracao):
    print(f'{y+1:<5}{x[0]:<15} {x[1]:>8.2f} MB  {porcent[y]:>15.2f}')
print(f'\nEspaco total ocupado: {somadorMB:.2f} MB\nEspaco medio utilizado: {somadorMB/6:.2f} MB')