print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} » '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    print('-=' * 10)
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('-=' * 10)
print('Progressão finalizada com {} termos mostrados.'.format(total))
