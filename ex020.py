from random import shuffle
a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')
r = [a1, a2, a3, a4]
shuffle(r)
print('-' * 45)
print('A ordem de apresentação do trablaho será: {}'.format(r))
