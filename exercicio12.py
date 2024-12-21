valor = float(input('Qual é o preço do produto? R$'))
percentual = 5
desconto = valor - (percentual / 100) * valor
print('O produto que custava R${}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(valor, percentual, desconto))