print('-' * 30)
print('{:^30}'.format(' LOJA SUPER BARATÃO '))
print('-' * 30)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        print('-' * 30)
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$ 1000.00 ')
print(f'O produto mais barato foi: {barato} que custa {menor:.2f}')
