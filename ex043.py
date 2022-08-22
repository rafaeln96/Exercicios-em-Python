kg = float(input('Qual é o seu peso? (Kg) '))
al = float(input('Qual é a sua altura? (m) '))
IMC = kg / (al ** 2)
print('O seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do Peso!')
elif IMC <= 25 and 18.5:
    print('Peso ideal!')
elif IMC <= 30 and 25:
    print('Sobrepeso')
elif IMC <= 40 and 30:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade mórbida')
