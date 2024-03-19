# Análise
frase = 'Curso em Video Python'
print(len(frase))  # mostra quanto caracteres tem a string
print(frase.count('o'))  # conta quantas letras 'o' tem na string
print(frase.count('o', 0, 14))  # conta quantas letras 'o' tem de 0 a 13
print(frase.find('deo'))  # encontra 'deo' e mostra em que posição começa
print(frase.find('android'))  # quando a string não existe retorna o valor -1
print('em' in frase)  #identifica se tem na str
