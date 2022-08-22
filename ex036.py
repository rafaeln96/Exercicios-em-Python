print('-=' * 15)
print('Financie a sua casa própria!')
print('-=' * 15)
valor = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos vai pagar?'))
vp = valor / (anos * 12)
ps = salario * 30 / 100
print('O valor das parcelas será de: R${:.2f}'.format(vp))
print('30 % do seu salário corresponde a: R${:.2f}'.format(ps))
if vp > ps:
    print('Financiamento não aprovado! O valor das parcelas não pode exceder 30% do seu salário!')
else:
    print('Seu financiamento foi APROVADO!')
