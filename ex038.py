v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))
if v1 > v2:
    print('O número {} é maior que {}'.format(v1, v2))
elif v1 < v2:
    print('O número {} é menor que {}'.format(v1, v2))
else:
    print('O número {} é igual ao {}'.format(v1, v2))
