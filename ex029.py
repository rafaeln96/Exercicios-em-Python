v1 = float(input('Qual é a velocidade atual do carro?: '))
m = (v1 - 80) * 7
if v1 >= 80:
    print('MULTADO! você excedeu o limite de velocidade em: {}km/h'.format(v1 - 80))
    print('O valor a ser pago é de: R${:.2f}'.format(m))
else:
    print('Parabéns, você está na velocidade correta da via!')
