'''chave = input('Digite a senha: ')

senha = " "
for letra in chave:
    if letra in "Aa": senha = senha + "1"
    elif letra in "Ba": senha = senha + "@"
    elif letra in "Cc": senha = senha + "2"
    elif letra in "Dd": senha = senha + "3"
    elif letra in "Ee": senha = senha + "#"
    else:
        senha = senha + letra

print(senha)'''

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']
r = 3
senha = input('Digite uma senha de 6 digito: ')
#print(alfabeto.index(senha[0]))

d0 = (alfabeto.index(senha[0]) + r) % len(alfabeto)
d1 = (alfabeto.index(senha[1]) + r) % len(alfabeto)
d2 = (alfabeto.index(senha[2]) + r) % len(alfabeto)
d3 = (alfabeto.index(senha[3]) + r) % len(alfabeto)
d4 = (alfabeto.index(senha[4]) + r) % len(alfabeto)
d5 = (alfabeto.index(senha[5]) + r) % len(alfabeto)

senha_c=(alfabeto[d0] + alfabeto[d1] + alfabeto[d2] + alfabeto[d3] + alfabeto[d4] + alfabeto[d5])
print(senha_c)

d0 = (alfabeto.index(senha_c[0]) - r) % len(alfabeto)
d1 = (alfabeto.index(senha_c[1]) - r) % len(alfabeto)
d2 = (alfabeto.index(senha_c[2]) - r) % len(alfabeto)
d3 = (alfabeto.index(senha_c[3]) - r) % len(alfabeto)
d4 = (alfabeto.index(senha_c[4]) - r) % len(alfabeto)
d5 = (alfabeto.index(senha_c[5]) - r) % len(alfabeto)


senha_d=(alfabeto[d0] + alfabeto[d1] + alfabeto[d2] + alfabeto[d3] + alfabeto[d4] + alfabeto[d5])
print(senha_d)




#i = alfabeto.index('a')
#i_c = (i + r) % len(alfabeto)
#i_d = (i - r) % len(alfabeto)
