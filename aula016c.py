# Na mesma tupla é possível declarar diferentes tipos primitivos
pessoa = ('Paulo', 50, 'M', 110)
print(pessoa)
# A única forma de mudar uma tupla é eliminando ela da memória com o comando del e recriar a variavel
del(pessoa)
pessoa = ('Gustavo', 39, 'M', 90.5)
print(pessoa)
