frase = 'Curso em Video Python'

print(frase)
print(len(frase))
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[::2])
print(frase[0:])
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.upper())
print(frase.upper().count('O'))
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.istitle())
print(frase.find('Python'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.rsplit())
div = frase.rsplit()
print(div[0])
print(div[0][3])
print('-'.join(frase))
print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são:
O Fatiamento de String, Análise com len(), count(), find(),
transformações com replace(), upper(),
lower(), capitalize(), title(), strip(), junção com join().""")



