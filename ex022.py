num = int(input('Digite um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Analisando o número {}...'.format(num))
print('Sua unidade é {}'.format(unidade))
print('Sua dezena é {}'.format(dezena))
print('Sua centena é {}'.format(centena))
print('Sua milhar é {}'.format(milhar))
