al = input('Informe o nome do aluno: ')
n1 = float(input('Informe a nota do primeiro semestre do aluno {}: ' .format(al)))
n2 = float(input('Informe a nota do segundo semestre do aluno {}: ' .format(al)))
s = (n1+n2)/2
print('A media de {} é de: {}' .format(al, s))
