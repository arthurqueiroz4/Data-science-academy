# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = (list(map(lambda x:[x.upper(),x.lower(),len(x)], palavras)))
for i in resultado:
    print(i)