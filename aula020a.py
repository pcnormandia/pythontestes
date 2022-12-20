# Definir uma função com passagem de parâmetros
def soma(a, b):
    print(f'A={a} e B={b}')
    s = a + b
    print(f'A soma de A + B é igual a {s}.')
    print('-=-'*10)


# Programa principal
soma(a=4, b=5)
soma(b=8, a=9)
soma(2, 1)
