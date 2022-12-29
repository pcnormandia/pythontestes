# Comandos que serão avaliados para determinar se irá ocorrer uma exceção
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
# except irá ocorrer quando houver uma exceção. Podem ser criados vários except
# pode ser identificado por um tipo de erro específico
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero')

# pode ser identificado por mais de um tipo de erro específico.
except (ValueError, TypeError):
    print(f'Tivemos problemas com o tipo de dados que você digitou')
# pode ser para qualquer erro, com definição de classe ou causa
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
    print(f'Problema do tipo {erro.__cause__}')
# else irá ocorrer quando NÃO ocorrer uma exceção
else:
    print(f'O resultado foi {r:.2f}')
# Finally irá ocorrer independente do resultado
finally:
    print('Volte sempre, muito obrigado')
