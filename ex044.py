print(f'{" VAREJÃO ":=^40}')
produto = float(input('Preço das compras: R$'))
print('=-' * 20)
print('FORMAS DE PAGAMENTO:')
print('=-' * 20)
print('''[ 1 ] À vista: Dinheiro ou Cheque com 10% de desconto
[ 2 ] À vista: No cartão com 5% de desconto
[ 3 ] Em até 2x no cartão com preço normal
[ 4 ] 3x ou mais no cartão com 20% de Juros''')
print('=-' * 20)
opcao = int(input('Escolha uma opção de pagamento: '))
if opcao == 1:
    total = produto - (produto * 10 / 100)
elif opcao == 2:
    total = produto - (produto * 5 / 100)
elif opcao == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = produto + (produto * 20 / 100)
    totpar = int(input('Quantas parcelas? '))
    parcela = total / totpar
    print('Sua compra parcelada em {}x vai custar R${:.2f} COM JUROS'.format(totpar, parcela))
else:
    total = produto
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(produto, total))
