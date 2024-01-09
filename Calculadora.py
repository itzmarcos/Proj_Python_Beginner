num1 = int(input('Digite um numero: '))
print('''FORMA DE CALCULAR
 [ 1 ] Soma
 [ 2 ] Subtraçao
 [ 3 ] Divisao
 [ 4 ] Multiplicação''')
opção = int(input('Qual opção: '))
if opção == 1:
    num2 = int(input('Digite um numero: '))
    print(f'{num1} + {num2} = {num1+num2}')
elif opção == 2:
    num2 = int(input('Digite um numero: '))
    print(f'{num1} - {num2} = {num1 - num2}')
elif opção == 3:
    num2 = int(input('Digite um numero: '))
    print(f'{num1} / {num2} = {num1 // num2}')
elif opção == 4:
    num2 = int(input('Digite um numero: '))
    print(f'{num1} * {num2} = {num1 * num2}')