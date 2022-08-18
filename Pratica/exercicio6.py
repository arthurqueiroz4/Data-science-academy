# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)
def neg(x):
    if x < 0:
        return x
list(filter(neg, range(-5,5)))