# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
lista = [0, 1, 2, 3, 4]

lst1 = [x**2 for x in lista]
lst2 = [x**3 for x in lista]
lst = list(zip(lst1,lst2))
print(lst)