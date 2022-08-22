from random import randint
from time import sleep
computador = randint(0, 5)#Faz o computador "PENSAR" (randomizando a escolha!)
print('-=-' * 22)
print('Bem-vindo! Espero que consiga decsobrir o número no qual vou pensar!')
print('-=-' * 22)
print('PENSANDO...')
print('Ah! Tem que ser entre 0 e 5, ok?')
print('-=-' * 45)
sleep(2)
jogador = int(input('Em que número eu pensei? '))#Jogador tenta adivinhar!
if jogador == computador:
    print('Você acertou o número no qual eu pensei, PARABÉNS!')
else: 
    print('GANHEI!!! pensei no número {} e não no {}, TENTE NOVAMENTE!'.format(computador, jogador))
print('-=-FIM-=-')
