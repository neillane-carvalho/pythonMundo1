# if - else
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite o segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Aprovado!')
    print('A sua média foi {:.1f}'.format(media))
else:
    print('Reprovado!')
    print('A sua média foi {:.1f}'.format(media))
