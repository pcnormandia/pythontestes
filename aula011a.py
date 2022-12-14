print('\033[0;31mOlá Mundo! \033[m')
print('\033[0;30;43mOlá Mundo! \033[m')
print('\033[4;34;45mOlá Mundo! \033[m')
print('\033[mOlá Mundo! \033[m')
print('\033[7;31mOlá Mundo! \033[m')
print('\033[30mOlá Mundo! \033[m')
print('\033[0;33;44mOlá Mundo! \033[m')
print('\033[7;33;44mOlá Mundo! \033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a, b))
print('Os valores são \033[1:32m{}\033[m e \033[4:31m{}\033[m !!!'.format(a, b))
nome = 'Paulo César'
print('Prazer {}{}{}'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
print('Olá {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
s = 19//2
print(s)