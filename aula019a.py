pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

pessoas['peso'] = 98.5
for k in pessoas.values():
    print(k)
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
