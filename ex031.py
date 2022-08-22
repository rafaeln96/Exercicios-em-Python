d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(d))
if d <= 200:
    p = d * 0.50
    print('O preço de sua viagem será de: R${:.2f}'.format(p))
else:
    p = d * 0.45
    print('O valor de sua viagem será de: R${:.2f}'.format(p))
