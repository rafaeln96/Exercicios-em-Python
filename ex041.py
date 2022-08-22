from datetime import date
an = int(input('Informe o seu ano de nascimento: '))
ano = date.today().year
idade = ano - an
print('Você tem {} anos e pertence a categoria:'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')
