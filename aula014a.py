
n = 1
soma = 0
totalPar = 0
totalImpar = 0
cont = 0
while n != 0:
    n = int(input('Digite um valor: '))

    if n != 0:
        soma += n
        cont += 1
        if n % 2 == 0:
            totalPar += 1
        else:
            totalImpar += 1

print('Foram digitados {} valores'.format(cont))
print('Somatória dos valores é {}'.format(soma))
print('Total de pares {}'.format(totalPar))
print('Total de impares {}'.format(totalImpar))
