salario = float(input('Qual é o salário do funcionário? R$ '))
percentual = 15
novosalario = salario + (percentual / 100) * salario
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salario, percentual, novosalario))