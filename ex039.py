from datetime import date
print('=-' * 10)
print('ALISTAMENTO MILITAR OBRIGATÓRIO:')
print('=-' * 10)
print('''Informe o seu sexo
[ 1 ] Homem
[ 2 ] Mulher''')
opcao = int(input('Escolha sua opção: '))
if opcao == 1:
    print('=-' * 10)
    print('Vamos inciar a verificação do seu alistamento!')
    print('=-' * 10)
else:
    print('Infelizmente não alistamos mulher de forma obrigatória!'), exit()
an = int(input('Informe o seu ano de nascimento: '))
ano = date.today().year
idade = ano - an
print('=-' * 10)
print('Você nasceu em {} e a sua idade é {:.0f} anos no ano de {}'.format(an, idade, ano))
if idade > 18:
    print('O seu período de alistamento já passou em {} anos'.format(idade - 18))
elif idade == 18:
    print('OPA!!! Está na hora de se ALISTAR no exército!')
else:
    print('Ainda faltam(a) {} anos para o seu alistamento!'.format(18 - idade))
