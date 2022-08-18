# Exercício 8 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}
def troca(d1, d2):
    dic = {}
    #para chave1 e valor 2 em um zip que contem as chaves do d1 e os valores do d2
    for k1,v2 in zip(d1,d2.values()):
        dic[k1] = v2 #novo dicionario com as chaves de d1 e os valores de d2
    return dic
dic3 = troca(dict1,dict2)
print(dic3)