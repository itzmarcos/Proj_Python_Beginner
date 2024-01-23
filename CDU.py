import time
print('CONVERTENDO KM EM OUTRAS UNIDADE DE DISTANCIA!')
time.sleep(2)
numero = int(input('Digite um valor: '))

metro = numero*1000
cm = numero*100000
mm = numero*1000000

print(f'O valor de {numero}KM tem {metro}m, {cm}cm, {mm}mm')

