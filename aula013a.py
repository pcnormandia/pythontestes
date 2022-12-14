for c in range(0, 11, 1):
    print(c)
print('FIM')

for c in range(1, 11, 2):
    print(c)
print('FIM')

for c in range(11, 0, -1):
    print(c)
print('FIM')

n1 = int(input('Digite um valor inicial do laço: '))
n2 = int(input('Digite um valor final do laço: '))
i = int(input('Digite um valor para os passos: '))
for c in range(n1, n2+1, i):
    print(c)
print('FIM')
