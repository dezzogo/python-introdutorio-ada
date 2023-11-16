#notas em lista

nota1 = 70
nota2 = 80
nota3 = 90
notas = [nota1, nota2, nota3, 100]

# criando lista vazia
lista = []
lista = list()
lista = ["dezzogo", 42, True, 3.14]


# indexação
print(lista[3])
print(lista[-3])


# slices
lista = [00, 11, 22, 33, 44, 55, 66, 77, 88, 99]
print(lista[2:5])
print(lista[4:])
print(lista[3:16:2])


# for com lista
print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
    print('Elemento da lista:', lista[i])


# MÉTODOS DE LISTAS
lista = [1, 3, 12, 8, 2]

# append -  add item ao final da lista
print('Antes do append', lista)
lista.append(3)
print('Depois do append', lista)

# insert - adiciona elemento no primeiro parâmetro, porém, escolhe a posição no segundo argumento.
print('Antes do insert', lista)
lista.insert(2, 10)
print('Depois do insert', lista)

#extend - adiciona uma lista à outra
lista2 = [1, 2, 3]
print('Antes do extend', lista2)
lista.extend(lista2)
print('Depois do extend', lista)

#pop - remove elemento pela posição especificada, ou o último elemento da lista, se não for especificado.
print('Antes do pop', lista2)
lista2.pop(1)
print('Depois do pop', lista2)

#remove - remove o elemento pelo valor especificado. Se houver mais elementos do mesmo valor especificado, ele sempre removerá o primeiro.
lista3 = [20, 40, 60, 80, 100]
print('Antes do remove', lista3)
lista3.remove(40)
print('Depois do remove', lista3)

#count - contar quantas vezes um elemento aparece na lista.
lista4 = [2, 3, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 2, 22, 222, 2222]
print('lista:', lista4)
print('Count para o 2:', lista4.count(2))

# index - indica em que posição está o elemento especificado. Também só mostra do primeiro, se houver mais de um.
print('Posição do 22:', lista4.index(22))

#sort - ordena a lista de forma crescente
print('Antes do sort:', lista4)
lista4.sort()
print('Depois do sort:', lista4)


# FUNÇÕES PARA LISTAS

#len - abrevia "length", mostra o comprimento.
print('Comprimento da lista com len:', len(lista4))

#sum - soma os elementos da lista
print(f'Soma dos elementos {lista4} com o sum:', sum(lista4))

#max - informa o valor do maior elemento da lista.
print('Maior elemento da lista com max:', max(lista4))

#min - informa o valor do menor elemento da lista.
print('Menor elemento da lista com min:', min(lista4))