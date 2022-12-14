nome = str(input('Qual é o seu nome: ')).upper()
if nome == 'PAULO':
    print('Que nome charmoso')
elif nome == 'JOÃO' or nome == 'MARIA' or nome == 'PEDRO' or nome == 'TIAGO' or nome == 'JOSÉ':
    print('Seu nome é biblico')
elif nome in 'ANA ANDREA CLÁUDIA JÉSSICA JULIANA MAYSA EMILIANA SHIRLEY HILDA':
    print('Que bonito nome feminino!')
else:
    print('Seu nome é normal')
print('Bom dia, {}!'.format(nome))
