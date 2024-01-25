print('Vamos calcular seu IMC!')
peso = float(input('Digite sua peso: '))
altura = float(input('Digite seu altura: '))
imc = peso / (altura) ** 2

print(f'Seu IMC é {imc:.2f}')