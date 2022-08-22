p = float(input('Qual é o preço do produto? R$'))
d = p - (p * 5 / 100)
print('O produto que custava {:.2f}, na promoção de 5% vai custar {:.2f}' .format(p, d))
