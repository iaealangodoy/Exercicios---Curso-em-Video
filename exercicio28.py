from random import randint
from time import sleep
n = randint(0,5)
print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)
num = int(input('Em que número eu pensei? '))
if num == n:
    print('PROCESSANDO...')
    sleep(3)
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('PROCESSANDO...')
    sleep(3)
    print('GANHEI! Eu pensei no número {} e não no {}' .format(n, num))