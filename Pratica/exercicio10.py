import random
alunos = ['Arthur', 'Jorge', 'JonJon', 'Barros', 'Levy', 'Yaslly', 'Laís',
 'Leo', 'Evandro', 'Pedro', 'Aldenor', 'Livia']
notas = []
for x in range(0,12):
  notas.append(random.randint(0,11))
zipados = list(zip(alunos,notas))
for x in (zipados):
  print(f'A nota do aluno {x[0]} foi {x[1]}')