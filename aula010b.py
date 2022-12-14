n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média está boa! Parabéns!')
else:
    print('Sua média está ruim. ESTUDE MAIS!')
