distancia = float(input('Digite a distancia da viagem em km: '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print('O valor da sua passagem é de R${:.2f}'.format(preco))
