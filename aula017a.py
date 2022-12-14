num = [2, 5, 9, 1]
print(num)

# Posso alterar um elemento da lista diretamente.
num[2] = 3
print(num)

# Método append é usado para adicionar novos elementos no final da lista
num.append(7)
print(num)

# Método insert é usado para adicionar novos elementos em qualquer posição
num.insert(2, 0)
print(num)

# Método pop é usado para eliminar elementos no final da lista (sem parametros) ou em outra posição (com parametros)
num.pop()
num.pop(4)

# Método remove é usado para eliminar a primeira ocorrência de um elemento na lista.
num.remove(0)
# Quando o valor solicitado não estiver na lista irá dar erro.
# Para previnir o erro é necessário utilizar o comando if combinado com in:
if 4 in num:
    num.remove(4)
else:
    print('Numero 4 não foi encontrado')

# Método sorted pode ser usado para ordenar uma lista
num.sort()
print(num)

# Método sorted acompanhado do argumento reverse pode ser usado para ordenar uma lista em ordem reversa
num.sort(reverse=True)
print(num)

# Comando len é usado para verificação de comprimento da lista
print(f'Essa lista tem {len(num)} elementos')
