# Definir uma função com passagem indefinida de parâmetros
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
    print('-=-'*10)


# Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
