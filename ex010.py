print('Bem-vindo ao conversor de moedas!')
print('-' * 40)
a = float(input('Quantos reais você possui em sua carteira? R$'))
print('-' * 40)
print('A cotação atual do Dolar é de: $5.19')
print('A cotação atual do Euro é de: $5.33')
print('A cotação atual da Libra é de: $6.36')
print('A cotação atual do Iene é de: $0.040')
print('-' * 40)
d = a / 5.19
e = a / 5.33
lb = a / 6.36
ie = a / 0.040
print('Você terá em Dolar: ${:.2f}' .format(d))
print('Você terá em Euro: ${:.2f}' .format(e))
print('Você terá em Libra: ${:.2f}' .format(lb))
print('Você terá em Iene: ${:.2f}' .format(ie))
print('-' * 40)
