# algumas funções básicas:

# print() imprime uma mensagem no console
# input() retorna um dado de entrada inserido pelo usuário
# len() recebe uma lista e retorna o tamanho dela
# max() retorna o maior valor de uma lista

# CRIAÇÃO DE FUNÇÃO

# função inicial
def saudacao1():
    nome = input('Qual é o seu nome? ')
    print(f'Olá, {nome}!')

saudacao1()


# função com parâmetros
def saudacao2(nome):
    print(f'Olá, {nome}!')

saudacao2('Dezzogo')

def saudacao3(nome, curso):
    print(f'Olá, {nome} que estuda {curso}!')

saudacao3(input('Qual é o seu nome? '), input('e o que vocẽ estuda? '))


#função com parâmetros default - o parâmetro recebe um valor pré-atribuído, que não precisa ser colocado na hora de chamar a função, mas pode ser alterado na hora de passar valor aos parâmetros.

def saudacao4(nome, curso='Engenharia'):
    print(f'Olá, {nome} que estuda {curso}!')

saudacao4('Dezzogo')


# função com retorno - é mais adequado usar return do que print ao criar funções. Além disso, o return faz a função parar de ser executada.

def soma(num1, num2):
    return num1 + num2
    print('este print não será executado')

resultado = soma(10, 11)
print (resultado)