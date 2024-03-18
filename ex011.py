preco = float(input('Digite o valor do produto: R$'))
desconto = preco - (preco * 0.05)
print('O produto que custava R${:.2f} com 5% de desconto vai custar R${:.2f}'.format(preco, desconto))