largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem {} m² e precisa de {} litros de tinta.'.format(area, tinta))
