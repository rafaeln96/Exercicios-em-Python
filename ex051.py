print('=' * 40)
print('         10 TERMOS DE UMA PA')
print('=' * 40)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
dc = pt + (10 - 1) * rz
for p in range(pt, dc + rz, rz):
    print('{}'.format(p), end=' → ')
print('ACABOU')
