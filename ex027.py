from random import randint

print('O computar está pensando em um número entre 0 e 5')
num = randint(0, 5)
jogador = int(input('Tente adivinhar qual número eu pensei? '))
print('PROCESSANDO...')
if jogador == num:
    print('Parabens! Voce conseguiu me vencer!')
else:
    print('Que pena, eu pensei no numero {}'.format(num))
