km = float(input('Quantos Km foram rodados? '))
dias = int(input('Quantos dias alugados? '))
valor = (dias * 60) + (km * 0*15)
print('O valor total a pagar é de R${:.2f}'.format(valor))