# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
lista = [3,5,6]
pot = list(map(lambda x:x**3,lista))
print(lista,"\n", pot)