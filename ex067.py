while True:
    v = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if v < 0:
        print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
        break
    for t in range(1, 11):
        print(f'{v} x {t:2} = {v * t}')
    print('-' * 20)
