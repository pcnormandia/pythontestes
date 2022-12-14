galera = list() #Criar uma lista para totalizar todos os dados digitados
dado = list() #Criar uma lista para receber os dados parciais
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Criar uma cópia dos dados parciais na lista galera
    dado.clear() #Limpar os dados parciais para receber novos dados
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1

print(f'Temos {totmaior} maiores de idade e {totmenor} de idade')
