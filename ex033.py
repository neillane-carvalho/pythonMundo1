salario = float(input('Digite o seu salário: R$'))
if salario > 1250:
    aumento = salario + (salario * 0.10)
    print('O seu aumento foi de R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print('Seu aumento foi de R${:.2f}'.format(aumento))
