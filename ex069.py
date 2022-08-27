print('-' * 30)
print('     CADASTRE UMA PESSOA')
print('-' * 30)
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-' * 30)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18} pessoa(s)')
print(f'Ao todo temos {totH} homem(ens) cadastrado(s)')
print(f'E temos {totM20} mulher(es) com menos de 20 anos')
