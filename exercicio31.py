distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia))
valor = distancia*0.50 if distancia <= 200 else distancia*0.45
'''if distancia <= 200:
    valor = distancia*0.50
else:
    valor = distancia*0.45'''
print('E o preço da sua passagem será de R${:.2f}'.format(valor))