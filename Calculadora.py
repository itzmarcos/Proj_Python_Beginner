num1 = int(input('Digite um numero: '))
print('''FORMA DE CALCULAR
 [ 1 ] Soma
 [ 2 ] Subtraçao
 [ 3 ] Divisao
 [ 4 ] Multiplicação''')
opção = int(input('Qual opção: '))
while True:
    num2 = int(input('Digite um numero: '))
    resp = " "
    if opção == 1:
        print(f'{num1} + {num2} = {num1+num2}')
    elif opção == 2:
        print(f'{num1} - {num2} = {num1 - num2}')
    elif opção == 3:
        print(f'{num1} / {num2} = {num1 // num2}')
    elif opção == 4:
        num2 = int(input('Digite um numero: '))
        print(f'{num1} * {num2} = {num1 * num2}')
    while resp not in "SN":
            resp = str(input('Pode afetuar o calculo? ')).upper()
    if resp == "S":
            break