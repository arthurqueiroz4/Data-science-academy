import numpy as np

#Criando um vetor com np
vetor = np.array([1,2,3,4,5,6])
print(vetor)

#Somando todos os elementos do vetores
print(vetor.cumsum())

#Mostrando o primeiro e ultimo elemento do vetor
print(vetor[0], vetor[(vetor.size - 1)])

#Alterando elementos do vetor
vetor[0] = 6
vetor[vetor.size - 1] = 1
print(vetor[0], vetor[(vetor.size - 1)])

#Retornar o formato do vetor
print(vetor.shape)
#unidimensional

#Criando uma matriz identidade
vetor1 = np.eye(3)
print(vetor1)

#Criando matriz com zeros
vetor2 = np.zeros(8)
print(vetor2)

#Criando matriz com uns
vetor3 = np.ones(8)
print(vetor3)