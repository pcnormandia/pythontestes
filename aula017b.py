valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

print(valores)

# Usando o comando for para imprimir cada valor separadamente
for v in valores:
    print(f'{v}!', end=' ')
print('')

# Funçao enumerate para imprimir a chave de indexação e o valor correspondente
for c, v in enumerate(valores):
    print(f'Na posição {c} encontramos o valor {v}!')
print('Cheguei ao final da lista')

