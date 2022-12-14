teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = []
# A declaração do teste como [:] não irá gerar uma ligação.
# Sendo possível inserir mudanças
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
