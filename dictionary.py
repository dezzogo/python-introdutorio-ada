# DICIONÁRIOS

# Criando dicionário - usa-se chaves

dicionario = {}
dicionario = dict()

dicionario = {'name': 'Dezzogo', 'country': 'Brazil', 'language':'Python', 'number': 42}

# é bem mais fácil acessar os elementos do dicionário:
print(dicionario['language'])

# adicionar elementos ao dicionário

dicionario['programador'] = True
dicionario['number'] = 10
# se um conteúdo não existe, ele é adicionado.
# se o conteúdo já existe, o novo sobrescreve.
print(dicionario)

# iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])
#neste exemplo, cada índice "chave" é printado com o seu valor.

# testando a existência de uma chave

print('peso' in dicionario)
print('programador' in dicionario)