n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A soma de {} e {} vale {}'.format(n1, n2, (n1+n2)))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potenciação é {}'.format(di, e))
print(' A soma é {} \n O produto é {} \n A divisão é {:.3f}\n'.format(s, m, d), end=' ')
print('A divisão inteira é {}, \n A potenciação é {}'.format(di, e))
