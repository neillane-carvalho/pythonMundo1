import math

angulo = float(input('Digite um angulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O angulo {} tem o SENO de {:.2f}'.format(angulo,sen))
print('O angulo {} tem o COSSENO de {:.2f}'.format(angulo,cos))
print('O angulo {} tem a TANGENTE de {:.2f}'.format(angulo,tan))