valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na {c}ª posição: ')))

for p, v in enumerate(valores):
    print(f'Na posição {p} o valor é {v}')
print('Fim da lista')
