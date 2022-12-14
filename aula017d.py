a = [2, 3, 4, 7]
b = a
print(a)
print(b)

# Quanto duas listas são igualadas forma-se uma cópia com ligação entre elas.
# Ao alterar um elemento de uma lista consequentemente a outra lista é alterada
b[2] = 8
print(a)
print(b)

# Para se criar uma cópia sem ligação é preciso utilizar o recurso de fatiamento
c = [1, 9, 4, 6]
d = c[:]
c[2] = 8
print(c)
print(d)
