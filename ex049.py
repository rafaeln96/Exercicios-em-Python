n = int(input('Informe um número para a tabuada: '))
print('=-' * 6)
for t in range(1, 11):
    print('{} x {:2} = {}'.format(n, t, n*t))
print('=-' * 6)
