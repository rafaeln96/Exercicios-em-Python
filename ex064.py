num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: ')) #Gambiarra lendo o comando duas vezes!!!
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
