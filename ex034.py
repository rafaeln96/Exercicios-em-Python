salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    valor = salario + (salario * 15 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, valor))
else:
    valor2 = salario + (salario * 10 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, valor2))
