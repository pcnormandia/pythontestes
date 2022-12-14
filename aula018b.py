galera = [['João', 19], ['Anna', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][0])
for pessoa in galera:
    print(pessoa[0])
for idade in galera:
    print(idade[1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
