velocidade = float(input('Digite a velocidade do seu carro: '))
if velocidade > 80:
    print('MULTADO!')
    multa = (velocidade * 7.0)
    print('O valor da multa é de R${:.2f}'.format(multa))
