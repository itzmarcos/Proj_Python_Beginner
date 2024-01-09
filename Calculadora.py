import time

print('''FORMAS DE PAGAMENTOS
 [ 1 ] Soma
 [ 2 ] Multiplicação
 [ 3 ] Divisao
 [ 4 ] Subtraçao''')
opção = (input('Qual opção: '))
time.sleep(1)
if opção == 1:
    n = int(input('Digite um numero: '))
    for c in range(0, 10):
        print('{} + {} = {}'.format(n, c, n+c))
elif opção == 2:
    n = int(input('Digite um numero: '))
    for c in range(0, 10):
        print('{} * {} = {}'.format(n, c, n*c))
