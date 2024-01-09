from random import randint
import time


print('Vamos jogar? lets go!')
time.sleep(1)
jogador = (int(input('Escolha um numero: ')))
computador = randint(1,5)
print(f'O computador escolheu {computador} e você {jogador}')
if computador == jogador:
        print('Você acertou!')
elif computador > jogador:
        print('Você errou!')
elif computador < jogador:
        print('Você errou!')