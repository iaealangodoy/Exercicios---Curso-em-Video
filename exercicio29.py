velocidade = float(input('Qual é a velocidade atual do carro? '))
limite = 80
if velocidade > limite:
    multa = (velocidade - limite)*7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')