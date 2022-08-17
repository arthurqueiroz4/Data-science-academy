# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def ind5(x):
    enum = list(enumerate(x))
    r = []
    for z in enum:
        if z[0] > 5:
            r.append(z[1])
    return r
enumerado = ind5(lista)
print('os elementos cujo índice for maior que 5: ',end='')
imprimir = [print(x,end=' ') for x in enumerado]