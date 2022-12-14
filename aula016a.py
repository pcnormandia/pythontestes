lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# Tuplas são imutáveis
# lanche[1] = 'Refrigerantes' *** Irá apresentar erro
print(lanche)
# A váriavel não muda com o método sorted, apenas é apresentado em ordem alfabética.
print(sorted(lanche))
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-4:])
for comida in lanche:
    print(f'Eu comi {comida}')
print('Comi demais!!! Tô cheio')
print(f'A variavél lanche tem {len(lanche)} elementos.')

for c in range(0, len(lanche)):
    print(c, end=' ')
print('')
for c in range(0, len(lanche)):
    print(lanche[c], end=' ')
print('')
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida}. Posição {pos}.')