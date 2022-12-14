from math import sqrt, ceil, floor
n = int(input('Digite um número: '))
raiz = sqrt(n)
print('A raiz quadrada de {} vale {:.2f}'.format(n, raiz))
print('A raiz quadrada arrendondada para cima de {} vale {}'.format(n, ceil(raiz)))
print('A raiz quadrada arrendondada para baixa de {} vale {}'.format(n, floor(raiz)))
