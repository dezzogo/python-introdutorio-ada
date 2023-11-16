# a função range suporta 1, 2 ou 3 parâmetros

# com um, ele vai de zero até o número anterior ao parâmetro
print('For com range de 1 parâmetro')
for index in range(10):
    print(index)

#com dois, ele vai do primeiro até o número anterior ao segundo parâmetro
print('For com range de 2 parâmetros')
for index in range(1, 11):
    print(index)

#com 3, o primeiro é o de início, o segundo é o de parada, e o terceiro é o step, de quanto em quanto ele conta
print('For com range de 3 parâmetros')
for index in range(30, 45, 3):
    print(index)


# cálculo de nota
soma = 0

for i in range(1, 4):
    nota = float(input(f'Digite a sua nota {i}: '))
    soma = soma + nota

print('Sua nota é:', soma // i)

# é usado "f" antes da primeira aspa em uma string se for concatenar com uma variável, que ficará entre {} na string.