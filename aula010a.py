nome = str(input('Qual o seu nome? ')).upper()
if nome == 'PAULO':
    print('Que nome mais lindo!!')

if nome == 'JOÃO':
    print('Seu nome é biblico')
else:
    print('Que nome legal')
print('Bom dia, {}. Prazer em te conhecer!'.format(nome))
