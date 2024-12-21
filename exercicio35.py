print('\033[1;46m-=\033[m' * 30)
print('\033[4;43mAnalisador de Triângulos\033[m')
print('\033[1;46m-=\033[m' * 30)
r1 = float(input('\033[7;40mPrimeiro segmento: \033[m'))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')