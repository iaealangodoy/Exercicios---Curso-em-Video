nome = str(input('Digite seu nome completo: '))
pn = nome.split()
nse = nome.replace(' ', '')
print('Analisando seu nome... \nSeu nome em maiúsculas é {} \nSeu nome em minúsculas é {} \nSeu nome tem ao todo {} letras \nSeu primeiro nome é {} e ele tem {} letras' .format(nome.upper(),nome.lower(),len(nse),pn[0],len(pn[0])))