frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('a') + 1))
