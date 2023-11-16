# estruturas condicionais

media = float(input('Insira a sua nota: '))

if media >= 70:
    print('Aprovad@!')
elif media >= 50:
    print('Recuperação.')
else:
    print('Reprovad@!')

# Não existe "else if" no Python, apenas "elif".
# condicional "e" = and
# condicional "ou" = or