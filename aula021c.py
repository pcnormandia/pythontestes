def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

r1 = fatorial(5)
r2 = fatorial(4)
r3 = fatorial()
print(f'Os resultados são {r1}, {r2} e {r3}')
