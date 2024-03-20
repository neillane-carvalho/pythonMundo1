# if - else simplificado
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite o segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi {:.1f}'.format(media))
print('O aluno foi aprovado' if media >= 7 else 'O aluno foi reprovado')
