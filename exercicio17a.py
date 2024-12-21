from math import sqrt
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = sqrt(oposto**2 + adjacente**2)
print('A Hipotenusa vai medir {:.2f}' .format(hipotenusa))