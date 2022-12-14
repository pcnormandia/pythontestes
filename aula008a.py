import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} vale {:.2f}'.format(num, raiz))
print('A raiz quadrada arrendondada para cima de {} vale {}'.format(num, math.ceil(raiz)))
print('A raiz quadrada arrendondada para baixo de {} vale {}'.format(num, math.floor(raiz)))
