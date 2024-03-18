import math

c1 = (float(input('Digite o comprimento do cateto oposto: ')))
c2 = (float(input('Digite o comprimento do cateto adjacente: ')))
hipotenusa = math.hypot(c1, c2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))