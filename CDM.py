resp = 'N'
soma = quant = media = 0

while resp in 'Nn':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    resp = str(input('Deseja efetuar a media? [S/N]').upper())
media = soma / quant
print(f'A media foi {media}')