from math import hypot
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hi = hypot(co, ca)
print('O comprimeiro da hipotenusa é: {:.2f}'.format(hi))
