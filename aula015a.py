s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print('Foram digitados {} valores e a soma total é {}'.format(c, s))

