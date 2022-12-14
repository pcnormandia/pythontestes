a = (2, 5, 4)
b = (5, 8, 1, 2)
# A ordem da soma é importante, pois altera a forma como a tupla é apresentada.
c = a + b
d = b + a
print(a)
print(b)
print(c)
print(d)
print(len(c))
print(sorted(c))
print(sorted(d))
# Método para verificar quantas vezes aparece o elemento.
print(c.count(5))
print(c.count(9))
# Método index permite identificar a 1ª posição de um elemento
print(c)
print(c.index(5))
# As demais posições são ignoradas a partir do posição escolhida
print(c.index(2))
print(c.index(2, 1))


