quant = 0
n = int(input('Digite um valor: '))
for c in range (1, n + 1):
    if  n % c == 0:
        print(c)
        quant += 1
if quant == 2:
    print(f'Esse numero foi dividido {quant} vezes por isso ele é primo.')
else:
    print(f'Esse foi dividido {quant} vezes por isso não primo.')
