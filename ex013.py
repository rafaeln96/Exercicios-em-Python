n = input('Informe o seu nome: ')
print('Olá, {}!' .format(n))
s = float(input('Informe o seu salário: R$'))
s1 = s * 15 / 100
print('O seu novo salário com o reajuste de 15% será: R$ {:.2f}' .format(s1+s))
print('O valor ajustado foi de: R${:.2f}' .format(s1))
