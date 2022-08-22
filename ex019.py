from random import choice
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
al = [a1, a2, a3, a4]
s = choice(al)
print('-' * 45)
print('Os alunos listados são: {}, {}, {}, {}'.format(a1, a2, a3, a4))
print('-' * 45)
print('O aluno que apagará o quadro é o(a): {}'.format(s))
