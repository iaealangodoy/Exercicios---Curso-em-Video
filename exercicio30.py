numero = str(input('Me diga um número qualquer ')).strip()
final = numero[:-1]
if final in '02468':
    print("par")
else:
    print('impar')