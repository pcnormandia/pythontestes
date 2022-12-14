nome = str (input('Qual é o seu nome: '))
print('Prazer em te conhecer {} !'.format(nome))
#sem alinhamento ou inclusão
print('Prazer em te conhecer {:20} !'.format(nome))
#inclusão de 20 espaços
print('Prazer em te conhecer {:>20} !'.format(nome))
#inclusão mais alinhamento direita
print('Prazer em te conhecer {:<20} !'.format(nome))
#inclusão mais alinhamento esquerda
print('Prazer em te conhecer {:^20} !'.format(nome))
#inclusão mais centralização
print('Prazer em te conhecer {:=^20} !'.format(nome))
#inclusão mais centralização com preenchimento dos espaços com o simbolo mencionado