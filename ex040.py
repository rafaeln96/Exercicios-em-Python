n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe a sua segunda nota: '))
media = (n1 + n2) / 2
print('A sua media foi {}:'.format(media))
if media >= 7.0:
    print('APROVADO')
elif media < 5.0:
    print('REPROVADO')
elif media <= 6.9 or 5.0:
    print('RECUPERAÇÃO')
